#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Narración masculina argentina (Tomás) sincronizada al reel."""
from __future__ import annotations

import asyncio
import subprocess
from pathlib import Path

import edge_tts

BUILD = Path(__file__).resolve().parent
OUT = BUILD / "out"
AUDIO = BUILD / "audio"
# usar video SIN audio previo si existe copia muda; si no, strip audio
VIDEO_BASE = OUT / "STLabs-Reel-Seguridad-Manus-MUTE.mp4"
VIDEO_FALLBACK = OUT / "STLabs-Reel-Seguridad-Manus.mp4"
VIDEO_OUT = OUT / "STLabs-Reel-Seguridad-Manus-VOZ.mp4"
VIDEO_MAIN = OUT / "STLabs-Reel-Seguridad-Manus.mp4"

DURATION = 28.0
VOICE = "es-AR-TomasNeural"
PITCH = "-8Hz"  # un poco más grave, tono adulto

T0 = 1.20
PER = 1.12
T_FINAL = T0 + 19 * PER

# frases cortas para entrar en ~1s
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


def sh(cmd: list[str]) -> None:
    print("+", " ".join(cmd[:10]), "...")
    subprocess.run(cmd, check=True)


async def synth(text: str, path: Path, rate: str) -> None:
    await edge_tts.Communicate(text, VOICE, rate=rate, pitch=PITCH).save(str(path))


def ensure_mute() -> Path:
    """Video base sin pista de audio (evita doblar voces)."""
    src = VIDEO_FALLBACK if VIDEO_FALLBACK.exists() else VIDEO_OUT
    if not src.exists():
        raise SystemExit("No hay video base")
    # si ya tiene audio, sacar pista
    sh([
        "ffmpeg", "-y", "-i", str(src),
        "-c:v", "copy", "-an",
        str(VIDEO_BASE),
    ])
    return VIDEO_BASE


async def build_clips() -> list[tuple[float, Path]]:
    AUDIO.mkdir(parents=True, exist_ok=True)
    clips: list[tuple[float, Path]] = []

    raw_intro = AUDIO / "intro_raw.mp3"
    await synth(
        "Veinte chequeos de seguridad antes de lanzar tu web.",
        raw_intro,
        rate="+5%",
    )
    intro = AUDIO / "intro.mp3"
    # máximo 1.1s
    sh([
        "ffmpeg", "-y", "-i", str(raw_intro),
        "-af", "atrim=0:1.05,afade=t=out:st=0.85:d=0.2",
        "-ar", "24000", str(intro),
    ])
    clips.append((0.10, intro))

    for i, tip in enumerate(TIPS):
        raw = AUDIO / f"tip_{i+1:02d}_raw.mp3"
        await synth(tip, raw, rate="+28%")
        clipped = AUDIO / f"tip_{i+1:02d}.mp3"
        sh([
            "ffmpeg", "-y", "-i", str(raw),
            "-af", "atrim=0:1.05,afade=t=out:st=0.85:d=0.18,volume=1.2",
            "-ar", "24000", str(clipped),
        ])
        clips.append((T0 + i * PER, clipped))

    raw_final = AUDIO / "final_raw.mp3"
    await synth(
        "Y veinte: manus punto i eme. Comentá manus.",
        raw_final,
        rate="-2%",
    )
    final = AUDIO / "final.mp3"
    sh([
        "ffmpeg", "-y", "-i", str(raw_final),
        "-af", "atrim=0:4.5,afade=t=out:st=4.0:d=0.4,volume=1.15",
        "-ar", "24000", str(final),
    ])
    clips.append((T_FINAL + 0.1, final))
    return clips


def mix_timeline(clips: list[tuple[float, Path]]) -> Path:
    silent = AUDIO / "silent.wav"
    sh([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "anullsrc=r=24000:cl=mono",
        "-t", str(DURATION), str(silent),
    ])

    inputs = ["-i", str(silent)]
    filters = []
    labels = ["[0:a]"]
    for idx, (start, path) in enumerate(clips, start=1):
        inputs += ["-i", str(path)]
        ms = int(start * 1000)
        filters.append(f"[{idx}:a]adelay={ms}|{ms}[a{idx}]")
        labels.append(f"[a{idx}]")

    mix = "".join(labels) + f"amix=inputs={len(labels)}:duration=first:dropout_transition=0:normalize=0[aout]"
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
    # probe
    sh(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,codec_name", "-of", "csv=p=0", str(out)])
    print("DONE →", out)


if __name__ == "__main__":
    asyncio.run(main())
