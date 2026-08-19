# -*- coding: utf-8 -*-
"""Render retina 3x (3240×4050) y JPEG Instagram 1080×1350 alta calidad."""
from pathlib import Path
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 6
CSS_W, CSS_H = 1080, 1350
DSF = 3  # 3240×4050


def main():
    png_dir = B / "png"
    jpg_dir = B / "jpg"
    png_dir.mkdir(exist_ok=True)
    jpg_dir.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(
            viewport={"width": 1180, "height": 1450},
            device_scale_factor=DSF,
        )
        pg.goto((B / "carrusel.html").as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.evaluate(
            """async () => {
              await Promise.all([
                document.fonts.load("800 120px Playfair"),
                document.fonts.load("italic 700 64px Playfair"),
                document.fonts.load("italic 800 72px Playfair"),
                document.fonts.load("800 58px Playfair"),
                document.fonts.load("700 28px Poppins"),
              ]);
            }"""
        )
        pg.wait_for_timeout(1500)
        slides = pg.query_selector_all(".slide")
        assert len(slides) == TOTAL, len(slides)
        for i, el in enumerate(slides, 1):
            raw = png_dir / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled")
            im = Image.open(raw).convert("RGB")
            if im.size != (CSS_W * DSF, CSS_H * DSF):
                im = im.resize((CSS_W * DSF, CSS_H * DSF), Image.Resampling.LANCZOS)
            # Nítido: el glow CSS ya no usa filter:blur; unsharp en 3 y 4 (serif grande)
            if i in (3, 4):
                im = im.filter(ImageFilter.UnsharpMask(radius=1.4, percent=145, threshold=1))
            else:
                im = im.filter(ImageFilter.UnsharpMask(radius=0.8, percent=110, threshold=2))
            out_png = png_dir / f"slide-{i:02d}.png"
            im.save(out_png, format="PNG", compress_level=1)
            ig = im.resize((CSS_W, CSS_H), Image.Resampling.LANCZOS)
            if i in (3, 4):
                ig = ig.filter(ImageFilter.UnsharpMask(radius=0.9, percent=160, threshold=1))
            ig.save(
                jpg_dir / f"slide-{i:02d}.jpg",
                format="JPEG",
                quality=98,
                subsampling=0,
                optimize=True,
            )
            raw.unlink(missing_ok=True)
            print("OK", out_png.name, im.size, f"{out_png.stat().st_size/1024:.0f}KB")
        br.close()


if __name__ == "__main__":
    main()
