# -*- coding: utf-8 -*-
"""Pipeline completo: extrae refs → genera HTML → render → QA → package."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

B = Path(__file__).resolve().parent
PY = sys.executable

STEPS = [
    "extract_from_refs.py",
    "edit_graphics.py",
    "generate.py",
    "render.py",
    "qa_overlap.py",
    "package.py",
]


def main() -> None:
    for script in STEPS:
        print(f"\n=== {script} ===")
        subprocess.run([PY, str(B / script)], check=True, cwd=B)
    print("\nOK pipeline completo")


if __name__ == "__main__":
    main()
