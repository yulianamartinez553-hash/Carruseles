# -*- coding: utf-8 -*-
"""QA geométrico: ningún texto puede tapar otro texto (intersección de bounding boxes)."""
import pathlib
from playwright.sync_api import sync_playwright

TEXT_SEL = ("h1, h4, .sub, .kick, .bub, .banner, .case, .chip, .card-lab, .code, .codehead, "
            ".net-lab, .net-pill, .web, .nav, .share, .fi-chip, .fi-q, .fi-row, .fi-meta, "
            ".fi-sign, .sello, .mast, .cuerpo, .stamp, .sticky, .stackbox, .adopbar, "
            ".rol, .rol-sub, .tl, .pill12")


def inter(a, b):
    x = min(a["x"] + a["width"], b["x"] + b["width"]) - max(a["x"], b["x"])
    y = min(a["y"] + a["height"], b["y"] + b["height"]) - max(a["y"], b["y"])
    return max(0, x) * max(0, y)


with sync_playwright() as p:
    br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
    pg = br.new_page(viewport={"width": 1180, "height": 1450})
    pg.goto(pathlib.Path("/tmp/build-query/carrusel.html").as_uri())
    pg.wait_for_function("document.fonts.ready")
    pg.wait_for_timeout(2500)
    problems = 0
    for si, slide in enumerate(pg.query_selector_all(".slide"), 1):
        sb = slide.bounding_box()
        els = []
        for el in slide.query_selector_all(TEXT_SEL):
            b = el.bounding_box()
            if not b or b["width"] == 0:
                continue
            # ignorar contenedores anidados (padre-hijo)
            els.append((el, b))
        for i in range(len(els)):
            for j in range(i + 1, len(els)):
                e1, b1 = els[i]
                e2, b2 = els[j]
                if e1.evaluate("(a,b)=>a.contains(b)||b.contains(a)", e2.as_element() if hasattr(e2, "as_element") else e2):
                    continue
                ov = inter(b1, b2)
                if ov > 140:  # px² tolerancia mínima (bordes/sombras)
                    c1 = e1.get_attribute("class") or e1.evaluate("e=>e.tagName")
                    c2 = e2.get_attribute("class") or e2.evaluate("e=>e.tagName")
                    print(f"slide {si:02d}: OVERLAP {ov:.0f}px² entre [{c1}] y [{c2}]"
                          f" @({b1['x']:.0f},{b1['y']:.0f}) vs ({b2['x']:.0f},{b2['y']:.0f})")
                    problems += 1
        # safe zone: texto a menos de 40px del borde del slide
        for el, b in els:
            rel_l = b["x"] - sb["x"]
            rel_r = (sb["x"] + sb["width"]) - (b["x"] + b["width"])
            rel_t = b["y"] - sb["y"]
            rel_b = (sb["y"] + sb["height"]) - (b["y"] + b["height"])
            if min(rel_l, rel_r, rel_t, rel_b) < 30:
                c = el.get_attribute("class") or "?"
                print(f"slide {si:02d}: SAFEZONE [{c}] margen {min(rel_l, rel_r, rel_t, rel_b):.0f}px")
                problems += 1
    br.close()
    print("QA:", "OK — sin solapamientos" if problems == 0 else f"{problems} problemas")
