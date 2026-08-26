# -*- coding: utf-8 -*-
"""Extrae gráficos diagrama desde screenshots IG 1284×2778 → graphic-XX.orig.png"""
from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image

B = Path(__file__).resolve().parent
ASSETS = B / "assets"
SRC = Path("/home/ubuntu/.cursor/projects/workspace/assets")

# (left, top, right, bottom) — solo diagrama, sin títulos ni footer EN
DIAGRAM_CROPS: dict[int, tuple[int, int, int, int]] = {
    1: (62, 980, 1220, 1680),
    2: (62, 820, 1220, 1680),
    3: (62, 860, 1220, 1680),
    4: (62, 960, 1220, 1680),
    5: (62, 860, 1220, 1720),
    6: (62, 840, 1220, 1680),
    7: (62, 860, 1220, 1720),
    8: (62, 820, 1220, 1450),
}


def main() -> None:
    refs = sorted(SRC.glob("01a0400f-*.jpg"))
    if len(refs) != 8:
        raise SystemExit(f"Expected 8 refs, got {len(refs)}")
    for i, src in enumerate(refs, 1):
        dst_raw = ASSETS / f"ref-slide-{i:02d}-raw.jpg"
        shutil.copy2(src, dst_raw)
        im = Image.open(src).convert("RGBA")
        box = DIAGRAM_CROPS[i]
        crop = im.crop(box)
        orig = ASSETS / f"graphic-{i:02d}.orig.png"
        crop.save(orig, optimize=True)
        print(f"OK {i}: raw → {dst_raw.name}, orig {crop.size}")


if __name__ == "__main__":
    main()
