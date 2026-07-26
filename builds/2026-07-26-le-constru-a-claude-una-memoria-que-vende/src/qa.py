# -*- coding: utf-8 -*-
"""QA geométrico: ningún texto puede tapar otro texto (bounding boxes)."""
import pathlib
from playwright.sync_api import sync_playwright

TEXT_SEL = (".blk, .ser, .body, .lab, .badge-row, .swipe, .web, .num-row, .circ-name, "
            ".circ-sub, .cta-pill, .win, .ag-h, .ag-sub, .ag-pill, .ag-input")


def inter(a, b):
    x = min(a["x"] + a["width"], b["x"] + b["width"]) - max(a["x"], b["x"])
    y = min(a["y"] + a["height"], b["y"] + b["height"]) - max(a["y"], b["y"])
    return max(0, x) * max(0, y)


with sync_playwright() as p:
    br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
    pg = br.new_page(viewport={"width": 1180, "height": 1450})
    pg.goto(pathlib.Path("/tmp/build-agente/carrusel.html").as_uri())
    pg.wait_for_function("document.fonts.ready")
    pg.wait_for_timeout(2500)
    problems = 0
    for si, slide in enumerate(pg.query_selector_all(".slide"), 1):
        sb = slide.bounding_box()
        els = []
        for el in slide.query_selector_all(TEXT_SEL):
            b = el.bounding_box()
            if b and b["width"] > 0:
                els.append((el, b))
        for i in range(len(els)):
            for j in range(i + 1, len(els)):
                e1, b1 = els[i]
                e2, b2 = els[j]
                if e1.evaluate("(a,b)=>a.contains(b)||b.contains(a)", e2):
                    continue
                ov = inter(b1, b2)
                if ov > 140:
                    c1 = e1.get_attribute("class")
                    c2 = e2.get_attribute("class")
                    print(f"slide {si}: OVERLAP {ov:.0f}px² [{c1}] vs [{c2}] "
                          f"@({b1['x']:.0f},{b1['y']:.0f}) vs ({b2['x']:.0f},{b2['y']:.0f})")
                    problems += 1
        for el, b in els:
            m = min(b["x"] - sb["x"], (sb["x"] + sb["width"]) - (b["x"] + b["width"]),
                    b["y"] - sb["y"], (sb["y"] + sb["height"]) - (b["y"] + b["height"]))
            if m < 30:
                print(f"slide {si}: SAFEZONE [{el.get_attribute('class')}] margen {m:.0f}px")
                problems += 1
    br.close()
    print("QA:", "OK — sin problemas" if problems == 0 else f"{problems} problemas")
