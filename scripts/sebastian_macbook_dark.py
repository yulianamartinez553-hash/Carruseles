#!/usr/bin/env python3
"""Sebastián + MacBook oscuro — generado de cero, identidad seb.jpg, sin overlays."""
from __future__ import annotations

import shutil
from pathlib import Path

import cv2
import insightface
import numpy as np
from insightface.app import FaceAnalysis
from PIL import Image

SOURCE = Path("/workspace/seb.jpg")
SCENE = Path("/opt/cursor/artifacts/assets/sebastian-macbook-dark-base-v3.png")
OUT_DIR = Path("/workspace/resultados/sebastian-macbook-dark")
SWAPPER = Path("/home/ubuntu/.insightface/models/inswapper_128.onnx")
ARTIFACT = Path("/opt/cursor/artifacts/assets/sebastian-macbook-dark.png")

DARKEN = 0.82
BLUR_BG = 16.0
BLUR_SUBJECT = 1.2


def largest_face(faces: list) -> insightface.app.common.Face:
    return max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))


def crop_4x5(bgr: np.ndarray) -> np.ndarray:
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(rgb)
    w, h = im.size
    target = 4 / 5
    if w / h > target:
        nw = int(h * target)
        im = im.crop(((w - nw) // 2, 0, (w + nw) // 2, h))
    else:
        nh = int(w / target)
        im = im.crop((0, (h - nh) // 2, w, (h + nh) // 2))
    return cv2.cvtColor(np.array(im.resize((1080, 1350), Image.Resampling.LANCZOS)), cv2.COLOR_RGB2BGR)


def apply_depth_blur(bgr: np.ndarray) -> np.ndarray:
    light = cv2.GaussianBlur(bgr, (0, 0), BLUR_SUBJECT).astype(np.float32)
    heavy = cv2.GaussianBlur(bgr, (0, 0), BLUR_BG).astype(np.float32)
    h, w = bgr.shape[:2]
    cx, cy = w * 0.5, h * 0.42
    xs = (np.arange(w, dtype=np.float32) - cx) / (w * 0.52)
    ys = (np.arange(h, dtype=np.float32) - cy) / (h * 0.50)
    dist = np.sqrt(xs[np.newaxis, :] ** 2 + ys[:, np.newaxis] ** 2)
    mask = np.clip((dist - 0.04) / 0.96, 0, 1) ** 1.1
    m3 = mask[..., np.newaxis]
    out = light * (1 - m3) + heavy * m3
    return np.clip(out * DARKEN, 0, 255).astype(np.uint8)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    app = FaceAnalysis(name="buffalo_l")
    app.prepare(ctx_id=-1, det_size=(640, 640))
    swapper = insightface.model_zoo.get_model(str(SWAPPER), providers=["CPUExecutionProvider"])

    source = cv2.imread(str(SOURCE))
    scene = cv2.imread(str(SCENE))
    if source is None or scene is None:
        raise SystemExit("No se pudo leer seb.jpg o la escena")

    src = largest_face(app.get(source))
    tgt = largest_face(app.get(scene))
    swapped = swapper.get(scene.copy(), tgt, src, paste_back=True)
    final = apply_depth_blur(swapped)
    final = crop_4x5(final)

    png = OUT_DIR / "sebastian-macbook-dark.png"
    jpg = OUT_DIR / "sebastian-macbook-dark.jpg"
    cv2.imwrite(str(png), final, [cv2.IMWRITE_PNG_COMPRESSION, 3])
    cv2.imwrite(str(jpg), final, [cv2.IMWRITE_JPEG_QUALITY, 94])
    shutil.copy(png, ARTIFACT)
    print(f"OK {png}")


if __name__ == "__main__":
    main()
