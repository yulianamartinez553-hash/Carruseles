# -*- coding: utf-8 -*-
"""Extrae SOLO elementos visuales 3D (robots, cerebro) desde refs IG — sin texto EN."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

B = Path(__file__).resolve().parent
ASSETS = B / "assets"
OUT = ASSETS / "elements"
OUT.mkdir(exist_ok=True)

# Recorte sobre ref-slide-XX-raw.jpg (1284×2778) — solo silueta del robot, sin labels EN
REF_CROPS: dict[str, tuple[str, tuple[int, int, int, int]]] = {
    "robot-metricas.png": ("ref-slide-03-raw.jpg", (115, 1145, 395, 1430)),
    "robot-agent.png": ("ref-slide-04-raw.jpg", (155, 1145, 395, 1430)),
    "robot-critico.png": ("ref-slide-04-raw.jpg", (790, 1125, 1170, 1415)),
    "robot-v1.png": ("ref-slide-06-raw.jpg", (130, 1110, 370, 1345)),
    "robot-v2.png": ("ref-slide-06-raw.jpg", (855, 1100, 1125, 1345)),
    "robot-vs-old.png": ("ref-slide-07-raw.jpg", (55, 1065, 310, 1395)),
    "robot-vs-new.png": ("ref-slide-07-raw.jpg", (755, 1055, 960, 1395)),
}

CEREBRO_BOX = (8, (455, 120, 665, 280))


def trim_alpha(im: Image.Image, thresh: int = 22, pad: int = 4) -> Image.Image:
    """Recorta al contenido visible (robot) con margen mínimo."""
    arr = np.array(im.convert("RGBA"))
    rgb = arr[:, :, :3].astype(int)
    bright = rgb.max(axis=2) > thresh
    ys, xs = np.where(bright)
    if len(xs) == 0:
        return im
    l, t, r, b = xs.min(), ys.min(), xs.max(), ys.max()
    return im.crop(
        (
            max(0, l - pad),
            max(0, t - pad),
            min(arr.shape[1], r + pad),
            min(arr.shape[0], b + pad),
        )
    )


def black_to_alpha(im: Image.Image, thresh: int = 24) -> Image.Image:
    arr = np.array(im.convert("RGBA"))
    bright = arr[:, :, :3].max(axis=2) > thresh
    arr[:, :, 3] = np.where(bright, 255, 0).astype(np.uint8)
    return Image.fromarray(arr)


def main() -> None:
    for name, (ref_name, box) in REF_CROPS.items():
        src = ASSETS / ref_name
        crop = trim_alpha(Image.open(src).convert("RGBA").crop(box))
        crop.save(OUT / name, optimize=True)
        print(f"OK {name} <- {ref_name} {crop.size}")

    num, box = CEREBRO_BOX
    cerebro = black_to_alpha(Image.open(ASSETS / f"graphic-{num:02d}.orig.png").convert("RGBA").crop(box))
    cerebro.save(OUT / "cerebro.png", optimize=True)
    print(f"OK cerebro.png <- G{num} {cerebro.size}")


if __name__ == "__main__":
    main()
