# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent
TOTAL = 10
CSS_W, CSS_H = 1080, 1350
DSF = 2


def main():
    png = B / "png"
    jpg = B / "jpg"
    png.mkdir(exist_ok=True)
    jpg.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(viewport={"width": 1180, "height": 1450}, device_scale_factor=DSF)
        pg.goto((B / "carrusel.html").as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(2500)
        frames = pg.query_selector_all(".slide")
        assert len(frames) == TOTAL, len(frames)
        for i, el in enumerate(frames, 1):
            raw = png / f"slide-{i:02d}-raw.png"
            el.screenshot(path=str(raw), type="png", animations="disabled")
            im = Image.open(raw).convert("RGB")
            target = (CSS_W * DSF, CSS_H * DSF)
            if im.size != target:
                im = im.resize(target, Image.Resampling.LANCZOS)
            im = im.filter(ImageFilter.UnsharpMask(radius=0.8, percent=110, threshold=2))
            out = png / f"slide-{i:02d}.png"
            im.save(out, format="PNG", compress_level=1)
            ig = im.resize((CSS_W, CSS_H), Image.Resampling.LANCZOS)
            ig.save(jpg / f"slide-{i:02d}.jpg", format="JPEG", quality=95, subsampling=0, optimize=True)
            raw.unlink(missing_ok=True)
            print("OK", out.name, im.size)
        br.close()


if __name__ == "__main__":
    main()
