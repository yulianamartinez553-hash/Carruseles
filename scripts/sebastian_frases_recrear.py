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


def sebastian_layer(path: Path, strength: float = 0.78) -> Image.Image:
    """Foto limpia sobre negro — sin grain ni desaturación pesada."""
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

    photo = cv2.GaussianBlur(np.array(im), (0, 0), 4).astype(np.float32)
    base = np.full((H, W, 3), 10.0, dtype=np.float32)

    xs = (np.arange(W, dtype=np.float32) - W * 0.5) / (W * 0.72)
    ys = (np.arange(H, dtype=np.float32) - H * 0.44) / (H * 0.64)
    dist = np.sqrt(xs[np.newaxis, :] ** 2 + ys[:, np.newaxis] ** 2)
    radial = 1.0 - np.clip(dist, 0, 1) ** 1.15 * 0.32
    blend = np.clip(radial * strength, 0, 1)[..., np.newaxis]

    out = base * (1.0 - blend) + photo * blend
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


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
    im = sebastian_layer(PHOTO, strength=0.78)
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


def slide_03_puente_turbo() -> Image.Image:
    """Puente: de la reflexión a delegar / recuperar tiempo."""
    im = add_grain(black_canvas(), seed=91)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(SERIF, 54)
    blocks = [
        ["No necesitás", "más horas en el día."],
        ["Necesitás dejar de hacer", "lo que un agente", "puede hacer por vos."],
    ]
    lh = 68
    gap = 44
    total_h = sum(len(b) for b in blocks) * lh + gap
    y = (H - total_h) // 2 - 50
    for bi, block in enumerate(blocks):
        if bi > 0:
            y += gap
        for line in block:
            tw = draw.textlength(line, font=font)
            draw.text(((W - tw) // 2, y), line, font=font, fill=WHITE)
            y += lh
    draw_firma(draw)
    return im


def slide_04_venta_turbo() -> Image.Image:
    """Oferta Turbo + CTA."""
    im = add_grain(black_canvas(), seed=103)
    draw = ImageDraw.Draw(im)
    font_serif = ImageFont.truetype(SERIF, 52)
    font_cta = ImageFont.truetype(MONO, 28)

    lines = [
        "Turbo busca clientes",
        "por vos 24/7",
        "y se mejora solo.",
    ]
    lh = 66
    total_h = lh * len(lines) + 120
    y0 = (H - total_h) // 2 - 30
    for i, line in enumerate(lines):
        if i == 0:
            # "Turbo" en verde, resto blanco — dibujar por partes
            part_a = "Turbo"
            part_b = " busca clientes"
            fa = ImageFont.truetype(SERIF, 58)
            w_a = draw.textlength(part_a, font=fa)
            w_b = draw.textlength(part_b, font=font_serif)
            x = (W - w_a - w_b) // 2
            draw.text((x, y0), part_a, font=fa, fill=GREEN)
            draw.text((x + w_a, y0), part_b, font=font_serif, fill=WHITE)
        else:
            tw = draw.textlength(line, font=font_serif)
            draw.text(((W - tw) // 2, y0 + i * lh), line, font=font_serif, fill=WHITE)

    cta = "Comentá TURBO"
    tw = draw.textlength(cta, font=font_cta)
    draw.text(((W - tw) // 2, y0 + len(lines) * lh + 48), cta, font=font_cta, fill=GREEN)

    draw_firma(draw)
    return im


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    s1 = slide_01_portada()
    s2 = slide_02_fondo_negro()
    s3 = slide_03_puente_turbo()
    s4 = slide_04_venta_turbo()

    p1 = OUT_DIR / "slide-01-y-si-todo-sale-bien.png"
    p2 = OUT_DIR / "slide-02-esta-en-tu-poder.png"
    p3 = OUT_DIR / "slide-03-puente-turbo.png"
    p4 = OUT_DIR / "slide-04-venta-turbo.png"
    s1.save(p1, optimize=True)
    s2.save(p2, optimize=True)
    s3.save(p3, optimize=True)
    s4.save(p4, optimize=True)
    s1.save(ARTIFACTS / "sebastian-frases-slide-01.png", optimize=True)
    s2.save(ARTIFACTS / "sebastian-frases-slide-02.png", optimize=True)
    s3.save(ARTIFACTS / "sebastian-frases-slide-03.png", optimize=True)
    s4.save(ARTIFACTS / "sebastian-frases-slide-04.png", optimize=True)
    print(f"OK {p1}\nOK {p2}\nOK {p3}\nOK {p4}")


if __name__ == "__main__":
    main()
