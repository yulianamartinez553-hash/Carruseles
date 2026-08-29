#!/usr/bin/env python3
"""Overlay «CONFÍA EN EL PROCESO» + tinte verde sutil en fondo."""
from __future__ import annotations

import shutil
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

PHOTO = Path("/workspace/resultados/sebastian-cafe-cinematic/sebastian-cinematic-macbook-photo.png")
FONT = Path("/tmp/stlabs-fonts/IBMPlexMono-Medium.ttf")
OUT_DIR = Path("/workspace/resultados/sebastian-cafe-cinematic")
ARTIFACT = Path("/opt/cursor/artifacts/assets/sebastian-cinematic-macbook-6x7.png")

PHRASE = "CONFÍA EN EL PROCESO"
LINES = 7
OPACITIES = [0.12, 0.28, 0.55, 1.0, 0.55, 0.28, 0.12]
FONT_SIZE = 42
LETTER_SPACING = 6
LINE_HEIGHT = 60

# Verde STLabs (#00FFB2) — tenue, más presente en sombras/fondo
GREEN = np.array([0, 255, 178], dtype=np.float32)
TINT_STRENGTH = 0.0  # sin verde
DARKEN = 0.78  # oscuridad como la versión anterior (más blur)
BLUR_BG = 13.0
BLUR_SUBJECT = 1.6
VIGNETTE = 0.22  # refuerzo de sombras en bordes


def apply_depth_blur(im: Image.Image) -> Image.Image:
    """Más blur en fondo; Sebastián con desenfoque leve."""
    arr = np.array(im.convert("RGB"))
    h, w = arr.shape[:2]

    light = cv2.GaussianBlur(arr, (0, 0), sigmaX=BLUR_SUBJECT, sigmaY=BLUR_SUBJECT).astype(np.float32)
    heavy = cv2.GaussianBlur(arr, (0, 0), sigmaX=BLUR_BG, sigmaY=BLUR_BG).astype(np.float32)

    cx, cy = w * 0.50, h * 0.40
    xs = (np.arange(w, dtype=np.float32) - cx) / (w * 0.50)
    ys = (np.arange(h, dtype=np.float32) - cy) / (h * 0.48)
    dist = np.sqrt(xs[np.newaxis, :] ** 2 + ys[:, np.newaxis] ** 2)
    mask = np.clip((dist - 0.05) / 0.95, 0.0, 1.0) ** 1.1
    mask3 = mask[..., np.newaxis]

    out = light * (1.0 - mask3) + heavy * mask3
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def darken(im: Image.Image, factor: float = DARKEN) -> Image.Image:
    arr = np.array(im.convert("RGB"), dtype=np.float32) * factor
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def apply_vignette(im: Image.Image, strength: float = VIGNETTE) -> Image.Image:
    arr = np.array(im.convert("RGB"), dtype=np.float32)
    h, w = arr.shape[:2]
    cx, cy = w * 0.5, h * 0.46
    xs = (np.arange(w, dtype=np.float32) - cx) / (w * 0.72)
    ys = (np.arange(h, dtype=np.float32) - cy) / (h * 0.78)
    dist = np.sqrt(xs[np.newaxis, :] ** 2 + ys[:, np.newaxis] ** 2)
    vig = 1.0 - np.clip(dist, 0.0, 1.0) ** 1.35 * strength
    return Image.fromarray(np.clip(arr * vig[..., np.newaxis], 0, 255).astype(np.uint8))


def apply_subtle_green_tint(im: Image.Image) -> Image.Image:
    """Verde sutil en fondo/sombras; piel y centro casi intactos."""
    arr = np.array(im.convert("RGB"), dtype=np.float32)
    h, w = arr.shape[:2]
    lum = arr.mean(axis=2) / 255.0
    shadow_mask = np.clip(1.0 - lum, 0.0, 1.0) ** 1.15

    cx, cy = w * 0.50, h * 0.40
    xs = (np.arange(w, dtype=np.float32) - cx) / (w * 0.50)
    ys = (np.arange(h, dtype=np.float32) - cy) / (h * 0.48)
    dist = np.sqrt(xs[np.newaxis, :] ** 2 + ys[:, np.newaxis] ** 2)
    bg_mask = np.clip((dist - 0.12) / 0.88, 0.0, 1.0) ** 0.95

    mask = np.clip(shadow_mask * 0.45 + bg_mask * 0.55, 0.0, 1.0) ** 1.05
    mask = mask[..., np.newaxis]
    tinted = arr + mask * (GREEN - arr) * TINT_STRENGTH
    return Image.fromarray(np.clip(tinted, 0, 255).astype(np.uint8))


def draw_spaced_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
) -> None:
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + LETTER_SPACING


def main() -> None:
    im = Image.open(PHOTO)
    im = apply_depth_blur(im)
    im = darken(im)
    im = apply_vignette(im)
    base = apply_subtle_green_tint(im).convert("RGBA")
    w, h = base.size
    font = ImageFont.truetype(str(FONT), FONT_SIZE)

    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    line_w = sum(probe.textlength(c, font=font) + LETTER_SPACING for c in PHRASE) - LETTER_SPACING

    block_center_y = h // 2
    block_h = (LINES - 1) * LINE_HEIGHT
    y0 = block_center_y - block_h // 2

    for i in range(LINES):
        alpha = int(255 * OPACITIES[i])
        fill = (255, 255, 255, alpha)
        y = y0 + i * LINE_HEIGHT
        x = (w - line_w) // 2
        draw_spaced_text(draw, (x, y), PHRASE, font, fill)

    out = Image.alpha_composite(base, overlay).convert("RGB")

    png = OUT_DIR / "sebastian-cinematic-macbook-6x7.png"
    jpg = OUT_DIR / "sebastian-cinematic-macbook-6x7.jpg"
    out.save(png, optimize=True)
    out.save(jpg, quality=94)
    shutil.copy(png, ARTIFACT)
    print(f"OK {png} · texto centrado y={block_center_y} · tinte verde {TINT_STRENGTH:.0%}")


if __name__ == "__main__":
    main()
