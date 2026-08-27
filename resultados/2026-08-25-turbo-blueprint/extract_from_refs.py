# -*- coding: utf-8 -*-
"""Re-extrae gráficos diagrama desde ref-slide-XX-raw.jpg → graphic-XX.orig.png"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

B = Path(__file__).resolve().parent
ASSETS = B / "assets"

# (left, top, right, bottom) — solo diagrama visual, sin título ni footer EN
DIAGRAM_CROPS: dict[int, tuple[int, int, int, int]] = {
    1: (62, 980, 1180, 1680),
    2: (62, 820, 1220, 1680),
    3: (62, 860, 1220, 1680),
    4: (62, 960, 1220, 1680),
    5: (62, 860, 1220, 1720),
    6: (62, 840, 1220, 1680),
    7: (62, 860, 1220, 1720),
    8: (62, 820, 1220, 1450),
}


def main() -> None:
    for i, box in DIAGRAM_CROPS.items():
        src = ASSETS / f"ref-slide-{i:02d}-raw.jpg"
        im = Image.open(src).convert("RGBA")
        crop = im.crop(box)
        out = ASSETS / f"graphic-{i:02d}.orig.png"
        crop.save(out, optimize=True)
        print(f"OK {i}: {crop.size} → {out.name}")


if __name__ == "__main__":
    main()
