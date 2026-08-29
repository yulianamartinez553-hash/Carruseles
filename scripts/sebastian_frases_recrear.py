#!/usr/bin/env python3
"""Slides frases — fondo negro, firma STLabs, portada con Sebastián sutil."""
from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

PHOTO = Path("/workspace/resultados/sebastian-cafe-cinematic/sebastian-cinematic-macbook-photo.png")
OUT_DIR = Path("/workspace/resultados/sebastian-frases-recrear")
ARTIFACTS = Path("/opt/cursor/artifacts/assets")
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
MONO = Path("/tmp/stlabs-fonts/IBMPlexMono-Medium.ttf")

W, H = 1080, 1350
BLACK = (10, 10, 10)
GREEN = (0, 255, 178)
WHITE = (242, 242, 242)
GRAIN = 14


def black_canvas() -> Image.Image:
    return Image.new("RGB", (W, H), BLACK)


def add_grain(im: Image.Image, seed: int = 42) -> Image.Image:
    arr = np.array(im).astype(np.float32)
    rng = np.random.default_rng(seed)
    arr += rng.normal(0, GRAIN, arr.shape[:2])[..., np.newaxis]
    specks = rng.random(arr.shape[:2]) < 0.0012
    arr[specks] = np.minimum(arr[specks] + 55, 255)
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def subtle_sebastian_layer(path: Path, opacity: float = 0.38) -> Image.Image:
    """Foto tenue pero más legible sobre negro."""
    im = Image.open(path).convert("RGB")
    iw, ih = im.size
    target = W / H
    if iw / ih > target:
        nw = int(ih * target)
        im = im.crop(((iw - nw) // 2, 0, (iw + nw) // 2, ih))
    else:
        nh = int(iw / target)
        y0 = max(0, int(ih * 0.12) - (nh - ih) // 2)
        im = im.crop((0, y0, iw, min(ih, y0 + nh)))
    im = im.resize((W, H), Image.Resampling.LANCZOS)

    arr = cv2.GaussianBlur(np.array(im), (0, 0), 10).astype(np.float32)
    arr *= 0.88
    gray = arr.mean(axis=2, keepdims=True)
    arr = arr * 0.72 + gray * 0.28

    # viñeta suave → negro en bordes
    xs = (np.arange(W, dtype=np.float32) - W * 0.5) / (W * 0.68)
    ys = (np.arange(H, dtype=np.float32) - H * 0.44) / (H * 0.62)
    dist = np.sqrt(xs[np.newaxis, :] ** 2 + ys[:, np.newaxis] ** 2)
    vig = 1.0 - np.clip(dist, 0, 1) ** 1.25 * 0.55
    arr *= vig[..., np.newaxis]

    photo = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    base = black_canvas().convert("RGBA")
    photo_rgba = photo.convert("RGBA")
    photo_rgba.putalpha(int(255 * opacity))
    return Image.alpha_composite(base, photo_rgba).convert("RGB")


def draw_firma(draw: ImageDraw.ImageDraw, y: int = H - 72) -> None:
    font = ImageFont.truetype(str(MONO), 22)
    text = "sebastian.stlabs.ar"
    tw = draw.textlength(text, font=font)
    x = (W - tw) // 2
    # letter-spacing manual
    spacing = 3
    cx = x
    for ch in text:
        draw.text((cx, y), ch, font=font, fill=GREEN)
        cx += draw.textlength(ch, font=font) + spacing


def slide_01_portada() -> Image.Image:
    im = subtle_sebastian_layer(PHOTO, opacity=0.58)
    im = add_grain(im, seed=42)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(SERIF, 58)

    nodes = {
        "¿Y": (430, 175),
        "si": (760, 215),
        "todo": (820, 610),
        "sale": (175, 930),
        "bien?": (115, 560),
    }
    order = ["¿Y", "si", "todo", "sale", "bien?", "¿Y"]
    pts = [nodes[k] for k in order]
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=WHITE, width=2)

    for word, (x, y) in nodes.items():
        draw.text((x, y), word, font=font, fill=WHITE)

    draw_firma(draw)
    return im


def slide_02_fondo_negro() -> Image.Image:
    im = add_grain(black_canvas(), seed=77)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(SERIF, 56)
    lines = [
        "Esta en tu poder",
        "vivir la vida",
        "de tus sueños.",
    ]
    lh = 72
    total_h = lh * len(lines)
    y0 = (H - total_h) // 2 - 40
    for i, line in enumerate(lines):
        tw = draw.textlength(line, font=font)
        draw.text(((W - tw) // 2, y0 + i * lh), line, font=font, fill=WHITE)
    draw_firma(draw)
    return im


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    s1 = slide_01_portada()
    s2 = slide_02_fondo_negro()

    p1 = OUT_DIR / "slide-01-y-si-todo-sale-bien.png"
    p2 = OUT_DIR / "slide-02-esta-en-tu-poder.png"
    s1.save(p1, optimize=True)
    s2.save(p2, optimize=True)
    s1.save(ARTIFACTS / "sebastian-frases-slide-01.png", optimize=True)
    s2.save(ARTIFACTS / "sebastian-frases-slide-02.png", optimize=True)
    print(f"OK {p1}\nOK {p2}")


if __name__ == "__main__":
    main()
