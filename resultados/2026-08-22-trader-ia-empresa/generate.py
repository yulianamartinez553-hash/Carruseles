# -*- coding: utf-8 -*-
"""Carrusel STLabs — Trader IA para tu empresa (8 slides, blueprint).
Modo negro STLabs · verde #00FFB2 · copy B2B primera persona · CTA REUNIÓN.
"""
from __future__ import annotations
import base64, json
from pathlib import Path

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
V = "#00FFB2"       # verde neón STLabs
BG = "#0A0A0A"      # negro mineral
TX = "#F2F2F2"      # texto principal
GY = "#9aa39c"      # texto secundario
CARD = "#141414"    # cajas
CARD2 = "#1E1E1E"  # cajas alt
RED = "#FF5247"     # solo riesgo/peligro
BDR = "rgba(255,255,255,.16)"


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
  <div><span>PROYECTO</span><b class="v">{proyecto}</b></div>
  <div><span>MODELO</span><b class="v">{modelo}</b></div>
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
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.55;
  background:radial-gradient(ellipse 80% 60% at 12% 8%,rgba(0,255,178,.06),transparent 55%),
             radial-gradient(ellipse 60% 50% at 92% 88%,rgba(0,255,178,.04),transparent 50%);}}
.grid{{position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);
  background-size:48px 48px;}}
.corner{{position:absolute;width:28px;height:28px;z-index:2;pointer-events:none;}}
.corner::before,.corner::after{{content:'';position:absolute;background:{TX};opacity:.28;}}
.corner.tl{{top:36px;left:36px;}} .corner.tr{{top:36px;right:36px;}}
.corner.bl{{bottom:90px;left:36px;}} .corner.br{{bottom:90px;right:36px;}}
.corner.tl::before{{width:14px;height:1px;top:0;left:0;}} .corner.tl::after{{width:1px;height:14px;top:0;left:0;}}
.corner.tr::before{{width:14px;height:1px;top:0;right:0;}} .corner.tr::after{{width:1px;height:14px;top:0;right:0;}}
.corner.bl::before{{width:14px;height:1px;bottom:0;left:0;}} .corner.bl::after{{width:1px;height:14px;bottom:0;left:0;}}
.corner.br::before{{width:14px;height:1px;bottom:0;right:0;}} .corner.br::after{{width:1px;height:14px;bottom:0;right:0;}}
.firma{{position:absolute;left:0;right:0;bottom:40px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:22px;letter-spacing:.12em;color:{V};}}
.ruler{{position:absolute;left:56px;right:56px;bottom:70px;height:18px;z-index:3;display:flex;justify-content:space-between;align-items:flex-end;
  border-bottom:1px solid rgba(255,255,255,.18);font-family:'IBM Plex Mono',monospace;font-size:12px;color:{GY};}}
.ruler span::before{{content:'';display:block;width:1px;height:6px;background:rgba(255,255,255,.28);margin:0 auto 2px;}}
.meta{{position:absolute;top:28px;left:30px;z-index:20;border:1px solid {BDR};padding:10px 14px;
  font-family:'IBM Plex Mono',monospace;font-size:12px;line-height:1.4;letter-spacing:.05em;background:rgba(10,10,10,.96);}}
.meta span{{color:{GY};margin-right:6px;}}
.meta b{{color:{TX};font-weight:600;}} .meta b.v{{color:{V};}}
.content{{position:absolute;left:30px;right:30px;top:158px;bottom:96px;z-index:5;overflow:hidden;
  display:flex;flex-direction:column;}}
.content.center{{justify-content:center;align-items:center;text-align:center;}}
.title{{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:96px;line-height:.94;letter-spacing:.01em;color:{TX};text-transform:uppercase;}}
.title .o,.title .v{{color:{V};}}
.title.xl{{font-size:102px;}} .title.lg{{font-size:88px;}} .title.md{{font-size:78px;}}
.sub{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:36px;letter-spacing:.04em;color:{TX};margin-top:10px;text-transform:uppercase;}}
.sub .o,.sub .v{{color:{V};}}
.body{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:32px;line-height:1.22;color:{GY};margin-top:10px;}}
.body b{{color:{TX};font-weight:700;}}
.tag{{display:inline-block;margin-top:14px;padding:10px 16px;border:1px dashed {V};font-family:'IBM Plex Mono',monospace;
  font-size:14px;letter-spacing:.1em;color:{V};background:rgba(0,255,178,.06);}}
.box{{border:1px solid {BDR};border-radius:6px;background:{CARD};padding:14px;}}
.box h4{{font-family:'IBM Plex Mono',monospace;font-size:15px;letter-spacing:.08em;color:{TX};margin-bottom:6px;}}
.box p{{font-family:'Barlow Condensed',sans-serif;font-size:24px;line-height:1.2;color:{GY};}}
.box .bar{{height:3px;width:48px;background:{V};margin-top:8px;}}
.hub{{position:relative;width:100%;height:360px;margin-top:0;flex:0 0 auto;min-height:340px;}}
.hub-core{{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);width:176px;height:176px;border:2px solid {V};
  border-radius:4px;background:{CARD2};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:12px;}}
.hub-core .ico{{width:50px;height:50px;border:2px solid {V};border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-family:'IBM Plex Mono',monospace;font-size:20px;font-weight:600;color:{V};margin-bottom:8px;}}
.hub-core .t1{{font-family:'Bebas Neue',sans-serif;font-size:32px;line-height:1;color:{TX};}}
.hub-core .t2{{font-family:'IBM Plex Mono',monospace;font-size:13px;letter-spacing:.1em;color:{GY};}}
.hub-core .bar{{width:64px;height:3px;background:{V};margin:6px 0;}}
.node{{position:absolute;width:132px;text-align:center;}}
.node .sq{{width:62px;height:62px;border:1px solid {BDR};border-radius:4px;margin:0 auto 8px;background:{CARD};
  display:flex;align-items:center;justify-content:center;font-size:24px;color:{V};font-family:'IBM Plex Mono',monospace;}}
.node .lbl{{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.06em;font-weight:600;color:{TX};}}
.hub-line{{position:absolute;background:{TX};opacity:.22;}}
.cards4{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:auto;padding-top:16px;}}
.card{{border:1px solid {BDR};border-radius:8px;padding:18px 14px;background:{CARD};position:relative;}}
.card .n{{font-family:'IBM Plex Mono',monospace;font-size:15px;color:{V};font-weight:600;}}
.card .t{{font-family:'Bebas Neue',sans-serif;font-size:40px;margin-top:4px;line-height:1;color:{TX};}}
.card .d{{font-family:'Barlow Condensed',sans-serif;font-size:24px;color:{GY};margin-top:8px;line-height:1.18;}}
.card::after{{content:'→';position:absolute;right:-14px;top:50%;transform:translateY(-50%);color:{V};opacity:.35;font-size:18px;}}
.card:last-child::after{{display:none;}}
.scan{{display:grid;grid-template-columns:1fr 230px 1fr;grid-template-rows:1fr 1fr;gap:14px;flex:1;min-height:0;margin-top:14px;}}
.scan-mid{{grid-row:1/span 2;grid-column:2;display:flex;align-items:center;justify-content:center;}}
.radar{{width:210px;height:210px;border:2px solid {V};border-radius:50%;position:relative;background:{CARD2};}}
.radar::before,.radar::after{{content:'';position:absolute;border:1px dashed rgba(255,255,255,.18);border-radius:50%;}}
.radar::before{{inset:28px;}} .radar::after{{inset:56px;}}
.radar .cross{{position:absolute;inset:0;}}
.radar .cross::before,.radar .cross::after{{content:'';position:absolute;background:rgba(255,255,255,.12);}}
.radar .cross::before{{left:50%;top:8%;bottom:8%;width:1px;transform:translateX(-50%);}}
.radar .cross::after{{top:50%;left:8%;right:8%;height:1px;transform:translateY(-50%);}}
.radar .dot{{position:absolute;width:7px;height:7px;border-radius:50%;background:{V};}}
.pane{{border:1px solid {BDR};border-radius:6px;padding:16px;background:{CARD};display:flex;flex-direction:column;justify-content:center;}}
.pane .ic{{font-family:'IBM Plex Mono',monospace;font-size:24px;color:{V};margin-bottom:8px;font-weight:600;}}
.pane .h{{font-family:'IBM Plex Mono',monospace;font-size:16px;font-weight:600;letter-spacing:.05em;color:{TX};}}
.pane .p{{font-family:'Barlow Condensed',sans-serif;font-size:22px;color:{GY};margin-top:6px;line-height:1.22;}}
.pane .bar{{height:3px;width:44px;background:{V};margin-top:12px;}}
.engine{{display:grid;grid-template-columns:1.05fr .95fr;gap:14px;margin-top:12px;flex:1;min-height:0;}}
.gear-box{{border:2px dashed rgba(255,255,255,.2);border-radius:8px;padding:18px;background:{CARD};display:flex;flex-direction:column;align-items:center;justify-content:center;}}
.gear{{width:100px;height:100px;border:3px solid {V};border-radius:50%;position:relative;margin:18px 0;
  background:conic-gradient(from 0deg,{CARD2} 0 30deg,transparent 30deg 60deg,{CARD2} 60deg 90deg,transparent 90deg 120deg,{CARD2} 120deg 150deg,transparent 150deg 180deg,{CARD2} 180deg 210deg,transparent 210deg 240deg,{CARD2} 240deg 270deg,transparent 270deg 300deg,{CARD2} 300deg 330deg,transparent 330deg 360deg);}}
.gear::after{{content:'';position:absolute;inset:32px;border-radius:50%;background:{CARD};border:2px solid {V};}}
.steps3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;width:100%;margin-top:12px;}}
.step-mini{{text-align:center;padding:12px;border-top:1px solid {BDR};}}
.step-mini .n{{font-family:'IBM Plex Mono',monospace;font-size:13px;color:{V};}}
.step-mini .t{{font-family:'Bebas Neue',sans-serif;font-size:28px;color:{TX};}}
.step-mini .d{{font-family:'Barlow Condensed',sans-serif;font-size:17px;color:{GY};}}
.patterns{{display:flex;flex-direction:column;gap:10px;flex:1;}}
.pat{{display:grid;grid-template-columns:100px 1fr;gap:12px;align-items:center;border:1px solid {BDR};border-radius:6px;padding:14px;background:{CARD};flex:1;}}
.pat .mini{{height:58px;border:1px solid {BDR};border-radius:4px;background:{CARD2};position:relative;overflow:hidden;}}
.pat .lbl{{font-family:'IBM Plex Mono',monospace;font-size:14px;font-weight:600;color:{TX};}}
.pat .desc{{font-family:'Barlow Condensed',sans-serif;font-size:19px;color:{GY};line-height:1.25;}}
.plan{{display:grid;grid-template-columns:220px 1fr 220px;gap:12px;margin-top:12px;flex:1;min-height:0;}}
.plan-mid{{border:1px solid {BDR};border-radius:6px;background:{CARD2};padding:14px;position:relative;overflow:hidden;}}
.chart{{position:relative;height:calc(100% - 48px);border-left:1px solid {BDR};border-bottom:1px solid {BDR};}}
.candle{{position:absolute;bottom:18%;width:10px;background:{TX};}}
.candle::before{{content:'';position:absolute;left:50%;width:1px;background:{TX};transform:translateX(-50%);height:120%;top:-10%;}}
.zone{{position:absolute;left:8%;right:8%;border:1px dashed {GY};background:rgba(0,255,178,.04);}}
.line-t{{position:absolute;left:0;right:130px;border-top:2px dashed {V};pointer-events:none;}}
.line-s{{position:absolute;left:0;right:130px;border-top:2px dashed {RED};pointer-events:none;}}
.line-i{{position:absolute;left:0;right:130px;border-top:1px dashed {GY};opacity:.7;pointer-events:none;}}
.lbl-side{{font-family:'IBM Plex Mono',monospace;font-size:12px;position:absolute;right:6px;transform:translateY(-50%);
  padding:3px 7px;background:{CARD2};letter-spacing:.04em;white-space:nowrap;z-index:2;}}
.risk{{display:grid;grid-template-columns:1fr 310px 1fr;gap:12px;margin-top:12px;flex:1;min-height:0;}}
.risk-mid{{border:1px solid {BDR};border-radius:6px;padding:18px;background:{CARD2};}}
.chk{{display:flex;align-items:center;gap:10px;font-family:'IBM Plex Mono',monospace;font-size:15px;margin:10px 0;color:{TX};}}
.chk .ok{{color:{V};font-weight:700;}}
.loop{{position:relative;flex:1;min-height:560px;margin-top:8px;}}
.ring{{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);width:360px;height:360px;border:2px solid {V};border-radius:50%;}}
.ring-dash{{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);width:285px;height:285px;border:2px dashed rgba(255,255,255,.2);border-radius:50%;}}
.loop-core{{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);text-align:center;width:210px;}}
.loop-core .big{{font-family:'Bebas Neue',sans-serif;font-size:84px;color:{V};line-height:1;}}
.loop-core .subt{{font-family:'IBM Plex Mono',monospace;font-size:14px;letter-spacing:.1em;color:{TX};}}
.memo{{border:1px solid {BDR};border-radius:8px;background:{CARD2};padding:18px;margin-top:14px;flex:1;}}
.memo-h{{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid {BDR};padding-bottom:10px;margin-bottom:8px;}}
.memo-h h3{{font-family:'Bebas Neue',sans-serif;font-size:40px;color:{TX};}}
.memo-h span{{font-family:'IBM Plex Mono',monospace;font-size:13px;color:{GY};}}
.memo-row{{display:grid;grid-template-columns:30px 1fr 90px;gap:10px;align-items:center;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.06);}}
.memo-row .num{{font-family:'IBM Plex Mono',monospace;font-size:15px;color:{V};font-weight:600;}}
.memo-row .txt{{font-family:'Barlow Condensed',sans-serif;font-size:26px;line-height:1.22;color:{TX};}}
.memo-row .ico{{font-family:'IBM Plex Mono',monospace;font-size:16px;color:{V};text-align:right;}}
.decisions{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:14px;}}
.dec{{border:2px solid {BDR};border-radius:8px;padding:18px;text-align:center;background:{CARD};}}
.dec.go{{border-color:{V};background:rgba(0,255,178,.08);}}
.dec.wait{{border-color:{GY};background:rgba(154,163,156,.08);}}
.dec.no{{border-color:{RED};background:rgba(255,82,71,.08);}}
.dec .ic{{font-family:'IBM Plex Mono',monospace;font-size:30px;color:{V};font-weight:700;}}
.dec.no .ic{{color:{RED};}}
.dec .t{{font-family:'Bebas Neue',sans-serif;font-size:36px;margin-top:6px;color:{TX};}}
.dec .d{{font-family:'Barlow Condensed',sans-serif;font-size:22px;color:{GY};}}
.flow6{{display:flex;justify-content:space-between;align-items:flex-start;margin:36px 0 28px;width:100%;}}
.flow6 .f{{text-align:center;flex:1;position:relative;}}
.flow6 .f::after{{content:'→';position:absolute;right:-8px;top:22px;color:{V};opacity:.3;font-size:22px;}}
.flow6 .f:last-child::after{{display:none;}}
.flow6 .ic{{width:78px;height:78px;border:1px solid {BDR};border-radius:6px;margin:0 auto 10px;background:{CARD};display:flex;align-items:center;justify-content:center;font-size:24px;color:{V};font-family:'IBM Plex Mono',monospace;}}
.flow6 .l{{font-family:'IBM Plex Mono',monospace;font-size:15px;font-weight:600;letter-spacing:.05em;color:{TX};}}
.cta-frame{{margin:28px auto 0;max-width:860px;width:100%;border:2px solid {V};padding:42px 32px;text-align:center;position:relative;background:{CARD};}}
.cta-frame::before,.cta-frame::after{{content:'';position:absolute;width:18px;height:18px;border:2px solid {V};}}
.cta-frame::before{{top:-8px;left:-8px;border-right:none;border-bottom:none;}}
.cta-frame::after{{bottom:-8px;right:-8px;border-left:none;border-top:none;}}
.cta-kw{{font-family:'Bebas Neue',sans-serif;font-size:110px;color:{V};letter-spacing:.06em;}}
.cta-hint{{font-family:'Barlow Condensed',sans-serif;font-size:40px;margin-top:14px;color:{TX};}}
.status{{display:flex;justify-content:space-between;gap:12px;margin-top:auto;padding-top:14px;}}
.status .sbox{{flex:1;border:1px solid {BDR};border-radius:6px;padding:20px;background:{CARD};
  font-family:'IBM Plex Mono',monospace;font-size:18px;line-height:1.35;color:{TX};}}
.status .sbox b.v{{color:{V};}}
.v{{color:{V};}}
.b.v,.status .sbox b.v{{color:{V};}}
"""


def build() -> str:
    s = []

    s.append(f"""
<section class="slide" data-id="01">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "ARQUITECTURA FINANCIERA"))}
  <div class="content">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start">
      <div>
        <h1 class="title xl">Te genero un<br><span class="v">trader ia</span><br>para tu empresa</h1>
        <p class="sub"><span class="v">+</span> diagnóstico · señales · riesgo · 24/7 <span class="v">+</span></p>
        <p class="body">Mapeo tu área financiera, detecto oportunidades y te dejo un sistema que <b>opera con control</b>.</p>
      </div>
      <div class="hub">
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
        <div class="node" style="left:36%;top:0%"><div class="sq">+</div><div class="lbl">DIAGNÓSTICO</div></div>
        <div class="node" style="right:0%;top:30%"><div class="sq">/</div><div class="lbl">SEÑALES</div></div>
        <div class="node" style="left:0%;top:30%"><div class="sq">!</div><div class="lbl">RIESGO</div></div>
        <div class="node" style="left:34%;bottom:-6%"><div class="sq">O</div><div class="lbl">MONITOR 24/7</div></div>
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
    <h1 class="title lg">Primero, mapeo<br>tu <span class="v">área financiera</span><br>24/7</h1>
    <p class="sub"><span class="v">+</span> caja · márgenes · flujo · alertas · <span class="v">+</span></p>
    <div class="scan">
      <div class="pane"><div class="ic">$</div><div class="h">FLUJO DE CAJA</div><div class="p">Movimientos y saldos en tiempo real.</div><div class="bar"></div></div>
      <div class="pane"><div class="ic">N</div><div class="h">CONTEXTO</div><div class="p">Eventos y variables que impactan tu negocio.</div><div class="bar"></div></div>
      <div class="scan-mid">
        <div style="text-align:center">
          <div class="radar"><div class="cross"></div>
            <div class="dot" style="left:62%;top:28%"></div><div class="dot" style="left:35%;top:55%"></div>
            <div class="dot" style="left:70%;top:68%"></div><div class="dot" style="left:48%;top:40%"></div>
          </div>
          <div class="sub" style="margin-top:14px;font-size:24px">ESCANEANDO<br><span class="v">TU OPERACIÓN</span></div>
        </div>
      </div>
      <div class="pane"><div class="ic">%</div><div class="h">MÁRGENES</div><div class="p">Rentabilidad por línea y unidad de negocio.</div><div class="bar"></div></div>
      <div class="pane"><div class="ic">*</div><div class="h">WATCHLIST</div><div class="p">KPIs críticos bajo seguimiento continuo.</div><div class="bar"></div></div>
    </div>
    <div class="status">
      <div class="sbox">MODO: <b class="v">ESCANEO</b><br>FRECUENCIA: <b class="v">CONTINUA</b></div>
      <div class="sbox">TEMPORALIDAD: <b class="v">24/7</b><br>ESTADO: <b class="v">ACTIVO</b></div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="03">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "MOTOR DE SEÑALES"))}
  <div class="content">
    <h1 class="title lg">Luego detecto<br><span class="v">oportunidades</span></h1>
    <p class="sub"><span class="v">+</span> setups de alta probabilidad para tu gestión <span class="v">+</span></p>
    <div class="engine">
      <div class="gear-box">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:15px;letter-spacing:.1em">MOTOR DE SEÑALES</div>
        <div class="gear"></div>
        <div class="steps3">
          <div class="step-mini"><div class="n">01</div><div class="t">ESCANEA</div><div class="d">Lee tus datos financieros</div></div>
          <div class="step-mini"><div class="n">02</div><div class="t">DETECTA</div><div class="d">Identifica patrones</div></div>
          <div class="step-mini"><div class="n">03</div><div class="t">PUNTÚA</div><div class="d">Rankea por impacto</div></div>
        </div>
      </div>
      <div class="patterns">
        <div class="pat"><div class="mini" style="background:linear-gradient(135deg,{CARD2} 40%,{CARD})"></div><div><div class="lbl">FLUJO</div><div class="desc">Desvío relevante en entradas o salidas de caja.</div></div></div>
        <div class="pat"><div class="mini" style="background:linear-gradient(180deg,{CARD2},{CARD})"></div><div><div class="lbl">MARGEN</div><div class="desc">Compresión o expansión de rentabilidad.</div></div></div>
        <div class="pat"><div class="mini"></div><div><div class="lbl">CAJA</div><div class="desc">Alerta de liquidez o exceso de capital ocioso.</div></div></div>
        <div class="pat"><div class="mini"></div><div><div class="lbl">TENDENCIA</div><div class="desc">Dirección sostenida en indicadores clave.</div></div></div>
        <div class="pat"><div class="mini"></div><div><div class="lbl">ALERTA</div><div class="desc">Evento que requiere decisión inmediata.</div></div></div>
        <div class="box" style="margin-top:6px"><h4>SEÑAL DETECTADA</h4><p>Setup de alta probabilidad para tu área financiera <span style="color:{V}">››››</span></p></div>
      </div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="04">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "PLAN DE GESTIÓN"))}
  <div class="content">
    <h1 class="title md">Después armo el<br><span class="v">plan de gestión</span></h1>
    <p class="sub"><span class="v">+</span> acción · objetivo · límite · invalidación <span class="v">+</span></p>
    <div class="plan">
      <div style="display:flex;flex-direction:column;gap:14px">
        <div class="box"><h4>ZONA DE ACCIÓN</h4><p>Rango óptimo para mover capital o recursos.</p><div class="bar"></div></div>
        <div class="box"><h4>LÍMITE DE RIESGO</h4><p>Tope definido antes de ejecutar cualquier movimiento.</p><div class="bar"></div></div>
        <div class="box"><h4>RIESGO / BENEFICIO</h4><p>Ratio calculado: <b style="color:{V}">1 : 2.2</b></p><div class="bar"></div></div>
      </div>
      <div class="plan-mid">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:15px;margin-bottom:10px">PLAN DE GESTIÓN</div>
        <div class="chart">
          <div class="zone" style="top:35%;height:28%"></div>
          <div class="line-t" style="top:18%"></div>
          <div class="lbl-side" style="top:18%;color:{V}">OBJETIVO</div>
          <div class="line-s" style="top:62%"></div>
          <div class="lbl-side" style="top:62%;color:{RED}">LÍMITE</div>
          <div class="line-i" style="top:82%"></div>
          <div class="lbl-side" style="top:82%">INVALIDACIÓN</div>
          <div class="candle" style="left:20%;height:35%"></div><div class="candle" style="left:32%;height:45%"></div>
          <div class="candle" style="left:44%;height:38%"></div><div class="candle" style="left:56%;height:52%"></div>
          <div class="candle" style="left:68%;height:48%"></div>
        </div>
        <div style="display:flex;gap:16px;margin-top:10px;font-family:'IBM Plex Mono',monospace;font-size:14px">
          <span>DIRECCIÓN: <b class="v">OPTIMIZAR</b></span>
          <span>HORIZONTE: <b>TRIMESTRE</b></span>
          <span>CONFIANZA: <b class="v">ALTA</b></span>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:14px">
        <div class="box"><h4>OBJETIVO</h4><p>Meta de retorno o eficiencia definida.</p><div class="bar"></div></div>
        <div class="box"><h4>INVALIDACIÓN</h4><p>Condición que cancela el plan si se rompe.</p><div class="bar"></div></div>
        <div class="box"><h4>PLAN LISTO</h4><p>Todos los niveles confirmados.</p><div class="bar"></div></div>
      </div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="05">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "MÓDULO DE RIESGO"))}
  <div class="content">
    <h1 class="title md">Pero el módulo<br>de <span class="v">riesgo</span> revisa todo</h1>
    <p class="sub"><span class="v">+</span> tamaño · exposición · pérdida · <span class="v">+</span></p>
    <div class="risk">
      <div style="display:flex;flex-direction:column;gap:14px">
        <div class="box"><h4>01 TAMAÑO</h4><p>Calcula cuánto mover según el riesgo por decisión.</p><div class="bar"></div></div>
        <div class="box"><h4>02 EXPOSICIÓN</h4><p>Revisa el total comprometido en todas las posiciones.</p><div class="bar"></div></div>
        <div class="box"><h4>03 DRAWDOWN</h4><p>Verifica el límite de caída permitido.</p><div class="bar"></div></div>
      </div>
      <div class="risk-mid">
        <div style="font-family:'IBM Plex Mono',monospace;font-size:15px;margin-bottom:12px">MÓDULO DE RIESGO</div>
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
      <div style="display:flex;flex-direction:column;gap:14px">
        <div class="box"><h4>04 VOLATILIDAD</h4><p>Confirma que el entorno sea aceptable.</p><div class="bar"></div></div>
        <div class="box"><h4>05 PÉRDIDA MÁX</h4><p>Asegura que no se supere el tope definido.</p><div class="bar"></div></div>
        <div class="box"><h4>RIESGO OK</h4><p>Protegiendo el capital en cada decisión.</p><div class="bar"></div></div>
      </div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="06">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "LOOP DE MONITOREO"))}
  <div class="content">
    <h1 class="title lg" style="text-align:center">El sistema queda<br><span class="v">activo 24/7</span></h1>
    <p class="sub" style="text-align:center"><span class="v">+</span> monitoreo · alertas · revisión · <span class="v">+</span></p>
    <div class="loop">
      <div class="ring"></div><div class="ring-dash"></div>
      <div class="loop-core"><div class="big">24/7</div><div class="subt">LOOP DE MONITOREO</div><div class="body" style="font-size:20px;margin-top:8px;color:#9aa39c">Seguimiento continuo de tu área financiera</div></div>
      <div class="node" style="left:2%;top:14%"><div class="sq">=</div><div class="lbl">WATCHLIST</div></div>
      <div class="node" style="right:2%;top:14%"><div class="sq">!</div><div class="lbl">ALERTAS</div></div>
      <div class="node" style="left:0%;top:46%"><div class="sq">%</div><div class="lbl">ESTADO</div></div>
      <div class="node" style="right:0%;top:46%"><div class="sq">~</div><div class="lbl">SEÑAL</div></div>
      <div class="node" style="left:14%;bottom:4%"><div class="sq">M</div><div class="lbl">MONITOR</div></div>
      <div class="node" style="right:14%;bottom:4%"><div class="sq">!</div><div class="lbl">RIESGO</div></div>
      <div class="node" style="left:42%;top:0%"><div class="sq">+</div><div class="lbl">ESCANEO</div></div>
    </div>
    <div class="status">
      <div class="sbox">SISTEMA EN LÍNEA 24/7<br><b class="v">Sin pausas. Sin botón de apagado.</b></div>
      <div class="sbox" style="text-align:right">LOOP ACTIVO<br><b class="v">Siempre atento. Siempre listo.</b></div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="07">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "DECISIÓN FINAL"))}
  <div class="content">
    <h1 class="title md" style="text-align:center">Al final recibís<br>una <span class="v">decisión clara</span></h1>
    <p class="sub" style="text-align:center">La tomás. La observás. O la descartás.</p>
    <div class="memo">
      <div class="memo-h"><h3>MEMO DE DECISIÓN</h3><span>ID: TG-247 · FECHA: HOY</span></div>
      <div class="memo-row"><div class="num">1</div><div class="txt"><b>Resumen:</b> alineación de flujo, margen y contexto de mercado favorable.</div><div class="ico">/</div></div>
      <div class="memo-row"><div class="num">2</div><div class="txt"><b>Fuerza de señal:</b> 4/5 — <span style="color:{V}">FUERTE</span></div><div class="ico">O</div></div>
      <div class="memo-row"><div class="num">3</div><div class="txt"><b>Nivel de riesgo:</b> MODERADO</div><div class="ico">●●●○</div></div>
      <div class="memo-row"><div class="num">4</div><div class="txt"><b>Plan:</b> acción definida · límite · objetivo calculado.</div><div class="ico">=</div></div>
      <div class="memo-row"><div class="num">5</div><div class="txt" style="font-family:'Bebas Neue',sans-serif;font-size:34px;color:{V}">DECISIÓN LISTA</div><div class="ico"></div></div>
    </div>
    <p class="tag" style="display:block;text-align:center;margin:10px auto 0;max-width:420px">— REVISIÓN HUMANA INCLUIDA —</p>
    <div class="decisions">
      <div class="dec go"><div class="ic">+</div><div class="t">EJECUTAR</div><div class="d">Aplicar el plan</div></div>
      <div class="dec wait"><div class="ic">O</div><div class="t">OBSERVAR</div><div class="d">Monitorear condiciones</div></div>
      <div class="dec no"><div class="ic">X</div><div class="t">DESCARTAR</div><div class="d">No mover ahora</div></div>
    </div>
  </div>
</section>""")

    s.append(f"""
<section class="slide" data-id="08">{chrome(meta("TRADER IA EMPRESARIAL", "A MEDIDA", "COORDINAR REUNIÓN"))}
  <div class="content center">
    <h1 class="title xl">Tu empresa merece<br><span class="v">gestión financiera</span><br>con ia</h1>
    <p class="sub"><span class="v">—</span> coordinemos una reunión <span class="v">—</span></p>
    <div class="flow6" style="max-width:1000px;width:100%">
      <div class="f"><div class="ic">+</div><div class="l">DIAGNÓSTICO</div></div>
      <div class="f"><div class="ic">/</div><div class="l">SEÑALES</div></div>
      <div class="f"><div class="ic">=</div><div class="l">PLAN</div></div>
      <div class="f"><div class="ic">!</div><div class="l">RIESGO</div></div>
      <div class="f"><div class="ic">O</div><div class="l">MONITOR</div></div>
      <div class="f"><div class="ic">*</div><div class="l">DECISIÓN</div></div>
    </div>
    <div class="cta-frame">
      <div class="cta-kw">REUNIÓN</div>
      <div class="cta-hint">Comentá <b style="color:{V}">REUNIÓN</b> y te escribo para coordinar.</div>
    </div>
    <p class="body" style="max-width:900px;margin-top:22px;font-size:34px">Te genero el trader IA, lo adapto a tu operación y te muestro cómo gestionar tu área financiera con control total.</p>
    <p class="tag" style="margin-top:22px;font-size:18px;padding:12px 18px">HECHO PARA ESCALAR. DISEÑADO PARA DECIDIR.</p>
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
        "fondo": "reticula_fina",
        "familia_visual": "before_after",
        "origen": "screenshot",
        "keyword_portada": "REUNIÓN",
        "modo": "negro",
        "resoluciones": {"4k": "4320x5400", "fhd": "1920x2400", "retina": "2160x2700"},
        "notas": "Modo negro STLabs. Blueprint trader B2B. Primera persona. CTA REUNIÓN.",
    }
    (B / "manifest.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OK 8 slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
