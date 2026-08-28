# -*- coding: utf-8 -*-
"""Empaqueta entrega: Word/ (4K + FHD), tira preview, ZIP, memoria, artifacts."""
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
WORD = REPO / "Word"
ARTIFACTS = Path("/opt/cursor/artifacts/carrusel-turbo-sistema-blanco")
OUT_NAME = "STLabs-Turbo-Sistema-Blanco"


def preview_tira() -> Path:
    pngs = sorted((B / "png-4k").glob("slide-*.png"))
    if not pngs:
        pngs = sorted((B / "png").glob("slide-*.png"))
    ims = [Image.open(p) for p in pngs]
    w, h = ims[0].size
    sc = 400
    strip = Image.new("RGB", (sc * len(ims), int(h * sc / w)), (10, 10, 10))
    for i, im in enumerate(ims):
        strip.paste(im.resize((sc, int(h * sc / w)), Image.Resampling.LANCZOS), (i * sc, 0))
    dest = B / "_preview-tira.png"
    strip.save(dest, optimize=True)
    return dest


def main() -> None:
    meta = json.loads((B / "content.json").read_text(encoding="utf-8"))
    preview_tira()

    png4k = sorted((B / "png-4k").glob("slide-*.png"))
    png_fhd = sorted((B / "png-fhd").glob("slide-*.png"))
    jpg4k = sorted((B / "jpg").glob("slide-*@4k.jpg"))
    jpg_fhd = sorted((B / "jpg").glob("slide-*@fhd.jpg"))
    html = B / "carrusel.html"

    if WORD.exists():
        shutil.rmtree(WORD)
    WORD.mkdir(parents=True)
    (WORD / "4k").mkdir()
    (WORD / "fhd").mkdir()

    for p in png4k:
        shutil.copy(p, WORD / "4k" / p.name)
        shutil.copy(p, WORD / p.name)
    for p in png_fhd:
        shutil.copy(p, WORD / "fhd" / p.name)
    for p in jpg4k:
        shutil.copy(p, WORD / "4k" / p.name)
    for p in jpg_fhd:
        shutil.copy(p, WORD / "fhd" / p.name)

    shutil.copy(B / "_preview-tira.png", WORD / "_preview-tira.png")
    shutil.copy(html, WORD / f"{OUT_NAME}.html")
    shutil.copy(B / "caption.txt", WORD / "caption.txt")
    shutil.copy(B / "MANIFIESTO-FUENTES.md", WORD / "MANIFIESTO-FUENTES.md")
    shutil.copy(B / "content.json", WORD / "content.json")
    shutil.copy(B / "manifest.json", WORD / "manifest.json")
    if (REPO / "assets" / "turbo" / "turbo-mascot.png").exists():
        shutil.copy(REPO / "assets" / "turbo" / "turbo-mascot.png", WORD / "turbo-mascot.png")

    slides = meta.get("slides", len(png4k))
    (WORD / "LEEME.txt").write_text(
        "\n".join(
            [
                "STLabs — Sistema Turbo (fondo negro)",
                "Dashboard técnico → sebastian.stlabs.ar",
                f"Slides: {slides} · Keyword: {meta['keyword_portada']}",
                "",
                "Resoluciones:",
                "  slide-XX.png + 4k/  → 4320×5400 PNG (4K, máxima calidad)",
                "  fhd/slide-XX.png    → 1920×2400 PNG (Full HD)",
                "  4k/slide-XX@4k.jpg  → JPEG 4K · fhd/slide-XX@fhd.jpg → JPEG FHD",
                "",
                "Accent #00FFB2 · Solo español",
                "",
            ]
        ),
        encoding="utf-8",
    )

    zip_path = WORD / f"{OUT_NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in png4k:
            zf.write(p, f"4k/{p.name}")
        for p in png_fhd:
            zf.write(p, f"fhd/{p.name}")
        for p in jpg4k:
            zf.write(p, f"4k/{p.name}")
        for p in jpg_fhd:
            zf.write(p, f"fhd/{p.name}")
        zf.write(WORD / f"{OUT_NAME}.html", f"{OUT_NAME}.html")
        zf.write(WORD / "caption.txt", "caption.txt")
        zf.write(WORD / "MANIFIESTO-FUENTES.md", "MANIFIESTO-FUENTES.md")
        zf.write(WORD / "LEEME.txt", "LEEME.txt")

    registrar_carrusel(B, meta)

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    shutil.copy(B / "_preview-tira.png", ARTIFACTS / "tira-preview.png")
    for p in png4k:
        shutil.copy(p, ARTIFACTS / p.name)

    print("OK Word/ →", WORD)
    if png4k:
        im = Image.open(png4k[0])
        print("OK 4K", im.size, "· FHD", Image.open(png_fhd[0]).size if png_fhd else "—")
    print("OK memoria →", meta["id"])
    print("OK artifacts →", ARTIFACTS)


if __name__ == "__main__":
    main()
