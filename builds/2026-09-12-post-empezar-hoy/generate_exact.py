# -*- coding: utf-8 -*-
"""Post Empezar Hoy — geometría idéntica a la referencia.

Los arcos NO son concéntricos: todos parten del punto «hoy».
Centro de cada arco = a la derecha del punto, radio = r.
Los 7 internos: semicírculo superior 180°→0° (terminan en la horizontal).
El externo: continúa por debajo del texto (~180°→-78°).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

W, H = 1080, 1350
SCALE = 4
WW, HH = W * SCALE, H * SCALE

VERDE = (0, 255, 178)
NEGRO = (10, 10, 10)
BLANCO = (255, 255, 255)

FONT_DIR = REPO / "fonts"
MAC_DIR = Path("/usr/share/fonts/truetype/macos")
HANDLE = "sebastian.stlabs.ar"

# Punto origen (fracción del content de la ref)
OX_F, OY_F = 0.125, 0.470

# Radios medidos en la ref (fracción del ancho) — 7 internos + 1 externo
INNER_RADII = [0.0405, 0.0775, 0.1153, 0.1569, 0.2009, 0.2469, 0.2928]
OUTER_RADIUS = 0.375
OUTER_END_DEG = -82.0  # envuelve debajo del texto

# Quote centrado, debajo de la horizontal del punto
QUOTE_CX_F = 0.50
QUOTE_TOP_F = 0.555


def font(path: Path, size_1x: float) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), int(size_1x * SCALE))


def draw_arc_from_point(
    draw: ImageDraw.ImageDraw,
    ox: float,
    oy: float,
    r: float,
    start_deg: float,
    end_deg: float,
    width: int,
) -> None:
    """Arco con centro a la derecha del punto: C=(ox+r, oy). Barrido horario."""
    cx, cy = ox + r, oy
    span = (start_deg - end_deg) % 360.0 or 360.0
    steps = max(36, int(span * 2.5))
    pts = []
    for i in range(steps + 1):
        a = start_deg - span * (i / steps)
        rad = math.radians(a)
        pts.append((cx + r * math.cos(rad), cy - r * math.sin(rad)))
    draw.line(pts, fill=NEGRO, width=width, joint="curve")
    rr = width / 2.0
    for x, y in (pts[0], pts[-1]):
        draw.ellipse([x - rr, y - rr, x + rr, y + rr], fill=NEGRO)


def render() -> tuple[Image.Image, list]:
    img = Image.new("RGB", (WW, HH), BLANCO)
    d = ImageDraw.Draw(img)

    ox, oy = OX_F * WW, OY_F * HH
    stroke = max(3, int(2.1 * SCALE))

    for rf in INNER_RADII:
        draw_arc_from_point(d, ox, oy, rf * WW, 180.0, 0.0, stroke)
    draw_arc_from_point(d, ox, oy, OUTER_RADIUS * WW, 180.0, OUTER_END_DEG, stroke)

    # Punto
    rd = 7.0 * SCALE
    d.ellipse([ox - rd, oy - rd, ox + rd, oy + rd], fill=NEGRO)

    # «hoy»
    f_hoy = font(FONT_DIR / "Lora-Italic-Variable.ttf", 17)
    hb = d.textbbox((0, 0), "hoy", font=f_hoy)
    hx = ox - (hb[2] - hb[0]) / 2 - hb[0]
    hy = oy + 15 * SCALE - hb[1]
    d.text((hx, hy), "hoy", font=f_hoy, fill=NEGRO)

    # Quote (serif; última línea italic) — misma posición relativa que la ref
    f_q = font(MAC_DIR / "Inter-Regular.ttf", 36)
    # Mejor serif si hay Lora roman; usamos Inter limpio + Lora italic en cierre
    f_qi = font(FONT_DIR / "Lora-Italic-Variable.ttf", 37)
    # Try to use a serif look closer to ref for lines 1-2 via Lora italic at slightly different optical size
    # Prefer DejaVu Serif if available
    serif = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
    if serif.exists():
        f_q = font(serif, 36)

    lines = [
        ("Dentro de un año", f_q),
        ("desearás haber", f_q),
        ("empezado hoy.", f_qi),
    ]
    cx = QUOTE_CX_F * WW
    y = QUOTE_TOP_F * HH
    gap = 48 * SCALE
    boxes = []
    for txt, fnt in lines:
        bb = d.textbbox((0, 0), txt, font=fnt)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        x = cx - tw / 2 - bb[0]
        d.text((x, y - bb[1]), txt, font=fnt, fill=NEGRO)
        boxes.append((x + bb[0], y, x + bb[0] + tw, y + th))
        y += gap

    # Footer STLabs
    f_mono = font(FONT_DIR / "IBMPlexMono-Medium.ttf", 18)
    accent_y = 0.825 * HH
    aw = 42 * SCALE
    d.rectangle(
        [WW / 2 - aw / 2, accent_y, WW / 2 + aw / 2, accent_y + 2.5 * SCALE],
        fill=VERDE,
    )
    bb = d.textbbox((0, 0), HANDLE, font=f_mono)
    tw = bb[2] - bb[0]
    d.text(
        ((WW - tw) / 2 - bb[0], 0.858 * HH - bb[1]),
        HANDLE,
        font=f_mono,
        fill=VERDE,
    )
    return img, boxes


def qa(img: Image.Image, boxes: list) -> dict:
    arr = np.array(img)
    only = Image.new("RGB", img.size, BLANCO)
    d = ImageDraw.Draw(only)
    serif = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
    f_q = font(serif if serif.exists() else MAC_DIR / "Inter-Regular.ttf", 36)
    f_qi = font(FONT_DIR / "Lora-Italic-Variable.ttf", 37)
    lines = [
        ("Dentro de un año", f_q),
        ("desearás haber", f_q),
        ("empezado hoy.", f_qi),
    ]
    cx = QUOTE_CX_F * WW
    y = QUOTE_TOP_F * HH
    gap = 48 * SCALE
    for txt, fnt in lines:
        bb = d.textbbox((0, 0), txt, font=fnt)
        tw = bb[2] - bb[0]
        x = cx - tw / 2 - bb[0]
        d.text((x, y - bb[1]), txt, font=fnt, fill=NEGRO)
        y += gap
    ref = np.array(only)
    extra = 0
    for x0, y0, x1, y1 in boxes:
        pad = int(2 * SCALE)
        xa, ya = max(0, int(x0) - pad), max(0, int(y0) - pad)
        xb, yb = min(arr.shape[1], int(x1) + pad), min(arr.shape[0], int(y1) + pad)
        a, b = arr[ya:yb, xa:xb], ref[ya:yb, xa:xb]
        da = (a[:, :, 0] < 50) & (a[:, :, 1] < 50) & (a[:, :, 2] < 50)
        db = (b[:, :, 0] < 50) & (b[:, :, 1] < 50) & (b[:, :, 2] < 50)
        extra += int((da & ~db).sum())
    return {"extra_dark_pixels": extra, "pass": extra < 50}


def main() -> None:
    out = BUILD / "out"
    out.mkdir(parents=True, exist_ok=True)
    img, boxes = render()
    result = qa(img, boxes)
    print("QA", result)
    if not result["pass"]:
        raise SystemExit(f"FAIL: líneas tapando texto ({result})")

    stem = "STLabs-Post-Empezar-Hoy"
    img.save(out / f"{stem}@4x.png", optimize=True)
    img.resize((2160, 2700), Image.Resampling.LANCZOS).save(
        out / f"{stem}@2x.png", optimize=True
    )
    img.resize((1080, 1350), Image.Resampling.LANCZOS).save(
        out / f"{stem}.png", optimize=True
    )
    img.resize((540, 675), Image.Resampling.LANCZOS).save(out / "_preview-post.png")

    # Compare
    ref = Image.open(BUILD / "assets" / "ref2.jpg").convert("RGB")
    ref_c = ref.crop((0, 375, 1284, 1978)).resize((540, 675), Image.Resampling.LANCZOS)
    ours = img.resize((540, 675), Image.Resampling.LANCZOS)
    board = Image.new("RGB", (540 * 2 + 16, 675 + 40), (245, 245, 245))
    board.paste(ref_c, (0, 40))
    board.paste(ours, (556, 40))
    d = ImageDraw.Draw(board)
    d.text((10, 10), "Referencia", fill=(0, 0, 0))
    d.text((566, 10), "STLabs (misma geometría)", fill=(0, 0, 0))
    board.save(out / "_compare-ref.png")

    # Keep buy post from previous generate if present
    print("OK", out / f"{stem}.png")


if __name__ == "__main__":
    main()
