# -*- coding: utf-8 -*-
"""Post feed: Los procesos no son lineales — clon blanco STLabs (4K + título verde)."""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import package, write_html  # noqa: E402

# Nodos medidos en la referencia (fracción del lienzo 4:5)
NODES = [
    # x, y, color, lines, side, align, dx, dy
    (0.108, 0.625, "#70FD94", ["Decides", "crecer"], "below", "left", -6, 16),
    (0.206, 0.534, "#F8D442", ["Sientes", "motivación"], "above", "left", -10, -18),
    (0.322, 0.659, "#6FFC94", ["Aparecen", "problemas"], "above", "left", 18, -18),
    (0.351, 0.766, "#80DDFF", ["Lo que funcionaba", "deja de funcionar"], "below", "center", 0, 18),
    (0.481, 0.634, "#FBD741", ["Empiezas a entender", "el problema"], "below", "left", 22, 18),
    (0.585, 0.496, "#7CDEFB", ["Construyes una mejor", "forma de hacerlo"], "above", "left", -24, -18),
    (0.728, 0.559, "#70FD97", ["Vuelves", "a fallar"], "below", "left", -8, 16),
    (0.843, 0.427, "#F6D43D", ["Sigues, pero con", "más criterio"], "above", "left", -36, -18),
]

EXTRA = """
@font-face{
  font-family:Inter;
  src:url('file:///usr/share/fonts/truetype/macos/Inter-Medium.ttf') format('truetype');
  font-weight:500; font-style:normal;
}
@font-face{
  font-family:Inter;
  src:url('file:///usr/share/fonts/truetype/macos/Inter-SemiBold.ttf') format('truetype');
  font-weight:600; font-style:normal;
}
@font-face{
  font-family:Inter;
  src:url('file:///usr/share/fonts/truetype/macos/Inter-Bold.ttf') format('truetype');
  font-weight:700; font-style:normal;
}
@font-face{
  font-family:Inter;
  src:url('file:///usr/share/fonts/truetype/macos/Inter-Bold.ttf') format('truetype');
  font-weight:800; font-style:normal;
}

.slide.s-proceso{
  background:#FFFFFF;
  color:#0A0A0A;
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
  text-rendering:geometricPrecision;
}
.slide.s-proceso::before{
  content:'';
  position:absolute; inset:0; pointer-events:none; opacity:.03; z-index:0;
  background-image:
    linear-gradient(#0A0A0A 1px, transparent 1px),
    linear-gradient(90deg, #0A0A0A 1px, transparent 1px);
  background-size:52px 52px;
}
.s-proceso .layer{position:absolute; inset:0; z-index:1;}

.handle{
  position:absolute; left:50%; top:56px; transform:translateX(-50%);
  display:inline-flex; align-items:center; justify-content:center;
  padding:13px 32px; border-radius:999px;
  border:2.5px solid #0A0A0A; background:#FFFFFF;
  font-family:"IBM Plex Mono", ui-monospace, monospace;
  font-weight:500; font-size:25px; letter-spacing:0.15px;
  color:#00FFB2; white-space:nowrap; line-height:1;
}
.title{
  position:absolute; left:50px; right:50px; top:140px;
  text-align:center;
  font-family:Inter, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight:800; font-size:76px; line-height:1.0;
  letter-spacing:-1.4px;
  color:#00FFB2;
}
.subpill{
  position:absolute; left:50%; top:328px; transform:translateX(-50%);
  display:inline-flex; align-items:center; justify-content:center;
  padding:15px 34px; border-radius:999px;
  background:#0A0A0A; color:#FFFFFF;
  font-family:Inter, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight:600; font-size:27px; line-height:1; white-space:nowrap;
}
.graph-wrap{
  position:absolute; left:0; right:0; top:0; bottom:0;
  pointer-events:none;
}
.graph-wrap svg{
  position:absolute; inset:0; width:100%; height:100%;
  shape-rendering:geometricPrecision;
}
.node-label{
  position:absolute;
  font-family:Inter, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight:700; font-size:23px; line-height:1.15;
  color:#0A0A0A; white-space:pre-line;
  max-width:280px;
}
.node-label.left{ text-align:left; }
.node-label.center{ text-align:center; }
.node-label.above.left{ transform:translateY(-100%); }
.node-label.above.center{ transform:translate(-50%,-100%); }
.node-label.below.center{ transform:translateX(-50%); }
.footer{
  position:absolute; left:0; right:0; bottom:48px; text-align:center;
  font-family:"IBM Plex Mono", ui-monospace, monospace;
  font-weight:500; font-size:20px; color:#00FFB2; letter-spacing:0.4px;
  z-index:2;
}
"""


def _svg_graph() -> str:
    w, h = 1080, 1350
    pts = [(n[0] * w, n[1] * h) for n in NODES]
    d = "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in pts)
    circles = [
        f'<circle cx="{x:.2f}" cy="{y:.2f}" r="11" fill="{n[2]}"/>'
        for (x, y), n in zip(pts, NODES)
    ]
    return f"""
<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <path d="{d}" fill="none" stroke="#0A0A0A" stroke-width="2.6"
        stroke-linecap="round" stroke-linejoin="round"/>
  {''.join(circles)}
</svg>
"""


def _labels() -> str:
    w, h = 1080, 1350
    bits = []
    for x_f, y_f, _c, lines, side, align, dx, dy in NODES:
        x = x_f * w + dx
        y = y_f * h + dy
        text = "<br>".join(lines)
        bits.append(
            f'<div class="node-label {side} {align}" style="left:{x:.1f}px;top:{y:.1f}px">{text}</div>'
        )
    return "\n".join(bits)


def build_slide() -> str:
    return f"""
<section class="slide s-proceso">
  <div class="layer">
    <div class="handle">sebastian.stlabs.ar</div>
    <div class="title">Los procesos<br>no son lineales</div>
    <div class="subpill">y eso también es avanzar</div>
    <div class="graph-wrap">{_svg_graph()}{_labels()}</div>
    <div class="footer">sebastian.stlabs.ar</div>
  </div>
</section>
"""


def render_4k(build_dir: Path, html_name: str = "carrusel.html", scale: int = 4) -> Path:
    """Render 4× (4320×5400) — master nítido, sin upscale artificial."""
    from playwright.sync_api import sync_playwright

    B = Path(build_dir)
    png_dir = B / "png"
    png_dir.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        pg = br.new_page(
            viewport={"width": 1180, "height": 1450},
            device_scale_factor=scale,
        )
        pg.goto((B / html_name).as_uri())
        pg.wait_for_function("document.fonts.ready")
        pg.wait_for_timeout(5000)
        el = pg.query_selector(".slide")
        out = png_dir / "slide-01.png"
        el.screenshot(path=str(out), type="png")
        br.close()
    return out


CAPTION = """Los procesos no son lineales.

Y eso también es avanzar.

Decidís crecer, aparece la motivación, después los problemas.
Lo que funcionaba deja de funcionar. Volvés a fallar.
Y seguís — pero con más criterio.

Si estás en esa curva rara entre “esto va” y “esto no”, no estás trabado:
estás construyendo una mejor forma de hacerlo.

sebastian.stlabs.ar

—
Comentá PROCESOS si querés el mapa completo para ordenar tu operación con IA.
"""

MANIFIESTO = """# Manifiesto de fuentes — Los procesos no son lineales

| Tipografía | Peso | Rol | Origen | Carga |
|---|---|---|---|---|
| Inter | 800 / Bold | Título display verde `#00FFB2` | `/usr/share/fonts/truetype/macos/Inter-Bold.ttf` | `@font-face` file:// |
| Inter | 700 / Bold | Labels del gráfico | idem | idem |
| Inter | 600 / SemiBold | Subtítulo en pill | Inter-SemiBold.ttf | idem |
| IBM Plex Mono | 500 / Medium | Handle + footer | kit STLabs | embebida base64 en package |

Master: **4320×5400** (4×). Export: 1080×1350 + @2x 2160×2700 + @4x.
"""


def main() -> None:
    write_html([build_slide()], BUILD / "carrusel.html", extra_css=EXTRA)
    master = render_4k(BUILD, scale=4)

    meta = {
        "id": "2026-09-12-post-procesos-no-lineales",
        "fecha": "2026-09-12",
        "titulo": "Los procesos no son lineales",
        "slides": 1,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "screenshot",
        "keyword_portada": "PROCESOS",
    }
    out_dir = package(BUILD, "STLabs-Post-Procesos-No-Lineales", meta=meta)

    out = BUILD / "out"
    out.mkdir(exist_ok=True)
    from PIL import Image

    im = Image.open(master).convert("RGB")
    im.save(out / "STLabs-Post-Procesos-No-Lineales@4x.png", optimize=True)
    im.resize((2160, 2700), Image.Resampling.LANCZOS).save(
        out / "STLabs-Post-Procesos-No-Lineales@2x.png", optimize=True
    )
    im.resize((1080, 1350), Image.Resampling.LANCZOS).save(
        out / "STLabs-Post-Procesos-No-Lineales.png", optimize=True
    )

    (BUILD / "CAPTION.txt").write_text(CAPTION, encoding="utf-8")
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(MANIFIESTO, encoding="utf-8")
    out_path = Path(out_dir)
    (out_path / "CAPTION.txt").write_text(CAPTION, encoding="utf-8")
    (out_path / "MANIFIESTO-FUENTES.md").write_text(MANIFIESTO, encoding="utf-8")
    print("OK", out, "master", im.size)


if __name__ == "__main__":
    main()
