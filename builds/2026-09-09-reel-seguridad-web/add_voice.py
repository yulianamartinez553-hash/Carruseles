#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Narración masculina argentina (Tomás) — frases completas, sin cortes."""
from __future__ import annotations

import asyncio
import subprocess
from pathlib import Path

import edge_tts

BUILD = Path(__file__).resolve().parent
OUT = BUILD / "out"
AUDIO = BUILD / "audio"
VIDEO_BASE = OUT / "STLabs-Reel-Seguridad-Manus-MUTE.mp4"
VIDEO_FALLBACK = OUT / "STLabs-Reel-Seguridad-Manus.mp4"
VIDEO_OUT = OUT / "STLabs-Reel-Seguridad-Manus-VOZ.mp4"
VIDEO_MAIN = OUT / "STLabs-Reel-Seguridad-Manus.mp4"

DURATION = 36.0
VOICE = "es-AR-TomasNeural"
PITCH = "-6Hz"

T0 = 2.40
PER = 1.55
T_FINAL = T0 + 19 * PER

INTRO = "Veinte chequeos de seguridad antes de lanzar tu web."
TIPS = [
    "Ocultá claves API",
    "Eliminá secretos Git",
    "Clave pública DB",
    "Seguridad row level",
    "Cifrado de datos",
    "Forzá autenticación",
    "Restringí registros",
    "Bloqueá campos",
    "Protegé cookies",
    "Hasheá contraseñas",
    "Limitá logins",
    "Protección bots",
    "Parametrizá consultas",
    "Validá entradas",
    "Escapá contenido",
    "Restringí archivos",
    "Limitá API",
    "Cabeceras seguridad",
    "Forzá HTTPS",
]
FINAL = "Y veinte: manus punto i eme. Comentá manus."


def sh(cmd: list[str]) -> None:
    print("+", " ".join(cmd[:10]), "...")
    subprocess.run(cmd, check=True)


def probe_dur(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=nw=1:nk=1",
            str(path),
        ],
        text=True,
    ).strip()
    return float(out)


async def synth(text: str, path: Path, rate: str) -> None:
    await edge_tts.Communicate(text, VOICE, rate=rate, pitch=PITCH).save(str(path))


def ensure_mute() -> Path:
    src = VIDEO_BASE if VIDEO_BASE.exists() else VIDEO_FALLBACK
    if not src.exists():
        raise SystemExit("No hay video base mudo")
    if src != VIDEO_BASE:
        sh(["ffmpeg", "-y", "-i", str(src), "-c:v", "copy", "-an", str(VIDEO_BASE)])
    return VIDEO_BASE


async def build_clips() -> list[tuple[float, Path]]:
    AUDIO.mkdir(parents=True, exist_ok=True)
    clips: list[tuple[float, Path]] = []

    raw_intro = AUDIO / "intro_raw.mp3"
    await synth(INTRO, raw_intro, rate="+0%")
    intro = AUDIO / "intro.mp3"
    d = probe_dur(raw_intro)
    fade_st = max(0.05, d - 0.18)
    sh([
        "ffmpeg", "-y", "-i", str(raw_intro),
        "-af", f"afade=t=out:st={fade_st:.3f}:d=0.18,volume=1.15",
        "-ar", "24000", str(intro),
    ])
    clips.append((0.12, intro))
    print(f"intro {probe_dur(intro):.2f}s")

    for i, tip in enumerate(TIPS):
        raw = AUDIO / f"tip_{i+1:02d}_raw.mp3"
        await synth(tip, raw, rate="+8%")
        clipped = AUDIO / f"tip_{i+1:02d}.mp3"
        d = probe_dur(raw)
        slot = PER - 0.08
        if d > slot:
            atempo = min(1.25, d / slot)
            out_d = d / atempo
            fade_st = max(0.05, out_d - 0.15)
            af = f"atempo={atempo:.4f},afade=t=out:st={fade_st:.3f}:d=0.15,volume=1.2"
        else:
            fade_st = max(0.05, d - 0.15)
            af = f"afade=t=out:st={fade_st:.3f}:d=0.15,volume=1.2"
        sh([
            "ffmpeg", "-y", "-i", str(raw),
            "-af", af,
            "-ar", "24000", str(clipped),
        ])
        start = T0 + i * PER
        clips.append((start, clipped))
        print(f"tip {i+1:02d} start={start:.2f} dur={probe_dur(clipped):.2f}s  «{tip}»")

    raw_final = AUDIO / "final_raw.mp3"
    await synth(FINAL, raw_final, rate="-2%")
    final = AUDIO / "final.mp3"
    d = probe_dur(raw_final)
    fade_st = max(0.05, d - 0.35)
    sh([
        "ffmpeg", "-y", "-i", str(raw_final),
        "-af", f"afade=t=out:st={fade_st:.3f}:d=0.35,volume=1.15",
        "-ar", "24000", str(final),
    ])
    clips.append((T_FINAL + 0.15, final))
    print(f"final start={T_FINAL + 0.15:.2f} dur={probe_dur(final):.2f}s")
    return clips


def mix_timeline(clips: list[tuple[float, Path]]) -> Path:
    silent = AUDIO / "silent.wav"
    sh([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "anullsrc=r=24000:cl=mono",
        "-t", str(DURATION), str(silent),
    ])

    inputs: list[str] = ["-i", str(silent)]
    filters: list[str] = []
    labels = ["[0:a]"]
    for idx, (start, path) in enumerate(clips, start=1):
        inputs += ["-i", str(path)]
        ms = int(round(start * 1000))
        filters.append(f"[{idx}:a]adelay={ms}|{ms}[a{idx}]")
        labels.append(f"[a{idx}]")

    mix = (
        "".join(labels)
        + f"amix=inputs={len(labels)}:duration=first:dropout_transition=0:normalize=0[aout]"
    )
    fc = ";".join(filters + [mix])
    mixed = AUDIO / "narracion.wav"
    sh(["ffmpeg", "-y", *inputs, "-filter_complex", fc, "-map", "[aout]", str(mixed)])
    return mixed


def mux(mute: Path, audio: Path) -> Path:
    sh([
        "ffmpeg", "-y",
        "-i", str(mute),
        "-i", str(audio),
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        str(VIDEO_OUT),
    ])
    sh(["cp", str(VIDEO_OUT), str(VIDEO_MAIN)])
    return VIDEO_OUT


async def main() -> None:
    mute = ensure_mute()
    clips = await build_clips()
    print("clips", len(clips))
    audio = mix_timeline(clips)
    out = mux(mute, audio)
    sh([
        "ffprobe", "-v", "error",
        "-show_entries", "stream=codec_type,codec_name",
        "-of", "csv=p=0", str(out),
    ])
    print("DONE →", out)


if __name__ == "__main__":
    asyncio.run(main())
