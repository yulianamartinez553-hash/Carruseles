# -*- coding: utf-8 -*-
"""Carrusel STLabs — Trader IA para tu empresa (8 slides, blueprint).
Clon estética técnica cream/naranja · copy B2B primera persona · CTA REUNIÓN.
"""
from __future__ import annotations
import base64, json
from pathlib import Path

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
O = "#E04F2A"
BK = "#1A1A1A"
GY = "#6B6560"
BG = "#F2EBE2"
GR = "#00B894"


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def font_css() -> str:
    faces = [
        ("Bebas Neue", "BebasNeue-Regular.ttf", 400, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Bold.ttf", 700, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-SemiBold.ttf", 600, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-Medium.ttf", 500, "normal"),
    ]
    out = []
    for fam, fn, w, st in faces:
        data = b64(FONTS / fn)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{data}) format('truetype');}}"
        )
    return "\n".join(out)


def meta(proyecto: str, modelo: str, sistema: str) -> str:
    return f"""<div class="meta">
  <div><span>PROYECTO</span><b class="o">{proyecto}</b></div>
  <div><span>MODELO</span><b class="o">{modelo}</b></div>
  <div><span>SISTEMA</span><b>{sistema}</b></div>
  <div><span>VERSIÓN</span><b>1.0</b></div>
</div>"""


def chrome(meta_html: str = "") -> str:
    return f"""{meta_html}
<div class="grid"></div>
<div class="corner tl"></div><div class="corner tr"></div>
<div class="corner bl"></div><div class="corner br"></div>
<div class="ruler"><span>00</span><span>25</span><span>50</span><span>75</span><span>100</span></div>
<div class="firma">sebastian.stlabs.ar</div>"""


CSS = f"""
{font_css()}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
html,body{{background:#111;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{BK};}}
.grid{{position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(0,0,0,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(0,0,0,.055) 1px,transparent 1px);
  background-size:48px 48px;}}
.corner{{position:absolute;width:28px;height:28px;z-index:2;pointer-events:none;}}
.corner::before,.corner::after{{content:'';position:absolute;background:{BK};opacity:.35;}}
.corner.tl{{top:36px;left:36px;}} .corner.tr{{top:36px;right:36px;}}
.corner.bl{{bottom:88px;left:36px;}} .corner.br{{bottom:88px;right:36px;}}
.corner.tl::before{{width:14px;height:1px;top:0;left:0;}} .corner.tl::after{{width:1px;height:14px;top:0;left:0;}}
.corner.tr::before{{width:14px;height:1px;top:0;right:0;}} .corner.tr::after{{width:1px;height:14px;top:0;right:0;}}
.corner.bl::before{{width:14px;height:1px;bottom:0;left:0;}} .corner.bl::after{{width:1px;height:14px;bottom:0;left:0;}}
.corner.br::before{{width:14px;height:1px;bottom:0;right:0;}} .corner.br::after{{width:1px;height:14px;bottom:0;right:0;}}
.firma{{position:absolute;left:0;right:0;bottom:42px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:20px;letter-spacing:.12em;color:{GR};}}
.ruler{{position:absolute;left:72px;right:72px;bottom:72px;height:18px;z-index:3;display:flex;justify-content:space-between;align-items:flex-end;
  border-bottom:1px solid rgba(0,0,0,.25);font-family:'IBM Plex Mono',monospace;font-size:11px;color:{GY};}}
.ruler span::before{{content:'';display:block;width:1px;height:6px;background:rgba(0,0,0,.35);margin:0 auto 2px;}}
.meta{{position:absolute;top:44px;left:52px;z-index:10;border:1px solid rgba(0,0,0,.35);padding:10px 14px;
  font-family:'IBM Plex Mono',monospace;font-size:11px;line-height:1.55;letter-spacing:.06em;background:rgba(242,235,226,.92);}}
.meta span{{color:{GY};margin-right:6px;}}
.meta b{{color:{BK};font-weight:600;}} .meta b.o{{color:{O};}}
.content{{position:absolute;left:52px;right:52px;top:120px;bottom:108px;z-index:5;}}
.title{{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:72px;line-height:.92;letter-spacing:.01em;color:{BK};text-transform:uppercase;}}
.title .o{{color:{O};}}
.title.xl{{font-size:84px;}} .title.lg{{font-size:64px;}} .title.md{{font-size:56px;}}
.sub{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:26px;letter-spacing:.08em;color:{BK};margin-top:10px;text-transform:uppercase;}}
.sub .o{{color:{O};}}
.body{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:22px;line-height:1.35;color:{GY};margin-top:12px;}}
.body b{{color:{BK};font-weight:700;}}
.tag{{display:inline-block;margin-top:14px;padding:8px 14px;border:1px dashed {O};font-family:'IBM Plex Mono',monospace;
  font-size:13px;letter-spacing:.1em;color:{O};background:rgba(224,79,42,.06);}}
.box{{border:1px solid rgba(0,0,0,.35);border-radius:6px;background:rgba(255,255,255,.35);padding:12px;}}
.box h4{{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.12em;color:{BK};margin-bottom:6px;}}
.box p{{font-family:'Barlow Condensed',sans-serif;font-size:17px;line-height:1.25;color:{GY};}}
.box .bar{{height:3px;width:42px;background:{O};margin-top:8px;}}
.hub{{position:relative;width:100%;height:340px;margin-top:18px;}}
.hub-core{{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);width:168px;height:168px;border:2px solid {BK};
  border-radius:4px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:10px;}}
.hub-core .ico{{width:44px;height:44px;border:2px solid {BK};border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-family:'IBM Plex Mono',monospace;font-size:18px;font-weight:600;margin-bottom:8px;}}
.hub-core .t1{{font-family:'Bebas Neue',sans-serif;font-size:28px;line-height:1;}}
.hub-core .t2{{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;color:{GY};}}
.hub-core .bar{{width:56px;height:3px;background:{O};margin:6px 0;}}
.node{{position:absolute;width:118px;text-align:center;}}
.node .sq{{width:54px;height:54px;border:1px solid {BK};border-radius:4px;margin:0 auto 6px;background:#fff;
  display:flex;align-items:center;justify-content:center;font-size:22px;}}
.node .lbl{{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.08em;font-weight:600;}}
.hub-line{{position:absolute;background:{BK};opacity:.45;}}
.cards4{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:16px;}}
.card{{border:1px solid rgba(0,0,0,.35);border-radius:8px;padding:14px 12px;background:rgba(255,255,255,.4);position:relative;}}
.card .n{{font-family:'IBM Plex Mono',monospace;font-size:13px;color:{O};font-weight:600;}}
.card .t{{font-family:'Bebas Neue',sans-serif;font-size:26px;margin-top:4px;line-height:1;}}
.card .d{{font-family:'Barlow Condensed',sans-serif;font-size:16px;color:{GY};margin-top:6px;line-height:1.2;}}
.card::after{{content:'→';position:absolute;right:-14px;top:50%;transform:translateY(-50%);color:{BK};opacity:.35;font-size:18px;}}
.card:last-child::after{{display:none;}}
.scan{{display:grid;grid-template-columns:1fr 220px 1fr;grid-template-rows:1fr 1fr;gap:12px;height:520px;margin-top:14px;}}
.scan-mid{{grid-row:1/span 2;grid-column:2;display:flex;align-items:center;justify-content:center;}}
.radar{{width:200px;height:200px;border:2px solid {BK};border-radius:50%;position:relative;background:#fff;}}
.radar::before,.radar::after{{content:'';position:absolute;border:1px dashed rgba(0,0,0,.25);border-radius:50%;}}
.radar::before{{inset:28px;}} .radar::after{{inset:56px;}}
.radar .cross{{position:absolute;inset:0;}}
.radar .cross::before,.radar .cross::after{{content:'';position:absolute;background:rgba(0,0,0,.15);}}
.radar .cross::before{{left:50%;top:8%;bottom:8%;width:1px;transform:translateX(-50%);}}
.radar .cross::after{{top:50%;left:8%;right:8%;height:1px;transform:translateY(-50%);}}
.radar .dot{{position:absolute;width:6px;height:6px;border-radius:50%;background:{O};}}
.pane{{border:1px solid rgba(0,0,0,.35);border-radius:6px;padding:10px;background:rgba(255,255,255,.45);}}
.pane .ic{{font-size:26px;margin-bottom:6px;}}
.pane .h{{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.06em;}}
.pane .p{{font-family:'Barlow Condensed',sans-serif;font-size:15px;color:{GY};margin-top:4px;line-height:1.2;}}
.pane .bar{{height:3px;width:36px;background:{O};margin-top:8px;}}
.engine{{display:grid;grid-template-columns:1.1fr .9fr;gap:14px;margin-top:12px;height:560px;}}
.gear-box{{border:2px dashed rgba(0,0,0,.3);border-radius:8px;padding:16px;background:rgba(255,255,255,.5);display:flex;flex-direction:column;align-items:center;}}
.gear{{width:90px;height:90px;border:3px solid {BK};border-radius:50%;position:relative;margin:20px 0;}}
.gear::before{{content:'⚙';position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:42px;}}
.steps3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;width:100%;margin-top:10px;}}
.step-mini{{text-align:center;padding:8px;border-top:1px solid rgba(0,0,0,.2);}}
.step-mini .n{{font-family:'IBM Plex Mono',monospace;font-size:11px;color:{O};}}
.step-mini .t{{font-family:'Bebas Neue',sans-serif;font-size:22px;}}
.step-mini .d{{font-family:'Barlow Condensed',sans-serif;font-size:14px;color:{GY};}}
.patterns{{display:flex;flex-direction:column;gap:8px;}}
.pat{{display:grid;grid-template-columns:90px 1fr;gap:10px;align-items:center;border:1px solid rgba(0,0,0,.25);border-radius:6px;padding:8px;background:rgba(255,255,255,.4);}}
.pat .mini{{height:48px;border:1px solid rgba(0,0,0,.2);border-radius:4px;background:#fff;position:relative;overflow:hidden;}}
.pat .lbl{{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;}}
.pat .desc{{font-family:'Barlow Condensed',sans-serif;font-size:15px;color:{GY};line-height:1.2;}}
.plan{{display:grid;grid-template-columns:200px 1fr 200px;gap:10px;margin-top:12px;height:560px;}}
.plan-mid{{border:1px solid rgba(0,0,0,.35);border-radius:6px;background:#fff;padding:12px;position:relative;overflow:hidden;}}
.chart{{position:relative;height:100%;border-left:1px solid rgba(0,0,0,.2);border-bottom:1px solid rgba(0,0,0,.2);}}
.candle{{position:absolute;bottom:20%;width:8px;background:{BK};}}
.candle::before{{content:'';position:absolute;left:50%;width:1px;background:{BK};transform:translateX(-50%);}}
.zone{{position:absolute;left:8%;right:8%;border:1px dashed {GY};background:rgba(0,0,0,.04);}}
.line-t{{position:absolute;left:0;right:0;border-top:2px dashed #2D8A4E;}}
.line-s{{position:absolute;left:0;right:0;border-top:2px dashed {O};}}
.line-i{{position:absolute;left:0;right:0;border-top:1px dashed {BK};opacity:.5;}}
.lbl-side{{font-family:'IBM Plex Mono',monospace;font-size:11px;position:absolute;right:4px;transform:translateY(-50%);}}
.risk{{display:grid;grid-template-columns:1fr 280px 1fr;gap:12px;margin-top:12px;height:540px;}}
.risk-mid{{border:1px solid rgba(0,0,0,.35);border-radius:6px;padding:14px;background:#fff;}}
.chk{{display:flex;align-items:center;gap:8px;font-family:'IBM Plex Mono',monospace;font-size:12px;margin:6px 0;}}
.chk .ok{{color:#2D8A4E;font-weight:700;}}
.loop{{position:relative;height:520px;margin-top:14px;}}
.ring{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:280px;height:280px;border:2px solid {BK};border-radius:50%;}}
.ring-dash{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:220px;height:220px;border:2px dashed rgba(0,0,0,.3);border-radius:50%;}}
.loop-core{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);text-align:center;}}
.loop-core .big{{font-family:'Bebas Neue',sans-serif;font-size:56px;color:{O};line-height:1;}}
.loop-core .subt{{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.1em;}}
.memo{{border:1px solid rgba(0,0,0,.35);border-radius:8px;background:#fff;padding:16px;margin-top:12px;}}
.memo-h{{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(0,0,0,.2);padding-bottom:10px;margin-bottom:10px;}}
.memo-h h3{{font-family:'Bebas Neue',sans-serif;font-size:28px;}}
.memo-h span{{font-family:'IBM Plex Mono',monospace;font-size:11px;color:{GY};}}
.memo-row{{display:grid;grid-template-columns:28px 1fr 120px;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid rgba(0,0,0,.08);}}
.memo-row .num{{font-family:'IBM Plex Mono',monospace;font-size:12px;color:{O};font-weight:600;}}
.memo-row .txt{{font-family:'Barlow Condensed',sans-serif;font-size:18px;line-height:1.25;}}
.decisions{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:14px;}}
.dec{{border:2px solid rgba(0,0,0,.25);border-radius:8px;padding:14px;text-align:center;background:rgba(255,255,255,.5);}}
.dec.go{{border-color:#2D8A4E;background:rgba(45,138,78,.08);}}
.dec.wait{{border-color:#C9A227;background:rgba(201,162,39,.08);}}
.dec.no{{border-color:{O};background:rgba(224,79,42,.08);}}
.dec .ic{{font-size:28px;}}
.dec .t{{font-family:'Bebas Neue',sans-serif;font-size:24px;margin-top:6px;}}
.dec .d{{font-family:'Barlow Condensed',sans-serif;font-size:15px;color:{GY};}}
.flow6{{display:flex;justify-content:space-between;align-items:flex-start;margin:28px 0 20px;}}
.flow6 .f{{text-align:center;flex:1;position:relative;}}
.flow6 .f::after{{content:'→';position:absolute;right:-8px;top:18px;color:{BK};opacity:.3;}}
.flow6 .f:last-child::after{{display:none;}}
.flow6 .ic{{width:52px;height:52px;border:1px solid {BK};border-radius:6px;margin:0 auto 8px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:22px;}}
.flow6 .l{{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:600;letter-spacing:.06em;}}
.cta-frame{{margin:24px auto 0;max-width:620px;border:2px solid {BK};padding:28px 24px;text-align:center;position:relative;background:rgba(255,255,255,.55);}}
.cta-frame::before,.cta-frame::after{{content:'';position:absolute;width:18px;height:18px;border:2px solid {O};}}
.cta-frame::before{{top:-8px;left:-8px;border-right:none;border-bottom:none;}}
.cta-frame::after{{bottom:-8px;right:-8px;border-left:none;border-top:none;}}
.cta-kw{{font-family:'Bebas Neue',sans-serif;font-size:64px;color:{O};letter-spacing:.08em;}}
.cta-hint{{font-family:'Barlow Condensed',sans-serif;font-size:26px;margin-top:10px;color:{BK};}}
.status{{position:absolute;bottom:108px;left:52px;right:52px;display:flex;justify-content:space-between;gap:12px;z-index:6;}}
.status .sbox{{flex:1;border:1px solid rgba(0,0,0,.3);border-radius:6px;padding:10px 12px;background:rgba(255,255,255,.45);
  font-family:'IBM Plex Mono',monospace;font-size:11px;line-height:1.5;}}
.status .sbox b.o{{color:{O};}}
"""


def build() -> str:
    s = []

    s.append(f"""
<section class="slide" data-id="01">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "ARQUITECTURA FINANCIERA"))}
  <div class="content" style="top:108px">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start">
      <div>
        <h1 class="title xl">Te genero un<br><span class="o">trader ia</span><br>para tu empresa</h1>
        <p class="sub"><span class="o">+</span> diagnóstico · señales · riesgo · 24/7 <span class="o">+</span></p>
        <p class="body">Mapeo tu área financiera, detecto oportunidades y te dejo un sistema que <b>opera con control</b>.</p>
      </div>
      <div class="hub" style="height:300px;margin-top:0">
        <div class="hub-line" style="width:1px;height:70px;left:50%;top:18%;"></div>
        <div class="hub-line" style="width:70px;height:1px;left:18%;top:38%;"></div>
        <div class="hub-line" style="width:70px;height:1px;right:18%;top:38%;"></div>
        <div class="hub-line" style="width:1px;height:70px;left:50%;bottom:18%;"></div>
        <div class="hub-core">
          <div class="ico">E</div>
          <div class="t1">TU EMPRESA</div>
          <div class="bar"></div>
          <div class="t2">TRADER IA</div>
        </div>
        <div class="node" style="left:38%;top:2%"><div class="sq">⌕</div><div class="lbl">DIAGNÓSTICO</div></div>
        <div class="node" style="right:2%;top:32%"><div class="sq">📈</div><div class="lbl">SEÑALES</div></div>
        <div class="node" style="left:2%;top:32%"><div class="sq">🛡</div><div class="lbl">RIESGO</div></div>
        <div class="node" style="left:38%;bottom:2%"><div class="sq">◉</div><div class="lbl">MONITOR 24/7</div></div>
      </div>
    </div>
    <div class="cards4">
      <div class="card"><div class="n">01</div><div class="t">DIAGNÓSTICO</div><div class="d">Mapeo flujos, caja y exposición de tu operación.</div></div>
      <div class="card"><div class="n">02</div><div class="t">SEÑALES</div><div class="d">Detecto y puntúo oportunidades de gestión.</div></div>
      <div class="card"><div class="n">03</div><div class="t">RIESGO</div><div class="d">Límites, drawdown y controles automáticos.</div></div>
      <div class="card"><div class="n">04</div><div class="t">24/7</div><div class="d">El sistema queda activo. Siempre monitoreando.</div></div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="02">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "ESCÁNER FINANCIERO"))}
  <div class="content">
    <h1 class="title lg">Primero, mapeo<br>tu <span class="o">área financiera</span><br>24/7</h1>
    <p class="sub"><span class="o">+</span> caja · márgenes · flujo · alertas · <span class="o">+</span></p>
    <div class="scan">
      <div class="pane"><div class="ic">📊</div><div class="h">FLUJO DE CAJA</div><div class="p">Movimientos y saldos en tiempo real.</div><div class="bar"></div></div>
      <div class="pane"><div class="ic">📰</div><div class="h">CONTEXTO</div><div class="p">Eventos y variables que impactan tu negocio.</div><div class="bar"></div></div>
      <div class="scan-mid">
        <div style="text-align:center">
          <div class="radar"><div class="cross"></div>
            <div class="dot" style="left:62%;top:28%"></div><div class="dot" style="left:35%;top:55%"></div>
            <div class="dot" style="left:70%;top:68%"></div><div class="dot" style="left:48%;top:40%"></div>
          </div>
          <div class="sub" style="margin-top:12px;font-size:18px">ESCANEANDO<br><span class="o">TU OPERACIÓN</span></div>
        </div>
      </div>
      <div class="pane"><div class="ic">📈</div><div class="h">MÁRGENES</div><div class="p">Rentabilidad por línea y unidad de negocio.</div><div class="bar"></div></div>
      <div class="pane"><div class="ic">⭐</div><div class="h">WATCHLIST</div><div class="p">KPIs críticos bajo seguimiento continuo.</div><div class="bar"></div></div>
    </div>
    <div class="status">
      <div class="sbox">MODO: <b class="o">ESCANEO</b><br>FRECUENCIA: <b class="o">CONTINUA</b></div>
      <div class="sbox">TEMPORALIDAD: <b class="o">24/7</b><br>ESTADO: <b class="o">ACTIVO</b></div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="03">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "MOTOR DE SEÑALES"))}
  <div class="content">
    <h1 class="title lg">Luego detecto<br><span class="o">oportunidades</span></h1>
    <p class="sub"><span class="o">+</span> setups de alta probabilidad para tu gestión <span class="o">+</span></p>
    <div class="engine">
      <div class="gear-box">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.1em">MOTOR DE SEÑALES</div>
        <div class="gear"></div>
        <div class="steps3">
          <div class="step-mini"><div class="n">01</div><div class="t">ESCANEA</div><div class="d">Lee tus datos financieros</div></div>
          <div class="step-mini"><div class="n">02</div><div class="t">DETECTA</div><div class="d">Identifica patrones</div></div>
          <div class="step-mini"><div class="n">03</div><div class="t">PUNTÚA</div><div class="d">Rankea por impacto</div></div>
        </div>
      </div>
      <div class="patterns">
        <div class="pat"><div class="mini" style="background:linear-gradient(135deg,#fff 40%,#eee)"></div><div><div class="lbl">FLUJO</div><div class="desc">Desvío relevante en entradas o salidas de caja.</div></div></div>
        <div class="pat"><div class="mini" style="background:linear-gradient(180deg,#fff,#f5f5f5)"></div><div><div class="lbl">MARGEN</div><div class="desc">Compresión o expansión de rentabilidad.</div></div></div>
        <div class="pat"><div class="mini"></div><div><div class="lbl">CAJA</div><div class="desc">Alerta de liquidez o exceso de capital ocioso.</div></div></div>
        <div class="pat"><div class="mini"></div><div><div class="lbl">TENDENCIA</div><div class="desc">Dirección sostenida en indicadores clave.</div></div></div>
        <div class="pat"><div class="mini"></div><div><div class="lbl">ALERTA</div><div class="desc">Evento que requiere decisión inmediata.</div></div></div>
        <div class="box" style="margin-top:6px"><h4>🎯 SEÑAL DETECTADA</h4><p>Setup de alta probabilidad para tu área financiera <span style="color:{O}">››››</span></p></div>
      </div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="04">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "PLAN DE GESTIÓN"))}
  <div class="content">
    <h1 class="title md">Después armo el<br><span class="o">plan de gestión</span></h1>
    <p class="sub"><span class="o">+</span> acción · objetivo · límite · invalidación <span class="o">+</span></p>
    <div class="plan">
      <div style="display:flex;flex-direction:column;gap:10px">
        <div class="box"><h4>ZONA DE ACCIÓN</h4><p>Rango óptimo para mover capital o recursos.</p><div class="bar"></div></div>
        <div class="box"><h4>LÍMITE DE RIESGO</h4><p>Tope definido antes de ejecutar cualquier movimiento.</p><div class="bar"></div></div>
        <div class="box"><h4>RIESGO / BENEFICIO</h4><p>Ratio calculado: <b style="color:{O}">1 : 2.2</b></p><div class="bar"></div></div>
      </div>
      <div class="plan-mid">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:12px;margin-bottom:8px">PLAN DE GESTIÓN</div>
        <div class="chart">
          <div class="zone" style="top:35%;height:28%"></div>
          <div class="line-t" style="top:18%"><span class="lbl-side" style="color:#2D8A4E">OBJETIVO</span></div>
          <div class="line-s" style="top:62%"><span class="lbl-side" style="color:{O}">LÍMITE</span></div>
          <div class="line-i" style="top:82%"><span class="lbl-side">INVALIDACIÓN</span></div>
          <div class="candle" style="left:20%;height:35%"></div><div class="candle" style="left:32%;height:45%"></div>
          <div class="candle" style="left:44%;height:38%"></div><div class="candle" style="left:56%;height:52%"></div>
          <div class="candle" style="left:68%;height:48%"></div>
        </div>
        <div style="display:flex;gap:16px;margin-top:10px;font-family:'IBM Plex Mono',monospace;font-size:11px">
          <span>DIRECCIÓN: <b class="o">OPTIMIZAR</b></span>
          <span>HORIZONTE: <b>TRIMESTRE</b></span>
          <span>CONFIANZA: <b class="o">ALTA</b></span>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:10px">
        <div class="box"><h4>OBJETIVO</h4><p>Meta de retorno o eficiencia definida.</p><div class="bar"></div></div>
        <div class="box"><h4>INVALIDACIÓN</h4><p>Condición que cancela el plan si se rompe.</p><div class="bar"></div></div>
        <div class="box"><h4>🎯 PLAN LISTO</h4><p>Todos los niveles confirmados.</p><div class="bar"></div></div>
      </div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="05">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "MÓDULO DE RIESGO"))}
  <div class="content">
    <h1 class="title md">Pero el módulo<br>de <span class="o">riesgo</span> revisa todo</h1>
    <p class="sub"><span class="o">+</span> tamaño · exposición · pérdida · <span class="o">+</span></p>
    <div class="risk">
      <div style="display:flex;flex-direction:column;gap:10px">
        <div class="box"><h4>01 TAMAÑO</h4><p>Calcula cuánto mover según el riesgo por decisión.</p><div class="bar"></div></div>
        <div class="box"><h4>02 EXPOSICIÓN</h4><p>Revisa el total comprometido en todas las posiciones.</p><div class="bar"></div></div>
        <div class="box"><h4>03 DRAWDOWN</h4><p>Verifica el límite de caída permitido.</p><div class="bar"></div></div>
      </div>
      <div class="risk-mid">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:12px;margin-bottom:10px">MÓDULO DE RIESGO</div>
        <div class="chk"><span class="ok">✓</span> CHECK DE TAMAÑO — OK</div>
        <div class="chk"><span class="ok">✓</span> CHECK DE EXPOSICIÓN — OK</div>
        <div class="chk"><span class="ok">✓</span> CHECK DE DRAWDOWN — OK</div>
        <div class="chk"><span class="ok">✓</span> CHECK DE VOLATILIDAD — OK</div>
        <div class="chk"><span class="ok">✓</span> CHECK DE PÉRDIDA MÁXIMA — OK</div>
        <div style="display:flex;gap:10px;margin-top:16px">
          <div class="dec go" style="flex:1;padding:10px"><div class="t" style="font-size:20px">PASA</div><div class="d">Continúa</div></div>
          <div class="dec no" style="flex:1;padding:10px"><div class="t" style="font-size:20px">FALLA</div><div class="d">Bloquea</div></div>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:10px">
        <div class="box"><h4>04 VOLATILIDAD</h4><p>Confirma que el entorno sea aceptable.</p><div class="bar"></div></div>
        <div class="box"><h4>05 PÉRDIDA MÁX</h4><p>Asegura que no se supere el tope definido.</p><div class="bar"></div></div>
        <div class="box"><h4>🛡 RIESGO OK</h4><p>Protegiendo el capital en cada decisión.</p><div class="bar"></div></div>
      </div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="06">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "LOOP DE MONITOREO"))}
  <div class="content">
    <h1 class="title lg" style="text-align:center">El sistema queda<br><span class="o">activo 24/7</span></h1>
    <p class="sub" style="text-align:center"><span class="o">+</span> monitoreo · alertas · revisión · <span class="o">+</span></p>
    <div class="loop">
      <div class="ring"></div><div class="ring-dash"></div>
      <div class="loop-core"><div class="big">24/7</div><div class="subt">LOOP DE MONITOREO</div><div class="body" style="font-size:16px;margin-top:6px">Seguimiento continuo de tu área financiera</div></div>
      <div class="node" style="left:8%;top:18%"><div class="sq">📋</div><div class="lbl">WATCHLIST</div></div>
      <div class="node" style="right:8%;top:18%"><div class="sq">🔔</div><div class="lbl">ALERTAS</div></div>
      <div class="node" style="left:4%;top:48%"><div class="sq">📊</div><div class="lbl">ESTADO</div></div>
      <div class="node" style="right:4%;top:48%"><div class="sq">📡</div><div class="lbl">SEÑAL</div></div>
      <div class="node" style="left:18%;bottom:8%"><div class="sq">🖥</div><div class="lbl">MONITOR</div></div>
      <div class="node" style="right:18%;bottom:8%"><div class="sq">🛡</div><div class="lbl">RIESGO</div></div>
      <div class="node" style="left:42%;top:4%"><div class="sq">⌕</div><div class="lbl">ESCANEO</div></div>
    </div>
    <div class="status">
      <div class="sbox">◉ SISTEMA EN LÍNEA 24/7<br><b class="o">Sin pausas. Sin botón de apagado.</b></div>
      <div class="sbox" style="text-align:right">LOOP ACTIVO<br><b class="o">Siempre atento. Siempre listo.</b></div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="07">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "DECISIÓN FINAL"))}
  <div class="content" style="top:108px">
    <h1 class="title md" style="text-align:center">Al final recibís<br>una <span class="o">decisión clara</span></h1>
    <p class="sub" style="text-align:center">La tomás. La observás. O la descartás.</p>
    <div class="memo">
      <div class="memo-h"><h3>MEMO DE DECISIÓN</h3><span>ID: TG-247 · FECHA: HOY</span></div>
      <div class="memo-row"><div class="num">1</div><div class="txt"><b>Resumen:</b> alineación de flujo, margen y contexto de mercado favorable.</div><div>📈</div></div>
      <div class="memo-row"><div class="num">2</div><div class="txt"><b>Fuerza de señal:</b> ★★★★☆ — <span style="color:{O}">FUERTE</span></div><div>◔</div></div>
      <div class="memo-row"><div class="num">3</div><div class="txt"><b>Nivel de riesgo:</b> MODERADO</div><div>●●●○</div></div>
      <div class="memo-row"><div class="num">4</div><div class="txt"><b>Plan:</b> acción definida · límite · objetivo calculado.</div><div>📊</div></div>
      <div class="memo-row"><div class="num">5</div><div class="txt" style="font-family:'Bebas Neue',sans-serif;font-size:28px;color:{O}">DECISIÓN LISTA</div><div></div></div>
    </div>
    <p class="tag" style="display:block;text-align:center;margin:14px auto 0;max-width:420px">— REVISIÓN HUMANA INCLUIDA —</p>
    <div class="decisions">
      <div class="dec go"><div class="ic">✓</div><div class="t">EJECUTAR</div><div class="d">Aplicar el plan</div></div>
      <div class="dec wait"><div class="ic">👁</div><div class="t">OBSERVAR</div><div class="d">Monitorear condiciones</div></div>
      <div class="dec no"><div class="ic">✕</div><div class="t">DESCARTAR</div><div class="d">No mover ahora</div></div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="08">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "COORDINAR REUNIÓN"))}
  <div class="content" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;top:130px">
    <h1 class="title xl">Tu empresa merece<br><span class="o">gestión financiera</span><br>con ia</h1>
    <p class="sub"><span class="o">—</span> coordinemos una reunión <span class="o">—</span></p>
    <div class="flow6" style="max-width:900px">
      <div class="f"><div class="ic">⌕</div><div class="l">DIAGNÓSTICO</div></div>
      <div class="f"><div class="ic">📈</div><div class="l">SEÑALES</div></div>
      <div class="f"><div class="ic">📋</div><div class="l">PLAN</div></div>
      <div class="f"><div class="ic">🛡</div><div class="l">RIESGO</div></div>
      <div class="f"><div class="ic">◉</div><div class="l">MONITOR</div></div>
      <div class="f"><div class="ic">🎯</div><div class="l">DECISIÓN</div></div>
    </div>
    <div class="cta-frame">
      <div class="cta-kw">REUNIÓN</div>
      <div class="cta-hint">Comentá <b style="color:{O}">REUNIÓN</b> y te escribo para coordinar.</div>
    </div>
    <p class="body" style="max-width:700px;margin-top:20px">Te genero el trader IA, lo adapto a tu operación y te muestro cómo gestionar tu área financiera con control total.</p>
    <p class="tag" style="margin-top:16px">HECHO PARA ESCALAR. DISEÑADO PARA DECIDIR.</p>
  </div>
</section>""")

    return "".join(s)


def main():
    html = (
        "<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'>"
        "<title>Trader IA Empresa — STLabs</title>"
        f"<style>{CSS}</style></head><body><div class='sheet'>"
        f"{build()}</div></body></html>"
    )
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    meta = {
        "id": "2026-08-22-trader-ia-empresa",
        "fecha": "2026-08-22",
        "titulo": "Te genero un trader IA para tu empresa",
        "slides": 8,
        "fondo": "lino_tela",
        "familia_visual": "before_after",
        "origen": "screenshot",
        "keyword_portada": "REUNIÓN",
        "modo": "blanco",
        "resoluciones": {"4k": "4320x5400", "fhd": "1920x2400", "retina": "2160x2700"},
        "notas": "Clon blueprint trader B2B. Primera persona. CTA REUNIÓN.",
    }
    (B / "manifest.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OK 8 slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
