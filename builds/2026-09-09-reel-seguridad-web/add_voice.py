#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Narración Tomás AR — frases completas, timeline secuencial sin solapes."""
from __future__ import annotations

import asyncio
import json
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
TIMELINE = BUILD / "timeline.json"

VOICE = "es-AR-TomasNeural"
PITCH = "-6Hz"
GAP = 0.12

INTRO = "Veinte chequeos de seguridad antes de lanzar tu web."
TIPS = [
    "Ocultá claves API",
    "Eliminá secretos Git",
    "Clave pública DB",
    "Seguridad row-level",
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


def fade_only(src: Path, dst: Path, volume: float = 1.15) -> float:
    """Copia el audio completo con fade suave al final. Sin cortes."""
    d = probe_dur(src)
    fade_st = max(0.05, d - 0.18)
    sh([
        "ffmpeg", "-y", "-i", str(src),
        "-af", f"afade=t=out:st={fade_st:.3f}:d=0.18,volume={volume}",
        "-ar", "24000", str(dst),
    ])
    return probe_dur(dst)


def ensure_mute() -> Path:
    src = VIDEO_BASE if VIDEO_BASE.exists() else VIDEO_FALLBACK
    if not src.exists():
        raise SystemExit("No hay video base mudo — corré generate_reel.py primero")
    if src != VIDEO_BASE:
        sh(["ffmpeg", "-y", "-i", str(src), "-c:v", "copy", "-an", str(VIDEO_BASE)])
    return VIDEO_BASE


async def build_clips() -> tuple[list[tuple[float, Path]], dict]:
    AUDIO.mkdir(parents=True, exist_ok=True)
    clips: list[tuple[float, Path]] = []
    tip_starts: list[float] = []

    t = 0.15
    raw_intro = AUDIO / "intro_raw.mp3"
    await synth(INTRO, raw_intro, rate="+5%")
    intro = AUDIO / "intro.mp3"
    d = fade_only(raw_intro, intro, 1.15)
    clips.append((t, intro))
    print(f"intro @{t:.2f} dur={d:.2f}s")
    t += d + GAP

    for i, tip in enumerate(TIPS):
        raw = AUDIO / f"tip_{i+1:02d}_raw.mp3"
        await synth(tip, raw, rate="+5%")
        clipped = AUDIO / f"tip_{i+1:02d}.mp3"
        d = fade_only(raw, clipped, 1.2)
        tip_starts.append(t)
        clips.append((t, clipped))
        print(f"tip {i+1:02d} @{t:.2f} dur={d:.2f}s  «{tip}»")
        t += d + GAP

    t_final = t
    raw_final = AUDIO / "final_raw.mp3"
    await synth(FINAL, raw_final, rate="-2%")
    final = AUDIO / "final.mp3"
    d = fade_only(raw_final, final, 1.15)
    # fade un poco más largo en el cierre
    fade_st = max(0.05, d - 0.35)
    sh([
        "ffmpeg", "-y", "-i", str(raw_final),
        "-af", f"afade=t=out:st={fade_st:.3f}:d=0.35,volume=1.15",
        "-ar", "24000", str(final),
    ])
    d = probe_dur(final)
    clips.append((t_final, final))
    print(f"final @{t_final:.2f} dur={d:.2f}s")
    duration = t_final + d + 0.35

    meta = {
        "duration": round(duration, 3),
        "t0": round(tip_starts[0], 3),
        "tip_starts": [round(x, 3) for x in tip_starts],
        "t_final": round(t_final, 3),
        "tips": TIPS,
        "final": FINAL,
        "intro": INTRO,
    }
    TIMELINE.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print("timeline →", TIMELINE, "duration", meta["duration"])
    return clips, meta


def mix_timeline(clips: list[tuple[float, Path]], duration: float) -> Path:
    silent = AUDIO / "silent.wav"
    sh([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "anullsrc=r=24000:cl=mono",
        "-t", str(duration), str(silent),
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


def extend_mute(mute: Path, duration: float) -> Path:
    """Si el video mudo es más corto que la narración, lo estira (último frame)."""
    vdur = probe_dur(mute)
    if abs(vdur - duration) < 0.15:
        return mute
    extended = OUT / "STLabs-Reel-Seguridad-Manus-MUTE-EXT.mp4"
    # tpad o loop: freeze last frame
    pad = max(0.0, duration - vdur)
    if pad <= 0:
        sh([
            "ffmpeg", "-y", "-i", str(mute),
            "-t", str(duration), "-c", "copy", str(extended),
        ])
    else:
        sh([
            "ffmpeg", "-y", "-i", str(mute),
            "-vf", f"tpad=stop_mode=clone:stop_duration={pad:.3f}",
            "-an", "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p",
            "-t", str(duration),
            str(extended),
        ])
    return extended


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
    clips, meta = await build_clips()
    duration = float(meta["duration"])
    mute = extend_mute(mute, duration)
    audio = mix_timeline(clips, duration)
    out = mux(mute, audio)
    sh([
        "ffprobe", "-v", "error",
        "-show_entries", "stream=codec_type,codec_name,duration",
        "-of", "default=nw=1", str(out),
    ])
    print("DONE →", out)
    print("Re-render overlays with: python3 generate_reel.py --from-timeline")


if __name__ == "__main__":
    asyncio.run(main())
