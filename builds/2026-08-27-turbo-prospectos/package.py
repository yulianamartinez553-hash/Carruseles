# -*- coding: utf-8 -*-
"""Empaqueta entrega: Word/, tira preview, ZIP, memoria, artifacts."""
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
ARTIFACTS = Path("/opt/cursor/artifacts/carrusel-turbo-prospectos")
OUT_NAME = "STLabs-Turbo-Prospectos"


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


def main() -> None:
    meta = json.loads((B / "content.json").read_text(encoding="utf-8"))
    preview_tira()

    png_retina = sorted((B / "png").glob("slide-*.png"))
    html = B / "carrusel.html"

    if WORD.exists():
        shutil.rmtree(WORD)
    WORD.mkdir(parents=True)

    for p in png_retina:
        shutil.copy(p, WORD / p.name)
    shutil.copy(B / "_preview-tira.png", WORD / "_preview-tira.png")
    shutil.copy(html, WORD / f"{OUT_NAME}.html")
    shutil.copy(B / "caption.txt", WORD / "caption.txt")
    shutil.copy(B / "MANIFIESTO-FUENTES.md", WORD / "MANIFIESTO-FUENTES.md")
    shutil.copy(B / "content.json", WORD / "content.json")
    shutil.copy(B / "manifest.json", WORD / "manifest.json")

    (WORD / "LEEME.txt").write_text(
        "\n".join(
            [
                "STLabs — Turbo busca prospectos",
                "Clone blueprint → sebastian.stlabs.ar",
                f"Slides: {meta['slides']} · Keyword: {meta['keyword_portada']}",
                "Accent #00FFB2 · Fondo negro (lino_tela) · Solo español",
                "Cierre: Turbo + especialización 1ª persona (Sebastián)",
                "",
            ]
        ),
        encoding="utf-8",
    )

    zip_path = WORD / f"{OUT_NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in png_retina:
            zf.write(p, p.name)
        zf.write(WORD / f"{OUT_NAME}.html", f"{OUT_NAME}.html")
        zf.write(WORD / "caption.txt", "caption.txt")
        zf.write(WORD / "MANIFIESTO-FUENTES.md", "MANIFIESTO-FUENTES.md")

    registrar_carrusel(B, meta)

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    shutil.copy(B / "_preview-tira.png", ARTIFACTS / "tira-preview.png")
    for i in range(1, 9):
        shutil.copy(B / "png" / f"slide-{i:02d}.png", ARTIFACTS / f"slide-{i:02d}.png")

    print("OK Word/ →", WORD)
    print("OK memoria →", meta["id"])
    print("OK artifacts →", ARTIFACTS)


if __name__ == "__main__":
    main()
