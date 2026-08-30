# -*- coding: utf-8 -*-
"""Render 4K HQ — supersampling 5× → 4320×5400 + Full HD 1920×2400."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 2
CSS_W, CSS_H = 1080, 1350
DSF = 5  # oversampling: 5400×6750 → downscale nítido a 4K
CAPTURE = (CSS_W * DSF, CSS_H * DSF)
SIZE_4K = (CSS_W * 4, CSS_H * 4)  # 4320×5400
FHD = (1920, 2400)


def polish(im: Image.Image, sharp: float = 1.05) -> Image.Image:
    im = ImageEnhance.Contrast(im).enhance(1.01)
    im = ImageEnhance.Sharpness(im).enhance(sharp)
    return im


def save_png(im: Image.Image, path: Path) -> None:
    im.save(path, "PNG", compress_level=1, optimize=False)


def main() -> None:
    png = B / "png"
    png4k = B / "png-4k"
    fhd_dir = B / "png-fhd"
    jpg = B / "jpg"
    for d in (png, png4k, fhd_dir, jpg):
        d.mkdir(exist_ok=True)
    html = B / "carrusel.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--font-render-hinting=medium",
                "--force-device-scale-factor=1",
            ]
        )
        page = browser.new_page(
            viewport={"width": CSS_W, "height": CSS_H},
            device_scale_factor=DSF,
        )
        page.goto(html.resolve().as_uri(), wait_until="networkidle")
        page.evaluate(
            """async () => {
              await document.fonts.ready;
              const loads = [
                '400 110px Impact',
                '400 80px Anton',
                '400 72px \"Bebas Neue\"',
                '700 34px \"Barlow Condensed\"',
                '600 20px \"IBM Plex Mono\"'
              ];
              for (const f of loads) await document.fonts.load(f).catch(() => null);
              await document.fonts.ready;
            }"""
        )
        page.wait_for_timeout(2000)
        slides = page.query_selector_all(".slide")
        assert len(slides) == TOTAL, f"expected {TOTAL}, got {len(slides)}"
        for i, el in enumerate(slides, 1):
            raw = png4k / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled", scale="device")
            im = Image.open(raw).convert("RGB")
            if im.size != CAPTURE:
                im = im.resize(CAPTURE, Image.Resampling.LANCZOS)
            # Downscale supersampled capture → 4K nativo
            im4k = im.resize(SIZE_4K, Image.Resampling.LANCZOS)
            im4k = polish(im4k, sharp=1.06)

            save_png(im4k, png4k / f"slide-{i:02d}.png")
            save_png(im4k, png / f"slide-{i:02d}.png")

            hd = im4k.resize(FHD, Image.Resampling.LANCZOS)
            hd = polish(hd, sharp=1.1)
            save_png(hd, fhd_dir / f"slide-{i:02d}.png")

            im4k.save(jpg / f"slide-{i:02d}@4k.jpg", "JPEG", quality=99, subsampling=0, optimize=True)
            hd.save(jpg / f"slide-{i:02d}@fhd.jpg", "JPEG", quality=99, subsampling=0, optimize=True)

            raw.unlink(missing_ok=True)
            print("OK", f"slide-{i:02d}", "capture", CAPTURE, "→ 4K", im4k.size, "FHD", hd.size)
        browser.close()


if __name__ == "__main__":
    main()
