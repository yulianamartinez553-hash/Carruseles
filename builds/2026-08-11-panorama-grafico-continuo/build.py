# -*- coding: utf-8 -*-
"""Render + package del panorama gráfico continuo."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import generate  # noqa: E402
from stlabs_kit import render, package  # noqa: E402
from stlabs_memory import load_index, save_index  # noqa: E402

BUILD_ID = "2026-08-11-panorama-grafico-continuo"


def cleanup_bad_slug():
    """Elimina el id mal slugificado (acentos → guiones) de un package previo."""
    bad = REPO / "builds" / "2026-08-11-panorama-gr-fico-continuo"
    if bad.exists():
        shutil.rmtree(bad)
    idx = load_index()
    idx["carruseles"] = [c for c in idx["carruseles"] if c.get("id") != "2026-08-11-panorama-gr-fico-continuo"]
    if idx.get("ultimo_id") == "2026-08-11-panorama-gr-fico-continuo":
        idx["ultimo_id"] = idx["carruseles"][-1]["id"] if idx["carruseles"] else None
    save_index(idx)


def main():
    cleanup_bad_slug()
    generate.main()
    pngs = render(BUILD)
    print(f"✓ Render: {len(pngs)} PNGs")

    meta = {
        "id": BUILD_ID,
        "titulo": "Panorama Grafico Continuo",
        "slides": 5,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "original",
        "keyword_portada": "CONTINUO",
        "notas": "Solo fondo grafico + firma. Sin copy. Continuidad panoramica entre slides.",
    }
    out = package(BUILD, "STLabs-Panorama-Grafico-Continuo", meta=meta, output_dir=BUILD)
    print(f"✓ Package → {out}")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
