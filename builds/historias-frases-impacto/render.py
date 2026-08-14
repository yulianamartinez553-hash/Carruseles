# -*- coding: utf-8 -*-
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
from PIL import Image

B = Path(__file__).resolve().parent


def main():
    stories = json.loads((B / "index.json").read_text(encoding="utf-8"))
    png_retina = B / "png-retina"
    png_upload = B / "png-1080"
    png_retina.mkdir(exist_ok=True)
    png_upload.mkdir(exist_ok=True)

    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(viewport={"width": 1200, "height": 2200}, device_scale_factor=2)
        pg.goto((B / "historias.html").as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(2500)
        slides = pg.query_selector_all(".slide")
        assert len(slides) == len(stories), f"{len(slides)} vs {len(stories)}"
        for i, (c, el) in enumerate(zip(stories, slides), 1):
            name = f"{i:02d}-{c['id']}.png"
            path = png_retina / name
            el.screenshot(path=str(path))
            img = Image.open(path)
            img.resize((1080, 1920), Image.Resampling.LANCZOS).save(
                png_upload / name, optimize=True
            )
            print("OK", name, img.size, "→ 1080x1920")
        br.close()


if __name__ == "__main__":
    main()
