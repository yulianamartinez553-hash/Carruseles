#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publicación STLabs — foto horizontal completa arriba + texto en negro inferior."""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

BUILD = Path(__file__).resolve().parent
REPO = BUILD.parents[1]
FONTS = REPO / "fonts"
OUT = BUILD / "out"
DATA = json.loads((BUILD / "index.json").read_text(encoding="utf-8"))

# Formato feed IG ~4:5 (1080×1350). La foto 4:3 queda arriba; abajo, negro natural.
W, H = 1080, 1350
SCALE = 2
RW, RH = W * SCALE, H * SCALE

NEGRO = (10, 10, 10, 255)
VERDE = (0, 255, 178, 255)
BLANCO = (242, 242, 242, 255)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def fit_width_full(img: Image.Image, target_w: int) -> Image.Image:
    """Escala la foto al ancho completo SIN recortar (mantiene toda la imagen)."""
    img = img.convert("RGB")
    iw, ih = img.size
    nh = int(round(target_w * ih / iw))
    return img.resize((target_w, nh), Image.Resampling.LANCZOS)


def soft_bottom_fade(photo: Image.Image, fade_px: int) -> Image.Image:
    """Degradé sutil solo en el borde inferior → se integra al negro del lienzo."""
    w, h = photo.size
    fade_px = min(fade_px, h // 2)
    rgba = photo.convert("RGBA")
    mask = Image.new("L", (w, h), 255)
    px = mask.load()
    start = h - fade_px
    for y in range(start, h):
        t = (y - start) / max(1, fade_px - 1)
        # curva suave: al final alpha→0
        a = int(255 * (1 - t) ** 1.6)
        for x in range(w):
            px[x, y] = a
    mask = mask.filter(ImageFilter.GaussianBlur(radius=max(2, fade_px // 18)))
    black = Image.new("RGBA", (w, h), NEGRO)
    return Image.composite(rgba, black, mask)


def draw_text_in_black_zone(canvas: Image.Image, zone_top: int) -> None:
    """Tipografía gruesa STLabs: tamaños variables para énfasis."""
    draw = ImageDraw.Draw(canvas)
    # chica < media < grande < xl (énfasis)
    size_map = {
        "chica": 40 * SCALE,
        "media": 50 * SCALE,
        "grande": 64 * SCALE,
        "xl": 78 * SCALE,
    }
    gap_map = {
        "chica": 10 * SCALE,
        "media": 12 * SCALE,
        "grande": 16 * SCALE,
        "xl": 18 * SCALE,
    }
    f_foot = font("IBMPlexMono-Medium.ttf", 28 * SCALE)

    lines = DATA["copy"]["lineas"]
    fonts_line = []
    gaps = []
    for line in lines:
        peso = line.get("peso", "media")
        fonts_line.append(font("Poppins-Bold.ttf", size_map.get(peso, 52 * SCALE)))
        gaps.append(gap_map.get(peso, 12 * SCALE))

    heights, widths = [], []
    for line, f in zip(lines, fonts_line):
        bbox = draw.textbbox((0, 0), line["texto"], font=f)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])

    block_h = sum(heights) + sum(gaps[:-1])
    foot_space = 110 * SCALE
    zone_h = RH - zone_top - foot_space
    y = zone_top + max(24 * SCALE, (zone_h - block_h) // 2)

    for line, f, lh, lw, g in zip(lines, fonts_line, heights, widths, gaps):
        color = VERDE if line["color"] == "verde" else BLANCO
        x = (RW - lw) // 2
        draw.text((x, y), line["texto"], font=f, fill=color)
        y += lh + g

    foot = DATA["firma"]
    fb = draw.textbbox((0, 0), foot, font=f_foot)
    fx = (RW - (fb[2] - fb[0])) // 2
    draw.text((fx, RH - 78 * SCALE), foot, font=f_foot, fill=VERDE)


def main() -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    photo = Image.open(BUILD / DATA["foto"])

    # Foto completa al ancho del post (sin crop / sin zoom)
    fitted = fit_width_full(photo, RW)
    # Degradé sutil solo donde la foto toca el negro
    faded = soft_bottom_fade(fitted, fade_px=int(90 * SCALE))

    canvas = Image.new("RGBA", (RW, RH), NEGRO)
    # pegar arriba
    canvas.paste(faded, (0, 0), faded)
    photo_h = faded.size[1]
    # zona de texto = todo lo negro debajo de la foto
    draw_text_in_black_zone(canvas, zone_top=photo_h - int(40 * SCALE))

    final = canvas.convert("RGB")
    preview = final.resize((W, H), Image.Resampling.LANCZOS)

    out_hi = OUT / "STLabs-Post-Tiempo-Ellas.png"
    out_prev = OUT / "preview.png"
    out_jpg = OUT / "STLabs-Post-Tiempo-Ellas.jpg"
    final.save(out_hi, "PNG", optimize=True)
    preview.save(out_prev, "PNG", optimize=True)
    preview.save(out_jpg, "JPEG", quality=93, optimize=True)

    print(f"foto={fitted.size[0]//SCALE}x{fitted.size[1]//SCALE}  canvas={W}x{H}")
    print("OK →", out_hi)
    return out_prev


if __name__ == "__main__":
    main()
