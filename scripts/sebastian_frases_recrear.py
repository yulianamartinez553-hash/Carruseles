#!/usr/bin/env python3
"""Recrea slides estilo referencia (¿Y si todo sale bien? / Esta en tu poder…) con foto Sebastián, sin verde."""
from __future__ import annotations

import shutil
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

PHOTO = Path("/workspace/resultados/sebastian-cafe-cinematic/sebastian-cinematic-macbook-photo.png")
OUT_DIR = Path("/workspace/resultados/sebastian-frases-recrear")
ARTIFACTS = Path("/opt/cursor/artifacts/assets")
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1080, 1350
DARKEN = 0.72
BLUR_BG = 14.0
BLUR_SUBJECT = 2.0
VIGNETTE = 0.28
DESAT = 0.42
GRAIN = 24


def prepare_background(path: Path) -> Image.Image:
    im = Image.open(path).convert("RGB")
    iw, ih = im.size
    target = W / H
    if iw / ih > target:
        nw = int(ih * target)
        im = im.crop(((iw - nw) // 2, 0, (iw + nw) // 2, ih))
    else:
        nh = int(iw / target)
        y0 = max(0, int(ih * 0.18) - (nh - ih) // 2)
        im = im.crop((0, y0, iw, min(ih, y0 + nh)))
    im = im.resize((W, H), Image.Resampling.LANCZOS)

    arr = np.array(im)
    light = cv2.GaussianBlur(arr, (0, 0), BLUR_SUBJECT).astype(np.float32)
    heavy = cv2.GaussianBlur(arr, (0, 0), BLUR_BG).astype(np.float32)
    cx, cy = W * 0.5, H * 0.42
    xs = (np.arange(W, dtype=np.float32) - cx) / (W * 0.52)
    ys = (np.arange(H, dtype=np.float32) - cy) / (H * 0.50)
    dist = np.sqrt(xs[np.newaxis, :] ** 2 + ys[:, np.newaxis] ** 2)
    mask = np.clip((dist - 0.04) / 0.96, 0, 1) ** 1.1
    m3 = mask[..., np.newaxis]
    out = light * (1 - m3) + heavy * m3
    out *= DARKEN

    # viñeta
    xs2 = (np.arange(W, dtype=np.float32) - W * 0.5) / (W * 0.72)
    ys2 = (np.arange(H, dtype=np.float32) - H * 0.46) / (H * 0.78)
    d2 = np.sqrt(xs2[np.newaxis, :] ** 2 + ys2[:, np.newaxis] ** 2)
    vig = 1.0 - np.clip(d2, 0, 1) ** 1.35 * VIGNETTE
    out *= vig[..., np.newaxis]

    # desaturar (look film, sin verde)
    gray = out.mean(axis=2, keepdims=True)
    out = out * (1 - DESAT) + gray * DESAT

    rng = np.random.default_rng(42)
    noise = rng.normal(0, GRAIN, out.shape[:2])
    for c in range(3):
        out[:, :, c] += noise
    specks = rng.random(out.shape[:2]) < 0.0018
    out[specks] = np.minimum(out[specks] + 90, 255)

    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def draw_branding(draw: ImageDraw.ImageDraw, y_base: int = H - 110) -> None:
    f_eq = ImageFont.truetype(SERIF, 34)
    f_handle = ImageFont.truetype(SANS, 22)
    eq = "1+1="
    three = "3"
    handle = "sebastian.stlabs.ar"
    w_eq = draw.textlength(eq, font=f_eq)
    w3 = draw.textlength(three, font=f_eq)
    total = w_eq + w3
    x = (W - total) // 2
    draw.text((x, y_base), eq, font=f_eq, fill=(242, 242, 242))
    draw.text((x + w_eq, y_base), three, font=f_eq, fill=(220, 40, 40))
    hw = draw.textlength(handle, font=f_handle)
    draw.text(((W - hw) // 2, y_base + 42), handle, font=f_handle, fill=(210, 210, 210))


def slide_01(base: Image.Image) -> Image.Image:
    im = base.copy()
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
        draw.line([pts[i], pts[i + 1]], fill=(235, 235, 235), width=2)

    for word, (x, y) in nodes.items():
        draw.text((x, y), word, font=font, fill=(245, 245, 245))

    draw_branding(draw)
    return im


def slide_02(base: Image.Image) -> Image.Image:
    im = base.copy()
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
        draw.text(((W - tw) // 2, y0 + i * lh), line, font=font, fill=(245, 245, 245))
    draw_branding(draw)
    return im


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    base = prepare_background(PHOTO)

    s1 = slide_01(base)
    s2 = slide_02(base)

    p1 = OUT_DIR / "slide-01-y-si-todo-sale-bien.png"
    p2 = OUT_DIR / "slide-02-esta-en-tu-poder.png"
    s1.save(p1, optimize=True)
    s2.save(p2, optimize=True)
    s1.save(ARTIFACTS / "sebastian-frases-slide-01.png", optimize=True)
    s2.save(ARTIFACTS / "sebastian-frases-slide-02.png", optimize=True)
    print(f"OK {p1}\nOK {p2}")


if __name__ == "__main__":
    main()
