#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reel STLabs — fondo negro + Sebastián PIP inferior-izq con degradé."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

BUILD = Path(__file__).resolve().parent
REPO = BUILD.parents[1]
FONTS_DIR = REPO / "fonts"
SRC = Path("/tmp/reel-seb/sebastian_src.mp4")
OUT_DIR = BUILD / "out"
OVER_DIR = BUILD / "overlays"
MASK_PATH = BUILD / "assets" / "pip_edge_mask.png"

W, H = 1080, 1920
DURATION = 28.0
FPS = 10

# PIP: menos de la mitad del frame, inferior izquierda
PIP_W = 460
PIP_H = 700
PIP_X = 0
PIP_Y = H - PIP_H  # pegado abajo
FADE_L, FADE_R, FADE_T, FADE_B = 48, 150, 160, 70

TITLE = (
    "20 cosas que decirle a la IA\n"
    "que añada a tu web antes de lanzarla\n"
    "(en menos de 30 segundos)"
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
NEGRO = (10, 10, 10, 255)


def fnt(name: str, size: int) -> ImageFont.FreeTypeFont:
    p = FONTS_DIR / name
    if not p.exists():
        raise FileNotFoundError(p)
    return ImageFont.truetype(str(p), size)


def sh(cmd: list[str]) -> None:
    print("+", " ".join(map(str, cmd[:12])), "...")
    subprocess.run(cmd, check=True)


def make_edge_mask() -> Path:
    """Máscara con degradé en costados/arriba/abajo → integración al negro."""
    MASK_PATH.parent.mkdir(parents=True, exist_ok=True)
    mask = Image.new("L", (PIP_W, PIP_H), 0)
    px = mask.load()
    for y in range(PIP_H):
        if y < FADE_T:
            ty = y / FADE_T
        elif y > PIP_H - 1 - FADE_B:
            ty = (PIP_H - 1 - y) / FADE_B
        else:
            ty = 1.0
        # curva suave
        ty = ty * ty * (3 - 2 * ty)
        for x in range(PIP_W):
            if x < FADE_L:
                tx = x / FADE_L
            elif x > PIP_W - 1 - FADE_R:
                tx = (PIP_W - 1 - x) / FADE_R
            else:
                tx = 1.0
            tx = tx * tx * (3 - 2 * tx)
            px[x, y] = int(255 * tx * ty)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=10))
    mask.save(MASK_PATH)
    return MASK_PATH


def prepare_bg() -> Path:
    """Fondo negro pleno + video Sebastián inferior-izq con degradé en bordes."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    mask = make_edge_mask()
    raw = OUT_DIR / "bg_vertical.mp4"
    factor = DURATION / 18.1

    # Fuente es 1920×1080 con rotación → forzar portrait 1080×1920 al escalar
    # Escala para cubrir PIP, crop centrado al tamaño PIP, alphamerge + overlay
    fc = (
        f"color=c=0x0A0A0A:s={W}x{H}:d={DURATION}:r={FPS}[bg];"
        f"[0:v]scale={PIP_W}:{PIP_H}:force_original_aspect_ratio=increase,"
        f"crop={PIP_W}:{PIP_H},setpts=PTS*{factor:.6f},"
        f"eq=brightness=-0.04:saturation=0.92,format=rgba[pip];"
        f"[1:v]format=gray,scale={PIP_W}:{PIP_H}[mask];"
        f"[pip][mask]alphamerge[pipa];"
        f"[bg][pipa]overlay=x={PIP_X}:y={PIP_Y}:format=auto,format=yuv420p[vout]"
    )
    sh([
        "ffmpeg", "-y",
        "-i", str(SRC),
        "-loop", "1", "-i", str(mask),
        "-filter_complex", fc,
        "-map", "[vout]",
        "-an", "-r", str(FPS), "-t", str(DURATION),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
        str(raw),
    ])
    return raw


def draw_timer(draw: ImageDraw.ImageDraw, t: float, font: ImageFont.FreeTypeFont) -> None:
    remain = max(0.0, 30.0 - t)
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


def draw_hero(draw: ImageDraw.ImageDraw, f_num: ImageFont.FreeTypeFont, f_txt: ImageFont.FreeTypeFont) -> None:
    n, t = "20.", "manus.im"
    bn = draw.textbbox((0, 0), n, font=f_num)
    bt = draw.textbbox((0, 0), t, font=f_txt)
    total_w = (bn[2] - bn[0]) + 22 + (bt[2] - bt[0])
    x0 = (W - total_w) // 2
    y = H // 2 - 90
    draw.text((x0, y), n, font=f_num, fill=GREEN)
    draw.text((x0 + (bn[2] - bn[0]) + 22, y + 22), t, font=f_txt, fill=WHITE)
    draw.rectangle([x0, y + (bn[3] - bn[1]) + 28, x0 + total_w, y + (bn[3] - bn[1]) + 36], fill=GREEN)


def make_overlay(t: float, fonts: dict) -> Image.Image:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    y = 72
    for line in TITLE.split("\n"):
        bbox = draw.textbbox((0, 0), line, font=fonts["title"])
        draw.text(((W - (bbox[2] - bbox[0])) // 2, y), line, font=fonts["title"], fill=WHITE)
        y += bbox[3] - bbox[1] + 2

    draw_timer(draw, t, fonts["timer"])

    t0, per = 1.15, 1.12
    t_final = t0 + 19 * per

    if t0 <= t < t_final:
        visible = min(19, int((t - t0) / per) + 1)
        draw_items(draw, visible, fonts["num"], fonts["item"], fonts["prog"])
    elif t >= t_final:
        img = Image.alpha_composite(img, Image.new("RGBA", (W, H), (10, 10, 10, 120)))
        draw = ImageDraw.Draw(img)
        draw_timer(draw, t, fonts["timer"])
        draw_hero(draw, fonts["hero_num"], fonts["hero_txt"])

    # Firma abajo-derecha para no tapar el PIP
    foot = "sebastian.stlabs.ar"
    fb = draw.textbbox((0, 0), foot, font=fonts["foot"])
    fw = fb[2] - fb[0]
    draw.text((W - fw - 48, H - 90), foot, font=fonts["foot"], fill=GREEN)
    return img


def render_overlays() -> None:
    OVER_DIR.mkdir(parents=True, exist_ok=True)
    fonts = {
        "title": fnt("Poppins-Bold.ttf", 48),
        "timer": fnt("IBMPlexMono-SemiBold.ttf", 52),
        "num": fnt("BebasNeue-Regular.ttf", 120),
        "item": fnt("Poppins-Bold.ttf", 64),
        "prog": fnt("IBMPlexMono-Medium.ttf", 36),
        "foot": fnt("IBMPlexMono-Medium.ttf", 36),
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
    for ss, name in [(1.5, "preview-01"), (6, "preview-06"), (14, "preview-14"), (24, "preview-24")]:
        sh([
            "ffmpeg", "-y", "-ss", str(ss), "-i", str(mute),
            "-vframes", "1", str(OUT_DIR / f"{name}.png"),
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
        '  "duracion_s": 28,\n'
        '  "formato": "1080x1920",\n'
        '  "fondo": "negro_mineral",\n'
        '  "familia_visual": "pip_manifiesto",\n'
        '  "origen": "screenshot",\n'
        '  "keyword_portada": "MANUS",\n'
        '  "layout": "fondo_negro_pip_inferior_izq_degrade"\n'
        "}\n",
        encoding="utf-8",
    )


def main() -> None:
    if not SRC.exists():
        sys.exit(f"Falta video fuente: {SRC}")
    write_meta()
    bg = prepare_bg()
    render_overlays()
    out = composite(bg)
    print("DONE →", out)


if __name__ == "__main__":
    main()
