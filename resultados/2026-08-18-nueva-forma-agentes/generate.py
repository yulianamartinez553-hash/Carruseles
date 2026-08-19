# -*- coding: utf-8 -*-
"""Carrusel 6 slides — clon editorial STLabs
Fondo: reticula_fina + glows · Familia: dossier_editorial · Modo: negro
Títulos: Playfair Display (serif elegante, gruesa) · Cuerpo: Poppins
JSON: 00-sistema-visual-carrusel.json (estilo editorial)
"""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
A = B / "assets"
FONTS = Path("/tmp/stlabs-fonts")
G = "#00FFB2"
W = "#F2F2F2"
BG = "#0A0A0A"


def uri(p: Path) -> str:
    return p.resolve().as_uri()


def build_css() -> str:
    f = str(FONTS)
    hero = uri(A / "sebas-hero.png")
    dude = uri(A / "pixel-dude.png")
    av = uri(A / "sebas-avatar.png")
    wch = uri(A / "pixel-wrench.png")
    cost = uri(A / "pixel-cost.png")
    bell = uri(A / "pixel-bell.png")
    claude = uri(A / "claude.png")
    return f"""
@font-face {{ font-family:'Playfair'; src:url('file://{f}/PlayfairDisplay.ttf') format('truetype'); font-weight:400 900; font-style:normal; }}
@font-face {{ font-family:'Playfair'; src:url('file://{f}/PlayfairDisplay-Italic.ttf') format('truetype'); font-weight:400 900; font-style:italic; }}
@font-face {{ font-family:'Poppins'; src:url('file://{f}/Poppins-ExtraBold.ttf') format('truetype'); font-weight:800; }}
@font-face {{ font-family:'Poppins'; src:url('file://{f}/Poppins-Bold.ttf') format('truetype'); font-weight:700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{f}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{f}/IBMPlexMono-SemiBold.ttf') format('truetype'); font-weight:600; }}

* {{ box-sizing:border-box; margin:0; padding:0; -webkit-font-smoothing:antialiased; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }}
.slide {{
  position:relative; width:1080px; height:1350px; overflow:hidden;
  background:{BG}; color:{W};
}}
.tex {{
  position:absolute; inset:0; z-index:0; pointer-events:none;
  background-image:
    linear-gradient(rgba(0,255,178,.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.07) 1px, transparent 1px);
  background-size:56px 56px;
  -webkit-mask-image: radial-gradient(ellipse 80% 70% at 50% 40%, #000 20%, transparent 78%);
  mask-image: radial-gradient(ellipse 80% 70% at 50% 40%, #000 20%, transparent 78%);
}}
.glow {{ position:absolute; border-radius:50%; pointer-events:none; z-index:0; filter:blur(48px); }}
.glow-tr {{
  top:-220px; right:-180px; width:560px; height:560px;
  background:radial-gradient(circle, rgba(0,255,178,.30) 0%, rgba(0,255,178,.10) 42%, transparent 72%);
}}
.glow-bl {{
  bottom:-180px; left:-160px; width:560px; height:560px;
  background:radial-gradient(circle, rgba(0,255,178,.26) 0%, rgba(0,255,178,.09) 42%, transparent 74%);
}}
.hline {{
  position:absolute; left:72px; right:72px; height:1px; background:rgba(0,255,178,.35); z-index:3;
}}
.hline.top {{ top:92px; }}
.hline.bot {{ bottom:118px; }}
.plus {{
  position:absolute; top:72px; right:72px; z-index:4;
  font-family:'Poppins',sans-serif; font-weight:800; font-size:28px; color:{G};
}}
.brand {{
  position:absolute; top:48px; left:72px; z-index:4;
  font-family:'IBM Plex Mono',monospace; font-weight:600; font-size:18px;
  letter-spacing:.12em; color:{G}; text-transform:uppercase;
}}
.kicker {{
  position:absolute; top:112px; left:72px; z-index:4;
  font-family:'IBM Plex Mono',monospace; font-weight:600; font-size:18px;
  letter-spacing:.14em; color:{G}; text-transform:uppercase;
}}
.pill {{
  position:absolute; top:42px; right:72px; z-index:4;
  display:flex; align-items:center; gap:10px;
  border:1.5px solid {G}; border-radius:999px; padding:8px 16px;
  font-family:'Poppins',sans-serif; font-weight:700; font-size:16px; color:{G};
  text-transform:uppercase; letter-spacing:.06em;
}}
.pill i {{ width:10px; height:10px; border-radius:50%; background:{G}; display:block; }}
.firma {{
  position:absolute; left:0; right:0; bottom:48px; text-align:center; z-index:8;
  font-family:'IBM Plex Mono',monospace; font-weight:500; font-size:20px;
  letter-spacing:.14em; color:{G};
}}
.cta-side {{
  position:absolute; right:72px; bottom:148px; z-index:6;
  font-family:'Playfair',Georgia,serif; font-style:italic; font-weight:700;
  font-size:22px; color:{G}; text-align:right;
}}

/* PORTADA — foto a tamaño de la referencia (llena el 4:5), sin línea que la corte */
.hero {{
  position:absolute; inset:0; z-index:1;
  background:url('{hero}') center top / cover no-repeat;
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, #000 22%, #000 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, #000 22%, #000 100%);
}}
.hero-fade {{
  position:absolute; left:0; right:0; top:0; height:38%; z-index:2; pointer-events:none;
  background:linear-gradient(180deg, {BG} 0%, {BG} 48%, rgba(10,10,10,.45) 78%, transparent 100%);
}}
.display {{
  position:absolute; left:72px; right:90px; top:168px; z-index:5;
  font-family:'Playfair',Georgia,serif; font-weight:800;
  font-size:64px; line-height:.98; letter-spacing:-.02em; color:{W};
  text-align:left;
}}
.display em {{ font-style:italic; color:{G}; font-weight:700; }}
.clip {{
  position:absolute; z-index:6; width:132px; height:132px;
}}
.clip img {{ width:88px; height:88px; image-rendering:pixelated; display:block; margin:22px auto; }}
.clip.dude {{ left:48px; top:58%; }}
.clip.cf {{ right:28px; top:60%; width:160px; height:auto; display:flex; flex-direction:column; align-items:center; }}
.claude {{ display:block; object-fit:contain; }}
.corners {{
  position:absolute; inset:0; pointer-events:none;
}}
.corners span {{
  position:absolute; width:22px; height:22px; border:2px solid {G};
}}
.corners .tl {{ top:0; left:0; border-right:none; border-bottom:none; }}
.corners .tr {{ top:0; right:0; border-left:none; border-bottom:none; }}
.corners .bl {{ bottom:0; left:0; border-right:none; border-top:none; }}
.corners .br {{ bottom:0; right:0; border-left:none; border-top:none; }}
.cf-mark {{
  font-family:'Poppins',sans-serif; font-weight:800; font-size:13px;
  letter-spacing:.16em; color:{W}; text-align:center; margin-top:6px;
}}

/* SLIDE 2 CARDS */
.h2 {{
  position:absolute; left:72px; right:72px; top:168px; z-index:4;
  font-family:'Playfair',Georgia,serif; font-weight:800;
  font-size:58px; line-height:1.02; color:{W}; text-align:left;
}}
.h2 em {{ font-style:italic; color:{G}; font-weight:700; }}
.sub {{
  position:absolute; left:72px; right:72px; top:300px; z-index:4;
  font-family:'Poppins',sans-serif; font-weight:700; font-size:28px; color:{W};
}}
.cards {{ position:absolute; left:72px; right:72px; top:380px; z-index:4; display:flex; flex-direction:column; gap:18px; }}
.card {{
  display:flex; align-items:center; gap:18px;
  background:#141414; border:1px solid #2A2A2A; border-radius:18px; padding:18px 22px;
}}
.card img {{ width:72px; height:72px; image-rendering:pixelated; flex-shrink:0; }}
.card .div {{ width:2px; height:64px; background:{G}; flex-shrink:0; }}
.card h3 {{ font-family:'Poppins',sans-serif; font-weight:800; font-size:26px; color:{W}; margin-bottom:6px; }}
.card p {{ font-family:'Poppins',sans-serif; font-weight:700; font-size:20px; color:#9aa39c; line-height:1.3; }}

/* SLIDE 3 */
.bubble {{
  position:absolute; left:72px; top:430px; z-index:4;
  max-width:640px; background:#141414; color:{W};
  font-family:'Poppins',sans-serif; font-weight:700; font-size:24px; line-height:1.35;
  padding:22px 26px; border-radius:18px 18px 18px 6px;
  border:1px solid #2A2A2A;
}}
.tag80 {{
  position:absolute; left:740px; top:448px; z-index:4;
  display:flex; align-items:center; gap:8px;
  border:1.5px solid {G}; border-radius:999px; padding:8px 16px;
  font-family:'Poppins',sans-serif; font-weight:800; font-size:18px; color:{G};
}}
.tag80 i {{ width:10px; height:10px; border-radius:50%; background:{G}; display:block; }}
.metric {{
  position:absolute; left:72px; right:72px; top:640px; z-index:4;
  border:1.5px dashed {G}; border-radius:18px; padding:36px 40px;
  background:rgba(0,255,178,.04);
}}
.metric .lab {{ font-family:'IBM Plex Mono',monospace; font-weight:600; font-size:18px; color:#9aa39c; letter-spacing:.06em; }}
.metric .num {{
  font-family:'Playfair',Georgia,serif; font-weight:800; font-size:120px; line-height:.9;
  color:{G}; margin:8px 0 4px;
}}
.metric .num span {{ font-size:36px; letter-spacing:.12em; margin-left:8px; vertical-align:super; }}
.metric .foot {{ font-family:'Poppins',sans-serif; font-weight:700; font-size:22px; color:{G}; }}

/* SLIDE 4 EQUATION */
.eq {{
  position:absolute; left:72px; right:72px; top:430px; z-index:4;
  display:flex; align-items:flex-start; justify-content:center; gap:28px;
}}
.eq-item {{ text-align:center; width:280px; }}
.eq-box {{
  width:160px; height:160px; margin:0 auto 16px; border-radius:28px;
  background:#141414; border:1px solid #2A2A2A;
  display:flex; align-items:center; justify-content:center;
}}
.eq-item strong {{ display:block; font-family:'Poppins',sans-serif; font-weight:800; font-size:24px; color:{W}; }}
.eq-item em {{ display:block; font-family:'Playfair',Georgia,serif; font-style:italic; font-weight:700; font-size:20px; color:{G}; }}
.plus-lg {{
  font-family:'Poppins',sans-serif; font-weight:800; font-size:64px; color:{G}; padding-top:48px;
}}
.result {{
  position:absolute; left:72px; right:72px; top:820px; z-index:4; text-align:center;
  font-family:'Playfair',Georgia,serif; font-style:italic; font-weight:700;
  font-size:42px; color:{G};
}}

/* SLIDE 5 CHAT */
.phone {{
  position:absolute; left:120px; right:120px; top:430px; z-index:4;
  background:#141414; border:1px solid #2A2A2A; border-radius:28px; overflow:hidden;
}}
.ph-head {{
  background:#0A0A0A; padding:16px 20px; display:flex; align-items:center; gap:12px;
  border-bottom:1px solid #2A2A2A;
}}
.ph-head .nm {{ font-family:'Poppins',sans-serif; font-weight:800; font-size:22px; color:{W}; }}
.ph-head .hr {{ font-family:'IBM Plex Mono',monospace; font-weight:500; font-size:16px; color:#9aa39c; margin-left:auto; }}
.ph-body {{ padding:22px 20px 28px; display:flex; flex-direction:column; gap:16px; }}
.row {{ display:flex; align-items:flex-end; gap:10px; }}
.row.me {{ justify-content:flex-end; }}
.bubble-u {{
  background:{G}; color:#0A0A0A; border-radius:18px 18px 4px 18px;
  padding:14px 16px; max-width:70%;
  font-family:'Poppins',sans-serif; font-weight:700; font-size:20px; line-height:1.3;
}}
.bubble-a {{
  background:#1E1E1E; color:{W}; border-radius:18px 18px 18px 4px;
  padding:14px 16px; max-width:74%;
  font-family:'Poppins',sans-serif; font-weight:700; font-size:20px; line-height:1.3;
}}
.av {{ width:44px; height:44px; border-radius:50%; object-fit:cover; flex-shrink:0; }}
.ts {{ font-family:'IBM Plex Mono',monospace; font-size:13px; color:#9aa39c; margin-top:4px; }}

/* SLIDE 6 CTA */
.ask {{
  position:absolute; left:72px; right:72px; top:200px; z-index:4; text-align:center;
  font-family:'Playfair',Georgia,serif; font-weight:800; font-size:52px; line-height:1.08; color:{W};
}}
.ask em {{ font-style:italic; color:{G}; font-weight:700; }}
.pre {{
  position:absolute; left:72px; right:72px; top:380px; z-index:4; text-align:center;
  font-family:'Poppins',sans-serif; font-weight:700; font-size:22px; line-height:1.35; color:{W};
}}
.kwbox {{
  position:absolute; left:120px; right:120px; top:510px; z-index:4;
  border:2px solid {G}; border-radius:18px; padding:36px 20px; text-align:center;
}}
.kwbox span {{
  font-family:'Playfair',Georgia,serif; font-weight:800; font-size:72px;
  letter-spacing:.18em; color:{G};
}}
.bottom-row {{
  position:absolute; left:72px; right:72px; top:800px; z-index:4;
  display:flex; align-items:center; justify-content:center;
}}
.send {{
  font-family:'Poppins',sans-serif; font-weight:700; font-size:26px; color:{W}; line-height:1.3;
  text-align:center;
}}
.send em {{ font-style:normal; color:{G}; }}
"""


def chrome(kicker: str, pill: str | None = None, plus: bool = True, bot_line: bool = True) -> str:
    p = ""
    if pill:
        p = f'<div class="pill"><i></i>{pill}</div>'
    pl = '<div class="plus">+</div>' if plus else ""
    bot = '<div class="hline bot"></div>' if bot_line else ""
    return (
        '<div class="tex"></div><div class="glow glow-tr"></div><div class="glow glow-bl"></div>'
        '<div class="hline top"></div>' + bot
        + f'<div class="brand">STLabs</div>{pl}'
        f'<div class="kicker">{kicker}</div>{p}'
        '<div class="firma">sebastian.stlabs.ar</div>'
    )


def mapa_icon() -> str:
    return (
        '<svg viewBox="0 0 64 64" width="88" height="88">'
        '<rect x="8" y="8" width="48" height="14" rx="4" fill="none" stroke="#00FFB2" stroke-width="3"/>'
        '<rect x="8" y="28" width="30" height="14" rx="4" fill="none" stroke="#00FFB2" stroke-width="3"/>'
        '<rect x="8" y="48" width="40" height="14" rx="4" fill="none" stroke="#00FFB2" stroke-width="3"/>'
        '<path d="M32 22v6M23 42v6" fill="none" stroke="#00FFB2" stroke-width="3"/>'
        '</svg>'
    )


def claude_img(size: int = 88) -> str:
    src = uri(A / "claude.png")
    return (
        f'<img class="claude" src="{src}" width="{size}" height="{size}" alt="" '
        f'style="width:{size}px;height:{size}px;object-fit:contain;">'
    )


def slide_01() -> str:
    dude = uri(A / "pixel-dude.png")
    return (
        '<section class="slide" data-id="01">'
        + chrome("01 / 05", pill="A medida", plus=False, bot_line=False)
        + '<div class="hero"></div><div class="hero-fade"></div>'
        + '<h1 class="display"><em>Así se genera</em><br>un agente<br><em>a medida.</em></h1>'
        + f'<div class="clip dude"><div class="corners"><span class="tl"></span><span class="tr"></span><span class="bl"></span><span class="br"></span></div><img src="{dude}" alt=""></div>'
        + f'<div class="clip cf">{claude_img(96)}</div>'
        + '<div class="cta-side">primero el proceso →</div>'
        + "</section>"
    )


def slide_02() -> str:
    wch, cost, bell = uri(A / "pixel-wrench.png"), uri(A / "pixel-cost.png"), uri(A / "pixel-bell.png")
    cards = [
        (wch, "Mapear la operación", "Sacamos de tu cabeza cada paso, dueño y excepción."),
        (cost, "Documentar el flujo", "Queda escrito, claro y delegable. Sin improvisar."),
        (bell, "Generar el agente", "Lo armamos sobre ESE proceso, no sobre uno genérico."),
    ]
    html_cards = "".join(
        f'<div class="card"><img src="{img}" alt=""><div class="div"></div><div><h3>{t}</h3><p>{d}</p></div></div>'
        for img, t, d in cards
    )
    return (
        '<section class="slide" data-id="02">'
        + chrome("01 / 05 — El proceso")
        + '<h1 class="h2">Los <em>3</em> pasos</h1>'
        + '<p class="sub">para generar un agente que arme tu operación.</p>'
        + f'<div class="cards">{html_cards}</div>'
        + '<div class="cta-side">y casi todos se saltean el primero →</div>'
        + "</section>"
    )


def slide_03() -> str:
    return (
        '<section class="slide" data-id="03">'
        + chrome("02 / 05 — Lo que se saltea")
        + '<h1 class="h2">Lo que casi<br><em>nadie</em> hace</h1>'
        + '<p class="sub">arrancan el agente sin mapa… y después <b style="color:#00FFB2">no escala.</b></p>'
        + '<div class="bubble">Poné un agente y que resuelva. El proceso lo vemos después.</div>'
        + '<div class="tag80"><i></i>9 de 10</div>'
        + '<div class="metric"><div class="lab">Primera sesión de mapeo · 1 operación</div>'
        '<div class="num">12<span>pasos</span></div>'
        '<div class="foot">y de ese mapa nace el agente</div></div>'
        + '<div class="cta-side">el método correcto es al revés →</div>'
        + "</section>"
    )


def slide_04() -> str:
    return (
        '<section class="slide" data-id="04">'
        + chrome("03 / 05 — El método")
        + '<h1 class="h2">El <em>método</em></h1>'
        + '<p class="sub">Primero el mapa. Después se genera el agente.</p>'
        + '<div class="eq">'
        f'<div class="eq-item"><div class="eq-box">{mapa_icon()}</div><strong>El mapa</strong><em>tu operación</em></div>'
        '<div class="plus-lg">+</div>'
        f'<div class="eq-item"><div class="eq-box">{claude_img(96)}</div><strong>Claude</strong><em>lo genera</em></div>'
        "</div>"
        + '<div class="result">= tu agente a medida</div>'
        + '<div class="cta-side">así se ve cuando lo pedís →</div>'
        + "</section>"
    )


def slide_05() -> str:
    av = uri(A / "sebas-avatar.png")
    return (
        '<section class="slide" data-id="05">'
        + chrome("04 / 05 — En vivo")
        + '<h1 class="h2"><em>Así</em> se genera</h1>'
        + '<p class="sub">Pedís el proceso. El agente queda mapeado y <b style="color:#00FFB2">listo para ejecutar.</b></p>'
        + '<div class="phone"><div class="ph-head">'
        f'{claude_img(32)}<div class="nm">Claude</div><div class="hr">11:20</div></div>'
        '<div class="ph-body">'
        f'<div class="row me"><div><div class="bubble-u">Armá el agente con el seguimiento comercial.</div><div class="ts" style="text-align:right">11:20</div></div><img class="av" src="{av}" alt=""></div>'
        f'<div class="row">{claude_img(36)}<div><div class="bubble-a">Listo. 12 pasos documentados y el agente ya corre el flujo.</div><div class="ts">11:24</div></div></div>'
        "</div></div>"
        + '<div class="cta-side">esto lo hacemos sobre tu operación →</div>'
        + "</section>"
    )


def slide_06() -> str:
    return (
        '<section class="slide" data-id="06">'
        + chrome("", pill="A medida", plus=False)
        + '<h1 class="ask">¿Querés que te genere<br>el <em>agente</em> a medida?</h1>'
        + '<p class="pre">Mapeo tu operación, documento el flujo y te dejo el agente personalizado listo.</p>'
        + '<div class="kwbox"><span>PROCESO</span></div>'
        + '<div class="bottom-row"><div class="send">Comentá <em>PROCESO</em> y arrancamos la generación <em>→</em></div></div>'
        + "</section>"
    )


def main():
    slides = [slide_01(), slide_02(), slide_03(), slide_04(), slide_05(), slide_06()]
    html = (
        "<!DOCTYPE html>\n<html lang=\"es\"><head><meta charset=\"UTF-8\">\n"
        "<title>Así se genera un agente a medida — STLabs</title>\n"
        f"<style>{build_css()}</style></head>\n"
        f"<body><div class=\"sheet\">{''.join(slides)}</div></body></html>"
    )
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    meta = {
        "titulo": "Así se genera un agente a medida",
        "slides": 6,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "clonado",
        "keyword_portada": "PROCESO",
        "modo": "negro",
        "id": "2026-08-18-nueva-forma-agentes",
        "fecha": "2026-08-18",
        "notas": "Copy nuevo: proceso de generación (mapear, documentar, generar). Datos 12 pasos / 9 de 10. Chat distinto. Keyword PROCESO.",
    }
    (B / "index.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(slides)} slides")


if __name__ == "__main__":
    main()
