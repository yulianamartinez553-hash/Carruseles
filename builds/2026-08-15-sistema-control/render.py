# -*- coding: utf-8 -*-
from pathlib import Path
from playwright.sync_api import sync_playwright

B = Path(__file__).resolve().parent


def main():
    png = B / "png"
    png.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(viewport={"width": 1180, "height": 1450}, device_scale_factor=2)
        pg.goto((B / "carrusel.html").as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(4000)
        slides = pg.query_selector_all(".slide")
        assert len(slides) == 10, len(slides)
        for i, el in enumerate(slides, 1):
            el.screenshot(path=str(png / f"slide-{i:02d}.png"))
            print("OK", f"slide-{i:02d}.png")
        br.close()


if __name__ == "__main__":
    main()
