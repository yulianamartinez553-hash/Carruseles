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
        assert len(slides) == 7, len(slides)
        for i, el in enumerate(slides, 1):
            path = png / f"slide-{i:02d}.png"
            el.screenshot(path=str(path))
            print("OK", path.name)
        # QA overlaps (texto vs texto)
        overlaps = pg.evaluate("""() => {
          const slides = [...document.querySelectorAll('.slide')];
          const bad = [];
          for (const s of slides) {
            const texts = [...s.querySelectorAll('h1,p,div.brand,div.badge,div.foot-url,div.foot-topic,div.cta-box,div.step-num,div.step-lab,b,span.script-inline')]
              .map(el => {
                const r = el.getBoundingClientRect();
                const sr = s.getBoundingClientRect();
                return {id: s.dataset.id, t: (el.innerText||'').slice(0,40),
                  x:r.x-sr.x, y:r.y-sr.y, w:r.width, h:r.height};
              }).filter(b => b.w>2 && b.h>2);
            for (let i=0;i<texts.length;i++) for (let j=i+1;j<texts.length;j++) {
              const a=texts[i], b=texts[j];
              const ox = Math.max(0, Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x));
              const oy = Math.max(0, Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y));
              if (ox>8 && oy>8) bad.push({slide:a.id, a:a.t, b:b.t, ox, oy});
            }
          }
          return bad.slice(0,20);
        }""")
        print("OVERLAPS", len(overlaps))
        for o in overlaps[:10]:
            print(" ", o)
        br.close()


if __name__ == "__main__":
    main()
