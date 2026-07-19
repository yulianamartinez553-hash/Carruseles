# -*- coding: utf-8 -*-
"""Clon Fable 5 Anthropic → STLabs · blanco · retícula · Impact · acento #00FFB2."""
from __future__ import annotations

import base64
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html, render, package  # noqa: E402

KEYWORD = "FABLE"
TOTAL = 7
WORD_DIR = REPO / "Word"
SEB_URI = f"data:image/jpeg;base64,{base64.b64encode((REPO / 'seb.jpg').read_bytes()).decode()}"

# Claude default del repo (bichito naranja cuadrado) — excepción al acento verde
CLAUDE_PNG = REPO / "assets" / "claude.png"
if not CLAUDE_PNG.exists():
    CLAUDE_PNG = BUILD / "assets" / "claude.png"
CLAUDE_URI = "data:image/png;base64," + base64.b64encode(CLAUDE_PNG.read_bytes()).decode()

# Acento STLabs: SIEMPRE reemplaza el naranja/coral del original
VERDE = "#00FFB2"
VERDE_SOFT = "rgba(0,255,178,.12)"
INK_ON_VERDE = "#04130b"

EXTRA_CSS = f"""
:root{{--acento:{VERDE};--acento-ink:{INK_ON_VERDE};}}
.sheet{{background:#e8e8e8;}}
.slide{{
  color:#0A0A0A;
  background:
    radial-gradient(42% 30% at 90% 8%, {VERDE_SOFT}, transparent 60%),
    linear-gradient(180deg,#FFFFFF 0%, #F7F7F5 100%);
}}
.slide.grid::before{{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.9;
  background-image:
    linear-gradient(rgba(10,10,10,.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(10,10,10,.045) 1px, transparent 1px);
  background-size:48px 48px;
}}
.web{{display:none!important;}}
.foot{{
  position:absolute;left:0;right:0;bottom:70px;z-index:8;text-align:center;
  font-family:var(--mono);font-size:22px;letter-spacing:1px;color:var(--verde);
}}
.swipe{{
  position:absolute;left:50%;transform:translateX(-50%);bottom:120px;z-index:8;
  font-family:var(--mono);font-size:18px;letter-spacing:1px;color:#6a736e;
  background:#fff;border:1px solid rgba(10,10,10,.12);border-radius:999px;
  padding:10px 22px;box-shadow:0 8px 20px rgba(10,10,10,.06);
}}
.wm{{
  position:absolute;right:40px;bottom:160px;z-index:1;pointer-events:none;
  font-family:var(--impact);font-weight:900;font-size:280px;line-height:1;
  color:rgba(10,10,10,.05);letter-spacing:-4px;
}}

/* ── COVER ── */
.cover{{padding:72px 64px 0;text-align:center;}}
.cover-k{{font-family:var(--mono);font-size:18px;letter-spacing:3px;color:#6a736e;text-transform:uppercase;}}
.cover-h{{
  margin-top:28px;font-family:var(--impact);font-weight:900;font-size:100px;line-height:.9;
  letter-spacing:1px;color:#0A0A0A;text-transform:none;
  -webkit-text-stroke:2.5px #0A0A0A;paint-order:stroke fill;
}}
.cover-line2{{margin-top:10px;display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;}}
.cover-script{{
  font-family:var(--serif);font-style:italic;font-weight:700;font-size:54px;color:var(--acento);
}}
.trampa{{
  display:inline-block;background:var(--acento);color:var(--acento-ink);border-radius:14px;
  padding:8px 22px;font-family:var(--serif);font-weight:700;font-size:42px;line-height:1.1;
}}
.cover-sub{{
  margin:22px auto 0;max-width:820px;font-family:var(--cond);font-size:30px;line-height:1.35;color:#3a3f3c;
}}
.cover-sub b{{color:#0A0A0A;}}

.chart{{
  position:absolute;left:90px;right:90px;bottom:170px;height:420px;z-index:4;
  display:flex;align-items:flex-end;justify-content:center;gap:28px;
}}
.bar{{
  width:200px;border-radius:18px 18px 8px 8px;position:relative;
  display:flex;flex-direction:column;align-items:center;justify-content:flex-end;
  padding:0 12px 28px;box-shadow:0 16px 40px rgba(10,10,10,.10);
}}
.bar.s{{height:190px;background:#D8D8D6;}}
.bar.m{{height:270px;background:#C4C4C1;}}
.bar.t{{height:360px;background:var(--acento);}}
.bar .star{{font-size:22px;color:#fff;margin-bottom:8px;line-height:1;}}
.bar.s .star,.bar.m .star{{color:#5a5a5a;}}
.bar.t .star{{color:var(--acento-ink);}}
.bar .name{{font-family:var(--pop);font-weight:800;font-size:28px;color:#fff;}}
.bar.s .name,.bar.m .name{{color:#2a2a2a;}}
.bar.t .name{{color:var(--acento-ink);}}
.bar .tag{{font-family:var(--mono);font-size:16px;letter-spacing:1px;color:rgba(255,255,255,.9);margin-top:4px;}}
.bar.s .tag,.bar.m .tag{{color:#555;}}
.bar.t .tag{{color:var(--acento-ink);opacity:.85;}}
.nuevo{{
  position:absolute;top:-14px;right:-10px;background:#fff;color:var(--acento);
  border:2px solid var(--acento);border-radius:999px;padding:4px 12px;
  font-family:var(--mono);font-size:14px;letter-spacing:1px;font-weight:600;
}}
.claude{{
  position:absolute;top:-118px;left:50%;transform:translateX(-50%);
  width:132px;height:124px;filter:drop-shadow(0 10px 18px rgba(0,0,0,.18));
}}
.claude img{{width:100%;height:100%;object-fit:contain;display:block;}}

/* ── USO slides ── */
.uso{{padding:88px 72px 0;text-align:left;}}
.uso-num{{
  font-family:var(--serif);font-style:italic;font-weight:700;font-size:54px;color:var(--acento);
  display:inline-block;margin-right:12px;line-height:1;
}}
.uso-lab{{font-family:var(--mono);font-size:18px;letter-spacing:2px;color:#8a918c;vertical-align:middle;}}
.uso-h{{
  margin-top:18px;font-family:var(--impact);font-weight:900;font-size:64px;line-height:.98;
  letter-spacing:.5px;color:#0A0A0A;text-align:left;
  -webkit-text-stroke:1.5px currentColor;paint-order:stroke fill;
}}
.uso-h .hl{{color:var(--acento);-webkit-text-stroke:1.5px var(--acento);}}
.uso-p{{
  margin-top:18px;font-family:var(--cond);font-size:28px;line-height:1.35;color:#4a524e;
  max-width:900px;text-align:left;
}}
.badge{{
  display:inline-flex;align-items:center;gap:10px;margin-top:16px;padding:10px 18px;
  border:1.5px solid var(--acento);border-radius:999px;background:#fff;
  font-family:var(--cond);font-size:24px;color:#2a2f2c;
}}
.badge .hl{{color:var(--acento);font-weight:700;}}

.prompt{{
  margin-top:36px;background:#fff;border:1.5px solid rgba(10,10,10,.12);border-radius:22px;
  padding:22px 24px 18px;box-shadow:0 18px 44px rgba(10,10,10,.08);text-align:left;
}}
.prompt-top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;}}
.prompt-top .left{{display:flex;align-items:center;gap:10px;font-family:var(--mono);font-size:16px;color:#7a817c;}}
.prompt-top .ico{{color:var(--acento);font-size:18px;}}
.copiar{{
  font-family:var(--mono);font-size:14px;letter-spacing:1px;color:var(--acento);
  border:1px solid var(--acento);border-radius:8px;padding:6px 12px;
}}
.prompt-body{{
  font-family:var(--cond);font-size:28px;line-height:1.4;color:#1a1a1a;text-align:left;
}}
.prompt-body .gt{{color:var(--acento);font-family:var(--mono);font-weight:600;margin-right:8px;}}
.prompt-body b{{color:#0A0A0A;}}
.prompt-bot{{
  margin-top:18px;display:flex;justify-content:space-between;align-items:center;
  font-family:var(--mono);font-size:16px;color:#8a918c;
}}
.send{{
  width:36px;height:36px;border-radius:50%;background:var(--acento);color:var(--acento-ink);
  display:inline-flex;align-items:center;justify-content:center;font-size:18px;margin-left:10px;
}}

/* flow 04 */
.flow{{margin-top:40px;display:flex;align-items:center;justify-content:center;gap:22px;}}
.box-prd{{
  width:340px;background:#fff;border:1.5px solid rgba(10,10,10,.12);border-radius:18px;
  padding:22px 24px;text-align:left;box-shadow:0 14px 36px rgba(10,10,10,.07);
}}
.box-prd .lab{{font-family:var(--mono);font-size:15px;color:#8a918c;margin-bottom:12px;}}
.box-prd li{{
  list-style:none;font-family:var(--cond);font-size:28px;color:#1a1a1a;margin-top:8px;
}}
.box-prd li span{{color:var(--acento);margin-right:8px;font-family:var(--mono);}}
.arrow{{font-family:var(--impact);font-size:48px;color:var(--acento);}}
.box-app{{
  width:300px;background:var(--acento);border-radius:18px;padding:40px 28px;text-align:center;
  box-shadow:0 18px 40px rgba(0,255,178,.35);color:var(--acento-ink);
}}
.box-app h3{{font-family:var(--impact);font-weight:900;font-size:42px;letter-spacing:1px;}}
.box-app p{{font-family:var(--mono);font-size:16px;margin-top:10px;opacity:.9;}}

/* panel 05 */
.panel{{
  margin-top:32px;background:#141414;border-radius:22px;padding:22px 22px 20px;color:#F2F2F2;
  box-shadow:0 22px 50px rgba(10,10,10,.18);text-align:left;
}}
.panel-top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;}}
.panel-top .l{{font-family:var(--mono);font-size:15px;color:#9aa39c;display:flex;align-items:center;gap:8px;}}
.panel-top .l i{{color:var(--acento);}}
.online{{font-family:var(--mono);font-size:14px;color:#28c840;display:flex;align-items:center;gap:8px;}}
.online i{{width:8px;height:8px;border-radius:50%;background:#28c840;display:inline-block;}}
.metrics{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;}}
.metric{{
  background:#1E1E1E;border:1px solid #2a2a2a;border-radius:14px;padding:16px 14px;text-align:left;
}}
.metric .lab{{font-family:var(--mono);font-size:13px;color:#8a918c;letter-spacing:1px;}}
.metric .val{{font-family:var(--impact);font-weight:900;font-size:48px;margin-top:6px;color:#F2F2F2;}}
.metric .val.hot{{color:var(--acento);}}
.actions{{margin-top:14px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;}}
.act{{
  border:1px solid #333;border-radius:999px;padding:12px 10px;text-align:center;
  font-family:var(--cond);font-size:20px;color:#d0d0d0;
}}
.act i{{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--acento);margin-right:6px;}}

/* CTA */
.cta{{padding:90px 64px 0;text-align:center;}}
.cta-q{{
  font-family:var(--serif);font-style:italic;font-weight:600;font-size:42px;color:#0A0A0A;line-height:1.2;
}}
.cta-pill{{
  display:inline-block;margin-top:22px;padding:10px 20px;border-radius:999px;
  background:#141414;color:#F2F2F2;font-family:var(--mono);font-size:16px;letter-spacing:2px;
}}
.cta-kw{{
  margin-top:18px;font-family:var(--impact);font-weight:900;font-size:120px;line-height:.92;
  letter-spacing:2px;color:var(--acento);
  -webkit-text-stroke:2.5px var(--acento);paint-order:stroke fill;
  text-shadow:0 0 40px rgba(0,255,178,.35);
}}
.cta-sub{{
  margin:18px auto 0;max-width:780px;font-family:var(--cond);font-size:28px;color:#3a3f3c;line-height:1.35;
}}
.cta-sub b{{color:#0A0A0A;}}
.profile{{
  margin:36px auto 0;width:720px;background:#fff;border-radius:22px;padding:22px 24px;
  border:1px solid rgba(10,10,10,.08);box-shadow:0 22px 50px rgba(10,10,10,.12);text-align:left;
}}
.profile .ph{{font-family:var(--mono);font-size:16px;color:#0A0A0A;margin-bottom:14px;}}
.profile .ph .v{{color:#3897f0;margin-left:4px;}}
.profile-row{{display:flex;gap:22px;align-items:center;}}
.profile-row img{{width:96px;height:96px;border-radius:50%;object-fit:cover;}}
.stats{{display:flex;gap:22px;flex:1;}}
.stats div{{text-align:center;}}
.stats b{{display:block;font-family:var(--pop);font-weight:800;font-size:26px;color:#0A0A0A;}}
.stats span{{font-family:var(--cond);font-size:18px;color:#6a736e;}}
.profile .name{{margin-top:14px;font-family:var(--pop);font-weight:800;font-size:26px;}}
.profile .bio{{margin-top:6px;font-family:var(--cond);font-size:22px;color:#4a524e;line-height:1.3;}}
.profile .bio em{{font-style:italic;font-weight:700;}}
.seguir{{
  margin-top:16px;background:var(--acento);color:var(--acento-ink);border-radius:12px;padding:14px;
  text-align:center;font-family:var(--pop);font-weight:800;font-size:24px;
}}
"""


def wrap(idx: int, inner: str, swipe: bool = True) -> str:
    html = chrome(idx, inner, total=TOTAL, bridges=None, footer=False)
    html = html.replace('class="slide"', 'class="slide grid"', 1)
    extras = '<div class="foot">sebastian.stlabs.ar</div>'
    if swipe and idx < TOTAL:
        extras = '<div class="swipe">deslizá →</div>' + extras
    return html.replace("</section>", extras + "</section>", 1)


def prompt_card(text_html: str) -> str:
    return f"""
<div class="prompt">
  <div class="prompt-top">
    <div class="left"><span class="ico">✶</span> prompt · fable 5</div>
    <div class="copiar">COPIAR</div>
  </div>
  <div class="prompt-body"><span class="gt">&gt;</span>{text_html}</div>
  <div class="prompt-bot">
    <span>+</span>
    <span>Fable 5 <span class="send">↑</span></span>
  </div>
</div>
"""


def slide1():
    return wrap(
        1,
        f"""
<div class="cover">
  <div class="cover-k">ANTHROPIC · SU MODELO MÁS POTENTE</div>
  <h1 class="cover-h">5 usos de Fable 5</h1>
  <div class="cover-line2">
    <span class="cover-script">que parecen</span>
    <span class="trampa">trampa</span>
  </div>
  <p class="cover-sub">Probé <b>el modelo nuevo de Anthropic</b> toda la semana. Esto no lo hace ningún otro.</p>
</div>
<div class="chart">
  <div class="bar s"><div class="star">✦</div><div class="name">Sonnet</div><div class="tag">RÁPIDO</div></div>
  <div class="bar m"><div class="star">✦</div><div class="name">Opus 4.8</div><div class="tag">POTENTE</div></div>
  <div class="bar t">
    <div class="claude"><img src="{CLAUDE_URI}" alt="Claude"></div>
    <div class="nuevo">NUEVO</div>
    <div class="star">✦</div>
    <div class="name">FABLE 5</div>
    <div class="tag">OTRO NIVEL</div>
  </div>
</div>
""",
    )


def slide2():
    return wrap(
        2,
        f"""
<div class="uso">
  <div><span class="uso-num">01</span><span class="uso-lab">USO</span></div>
  <h2 class="uso-h">Recreá ese SaaS que <span class="hl">pagás por mes</span></h2>
  <p class="uso-p">Le mostrás la herramienta que usás, estudia cómo funciona y te construye tu versión privada. Corre 100% en tu máquina, sin suscripción.</p>
  {prompt_card("Estudiá cómo funciona esta app que uso para [tarea] y construí una <b>versión privada y local</b> que corra entera en mi máquina, con las funciones que uso de verdad.")}
</div>
<div class="wm">01</div>
""",
    )


def slide3():
    return wrap(
        3,
        f"""
<div class="uso">
  <div><span class="uso-num">02</span><span class="uso-lab">USO</span></div>
  <h2 class="uso-h">Auditá cómo <span class="hl">usás Claude</span></h2>
  <p class="uso-p">Apuntalo a tu historial de Claude Code. Encuentra dónde te trabás siempre y lo convierte en skills nuevas, automatizaciones y mejoras a tu CLAUDE.md.</p>
  {prompt_card("Auditá mis sesiones recientes de Claude Code con subagentes. Agrupá dónde me trabo y proponé skills, automatizaciones y correcciones en el CLAUDE.md.")}
</div>
<div class="wm">02</div>
""",
    )


def slide4():
    return wrap(
        4,
        f"""
<div class="uso">
  <div><span class="uso-num">03</span><span class="uso-lab">USO</span></div>
  <div class="badge">✓ Con 1M de contexto entra <span class="hl">tu proyecto entero</span></div>
  <h2 class="uso-h">El mejor <span class="hl">caza-bugs</span> que probé</h2>
  <p class="uso-p">Acá Fable 5 se despega del resto: encuentra bugs reales, no detalles cosméticos. Lanza revisores en paralelo y verifica cada hallazgo antes de reportarlo.</p>
  {prompt_card("Cazá <b>bugs reales</b> en este proyecto. Lanzá revisores en paralelo, verificá cada hallazgo y rankealos por <b>severidad</b> con su plan de corrección.")}
</div>
<div class="wm">03</div>
""",
    )


def slide5():
    return wrap(
        5,
        """
<div class="uso">
  <div><span class="uso-num">04</span><span class="uso-lab">USO</span></div>
  <div class="badge">◷ Corre <span class="hl">horas</span> sin supervisión</div>
  <h2 class="uso-h">De un documento a la <span class="hl">app completa</span></h2>
  <p class="uso-p">Le das la spec detallada de lo que querés y lo dejás correr solo por horas. Vuelve con la app entera, funcional y testeada.</p>
  <div class="flow">
    <div class="box-prd">
      <div class="lab">PRD.MD</div>
      <ul>
        <li><span>#</span>objetivo</li>
        <li><span>#</span>pantallas</li>
        <li><span>#</span>reglas</li>
        <li><span>#</span>tests</li>
      </ul>
    </div>
    <div class="arrow">→</div>
    <div class="box-app">
      <h3>app lista</h3>
      <p>1 spec · 0 niñera</p>
    </div>
  </div>
</div>
<div class="wm">04</div>
""",
    )


def slide6():
    return wrap(
        6,
        """
<div class="uso">
  <div><span class="uso-num">05</span><span class="uso-lab">USO</span></div>
  <h2 class="uso-h">Tu asistente con <span class="hl">panel propio</span></h2>
  <p class="uso-p">Envolvé tu Claude Code en un panel con botones: el trabajo de todos los días queda a un click, con métricas que la terminal no muestra.</p>
  <div class="panel">
    <div class="panel-top">
      <div class="l"><i>✶</i> PANEL · MI ASISTENTE</div>
      <div class="online"><i></i>ONLINE</div>
    </div>
    <div class="metrics">
      <div class="metric"><div class="lab">SKILLS</div><div class="val">17</div></div>
      <div class="metric"><div class="lab">AUTOMATIZACIONES</div><div class="val hot">9</div></div>
      <div class="metric"><div class="lab">CONTEXTO</div><div class="val">12%</div></div>
    </div>
    <div class="actions">
      <div class="act"><i></i>rutina del día</div>
      <div class="act"><i></i>revisar inbox</div>
      <div class="act"><i></i>generar contenido</div>
    </div>
  </div>
</div>
<div class="wm">05</div>
""",
    )


def slide7():
    return wrap(
        7,
        f"""
<div class="cta">
  <p class="cta-q">¿Querés los 5 prompts listos para pegar?</p>
  <div class="cta-pill">COMENTÁ</div>
  <div class="cta-kw">“{KEYWORD}”</div>
  <p class="cta-sub">Y te mando <b>los 5 prompts completos</b> + cuándo conviene usar Fable 5 (y cuándo no) por DM.</p>
  <div class="profile">
    <div class="ph">sebastiangarcia.ar <span class="v">✓</span></div>
    <div class="profile-row">
      <img src="{SEB_URI}" alt="Sebastián García">
      <div class="stats">
        <div><b>61</b><span>publicaciones</span></div>
        <div><b>420</b><span>seguidores</span></div>
        <div><b>451</b><span>seguidos</span></div>
      </div>
    </div>
    <div class="name">Sebastian Garcia</div>
    <div class="bio"><em>Experto en ventas automatizadas</em><br>CRM y flujos de IA que trabajan por vos<br>sebastian.stlabs.ar</div>
    <div class="seguir">Seguir</div>
  </div>
</div>
""",
        swipe=False,
    )


def main():
    slides = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7()]
    write_html(slides, BUILD / "carrusel.html", extra_css=EXTRA_CSS)
    print("HTML:", BUILD / "carrusel.html")
    print("Claude asset:", CLAUDE_PNG)
    pngs = render(BUILD)
    print(f"Render OK: {len(pngs)}")

    meta = {
        "titulo": "Fable 5 Usos Que Parecen Trampa",
        "slides": TOTAL,
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "screenshot",
        "keyword_portada": KEYWORD,
        "modo_fondo": "blanco",
        "acento": VERDE,
        "feedback": {"estado": "borrador"},
    }
    out = package(BUILD, "STLabs-Fable5-UsosTrampa", meta=meta)
    print("Package:", out)

    KEEP = {".ttf", ".otf", ".woff", ".woff2"}
    KEEP_NAMES = {"befonts-license.txt", "impact-font.zip"}
    WORD_DIR.mkdir(parents=True, exist_ok=True)
    for p in list(WORD_DIR.iterdir()):
        if p.is_file() and p.suffix.lower() not in KEEP and p.name.lower() not in KEEP_NAMES:
            p.unlink()
    for fname in ("impact.ttf", "impacted.ttf", "unicodeimpact.ttf", "Befonts-License.txt"):
        src = REPO / "fonts" / fname
        if src.exists():
            shutil.copy2(src, WORD_DIR / fname)

    for name in (
        "STLabs-Fable5-UsosTrampa.html",
        "STLabs-Fable5-UsosTrampa.zip",
        "_preview-tira.png",
        "manifest.json",
        *[f"slide-{i:02d}.png" for i in range(1, TOTAL + 1)],
    ):
        src = out / name
        if src.exists():
            shutil.copy2(src, WORD_DIR / name)

    # Claude default del repo
    shutil.copy2(CLAUDE_PNG, WORD_DIR / "claude.png")
    for stale in ("claude-crop.png", "claude.svg"):
        p = WORD_DIR / stale
        if p.exists():
            p.unlink()

    (WORD_DIR / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Fable 5 Usos Que Parecen Trampa

| Fuente | Peso | Rol | Origen | Carga |
|---|---|---|---|---|
| Impact | 900 Super-Heavy | títulos | `impact-font.zip` → `fonts/impact.ttf` | `@font-face` base64 |
| Lora Italic | 600–700 | “que parecen” / acentos editoriales | `fonts/Lora-Italic-Variable.ttf` | `@font-face` base64 |
| Barlow Condensed | 400–700 | cuerpo / prompts | `fonts/BarlowCondensed-*.ttf` | `@font-face` base64 |
| IBM Plex Mono | 400–600 | labels, footer, COPIAR | `fonts/IBMPlexMono-*.ttf` | `@font-face` base64 |
| Poppins | 800 | nombres en barras / perfil | `fonts/Poppins-Bold.ttf` | `@font-face` base64 |

Acento: `#00FFB2` (reemplaza el naranja del original).
Claude de portada: `assets/claude.png` (bichito naranja default del repo).
Perfil: `seb.jpg` · sebastiangarcia.ar · 61 / 420 / 451 · sebastian.stlabs.ar
Modo blanco · retícula fina · keyword FABLE
""",
        encoding="utf-8",
    )
    (WORD_DIR / "LEEME.txt").write_text(
        f"""Carrusel STLabs — Fable 5 Usos Que Parecen Trampa
Identidad: sebastiangarcia.ar · foto seb.jpg · stats 61/420/451
Fondo: BLANCO · Textura: reticula_fina · Familia: dossier_editorial
Slides: {TOTAL} · Keyword: {KEYWORD}
Acento: #00FFB2 (reemplaza naranja del original)
Claude portada: assets/claude.png (bichito naranja default)
""",
        encoding="utf-8",
    )
    print("Word/:", WORD_DIR)


if __name__ == "__main__":
    main()
