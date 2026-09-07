# -*- coding: utf-8 -*-
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
ARTIFACTS = Path("/opt/cursor/artifacts/carrusel-stack-lanzar-ia")
OUT_NAME = "STLabs-Stack-Lanzar-IA"


def preview_tira() -> Path:
    pngs = sorted((B / "png").glob("slide-*.png"))
    pngs = [p for p in pngs if "-raw" not in p.name]
    ims = [Image.open(p) for p in pngs]
    w, h = ims[0].size
    sc = 280
    strip = Image.new("RGB", (sc * len(ims), int(h * sc / w)), (237, 232, 220))
    for i, im in enumerate(ims):
        strip.paste(im.resize((sc, int(h * sc / w)), Image.Resampling.LANCZOS), (i * sc, 0))
    dest = B / "_preview-tira.png"
    strip.save(dest, optimize=True)
    return dest


def main() -> None:
    meta = json.loads((B / "content.json").read_text(encoding="utf-8"))
    preview_tira()
    pngs = [p for p in sorted((B / "png").glob("slide-*.png")) if "-raw" not in p.name]
    png4k = sorted((B / "png-4k").glob("slide-*.png"))
    png_fhd = sorted((B / "png-fhd").glob("slide-*.png"))

    if WORD.exists():
        shutil.rmtree(WORD)
    WORD.mkdir(parents=True)
    (WORD / "4k").mkdir()
    (WORD / "fhd").mkdir()

    for p in pngs:
        shutil.copy(p, WORD / p.name)
    for p in png4k:
        shutil.copy(p, WORD / "4k" / p.name)
    for p in png_fhd:
        shutil.copy(p, WORD / "fhd" / p.name)

    shutil.copy(B / "_preview-tira.png", WORD / "_preview-tira.png")
    shutil.copy(B / "carrusel.html", WORD / f"{OUT_NAME}.html")
    for fn in ("caption.txt", "MANIFIESTO-FUENTES.md", "content.json", "manifest.json"):
        if (B / fn).exists():
            shutil.copy(B / fn, WORD / fn)

    (WORD / "LEEME.txt").write_text(
        "STLabs — El stack para lanzar apps (12 slides)\n"
        "Clon referencia · logos recortados · sebastian.stlabs.ar\n",
        encoding="utf-8",
    )

    # ZIP solo retina (evita >100MB)
    zip_path = WORD / f"{OUT_NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in pngs:
            zf.write(p, p.name)
        zf.write(WORD / f"{OUT_NAME}.html", f"{OUT_NAME}.html")
        zf.write(WORD / "caption.txt", "caption.txt")
        zf.write(WORD / "MANIFIESTO-FUENTES.md", "MANIFIESTO-FUENTES.md")

    registrar_carrusel(B, meta)

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS / "4k").mkdir(exist_ok=True)
    shutil.copy(B / "_preview-tira.png", ARTIFACTS / "tira-preview.png")
    for p in pngs:
        shutil.copy(p, ARTIFACTS / p.name)
    for p in png4k:
        shutil.copy(p, ARTIFACTS / "4k" / p.name)

    print("OK Word/ →", WORD)
    print("OK memoria →", meta["id"])
    print("OK artifacts →", ARTIFACTS)


if __name__ == "__main__":
    main()
