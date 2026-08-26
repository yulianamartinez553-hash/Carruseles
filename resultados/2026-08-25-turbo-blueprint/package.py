# -*- coding: utf-8 -*-
"""Empaqueta entrega: tira preview, ZIPs, resultados/ y memoria."""
from __future__ import annotations

import json
import shutil
import sys
import zipfile
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from stlabs_memory import registrar_carrusel

B = Path(__file__).resolve().parent
OUT = REPO / "resultados" / "2026-08-25-turbo-blueprint"


def preview_tira() -> Path:
    pngs = sorted((B / "png").glob("slide-*.png"))
    ims = [Image.open(p) for p in pngs]
    w, h = ims[0].size
    sc = 400
    strip = Image.new("RGB", (sc * len(ims), int(h * sc / w)), (10, 10, 10))
    for i, im in enumerate(ims):
        strip.paste(im.resize((sc, int(h * sc / w)), Image.Resampling.LANCZOS), (i * sc, 0))
    dest = B / "_preview-tira.png"
    strip.save(dest)
    return dest


def zip_dir(name: str, files: list[Path], root: Path) -> Path:
    zpath = root / name
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, f.name)
    return zpath


def main() -> None:
    meta = json.loads((B / "manifest.json").read_text(encoding="utf-8"))
    preview_tira()

    png_retina = sorted((B / "png").glob("slide-*.png"))
    png_fhd = sorted((B / "png-fhd").glob("slide-*.png"))
    png_4k = sorted((B / "png-4k").glob("slide-*.png"))
    html = B / "carrusel.html"

    zip_dir(
        "STLabs-turbo-blueprint.zip",
        png_retina + [html, B / "caption.txt", B / "MANIFIESTO-FUENTES.md"],
        B,
    )
    zip_dir("STLabs-turbo-blueprint-FHD.zip", png_fhd, B)
    zip_dir("STLabs-turbo-blueprint-4K.zip", png_4k, B)

    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(
        B,
        OUT,
        ignore=shutil.ignore_patterns("*.pyc", "__pycache__", "html", "debug*", "debug"),
    )

    registrar_carrusel(B, meta)

    artifacts = Path("/opt/cursor/artifacts")
    artifacts.mkdir(parents=True, exist_ok=True)
    d = artifacts / "turbo-blueprint"
    d.mkdir(exist_ok=True)
    shutil.copy(B / "_preview-tira.png", d / "tira-preview.png")
    for i in range(1, 9):
        shutil.copy(B / "png" / f"slide-{i:02d}.png", d / f"slide-{i:02d}.png")

    print("OK package →", OUT)
    print("OK memoria →", meta["id"])


if __name__ == "__main__":
    main()
