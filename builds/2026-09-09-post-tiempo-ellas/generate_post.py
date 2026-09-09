#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publicación STLabs — foto familia + frase tiempo (fondo negro, degradé)."""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

BUILD = Path(__file__).resolve().parent
REPO = BUILD.parents[1]
FONTS = REPO / "fonts"
OUT = BUILD / "out"
DATA = json.loads((BUILD / "index.json").read_text(encoding="utf-8"))

W, H = 1080, 1350
SCALE = 2  # retina
RW, RH = W * SCALE, H * SCALE

NEGRO = (10, 10, 10, 255)
VERDE = (0, 255, 178, 255)
BLANCO = (242, 242, 242, 255)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def cover_center(img: Image.Image, tw: int, th: int) -> Image.Image:
    img = img.convert("RGB")
    iw, ih = img.size
    scale = max(tw / iw, th / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = max(0, (nh - th) // 2 - int(th * 0.04))  # leve sesgo arriba (caras)
    return img.crop((left, top, left + tw, top + th))


def apply_edge_fade(photo: Image.Image) -> Image.Image:
    """Degradé sutil a negro: fuerte abajo, leve en laterales y arriba."""
    w, h = photo.size
    base = Image.new("RGBA", (w, h), NEGRO)
    photo_rgba = photo.convert("RGBA")

    # máscara de opacidad de la foto (255 = foto visible)
    mask = Image.new("L", (w, h), 255)
    px = mask.load()

    # fade inferior (últimos ~38% → negro integrado)
    fade_h = int(h * 0.38)
    for y in range(h - fade_h, h):
        t = (y - (h - fade_h)) / fade_h
        # curva suave
        a = int(255 * (1 - t * t))
        for x in range(w):
            px[x, y] = min(px[x, y], a)

    # fade lateral suave
    side = int(w * 0.08)
    for x in range(side):
        t = 1 - (x / side)
        a = int(255 * (1 - 0.55 * t * t))
        for y in range(h):
            px[x, y] = min(px[x, y], a)
            px[w - 1 - x, y] = min(px[w - 1 - x, y], a)

    # fade superior leve
    top_f = int(h * 0.10)
    for y in range(top_f):
        t = 1 - (y / top_f)
        a = int(255 * (1 - 0.35 * t * t))
        for x in range(w):
            px[x, y] = min(px[x, y], a)

    mask = mask.filter(ImageFilter.GaussianBlur(radius=18))
    return Image.composite(photo_rgba, base, mask)


def draw_text_block(canvas: Image.Image) -> None:
    draw = ImageDraw.Draw(canvas)
    # tipografía gruesa y grande
    f_big = font("Poppins-Bold.ttf", 78 * SCALE // 2)  # ~78 @1x → use 156 at 2x
    f_big = font("Poppins-Bold.ttf", 72 * SCALE)
    f_mid = font("Poppins-Bold.ttf", 58 * SCALE)
    f_foot = font("IBMPlexMono-Medium.ttf", 26 * SCALE)

    lines = DATA["copy"]["lineas"]
    # primeras 3 líneas un poco más grandes (hook)
    sizes = []
    for i, line in enumerate(lines):
        if i < 3:
            sizes.append(f_big)
        else:
            sizes.append(f_mid)

    # medir bloque
    gap = 10 * SCALE
    heights = []
    widths = []
    for line, f in zip(lines, sizes):
        bbox = draw.textbbox((0, 0), line["texto"], font=f)
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])

    block_h = sum(heights) + gap * (len(lines) - 1)
    # anclar en zona inferior-media (sobre el degradé negro)
    y = int(RH * 0.52)
    # si se pasa, subir
    if y + block_h > RH - 140 * SCALE:
        y = RH - 140 * SCALE - block_h

    for line, f, lh, lw in zip(lines, sizes, heights, widths):
        color = VERDE if line["color"] == "verde" else BLANCO
        x = (RW - lw) // 2
        # sombra suave para legibilidad
        draw.text((x + 3 * SCALE, y + 3 * SCALE), line["texto"], font=f, fill=(0, 0, 0, 180))
        draw.text((x, y), line["texto"], font=f, fill=color)
        y += lh + gap

    # firma
    foot = DATA["firma"]
    fb = draw.textbbox((0, 0), foot, font=f_foot)
    fx = (RW - (fb[2] - fb[0])) // 2
    draw.text((fx, RH - 90 * SCALE), foot, font=f_foot, fill=VERDE)


def main() -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    photo_path = BUILD / DATA["foto"]
    photo = Image.open(photo_path)
    # foto casi full-bleed, centrada
    covered = cover_center(photo, RW, RH)
    framed = apply_edge_fade(covered)

    canvas = Image.new("RGBA", (RW, RH), NEGRO)
    canvas = Image.alpha_composite(canvas, framed)
    draw_text_block(canvas)

    final = canvas.convert("RGB")
    preview = final.resize((W, H), Image.Resampling.LANCZOS)

    out_hi = OUT / "STLabs-Post-Tiempo-Ellas.png"
    out_prev = OUT / "preview.png"
    final.save(out_hi, "PNG", optimize=True)
    preview.save(out_prev, "PNG", optimize=True)
    # también jpg liviano para chat
    out_jpg = OUT / "STLabs-Post-Tiempo-Ellas.jpg"
    preview.save(out_jpg, "JPEG", quality=92, optimize=True)

    (BUILD / "caption.txt").write_text(
        "La meta de tener una empresa no era ser millonario.\n\n"
        "Era tener tiempo para estar con ellas cuando me necesiten..\n"
        "Sin tener que pedir permiso.\n\n"
        "#familia #empresa #tiempo #stlabs\n",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Post tiempo / ellas

| Familia | Peso | Rol | Origen |
|---|---|---|---|
| Poppins | 700 | Frase display | `/workspace/fonts/Poppins-Bold.ttf` |
| IBM Plex Mono | 500 | Firma | `/workspace/fonts/IBMPlexMono-Medium.ttf` |
""",
        encoding="utf-8",
    )
    print("OK →", out_hi)
    print("preview →", out_prev)
    return out_prev


if __name__ == "__main__":
    main()
