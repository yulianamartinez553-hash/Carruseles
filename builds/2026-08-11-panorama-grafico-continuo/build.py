# -*- coding: utf-8 -*-
"""Render + package del panorama Claude × WhatsApp."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import generate  # noqa: E402
from stlabs_kit import render, package  # noqa: E402

BUILD_ID = "2026-08-11-panorama-grafico-continuo"


def main():
    generate.main()
    pngs = render(BUILD)
    print(f"✓ Render: {len(pngs)} PNGs")

    meta = {
        "id": BUILD_ID,
        "titulo": "Claude WhatsApp Multinivel Ultimo Momento",
        "slides": 4,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "original",
        "keyword_portada": "PDF",
        "notas": "Panorama continuo + copy voseo. CTA Comentá PDF. Sin foto en slides 3–4 densos / CTA.",
    }
    out = package(BUILD, "STLabs-Claude-WhatsApp-Multinivel", meta=meta, output_dir=BUILD)
    print(f"✓ Package → {out}")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
