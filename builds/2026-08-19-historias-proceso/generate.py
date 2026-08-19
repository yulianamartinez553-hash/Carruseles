# -*- coding: utf-8 -*-
"""Historias IG 9:16 — necesidad del agente + CTA PROCESO.

Canvas 1080×1920. Fondo negro + lino (distinto al carrusel de retícula).
Familia manifiesto: Bebas monumental + Lora italic en la keyword.
Safe zone Stories: top 210 / bottom 360. Firma a 300px del borde inferior.
Sin contador tipo 1/6 en la zona de UI nativa de Instagram.
"""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
G = "#00FFB2"
W = "#F2F2F2"
BG = "#0A0A0A"
GRAY = "#9aa39c"

FRAMES = [
    {
        "id": "01",
        "kicker": "GANCHO",
        "claim": 'Si el seguimiento<br>vive en tu <em>cabeza</em>,<br>no tenés operación.',
        "apoyo": "Tenés un puesto.",
        "size": "lg",
    },
    {
        "id": "02",
        "kicker": "DOLOR",
        "claim": "Cada excepción<br>la resolvés <em>vos</em>.",
        "apoyo": "Cada seguimiento depende de que te acuerdes.",
        "size": "lg",
    },
    {
        "id": "03",
        "kicker": "CONSECUENCIA",
        "claim": "Eso no<br><em>escala</em>.",
        "apoyo": "El día que no estás, el proceso se cae.",
        "size": "xl",
    },
    {
        "id": "04",
        "kicker": "INSIGHT",
        "claim": "Un agente genérico<br>no te <em>salva</em>.",
        "apoyo": "Si el proceso no está escrito, no hay nada que ejecutar.",
        "size": "lg",
    },
    {
        "id": "05",
        "kicker": "MÉTODO",
        "claim": "Primero mapeamos<br>tu <em>operación</em>.",
        "apoyo": "Después se genera el agente. A medida.",
        "size": "lg",
    },
]


def css() -> str:
    f = str(FONTS)
    return f"""
@font-face {{ font-family:'Bebas Neue'; src:url('file://{f}/BebasNeue-Regular.ttf') format('truetype'); font-weight:400; font-display:block; }}
@font-face {{ font-family:'Lora'; src:url('file://{f}/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; font-weight:400 700; font-display:block; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{f}/BarlowCondensed-Medium.ttf') format('truetype'); font-weight:500; font-display:block; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{f}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; font-display:block; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{f}/IBMPlexMono-SemiBold.ttf') format('truetype'); font-weight:600; font-display:block; }}

* {{ box-sizing:border-box; margin:0; padding:0; -webkit-font-smoothing:antialiased; text-rendering:geometricPrecision; font-synthesis:none; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:40px; padding:32px; width:max-content; }}

.story {{
  position:relative; width:1080px; height:1920px; overflow:hidden;
  background:{BG}; color:{W};
}}

/* lino_tela — cruzado 0°/90°, opacidad baja + halo de esquina */
.tex {{
  position:absolute; inset:0; z-index:0; pointer-events:none;
  background-image:
    repeating-linear-gradient(0deg, rgba(242,242,242,.028) 0 1px, transparent 1px 7px),
    repeating-linear-gradient(90deg, rgba(242,242,242,.022) 0 1px, transparent 1px 7px);
}}
.glow {{
  position:absolute; border-radius:50%; pointer-events:none; z-index:0;
}}
.glow-tr {{
  top:-260px; right:-180px; width:760px; height:760px;
  background:radial-gradient(circle, rgba(0,255,178,.26) 0%, rgba(0,255,178,.07) 46%, transparent 72%);
}}
.glow-bl {{
  bottom:-200px; left:-160px; width:620px; height:620px;
  background:radial-gradient(circle, rgba(0,255,178,.16) 0%, rgba(0,255,178,.05) 44%, transparent 74%);
}}
.edge {{
  position:absolute; inset:40px; z-index:2; pointer-events:none;
  border:1px solid rgba(0,255,178,.16);
}}

.safe {{
  position:absolute; left:80px; right:80px; top:220px; bottom:360px;
  z-index:5; display:flex; flex-direction:column;
}}
.top {{
  display:flex; justify-content:space-between; align-items:baseline;
}}
.brand {{
  font-family:'IBM Plex Mono',monospace; font-weight:600; font-size:18px;
  letter-spacing:.16em; color:{GRAY}; text-transform:uppercase;
}}
.kicker {{
  font-family:'IBM Plex Mono',monospace; font-weight:600; font-size:18px;
  letter-spacing:.14em; color:{W}; text-transform:uppercase;
}}
.bars {{
  display:flex; gap:8px; margin-top:22px;
}}
.bars i {{
  flex:1; height:3px; background:rgba(242,242,242,.16); border-radius:99px; display:block;
}}
.bars i.on {{ background:{W}; }}

.mid {{
  flex:1; display:flex; flex-direction:column; justify-content:center;
}}
.claim {{
  font-family:'Bebas Neue', Impact, sans-serif; font-weight:400;
  font-size:96px; line-height:.92; letter-spacing:.01em; color:{W};
  text-align:left; max-width:920px;
}}
.claim.xl {{ font-size:128px; line-height:.88; }}
.claim.cta {{ font-size:88px; text-align:center; width:100%; max-width:none; }}
.claim em {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  color:{G}; font-size:0.72em; letter-spacing:0;
  display:inline-block; line-height:1;
}}
.rule {{
  width:112px; height:5px; background:{G}; border-radius:2px;
  margin:36px 0 28px;
}}
.cta .rule {{ margin-left:auto; margin-right:auto; }}
.apoyo {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:36px;
  line-height:1.32; color:{GRAY}; max-width:820px;
}}
.cta .apoyo {{ text-align:center; max-width:none; color:{W}; }}

.kw {{
  margin:8px auto 0; width:100%; max-width:720px;
  border:3px solid {G}; border-radius:18px; padding:28px 16px; text-align:center;
}}
.kw span {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:72px;
  letter-spacing:.18em; color:{G};
}}
.hint {{
  margin-top:36px; text-align:center;
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:32px;
  line-height:1.35; color:{W};
}}
.hint strong {{ font-weight:500; color:{G}; }}

.firma {{
  position:absolute; left:0; right:0; bottom:300px; text-align:center; z-index:8;
  font-family:'IBM Plex Mono',monospace; font-weight:500; font-size:22px;
  letter-spacing:.14em; color:{G}; opacity:.92;
}}
"""


def chrome(n: int, kicker: str) -> str:
    bars = "".join(f'<i class="{"on" if i <= n else ""}"></i>' for i in range(1, 7))
    return (
        '<div class="tex"></div><div class="glow glow-tr"></div><div class="glow glow-bl"></div>'
        '<div class="edge"></div>'
        '<div class="safe">'
        f'<div class="top"><div class="brand">STLabs</div><div class="kicker">{kicker}</div></div>'
        f'<div class="bars">{bars}</div>'
    )


def story_html(n: int, frame: dict) -> str:
    size = frame.get("size", "lg")
    cls = f"claim {size}".strip()
    return (
        f'<section class="story" data-id="{frame["id"]}">'
        + chrome(n, frame["kicker"])
        + '<div class="mid">'
        + f'<h1 class="{cls}">{frame["claim"]}</h1>'
        + '<div class="rule"></div>'
        + f'<p class="apoyo">{frame["apoyo"]}</p>'
        + "</div></div>"
        + '<div class="firma">sebastian.stlabs.ar</div>'
        + "</section>"
    )


def cta_html() -> str:
    return (
        '<section class="story" data-id="06">'
        + chrome(6, "RESPONDÉ")
        + '<div class="mid cta">'
        + '<h1 class="claim cta">¿Querés que te<br>lo <em>genere</em>?</h1>'
        + '<div class="rule"></div>'
        + '<div class="kw"><span>PROCESO</span></div>'
        + '<p class="hint">Respondé esta historia con <strong>PROCESO</strong><br>y te escribo para arrancar.</p>'
        + "</div></div>"
        + '<div class="firma">sebastian.stlabs.ar</div>'
        + "</section>"
    )


def main():
    frames = [story_html(i, fr) for i, fr in enumerate(FRAMES, 1)]
    frames.append(cta_html())
    html = (
        "<!DOCTYPE html>\n<html lang=\"es\"><head><meta charset=\"UTF-8\">\n"
        "<title>Historias PROCESO — STLabs</title>\n"
        f"<style>{css()}</style></head>\n"
        f"<body><div class=\"sheet\">{''.join(frames)}</div></body></html>"
    )
    (B / "historias.html").write_text(html, encoding="utf-8")
    meta = {
        "titulo": "Historias: necesidad del agente",
        "slides": 6,
        "formato": "1080x1920",
        "fondo": "lino_tela",
        "familia_visual": "manifiesto",
        "origen": "original",
        "keyword_portada": "PROCESO",
        "modo": "negro",
        "id": "2026-08-19-historias-proceso",
        "fecha": "2026-08-19",
        "notas": "6 historias 9:16. CTA: respondé PROCESO. Sticker nativo Pregunta al publicar.",
    }
    (B / "index.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (B / "manifest.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(frames)} stories")


if __name__ == "__main__":
    main()
