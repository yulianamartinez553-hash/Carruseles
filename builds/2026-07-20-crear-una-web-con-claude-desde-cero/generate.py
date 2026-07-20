# -*- coding: utf-8 -*-
"""
Clon STLabs — "Si tuviera que aprender a crear una Web con Claude desde Cero"
Referencia: carrusel @ignaciorodriguezb_ (8 slides, fondo negro, titulo serif +
acento cobre + manuscrita). Clon en MODO BLANCO con identidad STLabs:
- Titulo serif elegante y grueso (Playfair Display Black) graphite + acento verde.
- Lineas de acento manuscritas (Caveat) en verde.
- Diagramas line-art recreados en graphite con acentos verdes.
- Logo/rafaga de Claude: naranja (intacto).
- Firma sebastian.stlabs.ar en cada slide. Sin @handle, sin contador, sin UI de IG.
"""
from __future__ import annotations
import base64, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from stlabs_kit import chrome, write_html, render, package  # noqa: E402

FONTS = REPO / "fonts"
ASSETS = REPO / "assets"


def _b64_font(fname):
    return base64.b64encode((FONTS / fname).read_bytes()).decode()


def _b64_img(path):
    return base64.b64encode(Path(path).read_bytes()).decode()


PLAYFAIR = _b64_font("PlayfairDisplay[wght].ttf")
PLAYFAIR_IT = _b64_font("PlayfairDisplay-Italic[wght].ttf")
CAVEAT = _b64_font("Caveat[wght].ttf")
HERO_URI = f"data:image/png;base64,{_b64_img(ASSETS / 'slide1-hero.png')}"
SEB_URI = f"data:image/jpeg;base64,{_b64_img(REPO / 'seb.jpg')}"

# ── acentos de marca ──
V = "#00FFB2"          # verde STLabs
INK = "#0A0A0A"        # tinta principal
INK2 = "#20221f"       # tinta line-art
BODY = "#3a3f3c"       # cuerpo
CLAUDE = "#D97757"     # naranja Claude (intacto)
GOLD = "#E4B24A"       # dorado thumbnail (elemento recreado)

FONT_FACES = f"""
@font-face{{font-family:'Playfair Display';font-weight:400 900;font-style:normal;font-display:block;
 src:url(data:font/ttf;base64,{PLAYFAIR}) format('truetype');}}
@font-face{{font-family:'Playfair Display';font-weight:400 900;font-style:italic;font-display:block;
 src:url(data:font/ttf;base64,{PLAYFAIR_IT}) format('truetype');}}
@font-face{{font-family:'Caveat';font-weight:400 700;font-style:normal;font-display:block;
 src:url(data:font/ttf;base64,{CAVEAT}) format('truetype');}}
"""

EXTRA_CSS = FONT_FACES + f"""
:root{{--claude:{CLAUDE};--gold:{GOLD};--ink:{INK};--ink2:{INK2};--body:{BODY};
 --serif:'Playfair Display',serif;--hand:'Caveat',cursive;}}

/* ── MODO BLANCO ── */
.sheet{{background:#e6e6e6;}}
.slide{{
  color:var(--ink);
  background:
    radial-gradient(46% 30% at 90% 6%, rgba(0,255,178,.10), transparent 62%),
    radial-gradient(44% 32% at 6% 96%, rgba(0,255,178,.07), transparent 60%),
    linear-gradient(168deg,#FFFFFF 0%, #F8F8F6 55%, #F1F2F0 100%);
}}
.slide.grid::before{{
  opacity:1;
  background-image:
    linear-gradient(rgba(10,10,10,.038) 1px, transparent 1px),
    linear-gradient(90deg, rgba(10,10,10,.038) 1px, transparent 1px);
  background-size:58px 58px;
}}
.web{{color:var(--verde);opacity:.95;font-weight:500;bottom:64px;}}

/* ── tipografia ── */
.pad{{position:absolute;inset:0;padding:96px 82px 0;z-index:5;}}
.h{{font-family:var(--serif);font-weight:900;color:var(--ink);line-height:1.02;letter-spacing:-.5px;text-align:left;}}
.h .gr{{color:var(--verde);font-family:var(--serif);font-weight:900;font-style:italic;}}
.body{{font-family:var(--cond);font-weight:500;font-size:35px;line-height:1.34;color:var(--body);text-align:left;max-width:915px;}}
.body b{{color:var(--ink);font-weight:700;}}
.body .gr{{color:#0b7d57;font-weight:700;}}   /* verde legible SOLO para negrita de cuerpo */
.hand{{font-family:var(--hand);font-weight:700;color:var(--verde);font-size:60px;line-height:1;
  text-shadow:0 1px 0 rgba(6,60,42,.30);letter-spacing:.5px;}}

/* caja inferior con borde verde */
.boxg{{position:absolute;left:82px;right:82px;z-index:6;padding:30px 34px;border-radius:22px;
  border:2px solid var(--verde);background:rgba(0,255,178,.07);
  box-shadow:0 14px 40px rgba(10,10,10,.06);}}
.boxg p{{font-family:var(--cond);font-weight:500;font-size:34px;line-height:1.28;color:var(--ink);text-align:center;}}
.boxg b{{font-weight:700;color:#0b7d57;}}

/* ── SLIDE 1 cover ── */
.s1-top{{font-family:var(--serif);font-weight:900;font-size:70px;line-height:1;color:var(--ink);}}
.s1-top .gr{{color:var(--verde);font-style:italic;}}
.brush{{position:absolute;right:120px;top:60px;z-index:7;}}
.s1-img{{position:absolute;left:82px;right:82px;top:212px;height:430px;z-index:4;border-radius:18px;overflow:hidden;
  border:3px solid rgba(0,255,178,.55);box-shadow:0 26px 60px rgba(10,10,10,.20);}}
.s1-img img{{width:100%;height:100%;object-fit:cover;object-position:center 42%;}}
.s1-title{{position:absolute;left:82px;right:82px;top:690px;z-index:5;font-family:var(--serif);font-weight:900;
  font-size:66px;line-height:1.06;color:var(--ink);text-align:left;}}
.s1-title .gr{{color:var(--verde);font-style:italic;}}
.s1-hand{{position:absolute;left:82px;bottom:150px;z-index:6;}}
.s1-hand .arw{{display:inline-block;margin-left:14px;}}

/* ── flow slide 2 ── */
.flow{{position:absolute;left:60px;right:60px;top:470px;z-index:5;display:flex;justify-content:space-between;align-items:flex-start;}}
.fcol{{width:246px;display:flex;flex-direction:column;align-items:center;text-align:center;}}
.fbox{{width:150px;height:150px;border-radius:26px;border:3px solid var(--ink2);background:#fff;
  display:flex;align-items:center;justify-content:center;box-shadow:0 10px 26px rgba(10,10,10,.08);position:relative;}}
.fbox::after{{content:'';position:absolute;inset:-3px;border-radius:26px;border:2px solid rgba(0,255,178,.5);
  clip-path:polygon(0 0,42% 0,42% 12%,12% 12%,12% 42%,0 42%);}}
.flab{{font-family:var(--pop);font-weight:800;font-size:31px;color:var(--ink);margin-top:22px;letter-spacing:.5px;}}
.fsub{{font-family:var(--mono);font-weight:500;font-size:22px;color:var(--body);margin-top:4px;}}
.fconn{{flex:1;height:150px;display:flex;align-items:center;justify-content:center;}}

/* ── diagram generico centrado ── */
.diag{{position:absolute;left:0;right:0;z-index:4;display:flex;justify-content:center;align-items:center;}}

/* ── SLIDE 8 CTA ── */
.s8-top{{font-family:var(--cond);font-weight:500;font-size:33px;line-height:1.3;color:var(--body);text-align:left;}}
.s8-top b{{color:var(--ink);font-weight:700;}}
.s8-title{{font-family:var(--serif);font-weight:900;font-size:78px;line-height:1.0;color:var(--ink);text-align:left;margin-top:14px;}}
.s8-title .gr{{color:var(--verde);font-style:italic;}}
.thumb{{position:absolute;left:120px;right:120px;top:520px;height:372px;z-index:5;border-radius:20px;overflow:hidden;
  border:3px solid var(--claude);box-shadow:0 22px 55px rgba(10,10,10,.22);background:#0A0A0A;}}
.thumb img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;
  filter:brightness(.82) contrast(1.05) saturate(.9);}}
.thumb-scrim{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,10,10,.86) 0%,rgba(10,10,10,.35) 46%,rgba(10,10,10,.12) 100%);}}
.thumb-super{{position:absolute;left:34px;top:70px;font-family:var(--pop);font-weight:800;font-size:60px;line-height:.92;
  color:var(--gold);text-shadow:0 3px 12px rgba(0,0,0,.6);letter-spacing:1px;}}
.thumb-claude{{position:absolute;left:36px;bottom:52px;width:78px;height:78px;border-radius:18px;background:var(--claude);
  display:flex;align-items:center;justify-content:center;box-shadow:0 8px 22px rgba(217,119,87,.5);}}
.thumb-play{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:96px;height:96px;border-radius:50%;
  background:rgba(255,255,255,.92);display:flex;align-items:center;justify-content:center;box-shadow:0 8px 26px rgba(0,0,0,.4);}}
.thumb-play::after{{content:'';border-left:30px solid #0A0A0A;border-top:19px solid transparent;border-bottom:19px solid transparent;margin-left:7px;}}
.s8-hand{{position:absolute;right:96px;top:905px;z-index:6;text-align:right;}}
.s8-bot{{position:absolute;left:82px;right:82px;top:1010px;z-index:5;font-family:var(--cond);font-weight:500;
  font-size:34px;line-height:1.3;color:var(--body);text-align:left;}}
.s8-bot b{{color:var(--ink);font-weight:700;}}
"""


# ─────────────────────────────────────────── SVG helpers (line-art) ──
def _svg(w, h, inner, extra=""):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" '
            f'xmlns="http://www.w3.org/2000/svg" {extra}>{inner}</svg>')


ST = 'stroke="#20221f" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" fill="none"'
STG = 'stroke="#00FFB2" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" fill="none"'


def icon_brush():
    return _svg(76, 76, f'''
      <rect x="14" y="10" width="30" height="20" rx="5" {ST} transform="rotate(38 29 20)"/>
      <path d="M40 26 L60 46" {ST}/>
      <path d="M20 40 C14 50 12 58 22 60 C34 62 34 52 30 48" {STG}/>
      <path d="M24 54 L30 60" {STG}/>''')


def icon_code():
    return _svg(80, 76, f'''
      <rect x="10" y="14" width="60" height="48" rx="8" {ST}/>
      <path d="M10 26 H70" {ST}/>
      <circle cx="19" cy="20" r="2.4" fill="#20221f"/><circle cx="27" cy="20" r="2.4" fill="#20221f"/>
      <path d="M30 38 L23 45 L30 52" {STG}/>
      <path d="M50 38 L57 45 L50 52" {STG}/>
      <path d="M44 35 L36 55" {STG}/>''')


def icon_rocket():
    return _svg(76, 76, f'''
      <path d="M38 8 C50 16 54 30 54 42 L38 52 L22 42 C22 30 26 16 38 8 Z" {ST}/>
      <circle cx="38" cy="30" r="7" {STG}/>
      <path d="M22 42 L14 52 L26 50" {ST}/>
      <path d="M54 42 L62 52 L50 50" {ST}/>
      <path d="M32 56 C34 64 42 64 44 56" {STG}/>''')


def conn_arrow(w=150):
    dots = "".join(
        f'<circle cx="{18 + i*20}" cy="75" r="4" fill="#20221f" opacity="{0.35 + i*0.13:.2f}"/>'
        for i in range(4))
    ax = 18 + 4 * 20
    head = (f'<path d="M{ax} 75 H{w-14}" {STG}/>'
            f'<path d="M{w-26} 66 L{w-13} 75 L{w-26} 84" {STG}/>')
    return _svg(w, 150, dots + head)


# ─────────────────────────────────────────── SLIDES ──
def _grid(section):
    return section.replace('class="slide"', 'class="slide grid"', 1)


def slide1():
    inner = f"""
<div class="brush">{icon_brush()}</div>
<div class="pad" style="padding-top:70px;">
  <h1 class="s1-top">Si tuviera <span class="gr">que aprender</span></h1>
</div>
<div class="s1-img"><img src="{HERO_URI}" alt="pantalla diseno de web"></div>
<h2 class="s1-title">Crear una Web con<br><span class="gr">Claude Design + Claude Code</span><br>desde Cero&hellip;</h2>
<div class="s1-hand"><span class="hand">esto es lo que har&iacute;a</span><span class="hand arw">&rarr;</span></div>
"""
    return _grid(chrome(1, inner, bridges=None, footer=True))


def slide2():
    inner = f"""
<div class="pad">
  <h2 class="h" style="font-size:82px;">Primero: <span class="gr">el flujo.</span></h2>
  <p class="body" style="margin-top:26px;">Crear una web profesional con Claude tiene 3 etapas claras. Si te salt&aacute;s una, se nota. El secreto es el orden.</p>
</div>
<div class="flow">
  <div class="fcol"><div class="fbox">{icon_brush()}</div><div class="flab">DISE&Ntilde;O</div><div class="fsub">Claude Design</div></div>
  <div class="fconn">{conn_arrow(150)}</div>
  <div class="fcol"><div class="fbox">{icon_code()}</div><div class="flab">C&Oacute;DIGO</div><div class="fsub">Claude Code</div></div>
  <div class="fconn">{conn_arrow(150)}</div>
  <div class="fcol"><div class="fbox">{icon_rocket()}</div><div class="flab">DEPLOY</div><div class="fsub">Vercel</div></div>
</div>
<div class="boxg" style="bottom:150px;"><p><b>Dise&ntilde;&aacute;s</b>, baj&aacute;s a c&oacute;digo y public&aacute;s. Ese es todo el juego.</p></div>
"""
    return _grid(chrome(2, inner, bridges=None, footer=True))


def slide3():
    diag = _svg(560, 400, f'''
      <rect x="40" y="40" width="480" height="320" rx="16" {ST}/>
      <path d="M40 92 H520" {ST}/>
      <circle cx="66" cy="66" r="5" {ST}/><circle cx="86" cy="66" r="5" {ST}/><circle cx="106" cy="66" r="5" {ST}/>
      <rect x="70" y="120" width="150" height="200" rx="8" {ST}/>
      <path d="M92 150 H198 M92 176 H180 M92 202 H198 M92 228 H170" {ST}/>
      <rect x="250" y="120" width="200" height="120" rx="8" {STG}/>
      <path d="M270 210 L305 172 L330 196 L360 160 L430 210 Z" {STG}/>
      <circle cx="300" cy="150" r="10" {STG}/>
      <path d="M300 270 H450 M300 296 H420" {ST}/>
      <path d="M470 300 L470 340 L438 340 M470 300 L438 300 L438 340" {STG}/>
      <path d="M470 300 l0 0" stroke="#00FFB2"/>
      <path d="M452 322 l18 18 l18 -18" {STG}/>
      <!-- paleta de color -->
      <rect x="360" y="60" width="130" height="26" rx="6" {ST}/>
      <rect x="366" y="66" width="24" height="14" rx="3" fill="#20221f"/>
      <rect x="394" y="66" width="24" height="14" rx="3" fill="#00FFB2"/>
      <rect x="422" y="66" width="24" height="14" rx="3" fill="#9aa39c"/>
      <rect x="450" y="66" width="24" height="14" rx="3" fill="#20221f" opacity=".4"/>
    ''')
    inner = f"""
<div class="pad">
  <h2 class="h" style="font-size:72px;">Dise&ntilde;&aacute; en <span class="gr">Claude&nbsp;Design.</span></h2>
  <p class="body" style="margin-top:24px;">Antes de tocar c&oacute;digo, dise&ntilde;&aacute;. Claude Design es como tener un dise&ntilde;ador UX/UI experto. Le pas&aacute;s tu idea y arma el mockup completo de la web.</p>
</div>
<div class="diag" style="top:520px;">{diag}</div>
<div style="position:absolute;left:82px;bottom:170px;z-index:6;"><span class="hand">tu dise&ntilde;ador UX en 5 min</span><span class="hand" style="margin-left:12px;">&rarr;</span></div>
"""
    return _grid(chrome(3, inner, bridges=None, footer=True))


def slide4():
    diag = _svg(620, 360, f'''
      <!-- pergamino super prompt -->
      <path d="M70 60 C50 60 50 96 70 96 L70 300 C50 300 50 336 70 336 L300 336 C320 336 320 300 300 300 L300 96 C320 96 320 60 300 60 Z" {STG}/>
      <path d="M100 198 H270 M100 232 H250 M100 266 H236" {ST}/>
      <path d="M300 200 L410 200" {STG}/>
      <path d="M392 186 L412 200 L392 214" {STG}/>
      <!-- browser destino -->
      <rect x="430" y="120" width="160" height="150" rx="10" {ST}/>
      <path d="M430 150 H590" {ST}/>
      <path d="M450 172 H570 M450 196 H540 M450 220 H570 M450 244 H520" {ST}/>
    ''')
    inner = f"""
<div class="pad">
  <h2 class="h" style="font-size:70px;">Empez&aacute; con un <span class="gr">Super&nbsp;Prompt.</span></h2>
  <p class="body" style="margin-top:22px;">No le digas &lsquo;haceme una web&rsquo;. Pedile a Claude que TE arme el prompt: contale tu idea, los colores, el estilo y la identidad. Que &eacute;l lo convierta en un super prompt detallado.</p>
</div>
<div class="diag" style="top:470px;">{diag}</div>
<div style="position:absolute;left:224px;top:566px;z-index:7;font-family:var(--pop);font-weight:800;font-size:29px;color:var(--verde);transform:rotate(-4deg);text-align:center;line-height:1.02;">SUPER<br>PROMPT</div>
<div class="boxg" style="bottom:150px;"><p>Un buen prompt <b>rinde m&aacute;s que 25 mensajes</b> dialogando.</p></div>
"""
    return _grid(chrome(4, inner, bridges=None, footer=True))


def slide5():
    diag = _svg(640, 340, f'''
      <!-- wireframe -->
      <rect x="30" y="60" width="230" height="230" rx="12" {ST}/>
      <path d="M30 96 H260" {ST}/>
      <path d="M55 130 L120 130 M55 130 L55 250 L235 250 L235 130 L170 130" {ST}/>
      <path d="M55 130 L235 250 M235 130 L55 250" {ST}/>
      <!-- arrow -->
      <path d="M290 175 L360 175" {STG}/>
      <path d="M342 160 L362 175 L342 190" {STG}/>
      <!-- code window -->
      <rect x="390" y="60" width="230" height="230" rx="12" {STG}/>
      <path d="M390 96 H620" {ST}/>
      <circle cx="410" cy="78" r="4" {ST}/><circle cx="426" cy="78" r="4" {ST}/>
      <path d="M596 78 l-14 -12 M596 78 l-14 12 M582 66 l0 0" stroke="#00FFB2" stroke-width="3" fill="none"/>
      <path d="M420 130 H470 M420 156 H540 M440 182 H580 M440 208 H520 M420 234 H500" {STG}/>
      <path d="M580 118 l16 12 l-16 12 M418 118 l-2 0" {ST}/>
    ''')
    inner = f"""
<div class="pad">
  <h2 class="h" style="font-size:72px;">Baj&aacute; el dise&ntilde;o a <span class="gr">C&oacute;digo.</span></h2>
  <p class="body" style="margin-top:22px;">Cuando el dise&ntilde;o te gusta, pedile a Claude Design que lo exporte en estructura de c&oacute;digo. Despu&eacute;s lo llev&aacute;s a Claude Code, que lo lee y lo construye de verdad.</p>
</div>
<div class="diag" style="top:520px;">{diag}</div>
<div style="position:absolute;left:82px;bottom:168px;z-index:6;"><span class="hand" style="border-bottom:3px solid var(--verde);padding-bottom:4px;">del mockup al c&oacute;digo real</span></div>
"""
    return _grid(chrome(5, inner, bridges=None, footer=True))


def slide6():
    # escalera de fases
    steps = ""
    for i in range(5):
        x = 60 + i * 108
        h = 60 + i * 62
        y = 360 - h
        steps += f'<rect x="{x}" y="{y}" width="104" height="{h}" rx="8" {ST}/>'
        steps += (f'<text x="{x+52}" y="390" font-family="IBM Plex Mono" font-size="21" '
                  f'fill="#20221f" text-anchor="middle">Fase {i}</text>')
        steps += f'<path d="M{x+42} {y+20} l8 9 l16 -18" {STG}/>'
    # mini browser arriba del ultimo escalon
    top_x = 60 + 4 * 108
    steps += f'<rect x="{top_x+8}" y="8" width="88" height="66" rx="8" {STG}/>'
    steps += f'<path d="M{top_x+8} 28 H{top_x+96}" {STG}/>'
    steps += f'<path d="M{top_x+22} 44 H{top_x+82} M{top_x+22} 58 H{top_x+70}" {ST}/>'
    diag = _svg(620, 410, steps)
    inner = f"""
<div class="pad">
  <h2 class="h" style="font-size:82px;">Constru&iacute; por <span class="gr">Fases.</span></h2>
  <p class="body" style="margin-top:24px;">No le pidas todo de una. Claude Code construye la web por <b>fases</b>: estructura, secciones, estilos, responsive. Aprob&aacute;s e iter&aacute;s en cada paso.</p>
</div>
<div class="diag" style="top:470px;">{diag}</div>
<div class="boxg" style="bottom:150px;"><p>Us&aacute; <b>Sonnet</b> para <b>construir r&aacute;pido.</b> Esfuerzo bajo, resultados altos.</p></div>
"""
    return _grid(chrome(6, inner, bridges=None, footer=True))


def slide7():
    diag = _svg(660, 320, f'''
      <!-- captura con error -->
      <rect x="30" y="70" width="200" height="200" rx="12" {ST}/>
      <path d="M30 104 H230" {ST}/>
      <rect x="55" y="128" width="150" height="70" rx="6" {ST}/>
      <path d="M55 220 H205 M55 244 H170" {ST}/>
      <circle cx="210" cy="90" r="18" {STG.replace('#00FFB2','#FF9D3C')}/>
      <path d="M210 82 V92" stroke="#FF9D3C" stroke-width="3.4" stroke-linecap="round"/>
      <circle cx="210" cy="99" r="2.4" fill="#FF9D3C"/>
      <!-- chispa -->
      <path d="M300 170 L318 170 M309 161 L309 179 M303 164 L315 176 M315 164 L303 176" {STG}/>
      <path d="M348 170 L418 170" {STG}/>
      <path d="M400 156 L420 170 L400 184" {STG}/>
      <!-- captura arreglada -->
      <rect x="440" y="70" width="200" height="200" rx="12" {STG}/>
      <path d="M440 104 H640" {ST}/>
      <rect x="465" y="132" width="150" height="46" rx="10" {STG}/>
      <path d="M500 155 l12 12 l24 -26" {STG}/>
      <path d="M465 210 H615 M465 234 H580" {ST}/>
    ''')
    inner = f"""
<div class="pad">
  <h2 class="h" style="font-size:74px;">Corregi&iacute; con <span class="gr">Capturas.</span></h2>
  <p class="body" style="margin-top:22px;">&iquest;Un texto se sale de un bot&oacute;n? &iquest;No te gusta un color? Mandale una captura de pantalla y dec&iacute;selo en tu idioma normal. Claude detecta el error en el c&oacute;digo y lo arregla solo.</p>
</div>
<div class="diag" style="top:520px;">{diag}</div>
<div style="position:absolute;left:82px;bottom:168px;z-index:6;"><span class="hand">sin saber nada t&eacute;cnico</span><span class="hand" style="margin-left:12px;">&nearr;</span></div>
"""
    return _grid(chrome(7, inner, bridges=None, footer=True))


def slide8():
    claude_burst = _svg(46, 46,
        "".join(f'<rect x="21" y="4" width="4" height="16" rx="2" fill="#fff" '
                f'transform="rotate({a} 23 23)"/>' for a in range(0, 360, 30)))
    inner = f"""
<div class="pad" style="padding-top:78px;">
  <p class="s8-top">&hellip;si llegaste hasta ac&aacute;, ya sab&eacute;s que crear una web con Claude no es magia, es <b>proceso.</b></p>
  <h2 class="s8-title">&iquest;Quer&eacute;s el<br><span class="gr">flujo completo?</span></h2>
</div>
<div class="thumb">
  <img src="{SEB_URI}" alt="Sebastian Garcia">
  <div class="thumb-scrim"></div>
  <div class="thumb-super">SUPERA<br>AL 99%</div>
  <div class="thumb-claude">{claude_burst}</div>
  <div class="thumb-play"></div>
</div>
<div class="s8-hand"><span class="hand">mi entrenamiento completo.</span></div>
<p class="s8-bot">Arm&eacute; un entrenamiento gratis donde <b>muestro paso a paso todo: el dise&ntilde;o, el c&oacute;digo, el deploy.</b> Todo lo que uso para crear webs.</p>
"""
    return _grid(chrome(8, inner, bridges=None, footer=True))


def main():
    slides = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]
    write_html(slides, str(BUILD / "carrusel.html"), extra_css=EXTRA_CSS)
    render(str(BUILD))
    meta = {
        "titulo": "Crear Una Web Con Claude Desde Cero",
        "slides": 8,
        "fondo": "reticula_fina_blanco",
        "familia_visual": "blueprint",
        "origen": "screenshot",
        "keyword_portada": "WEB",
    }
    out = package(str(BUILD), "STLabs-CrearWebConClaude", meta=meta)
    print("OK ->", out)


if __name__ == "__main__":
    main()
