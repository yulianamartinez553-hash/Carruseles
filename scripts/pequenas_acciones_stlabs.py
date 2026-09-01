#!/usr/bin/env python3
"""Infográfico Pequeñas acciones / Grandes resultados — identidad STLabs."""
from __future__ import annotations

import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path("/workspace/resultados/pequenas-acciones-stlabs")
ARTIFACT = Path("/opt/cursor/artifacts/assets/pequenas-acciones-stlabs.png")

W, H = 1080, 1350
BG = (10, 10, 10)
GREEN = (0, 255, 178)
DARK = (10, 10, 10)
WHITE = (242, 242, 242)

F_BEBAS = "/tmp/stlabs-fonts/BebasNeue-Regular.ttf"
F_MONO_M = "/tmp/stlabs-fonts/IBMPlexMono-Medium.ttf"
F_MONO_SB = "/tmp/stlabs-fonts/IBMPlexMono-SemiBold.ttf"
F_BARLOW = "/tmp/stlabs-fonts/BarlowCondensed-Bold.ttf"


def draw_inverted_line(
    draw: ImageDraw.ImageDraw,
    parts: list[tuple[str, bool]],
    y: int,
    font: ImageFont.FreeTypeFont,
    pad_x: int = 14,
    pad_y: int = 6,
    gap: int = 10,
) -> None:
    """parts: (text, inverted) — inverted = caja verde con texto oscuro."""
    sizes = []
    for text, inv in parts:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if inv:
            sizes.append((tw + pad_x * 2, th + pad_y * 2, text, True))
        else:
            sizes.append((tw, th, text, False))

    total_w = sum(s[0] for s in sizes) + gap * (len(sizes) - 1)
    x = (W - total_w) // 2
    for tw, th, text, inv in sizes:
        if inv:
            draw.rounded_rectangle(
                (x, y, x + tw, y + th),
                radius=4,
                fill=GREEN,
            )
            bbox = draw.textbbox((0, 0), text, font=font)
            tx = x + (tw - (bbox[2] - bbox[0])) // 2
            ty = y + (th - (bbox[3] - bbox[1])) // 2 - bbox[1]
            draw.text((tx, ty), text, font=font, fill=DARK)
            x += tw + gap
        else:
            bbox = draw.textbbox((0, 0), text, font=font)
            ty = y + (sizes[0][1] - (bbox[3] - bbox[1])) // 2 - bbox[1]
            draw.text((x, ty), text, font=font, fill=GREEN)
            x += tw + gap


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    im = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(im)

    f_brand = ImageFont.truetype(F_MONO_M, 26)
    f_head = ImageFont.truetype(F_BEBAS, 72)
    f_label = ImageFont.truetype(F_BARLOW, 34)
    f_label_sm = ImageFont.truetype(F_MONO_SB, 28)
    f_exito = ImageFont.truetype(F_BEBAS, 42)

    # Firma superior
    brand = "sebastian.stlabs.ar"
    spacing = 4
    tw = sum(draw.textlength(c, font=f_brand) + spacing for c in brand) - spacing
    cx = (W - tw) // 2
    y_brand = 72
    for ch in brand:
        draw.text((cx, y_brand), ch, font=f_brand, fill=GREEN)
        cx += draw.textlength(ch, font=f_brand) + spacing

    # Línea divisoria sutil
    draw.line([(W // 2 - 120, y_brand + 44), (W // 2 + 120, y_brand + 44)], fill=GREEN, width=1)

    # Título — mismo patrón invertido que la ref
    draw_inverted_line(
        draw,
        [("Pequeñas", True), ("acciones", False)],
        y=200,
        font=f_head,
        pad_x=16,
        pad_y=8,
        gap=14,
    )
    draw_inverted_line(
        draw,
        [("Grandes", False), ("resultados", True)],
        y=290,
        font=f_head,
        pad_x=16,
        pad_y=8,
        gap=14,
    )

    # Gráfico diagonal
    pts = [
        (120, 1080, "1%", "below", 10),
        (280, 920, "Hoy", "above", 12),
        (440, 760, "Disciplina", "above", 12),
        (600, 600, "Hábito", "above", 12),
        (760, 440, "Acción", "above", 12),
        (920, 280, "Éxito", "circle", 52),
    ]

    # Línea
    draw.line([(pts[0][0], pts[0][1]), (pts[-1][0], pts[-1][1])], fill=GREEN, width=3)

    for i, (px, py, label, mode, r) in enumerate(pts):
        if mode == "circle":
            draw.ellipse((px - r, py - r, px + r, py + r), fill=GREEN)
            bbox = draw.textbbox((0, 0), label, font=f_exito)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            draw.text((px - tw // 2, py - th // 2 - bbox[1]), label, font=f_exito, fill=DARK)
        else:
            draw.ellipse((px - r, py - r, px + r, py + r), fill=GREEN)
            font = f_label_sm if label == "1%" else f_label
            bbox = draw.textbbox((0, 0), label, font=font)
            tw = bbox[2] - bbox[0]
            if mode == "above":
                ty = py - r - 14 - (bbox[3] - bbox[1])
            else:
                ty = py + r + 10
            draw.text((px - tw // 2, ty - bbox[1]), label, font=font, fill=GREEN)

    # Firma inferior
    f_foot = ImageFont.truetype(F_MONO_M, 20)
    foot = "RevOps · CRM · IA"
    fw = draw.textlength(foot, font=f_foot)
    draw.text(((W - fw) // 2, H - 64), foot, font=f_foot, fill=GREEN)

    png = OUT / "pequenas-acciones-grandes-resultados.png"
    jpg = OUT / "pequenas-acciones-grandes-resultados.jpg"
    im.save(png, optimize=True)
    im.save(jpg, quality=94)
    shutil.copy(png, ARTIFACT)
    print(f"OK {png}")


if __name__ == "__main__":
    main()
