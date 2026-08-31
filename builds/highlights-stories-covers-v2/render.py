# -*- coding: utf-8 -*-
from pathlib import Path
from playwright.sync_api import sync_playwright
import json

B = Path(__file__).resolve().parent


def main():
    covers = json.loads((B / "index.json").read_text(encoding="utf-8"))
    png = B / "png"
    png.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(viewport={"width": 1200, "height": 2200}, device_scale_factor=2)
        pg.goto((B / "covers.html").as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(2500)
        slides = pg.query_selector_all(".slide")
        assert len(slides) == len(covers)
        for i, (c, el) in enumerate(zip(covers, slides), 1):
            name = f"{i:02d}-{c['id']}.png"
            el.screenshot(path=str(png / name))
            print("OK", name)
        br.close()


if __name__ == "__main__":
    main()
