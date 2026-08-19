# -*- coding: utf-8 -*-
"""Empaqueta historias 9:16 → resultados/ + artifacts + memoria STLabs."""
from pathlib import Path
import json
import shutil
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from stlabs_memory import registrar_carrusel, validar_meta, resolve_build_id

B = Path(__file__).resolve().parent
RID = "2026-08-19-historias-proceso"
OUT = ROOT / "resultados" / RID
ART = Path("/opt/cursor/artifacts/historias-proceso")


def main():
    meta = json.loads((B / "manifest.json").read_text(encoding="utf-8"))
    validar_meta(meta)
    resolve_build_id(meta, "STLabs-historias-proceso")

    for d in (OUT, ART):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    files = [
        B / "historias.html",
        B / "historias.txt",
        B / "generate.py",
        B / "render.py",
        B / "MANIFIESTO-FUENTES.md",
        B / "manifest.json",
        B / "index.json",
        B / "_preview-tira.png",
    ]
    for src in files:
        if src.exists():
            shutil.copy(src, OUT / src.name)
            shutil.copy(src, ART / src.name)

    for folder in ("png-1080", "png-retina", "jpg"):
        src = B / folder
        if not src.exists():
            continue
        shutil.copytree(src, OUT / folder)
        shutil.copytree(src, ART / folder)

    # atajos en la raíz de entrega (1080 listos para subir)
    for p in sorted((B / "png-1080").glob("historia-*.png")):
        shutil.copy(p, OUT / p.name)
        shutil.copy(p, ART / p.name)
    for p in sorted((B / "jpg").glob("historia-*.jpg")):
        shutil.copy(p, OUT / p.name)
        shutil.copy(p, ART / p.name)

    zip_path = OUT / "STLabs-historias-proceso.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted((B / "png-1080").glob("historia-*.png")):
            zf.write(p, f"png-1080/{p.name}")
        for p in sorted((B / "png-retina").glob("historia-*.png")):
            zf.write(p, f"png-retina/{p.name}")
        for p in sorted((B / "jpg").glob("historia-*.jpg")):
            zf.write(p, f"jpg/{p.name}")
        zf.write(B / "historias.html", "historias.html")
        zf.write(B / "historias.txt", "historias.txt")
        zf.write(B / "MANIFIESTO-FUENTES.md", "MANIFIESTO-FUENTES.md")
    shutil.copy(zip_path, ART / zip_path.name)

    dest = registrar_carrusel(B, meta)
    print("packaged", OUT)
    print("artifacts", ART)
    print("memoria", dest)


if __name__ == "__main__":
    main()
