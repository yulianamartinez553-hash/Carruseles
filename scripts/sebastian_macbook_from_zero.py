#!/usr/bin/env python3
"""Sebastián (seb.jpg) + fondo cinematográfico + MacBook. Pipeline mínimo."""
from __future__ import annotations

from pathlib import Path

import cv2
import insightface
import numpy as np
from insightface.app import FaceAnalysis
from PIL import Image

SOURCE = Path("/workspace/seb.jpg")
SCENE = Path("/opt/cursor/artifacts/assets/sebastian-macbook-v2-base.png")
OUT_DIR = Path("/workspace/resultados/sebastian-cafe-cinematic")
SWAPPER = Path("/home/ubuntu/.insightface/models/inswapper_128.onnx")


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))


def largest_face(faces: list) -> insightface.app.common.Face:
    return max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))


def crop_6x7(bgr: np.ndarray) -> np.ndarray:
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(rgb)
    w, h = im.size
    target = 6 / 7
    if w / h > target:
        nw = int(h * target)
        im = im.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
    else:
        nh = int(w / target)
        im = im.crop((0, (h - nh) // 2, w, (h + nh) // 2))
    return cv2.cvtColor(np.array(im.resize((1080, 1260), Image.Resampling.LANCZOS)), cv2.COLOR_RGB2BGR)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    app = FaceAnalysis(name="buffalo_l")
    app.prepare(ctx_id=-1, det_size=(640, 640))
    swapper = insightface.model_zoo.get_model(str(SWAPPER), providers=["CPUExecutionProvider"])

    source = cv2.imread(str(SOURCE))
    scene = cv2.imread(str(SCENE))
    if source is None or scene is None:
        raise SystemExit(f"No se pudo leer {SOURCE} o {SCENE}")

    src = largest_face(app.get(source))
    tgt = largest_face(app.get(scene))
    src_emb = src.embedding

    out = swapper.get(scene.copy(), tgt, src, paste_back=True)
    faces = app.get(out)
    sim = cosine(src_emb, largest_face(faces).embedding) if faces else 0.0
    print(f"identidad post-swap: {sim:.4f}")

    final_bgr = crop_6x7(out)
    png = OUT_DIR / "sebastian-cinematic-macbook-photo.png"
    jpg = OUT_DIR / "sebastian-cinematic-macbook-photo.jpg"
    cv2.imwrite(str(png), final_bgr, [cv2.IMWRITE_PNG_COMPRESSION, 3])
    cv2.imwrite(str(jpg), final_bgr, [cv2.IMWRITE_JPEG_QUALITY, 94])
    print(f"OK {png}")


if __name__ == "__main__":
    main()
