#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reel STLabs — video Sebastián full-bleed a color + tips de seguridad."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BUILD = Path(__file__).resolve().parent
REPO = BUILD.parents[1]
FONTS_DIR = REPO / "fonts"
SRC = Path("/tmp/reel-seb/sebastian_src.mp4")
OUT_DIR = BUILD / "out"
OVER_DIR = BUILD / "overlays"
TIMELINE = BUILD / "timeline.json"

W, H = 1080, 1920
DURATION = 36.0
FPS = 10
TIMER_BASE = 40.0

# Fallback sync (si no hay timeline.json)
T0 = 2.40
PER = 1.55
T_FINAL = T0 + 19 * PER
TIP_STARTS: list[float] = []

TITLE = (
    "20 cosas que decirle a la IA\n"
    "que añada a tu web antes de lanzarla\n"
    "(en menos de 40 segundos)"
)

ITEMS = [
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
    "manus.im",
]

GREEN = (0, 255, 178, 255)
WHITE = (242, 242, 242, 255)


def fnt(name: str, size: int) -> ImageFont.FreeTypeFont:
    p = FONTS_DIR / name
    if not p.exists():
        raise FileNotFoundError(p)
    return ImageFont.truetype(str(p), size)


def sh(cmd: list[str]) -> None:
    print("+", " ".join(map(str, cmd[:12])), "...")
    subprocess.run(cmd, check=True)


def prepare_bg() -> Path:
    """Video full-bleed a color (sin oscurecer / desaturar)."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = OUT_DIR / "bg_vertical.mp4"
    factor = DURATION / 18.1
    vf = (
        f"scale=-2:{H},crop={W}:{H},"
        f"setpts=PTS*{factor:.6f},"
        f"drawbox=x=0:y=0:w={W}:h={H}:color=black@0.18:t=fill"
    )
    sh([
        "ffmpeg", "-y", "-i", str(SRC),
        "-vf", vf, "-an", "-r", str(FPS), "-t", str(DURATION),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17",
        str(raw),
    ])
    return raw


def load_timeline() -> None:
    """Ajusta duración y starts de tips desde timeline.json (add_voice.py)."""
    global DURATION, T0, T_FINAL, TIP_STARTS, TIMER_BASE, PER
    if not TIMELINE.exists():
        TIP_STARTS = [T0 + i * PER for i in range(19)]
        return
    meta = json.loads(TIMELINE.read_text(encoding="utf-8"))
    DURATION = float(meta["duration"])
    TIP_STARTS = [float(x) for x in meta["tip_starts"]]
    T0 = float(meta.get("t0", TIP_STARTS[0]))
    T_FINAL = float(meta["t_final"])
    TIMER_BASE = max(40.0, float(int(DURATION) + 1))
    print(f"timeline: duration={DURATION:.2f}s tips={len(TIP_STARTS)} final@{T_FINAL:.2f}")


def tip_index_at(t: float) -> int:
    """Índice 1..19 del tip visible en t, o 0 / 20."""
    if t < T0:
        return 0
    if t >= T_FINAL:
        return 20
    if not TIP_STARTS:
        return min(19, int((t - T0) / PER) + 1)
    idx = 0
    for i, start in enumerate(TIP_STARTS):
        if t >= start:
            idx = i + 1
    return idx


def draw_timer(draw: ImageDraw.ImageDraw, t: float, font: ImageFont.FreeTypeFont) -> None:
    remain = max(0.0, TIMER_BASE - t)
    label = f"{int(remain // 60):02d}:{int(remain % 60):02d},{int((remain % 1) * 100):02d}"
    bbox = draw.textbbox((0, 0), label, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 28, 14
    x, y = (W - tw) // 2, 318
    draw.rounded_rectangle(
        [x - pad_x, y - pad_y, x + tw + pad_x, y + th + pad_y],
        radius=12, fill=(0, 0, 0, 220), outline=GREEN, width=3,
    )
    draw.text((x, y), label, font=font, fill=WHITE)


def draw_items(
    draw: ImageDraw.ImageDraw,
    visible: int,
    f_num: ImageFont.FreeTypeFont,
    f_item: ImageFont.FreeTypeFont,
    f_prog: ImageFont.FreeTypeFont,
) -> None:
    if visible < 1:
        return
    i = min(visible, 19) - 1
    num = f"{i + 1}."
    text = ITEMS[i]
    prog = f"{i + 1} / 20"
    pb = draw.textbbox((0, 0), prog, font=f_prog)
    draw.text(((W - (pb[2] - pb[0])) // 2, 430), prog, font=f_prog, fill=GREEN)

    bn = draw.textbbox((0, 0), num, font=f_num)
    bt = draw.textbbox((0, 0), text, font=f_item)
    total_w = (bn[2] - bn[0]) + 24 + (bt[2] - bt[0])
    y = 560
    if total_w > W - 80:
        x_num = (W - (bn[2] - bn[0])) // 2
        draw.text((x_num, y), num, font=f_num, fill=GREEN)
        x_txt = (W - (bt[2] - bt[0])) // 2
        draw.text((x_txt, y + (bn[3] - bn[1]) + 20), text, font=f_item, fill=WHITE)
    else:
        x0 = (W - total_w) // 2
        draw.text((x0, y), num, font=f_num, fill=GREEN)
        draw.text((x0 + (bn[2] - bn[0]) + 24, y + 18), text, font=f_item, fill=WHITE)


def draw_hero(
    draw: ImageDraw.ImageDraw,
    f_num: ImageFont.FreeTypeFont,
    f_txt: ImageFont.FreeTypeFont,
) -> None:
    n, t = "20.", "manus.im"
    bn = draw.textbbox((0, 0), n, font=f_num)
    bt = draw.textbbox((0, 0), t, font=f_txt)
    total_w = (bn[2] - bn[0]) + 22 + (bt[2] - bt[0])
    x0 = (W - total_w) // 2
    y = H // 2 - 90
    draw.text((x0, y), n, font=f_num, fill=GREEN)
    draw.text((x0 + (bn[2] - bn[0]) + 22, y + 22), t, font=f_txt, fill=WHITE)
    draw.rectangle(
        [x0, y + (bn[3] - bn[1]) + 28, x0 + total_w, y + (bn[3] - bn[1]) + 36],
        fill=GREEN,
    )


def make_overlay(t: float, fonts: dict) -> Image.Image:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    y = 72
    for line in TITLE.split("\n"):
        bbox = draw.textbbox((0, 0), line, font=fonts["title"])
        draw.text(((W - (bbox[2] - bbox[0])) // 2, y), line, font=fonts["title"], fill=WHITE)
        y += bbox[3] - bbox[1] + 2

    draw_timer(draw, t, fonts["timer"])

    tip_i = tip_index_at(t)
    if 1 <= tip_i <= 19:
        draw_items(draw, tip_i, fonts["num"], fonts["item"], fonts["prog"])
    elif tip_i >= 20:
        img = Image.alpha_composite(img, Image.new("RGBA", (W, H), (10, 10, 10, 140)))
        draw = ImageDraw.Draw(img)
        draw_timer(draw, t, fonts["timer"])
        draw_hero(draw, fonts["hero_num"], fonts["hero_txt"])

    foot = "sebastian.stlabs.ar"
    fb = draw.textbbox((0, 0), foot, font=fonts["foot"])
    draw.text(((W - (fb[2] - fb[0])) // 2, H - 120), foot, font=fonts["foot"], fill=GREEN)
    return img


def render_overlays() -> None:
    OVER_DIR.mkdir(parents=True, exist_ok=True)
    fonts = {
        "title": fnt("Poppins-Bold.ttf", 48),
        "timer": fnt("IBMPlexMono-SemiBold.ttf", 52),
        "num": fnt("BebasNeue-Regular.ttf", 120),
        "item": fnt("Poppins-Bold.ttf", 64),
        "prog": fnt("IBMPlexMono-Medium.ttf", 36),
        "foot": fnt("IBMPlexMono-Medium.ttf", 40),
        "hero_num": fnt("BebasNeue-Regular.ttf", 200),
        "hero_txt": fnt("Poppins-Bold.ttf", 128),
    }
    n_frames = int(DURATION * FPS)
    for i in range(n_frames):
        make_overlay(i / FPS, fonts).save(OVER_DIR / f"ov_{i:05d}.png")
        if i % 90 == 0:
            print(f"overlay {i}/{n_frames}")


def composite(bg: Path) -> Path:
    mute = OUT_DIR / "STLabs-Reel-Seguridad-Manus-MUTE.mp4"
    out = OUT_DIR / "STLabs-Reel-Seguridad-Manus.mp4"
    sh([
        "ffmpeg", "-y",
        "-i", str(bg),
        "-framerate", str(FPS),
        "-i", str(OVER_DIR / "ov_%05d.png"),
        "-filter_complex", "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p",
        "-t", str(DURATION),
        "-c:v", "libx264", "-crf", "17", "-preset", "medium",
        "-an",
        "-movflags", "+faststart",
        str(mute),
    ])
    sh(["cp", str(mute), str(out)])
    for ss, name in [(1.5, "preview-01"), (6, "preview-06"), (14, "preview-14"), (32, "preview-32")]:
        sh([
            "ffmpeg", "-y", "-ss", str(ss), "-i", str(mute),
            "-frames:v", "1", "-update", "1", str(OUT_DIR / f"{name}.png"),
        ])
    return mute


def write_meta() -> None:
    (BUILD / "caption.txt").write_text(
        "20 cosas que decirle a la IA que añada a tu web antes de lanzarla.\n\n"
        "Seguridad. Autenticación. Cabeceras. HTTPS.\n"
        "Y la número 20: manus.im\n\n"
        "Comentá MANUS y te mando la guía.\n\n"
        "#seguridadweb #ia #lanzamiento #stlabs #manus\n",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        "# Manifiesto de fuentes — Reel seguridad + manus.im\n\n"
        "| Familia | Peso | Rol | Origen |\n|---|---|---|---|\n"
        "| Poppins | 700 | Título / ítems / manus.im | `/workspace/fonts/Poppins-Bold.ttf` |\n"
        "| Bebas Neue | 400 | Números | `/workspace/fonts/BebasNeue-Regular.ttf` |\n"
        "| IBM Plex Mono | 500–600 | Timer + firma | `/workspace/fonts/IBMPlexMono-*.ttf` |\n",
        encoding="utf-8",
    )
    (BUILD / "index.json").write_text(
        "{\n"
        '  "id": "2026-09-09-reel-seguridad-web",\n'
        '  "titulo": "20 cosas de seguridad web antes de lanzar + manus.im",\n'
        '  "tipo": "reel",\n'
        f'  "duracion_s": {int(round(DURATION))},\n'
        '  "formato": "1080x1920",\n'
        '  "fondo": "video_sebastian_color",\n'
        '  "familia_visual": "manifiesto",\n'
        '  "origen": "screenshot",\n'
        '  "keyword_portada": "MANUS",\n'
        '  "layout": "full_bleed_color"\n'
        "}\n",
        encoding="utf-8",
    )


def main() -> None:
    if not SRC.exists():
        sys.exit(f"Falta video fuente: {SRC}")
    load_timeline()
    write_meta()
    bg = prepare_bg()
    render_overlays()
    out = composite(bg)
    print("DONE →", out)


if __name__ == "__main__":
    main()
