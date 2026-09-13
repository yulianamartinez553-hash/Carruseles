#!/usr/bin/env python3
"""Carrusel Prospectar vs Perder el tiempo — STLabs (HTML + Playwright retina)."""
from __future__ import annotations

import base64
import math
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from stlabs_kit import package, render  # noqa: E402

BUILD = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_faces() -> str:
    faces = [
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-BoldItalic.ttf", 700, "italic"),
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-Italic.ttf", 400, "italic"),
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-Bold.ttf", 700, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Regular.ttf", 400, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Light.ttf", 300, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Regular.ttf", 400, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Medium.ttf", 500, "normal"),
    ]
    out = []
    for fam, path, w, style in faces:
        if not path.exists():
            raise FileNotFoundError(path)
        d = b64(path)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{d}) format('truetype');}}"
        )
    return "".join(out)


CSS = r"""
:root{
  --verde:#00FFB2;
  --verde-ink:#0A5C45;
  --verde-deep:#006B4F;
  --ink:#0A0A0A;
  --paper:#FAFAF7;
  --serif:'Playfair Display',Georgia,serif;
  --sans:'IBM Plex Sans',Helvetica,sans-serif;
  --mono:'IBM Plex Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}
body{background:#111;}
.sheet{display:flex;flex-direction:column;gap:40px;padding:40px;background:#111;}
.slide{
  position:relative;width:1080px;height:1350px;overflow:hidden;
  background:var(--paper);color:var(--verde-ink);
}
.slide::before{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.55;
  background-image:
    radial-gradient(circle at 20% 30%, rgba(0,0,0,.035) 0.6px, transparent 1.2px),
    radial-gradient(circle at 70% 60%, rgba(0,0,0,.03) 0.5px, transparent 1.1px),
    radial-gradient(circle at 40% 80%, rgba(0,0,0,.028) 0.55px, transparent 1.15px);
  background-size:3px 3px, 4px 4px, 5px 5px;
}
.slide::after{
  content:'';position:absolute;inset:0;z-index:1;pointer-events:none;opacity:.52;mix-blend-mode:multiply;
  background:repeating-linear-gradient(90deg,
    rgba(0,0,0,.06) 0px, rgba(0,0,0,.06) 1.5px,
    rgba(255,255,255,0) 3px, rgba(255,255,255,0) 8px,
    rgba(0,40,30,.09) 10px, rgba(0,40,30,.09) 12px,
    rgba(255,255,255,0) 14px);
}
.stains,.arcs,.stipple,.content,.web{position:absolute;z-index:3;}
.stains{inset:0;z-index:2;pointer-events:none;}
.stain{
  position:absolute;border-radius:50%;
  background:radial-gradient(circle, rgba(210,255,240,.12) 0%, rgba(160,255,220,.06) 45%, rgba(0,255,178,0) 76%);
  filter:blur(4px);
}
.arcs{inset:0;z-index:2;pointer-events:none;}
.arcs svg{width:100%;height:100%;}
.stipple{pointer-events:none;inset:0;}
.content{inset:0;z-index:5;padding:0;}
.web{
  left:0;right:0;bottom:70px;text-align:center;z-index:6;
  font-family:var(--mono);font-size:22px;letter-spacing:1.5px;color:var(--verde);
}
.t{font-family:var(--serif);font-style:italic;font-weight:700;line-height:1.05;letter-spacing:-0.5px;}
.b{font-family:var(--sans);font-weight:400;line-height:1.35;}
.b.light{font-weight:300;font-style:italic;}
.g{color:var(--verde);}
.ink{color:var(--verde-ink);}
.deep{color:var(--verde-deep);}
/* sobre manchas claras: tinta oscura (no blanco) */
.w{color:var(--verde-ink) !important;text-shadow:none;}
.blk{color:var(--ink);}

.s1 .block{position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);width:860px;text-align:center;}
.s1 .t{font-size:78px;}
.s1 .line{display:block;}
.s1 .sub{margin-top:36px;font-size:28px;color:var(--ink);text-align:left;display:inline-block;}

.s2 .block{position:absolute;left:120px;top:400px;width:820px;}
.s2 .t{font-size:54px;margin-bottom:48px;}
.s2 .b{font-size:28px;}
.s2 .gap{height:28px;}

.s3 .block{position:absolute;left:140px;top:420px;width:800px;}
.s3 .t{font-size:58px;margin-bottom:42px;}
.s3 .b{font-size:30px;margin-bottom:8px;}
.s3 .concl{margin-top:28px;font-size:28px;font-style:normal;}

.s4 .block{position:absolute;left:110px;top:380px;width:860px;}
.s4 .t{font-size:52px;margin-bottom:44px;}
.s4 .b{font-size:28px;}
.s4 .gap{height:32px;}

.s5 .block{position:absolute;left:130px;top:400px;width:820px;}
.s5 .t{font-size:64px;margin-bottom:48px;}
.s5 .b{font-size:28px;color:var(--ink);margin-bottom:14px;}

.s6 .block{position:absolute;left:110px;top:420px;width:860px;}
.s6 .t{font-size:56px;margin-bottom:48px;}
.s6 .b{font-size:28px;margin-bottom:10px;}

.s7 .block{position:absolute;left:70px;right:70px;top:50%;transform:translateY(-52%);text-align:center;}
.s7 .t{font-size:46px;}
.s7 .t .g{display:block;margin-top:8px;}
.s7 .b{margin-top:48px;font-size:26px;color:var(--ink);}
.s7 .q{margin-top:28px;font-size:26px;color:var(--verde-deep);}

.s8 .block{position:absolute;left:80px;right:80px;top:48%;transform:translateY(-50%);text-align:center;}
.s8 .t{font-size:56px;}
.s8 .kw{font-size:64px;margin-top:12px;}
.s8 .b{margin-top:48px;font-size:28px;}
"""


def stain(x: int, y: int, w: int, h: int, deep: bool = False, plate: bool = False) -> str:
    return ""


def arcs_svg(ox: int, oy: int, radii: list[int], opacity: float = 0.55) -> str:
    paths = []
    for r in radii:
        d = f"M {ox} {oy} A {r} {r} 0 0 1 {ox + 2 * r} {oy}"
        paths.append(
            f'<path d="{d}" fill="none" stroke="#00FFB2" stroke-width="2.2" '
            f'stroke-opacity="{opacity}"/>'
        )
        d2 = f"M {ox} {oy} A {r} {r} 0 0 0 {ox + 2 * r} {oy}"
        paths.append(
            f'<path d="{d2}" fill="none" stroke="#00FFB2" stroke-width="1.4" '
            f'stroke-opacity="{opacity * 0.45}"/>'
        )
    return (
        f'<div class="arcs"><svg viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">'
        f'{"".join(paths)}</svg></div>'
    )


def stipple_svg() -> str:
    return ""



def slide(cls: str, stains: str, arcs: str, inner: str, extra: str = "") -> str:
    return (
        f'<section class="slide {cls}">'
        f'<div class="stains">{stains}</div>{arcs}{extra}'
        f'<div class="content">{inner}</div>'
        f'<div class="web">sebastian.stlabs.ar</div>'
        f"</section>"
    )


def build_html() -> Path:
    s1 = slide(
        "s1",
        stain(720, -60, 400, 360)
        + stain(40, 980, 340, 280),
        arcs_svg(920, 160, [90, 150, 220, 300], 0.5),
        """<div class="block">
          <div class="t">
            <span class="line ink">PROSPECTAR</span>
            <span class="line"><span class="ink">VS.</span> <span class="g">PERDER EL</span></span>
            <span class="line g">TIEMPO.</span>
          </div>
          <div class="sub b">Se ven igual desde afuera.<br>Por dentro no tienen nada en común.</div>
        </div>""",
    )

    s2 = slide(
        "s2",
        stain(700, 40, 360, 300)
        + stain(-40, 1000, 340, 280),
        arcs_svg(60, 180, [140, 230, 340], 0.45),
        """<div class="block">
          <div class="t"><span class="w">Prospectar es hablar con</span><br>
          <span class="w">quien </span><span class="g">puede comprar.</span></div>
          <div class="b w">Perder el tiempo es hablar con quien<br>te cae bien.</div>
          <div class="gap"></div>
          <div class="b ink">No es lo mismo.</div>
        </div>""",
    )

    s3 = slide(
        "s3",
        stain(700, 60, 360, 300)
        + stain(40, 1000, 340, 280),
        arcs_svg(980, 1180, [120, 200, 300], 0.4),
        """<div class="block">
          <div class="t ink">Prospectar tiene <span class="g">criterio.</span></div>
          <div class="b light ink">¿Tiene el problema?</div>
          <div class="b light ink">¿Tiene presupuesto?</div>
          <div class="b light ink">¿Decide?</div>
          <div class="b concl ink">Sin las tres, no es prospecto.<br>Es conversación.</div>
        </div>""",
    )

    s4 = slide(
        "s4",
        stain(720, 40, 340, 280)
        + stain(40, 1000, 360, 280),
        arcs_svg(40, 160, [120, 210, 320], 0.45),
        """<div class="block">
          <div class="t"><span class="w">Perder el tiempo se puede</span><br>
          <span class="g">sentir productivo.</span></div>
          <div class="b w">Llamadas. Reuniones. Seguimientos.<br>Mucho movimiento.</div>
          <div class="gap"></div>
          <div class="b ink">Tené cuidado si eso no te está dando<br>ningún avance.</div>
        </div>""",
    )

    s5 = slide(
        "s5",
        stain(700, 80, 360, 300)
        + stain(40, 1000, 340, 280),
        arcs_svg(540, 100, [160, 260, 380], 0.35),
        """<div class="block">
          <div class="t ink">Prospectar <span class="g">incomoda.</span></div>
          <div class="b">Significa decir que no a prospectos malos.</div>
          <div class="b">Significa soltar rápido.</div>
          <div class="b">Significa priorizar calidad sobre cantidad.</div>
        </div>""",
    )

    s6 = slide(
        "s6",
        stain(720, 40, 340, 280)
        + stain(40, 1000, 360, 280),
        arcs_svg(1000, 200, [130, 220, 340], 0.45),
        """<div class="block">
          <div class="t"><span class="w">La diferencia está</span><br>
          <span class="g">en los números.</span></div>
          <div class="b w">No cuántas llamadas hiciste.</div>
          <div class="b w">Cuántas fueron con la persona correcta.</div>
          <div class="b ink">Ahí está todo.</div>
        </div>""",
    )

    s7 = slide(
        "s7",
        stain(700, 60, 360, 300)
        + stain(40, 1000, 340, 280),
        arcs_svg(540, 1240, [150, 260, 400], 0.4),
        """<div class="block">
          <div class="t ink">Un pipeline lleno de<br>prospectos malos no es<br>una oportunidad.
            <span class="g">Es trabajo disfrazado<br>de progreso.</span>
          </div>
          <div class="b">Prospectá menos. Mejor. Con criterio.</div>
          <div class="q b">¿Cuántas conversaciones esta<br>semana fueron prospección real?</div>
        </div>""",
    )

    s8 = slide(
        "s8",
        stain(40, 60, 340, 280)
        + stain(720, 1000, 340, 280),
        arcs_svg(180, 1120, [100, 170, 260], 0.55),
        """<div class="block">
          <div class="t w">Si esto te pegó,</div>
          <div class="t kw g">comentá CRITERIO.</div>
          <div class="b ink">Te paso el filtro de las tres preguntas<br>para dejar de confundir movimiento<br>con prospección real.</div>
        </div>""",
    )

    html = (
        "<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'>"
        f"<style>{font_faces()}{CSS}</style></head>"
        f"<body><div class='sheet'>{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}</div></body></html>"
    )
    path = BUILD / "carrusel.html"
    path.write_text(html, encoding="utf-8")
    print(f"HTML → {path}")
    return path


def main() -> None:
    build_html()
    print("Render retina…")
    pngs = render(BUILD)
    print(f"PNGs: {len(pngs)}")
    meta = {
        "titulo": "Prospectar vs Perder el Tiempo",
        "slides": 8,
        "fondo": "papel_arroz_corrugado_manchas_verdes",
        "familia_visual": "editorial_didot_serif",
        "origen": "screenshot",
        "keyword_portada": "PROSPECTAR",
        "id": "2026-09-13-carrusel-prospectar",
    }
    out = package(BUILD, "STLabs-Prospectar-vs-Tiempo", meta=meta)
    print(f"Package → {out}")
    (BUILD / "CAPTION.txt").write_text(
        """Prospectar y perder el tiempo se ven igual desde afuera.

Por dentro no tienen nada en común.

Una es hablar con quien puede comprar.
La otra es hablar con quien te cae bien.

Sin problema, presupuesto y decisión…
no es prospecto. Es conversación.

Comentá CRITERIO y te mando el filtro de las tres preguntas.

#prospección #ventas #pipeline #revops #crm
""",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Prospectar vs Perder el Tiempo

| Tipografía | Peso/estilo | Rol | Origen | Carga |
|---|---|---|---|---|
| Playfair Display | 700 italic | Título display | Google Fonts / github.com/googlefonts/playfair | `@font-face` embebido base64 en HTML |
| Playfair Display | 400 italic | Acento display | idem | idem |
| IBM Plex Sans | 300 / 400 / 500 | Cuerpo | github.com/googlefonts/ibmplex | idem |
| IBM Plex Mono | 400 / 500 | Footer `sebastian.stlabs.ar` | pack STLabs / fonts/ | idem |

Instalación local (opcional):
```bash
# ya en /workspace/fonts/playfair y /workspace/fonts/ibm-plex-sans
```
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
