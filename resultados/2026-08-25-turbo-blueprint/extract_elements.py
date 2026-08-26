# -*- coding: utf-8 -*-
"""Extrae SOLO elementos visuales 3D (robots, cerebro) — sin texto EN."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

B = Path(__file__).resolve().parent
ASSETS = B / "assets"
OUT = ASSETS / "elements"
OUT.mkdir(exist_ok=True)

# (graphic_num, box) — recorte ajustado para excluir labels EN
CROPS: dict[str, tuple[int, tuple[int, int, int, int]]] = {
    "robot-agent.png": (4, (115, 195, 305, 415)),
    "robot-critico.png": (4, (755, 130, 1105, 395)),
    "robot-metricas.png": (3, (95, 300, 295, 580)),
    "robot-v1.png": (6, (125, 275, 315, 485)),
    "robot-v2.png": (6, (865, 235, 1055, 445)),
    "robot-vs-old.png": (7, (95, 210, 285, 430)),
    "robot-vs-new.png": (7, (815, 200, 1005, 420)),
    "cerebro.png": (8, (455, 120, 665, 280)),
}


def main() -> None:
    for name, (num, box) in CROPS.items():
        src = ASSETS / f"graphic-{num:02d}.orig.png"
        im = Image.open(src).convert("RGBA")
        crop = im.crop(box)
        crop.save(OUT / name, optimize=True)
        print(f"OK {name} <- G{num} {crop.size}")


if __name__ == "__main__":
    main()
