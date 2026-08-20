# -*- coding: utf-8 -*-
"""Render + package — Agente simplifica procesos."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import generate  # noqa: E402
from stlabs_kit import package, render  # noqa: E402

BUILD_ID = "2026-08-20-agente-simplifica-procesos"


def main() -> None:
    generate.main()
    pngs = render(BUILD)
    print(f"✓ Render: {len(pngs)} PNGs")

    meta = {
        "id": BUILD_ID,
        "titulo": "Agente Simplifica Procesos",
        "slides": 8,
        "fondo": "reticula_fina",
        "familia_visual": "before_after",
        "origen": "screenshot",
        "keyword_portada": "PROCESOS",
        "notas": "Modo negro + retícula verde. Portada Sebastián B&W. CTA Comentá PROCESOS.",
    }
    out = package(BUILD, "STLabs-Agente-Simplifica-Procesos", meta=meta, output_dir=BUILD)
    print(f"✓ Package → {out}")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
