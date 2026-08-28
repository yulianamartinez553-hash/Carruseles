# -*- coding: utf-8 -*-
"""Render 4K HQ — captura nativa 4× (4320×5400) + Full HD (1920×2400)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 10
CSS_W, CSS_H = 1080, 1350
DSF = 4  # captura nativa → 4320×5400 (4K vertical IG)
SIZE_4K = (CSS_W * DSF, CSS_H * DSF)
FHD = (1920, 2400)


def polish(im: Image.Image, sharp: float = 1.06) -> Image.Image:
    im = ImageEnhance.Contrast(im).enhance(1.015)
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
                "--font-render-hinting=none",
                "--disable-lcd-text",
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
                '400 72px \"Bebas Neue\"',
                '700 32px \"Barlow Condensed\"',
                '600 18px \"IBM Plex Mono\"'
              ];
              for (const f of loads) await document.fonts.load(f).catch(() => null);
              await document.fonts.ready;
            }"""
        )
        page.wait_for_timeout(1600)
        slides = page.query_selector_all(".slide")
        assert len(slides) == TOTAL, f"expected {TOTAL}, got {len(slides)}"
        for i, el in enumerate(slides, 1):
            raw = png4k / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled", scale="device")
            im = Image.open(raw).convert("RGB")
            if im.size != SIZE_4K:
                im = im.resize(SIZE_4K, Image.Resampling.LANCZOS)
            im = polish(im, sharp=1.04)

            save_png(im, png4k / f"slide-{i:02d}.png")
            save_png(im, png / f"slide-{i:02d}.png")  # master = 4K

            hd = im.resize(FHD, Image.Resampling.LANCZOS)
            hd = polish(hd, sharp=1.08)
            save_png(hd, fhd_dir / f"slide-{i:02d}.png")

            im.save(jpg / f"slide-{i:02d}@4k.jpg", "JPEG", quality=98, subsampling=0, optimize=True)
            hd.save(jpg / f"slide-{i:02d}@fhd.jpg", "JPEG", quality=98, subsampling=0, optimize=True)

            raw.unlink(missing_ok=True)
            print("OK", f"slide-{i:02d}", "4K", im.size, "| FHD", hd.size)
        browser.close()


if __name__ == "__main__":
    main()
