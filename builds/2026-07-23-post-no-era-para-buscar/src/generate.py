# -*- coding: utf-8 -*-
"""Carrusel STLabs — clon del carrusel 'QUERY / RFC 10008' (12 slides), modo blanco."""
import sys

sys.path.insert(0, "/workspace")
from stlabs_kit import chrome, write_html  # noqa: E402
from robots import robot, penguin, squiggle, cloud, server, NARANJA, VERDE, AZUL  # noqa: E402

BUILD = "/tmp/build-query"

# ─────────────────────────────── CSS ───────────────────────────────
CSS = """
/* ── MODO BLANCO STLabs ── */
.slide{background:#FFFFFF;color:#0A0A0A;}
.slide::before{content:'';position:absolute;inset:0;z-index:0;
 background-image:linear-gradient(rgba(10,10,10,.05) 1px,transparent 1px),
  linear-gradient(90deg,rgba(10,10,10,.05) 1px,transparent 1px);background-size:60px 60px;
 -webkit-mask-image:radial-gradient(80% 80% at 50% 42%,#000 30%,transparent 100%);
         mask-image:radial-gradient(80% 80% at 50% 42%,#000 30%,transparent 100%);}
.slide::after{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
 background:radial-gradient(46% 30% at 88% 4%, rgba(0,255,178,.10), transparent 60%),
            radial-gradient(42% 26% at 8% 100%, rgba(0,255,178,.07), transparent 60%);}
b{color:#0A0A0A;}
.web{left:50%;right:auto;transform:translateX(-50%);width:max-content;opacity:1;text-shadow:0 0 1px rgba(0,90,60,.35);}
.rol,.rol-sub{width:max-content;margin-left:auto;margin-right:auto;}

/* chrome superior e inferior */
.topsq{position:absolute;top:52px;left:0;right:0;text-align:center;z-index:5;}
.nav{position:absolute;bottom:62px;z-index:6;font-family:var(--mono);font-size:22px;color:#8a8f8b;}
.nav-l{left:84px;} .nav-r{right:84px;}

/* tipografía base */
.kick{font-family:var(--mono);font-weight:600;font-size:25px;letter-spacing:3px;color:#0A0A0A;}
.kick::before{content:'';display:inline-block;width:14px;height:14px;background:var(--verde);
 margin-right:14px;border:2px solid #0A0A0A;}
h1{font-family:var(--pop);font-weight:800;font-size:88px;line-height:1.08;color:#0A0A0A;text-align:left;}
.hl{display:inline-block;background:var(--verde);color:#062a1e;border-radius:10px;padding:0 22px 6px;
 box-shadow:4px 5px 0 rgba(10,10,10,.9);}
.hl.amb{background:var(--am);color:#33150a;}
.sub{font-family:var(--cond);font-weight:500;font-size:37px;line-height:1.32;color:#3c403d;max-width:850px;text-align:left;}
.sub b{font-weight:700;}
.wrap{position:absolute;inset:0;padding:150px 84px 0;z-index:3;}

/* burbujas de diálogo pixel */
.bub{position:absolute;background:#fff;border:3.5px solid #10131a;border-radius:16px;
 padding:14px 20px;font-family:var(--cond);font-weight:600;font-size:28px;line-height:1.12;color:#0A0A0A;
 text-align:center;box-shadow:5px 6px 0 rgba(10,10,10,.14);z-index:6;}
.bub::after{content:'';position:absolute;bottom:-13px;left:50%;transform:translateX(-50%) rotate(45deg);
 width:20px;height:20px;background:#fff;border-right:3.5px solid #10131a;border-bottom:3.5px solid #10131a;}

/* banner protocolo */
.banner{position:absolute;left:50%;transform:translateX(-50%) skewX(-8deg);background:#ECECE6;
 border:2.5px solid #c9c9c1;border-radius:40px;padding:15px 44px;font-family:var(--pop);font-weight:800;
 font-style:italic;font-size:30px;letter-spacing:2px;color:#111;z-index:6;white-space:nowrap;
 box-shadow:0 6px 0 rgba(10,10,10,.10);}

/* valija RFC */
.case{position:absolute;background:#fff;border:3.5px solid #10131a;border-radius:12px;
 padding:10px 18px;font-family:var(--mono);font-weight:600;font-size:26px;color:#0A0A0A;z-index:6;
 box-shadow:4px 5px 0 rgba(10,10,10,.14);}
.case::before{content:'';position:absolute;top:-14px;left:50%;transform:translateX(-50%);
 width:46px;height:22px;border:3.5px solid #10131a;border-bottom:none;border-radius:10px 10px 0 0;}

/* chips de estado */
.chip{display:inline-block;font-family:var(--mono);font-weight:600;font-size:24px;border-radius:10px;
 padding:9px 18px;background:#fff;border:2.5px solid #d8d8d0;color:#3c403d;box-shadow:3px 4px 0 rgba(10,10,10,.08);}
.chip.neg{color:#c23a12;border-color:#ffb59d;background:#fff4ef;}
.chip.pos{color:#04130b;border-color:rgba(0,180,125,.65);background:rgba(0,255,178,.16);}

/* cards genéricas */
.card{background:#fff;border:2.5px solid #e0e0d8;border-radius:20px;box-shadow:0 14px 34px rgba(10,10,10,.08);}
.card-lab{font-family:var(--mono);font-weight:600;font-size:23px;letter-spacing:1px;color:#6a6f6b;}

/* código */
.code{background:#101418;border-radius:16px;padding:26px 30px;font-family:var(--mono);
 font-size:29px;line-height:1.5;color:#cfd6cf;text-align:left;box-shadow:0 12px 30px rgba(10,10,10,.18);}
.code .vq{color:var(--verde);font-weight:600;} .code .vp{color:#FF7A50;font-weight:600;}
.code .vg{color:#6FA8FF;font-weight:600;} .code .va{color:var(--am);font-weight:600;}
.code .cm{color:#7ef7cd;} .code .dim{color:#8b949e;}
.codehead{font-family:var(--mono);font-weight:600;font-size:24px;letter-spacing:1px;border-radius:10px 10px 0 0;
 padding:12px 24px;color:#fff;text-align:left;}

/* servidores */
.srv{display:flex;flex-direction:column;gap:7px;justify-content:center;}
.srv-bar{flex:1;width:96px;background:#fff;border:3px solid #10131a;border-radius:8px;
 display:flex;align-items:center;gap:7px;padding-left:12px;}
.srv-bar i{width:9px;height:9px;border-radius:50%;background:var(--verde);border:1.6px solid #0A0A0A;}
.srv-bar i:last-child{background:#d8d8d0;}

/* timeline S4 */
.tl{display:flex;align-items:center;gap:22px;font-family:var(--mono);font-weight:600;font-size:27px;color:#9aa39c;}
.tl .ln{flex:1;height:3px;background:#d8d8d0;}
.tl .on{color:#04130b;background:rgba(0,255,178,.2);border:2.5px solid rgba(0,160,110,.6);
 border-radius:10px;padding:6px 18px;}

/* ficha técnica S5 */
.ficha{position:relative;background:#0e1116;border-radius:22px;padding:44px 52px 38px;color:#F2F2F2;
 box-shadow:0 22px 44px rgba(10,10,10,.28);text-align:left;}
.ficha::before{content:'';position:absolute;left:0;right:0;top:118px;border-top:3px dashed #2c313a;}
.fi-chip{display:inline-block;background:var(--verde);color:#04130b;font-family:var(--mono);font-weight:600;
 font-size:23px;padding:8px 16px;border-radius:8px;}
.fi-q{font-family:var(--pop);font-weight:800;font-size:56px;color:#fff;margin-left:26px;vertical-align:middle;}
.fi-row{display:flex;align-items:center;gap:20px;font-family:var(--cond);font-weight:600;font-size:38px;margin-top:22px;}
.fi-row i{font-style:normal;color:var(--verde);font-family:var(--mono);font-weight:600;font-size:34px;}
.fi-meta{margin-top:34px;font-family:var(--mono);font-size:23px;color:#8b949e;line-height:1.5;}
.fi-sign{margin-top:22px;display:flex;justify-content:space-between;align-items:center;}
.fi-sign .names{font-family:'Caveat',cursive;font-size:40px;color:#c9d1d9;}
.sello{font-family:var(--mono);font-size:21px;color:#aab3bc;border:2.5px solid #57606a;border-radius:40px;
 padding:10px 22px;transform:rotate(-6deg);}

/* diagramas de red S7/S8 */
.net-lab{font-family:var(--mono);font-weight:600;font-size:23px;letter-spacing:1px;}
.net-pill{border-radius:14px;padding:16px 24px;font-family:var(--mono);font-size:27px;text-align:left;}
.net-line{position:absolute;height:3px;background:#d0d0c8;z-index:1;}
.dotline{border-top:3.5px dotted #b9b9b1;}

/* diario S9 */
.paper9{position:relative;width:660px;background:#FBF7EC;border:2.5px solid #d9d2be;border-radius:6px;
 padding:34px 40px;transform:rotate(-2.5deg);box-shadow:0 18px 40px rgba(10,10,10,.16);text-align:left;}
.paper9 .mast{font-family:var(--serif);font-style:italic;font-weight:700;font-size:27px;color:#3b3628;
 border-bottom:3px solid #3b3628;padding-bottom:10px;letter-spacing:1px;}
.paper9 h4{font-family:var(--serif);font-style:italic;font-weight:700;font-size:47px;color:#191713;
 margin-top:18px;line-height:1.15;border-bottom:2px solid #cfc7b0;padding-bottom:16px;}
.paper9 .tach{position:relative;white-space:nowrap;}
.paper9 .tach::after{content:'';position:absolute;left:-4px;right:-4px;top:54%;height:5px;background:#c23a12;transform:rotate(-3deg);}
.paper9{padding-bottom:118px;}
.paper9 .cuerpo{margin-top:14px;font-family:var(--serif);font-style:italic;font-size:24px;color:#8d8571;}
.stamp{position:absolute;left:36px;bottom:26px;font-family:var(--mono);font-weight:600;font-size:27px;
 color:#D6301B;border:4px solid #D6301B;border-radius:8px;padding:8px 18px;transform:rotate(-9deg);opacity:.85;}
.sticky{position:absolute;right:-58px;bottom:-30px;width:210px;height:190px;background:#FFD84D;
 box-shadow:0 12px 24px rgba(10,10,10,.22);transform:rotate(4deg);padding:20px 22px;
 font-family:'Caveat',cursive;font-weight:700;font-size:44px;line-height:1.02;color:#241d05;text-align:left;}

/* adopción S10 */
.stackbox{background:#fff;border:2.5px solid #d8d8d0;border-radius:14px;padding:22px 8px;
 font-family:var(--mono);font-weight:600;font-size:25px;color:#565b57;text-align:center;
 box-shadow:4px 5px 0 rgba(10,10,10,.07);position:relative;overflow:hidden;}
.stackbox::before{content:'';position:absolute;inset:0;
 background:repeating-linear-gradient(45deg,rgba(10,10,10,.045) 0 10px,transparent 10px 20px);}
.adopbar{height:16px;border-radius:10px;background:#e7e7df;border:2px solid #cfcfc7;overflow:hidden;}
.adopbar span{display:block;height:100%;width:15%;background:var(--verde);}

/* junior/senior S11 */
.rol{font-family:var(--serif);font-style:italic;font-weight:700;font-size:64px;text-align:center;}
.rol-sub{font-family:var(--cond);font-weight:500;font-size:31px;color:#6a6f6b;text-align:center;margin-top:2px;}

/* CTA S12 */
.cta-pill{display:inline-block;background:#fff;border:3px solid #10131a;border-radius:ied 40px;}
.pill12{display:inline-block;background:#fff;border:3px solid #10131a;border-radius:40px;padding:18px 44px;
 font-family:var(--cond);font-weight:700;font-size:34px;color:#0A0A0A;box-shadow:5px 6px 0 rgba(0,255,178,.8);}
.share{position:absolute;bottom:132px;z-index:6;font-family:var(--cond);font-weight:600;font-size:27px;color:#3c403d;}
.arrowup{position:absolute;left:120px;top:96px;z-index:5;}
"""

TOP = f'<div class="topsq">{squiggle(128)}</div>'


def navs(l="&#8592; Desliz&aacute;", r="Guardalo"):
    return f'<div class="nav nav-l">{l}</div><div class="nav nav-r">{r}</div>'


S = []

# ─────────────────────────── SLIDE 1 — Portada ───────────────────────────
S.append(TOP + f'''
<div class="wrap" style="padding-top:132px;">
  <div class="kick">RFC 10008 &middot; IETF &middot; JUNIO 2026</div>
  <h1 style="font-size:99px;margin-top:34px;">POST no era para<br>
    <span class="hl" style="margin:10px 0 6px;">buscar</span><br>
    Nunca lo fue.</h1>
  <div class="sub" style="margin-top:30px;max-width:660px;">Llev&aacute;s a&ntilde;os buscando con <b>POST</b> y
    rompiendo la sem&aacute;ntica de HTTP sin saberlo.</div>
</div>
<div class="bub" style="left:74px;top:672px;width:180px;">&iquest;y ese qui&eacute;n es?</div>
<div style="position:absolute;left:96px;top:836px;z-index:5;">{robot("get", 150)}</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:742px;z-index:5;">{robot("query", 296)}</div>
<div class="case" style="left:704px;top:940px;">RFC 10008</div>
<div class="bub" style="right:66px;top:646px;width:230px;">seguro nos quita tr&aacute;fico</div>
<div style="position:absolute;right:88px;top:836px;z-index:5;">{robot("post", 150)}</div>
<div class="banner" style="top:1120px;">BIENVENIDO AL PROTOCOLO</div>
''' + navs())

# ─────────────────────────── SLIDE 2 — junior o senior ───────────────────────────
S.append(TOP + '''
<div class="wrap">
  <h1>C&oacute;mo <span class="hl">busc&aacute;s</span> te delata:<br>junior o senior</h1>
  <div class="sub" style="margin-top:34px;">Met&eacute;s muchos filtros y lo mand&aacute;s con <b>POST /search</b>.
   Pero POST le grita a la red: <b>&laquo;voy a crear o modificar&raquo;</b>. Y vos solo quer&iacute;as <b>leer</b>.</div>
</div>
<div class="card" style="position:absolute;left:84px;top:678px;width:428px;height:420px;padding:30px 32px;z-index:5;">
  <div class="card-lab">lo que escrib&iacute;s</div>
  <div class="code" style="margin-top:22px;font-size:28px;">
    <span class="vp">POST</span> /search<br>{ <span class="dim">"filtros"</span>: {&hellip;}<br>}
  </div>
  <div style="font-family:var(--cond);font-weight:600;font-size:29px;color:#6a6f6b;margin-top:26px;">&iquest;te suena?</div>
</div>
<div class="card" style="position:absolute;right:84px;top:678px;width:428px;height:420px;padding:30px 32px;z-index:5;">
  <div class="card-lab" style="color:#c23a12;">lo que la red entiende</div>
  <div class="code" style="margin-top:22px;font-size:28px;">
    <span class="vp">ESCRITURA</span><br><span class="dim">&middot; no cachear</span><br><span class="dim">&middot; no es safe</span>
  </div>
  <div style="font-family:var(--mono);font-weight:600;font-size:27px;color:#c23a12;margin-top:26px;">&rarr; malentendido</div>
</div>
''' + navs())

# ─────────────────────────── SLIDE 3 — dos malas opciones ───────────────────────────
S.append(TOP + f'''
<div class="wrap">
  <h1>Antes solo ten&iacute;as <span class="hl">dos</span><br>malas opciones</h1>
  <div class="sub" style="margin-top:34px;"><b>GET</b> mete la consulta en la URL y se queda corto.
   <b>POST</b> lleva body, pero crea o modifica: <b>ni safe ni cacheable</b>.</div>
</div>
<div class="bub" style="left:160px;top:640px;width:220px;">&iquest;URLs largas otra vez?</div>
<div class="bub" style="right:160px;top:640px;width:220px;">y encima nadie me avis&oacute;</div>
<div style="position:absolute;left:190px;top:800px;z-index:5;">{robot("get", 176)}</div>
<div style="position:absolute;right:190px;top:800px;z-index:5;">{robot("post", 176)}</div>
<div style="position:absolute;left:110px;top:1024px;width:340px;text-align:center;z-index:5;">
  <span class="chip neg">longitud m&aacute;xima</span><br>
  <span class="chip neg" style="margin-top:14px;">sin body</span>
</div>
<div style="position:absolute;right:110px;top:1024px;width:340px;text-align:center;z-index:5;">
  <span class="chip neg">no safe</span><br>
  <span class="chip neg" style="margin-top:14px;">no cacheable</span>
</div>
''' + navs())

# ─────────────────────────── SLIDE 4 — llega QUERY ───────────────────────────
S.append(TOP + f'''
<div class="wrap">
  <h1>Llega <span class="hl">QUERY</span>: GET,<br>pero con body</h1>
  <div class="sub" style="margin-top:34px;">Se ubica entre GET y POST: manda la consulta en el
   <b>body (JSON)</b>, pero es de <b>solo lectura</b> y no toca el servidor.</div>
  <div class="tl" style="margin-top:52px;max-width:640px;">
    <span>GET</span><span class="ln"></span><span class="on">QUERY</span><span class="ln"></span><span>POST</span>
  </div>
</div>
<div class="bub" style="left:50%;transform:translateX(-50%);top:702px;width:330px;">traje body, sem&aacute;ntica limpia y soy <b style="color:#00795a;">cacheable</b>.</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:846px;z-index:7;">{robot("query", 262)}</div>
<div class="case" style="left:682px;top:1000px;">RFC 10008</div>
<div class="banner" style="top:1120px;">BIENVENIDO AL PROTOCOLO</div>
''' + navs())

# ─────────────────────────── SLIDE 5 — ficha técnica ───────────────────────────
S.append(TOP + '''
<div class="wrap">
  <h1>La <span class="hl">ficha</span> t&eacute;cnica de<br>QUERY</h1>
  <div class="sub" style="margin-top:34px;"><b>safe</b> = no cambia el estado &middot;
   <b>idempotente</b> = repetir da lo mismo &middot; <b>cacheable</b> = la red guarda la respuesta.</div>
</div>
<div class="ficha" style="position:absolute;left:84px;right:84px;top:636px;z-index:5;">
  <div><span class="fi-chip">M&Eacute;TODO HTTP</span><span class="fi-q">QUERY</span></div>
  <div style="margin-top:30px;">
    <div class="fi-row"><i>&#10003;</i> safe</div>
    <div class="fi-row"><i>&#10003;</i> idempotente</div>
    <div class="fi-row"><i>&#10003;</i> cacheable</div>
    <div class="fi-row"><i>&#10003;</i> lleva body (JSON)</div>
  </div>
  <div class="fi-meta">RFC 10008 &middot; IETF Standards Track &middot; emitido jun 2026</div>
  <div class="fi-sign">
    <span class="names">Reschke &middot; Snell &middot; Bishop</span>
    <span class="sello">IESG &middot; 2025-11-20</span>
  </div>
</div>
''' + navs())

# ─────────────────────────── SLIDE 6 — request QUERY ───────────────────────────
S.append(TOP + '''
<div class="wrap">
  <h1 style="font-size:82px;">As&iacute; se ve una request<br><span class="hl">QUERY</span></h1>
  <div class="sub" style="margin-top:34px;">Mismo body, mismos filtros. Solo cambia el verbo&hellip;
   y ahora la red <b>puede cachear</b> la respuesta.</div>
</div>
<div style="position:absolute;left:84px;right:84px;top:678px;z-index:5;text-align:left;">
  <div class="codehead" style="background:#B3411B;">ANTES &middot; ABUSANDO DE POST</div>
  <div class="code" style="border-radius:0 0 16px 16px;">
    <span class="vp">POST</span> /productos/search HTTP/1.1<br>{ <span class="dim">"color"</span>: "azul", <span class="dim">"precio_max"</span>: 50 }
  </div>
</div>
<div style="position:absolute;left:84px;right:84px;top:934px;z-index:5;text-align:left;">
  <div class="codehead" style="background:#00795a;">AHORA &middot; CON QUERY</div>
  <div class="code" style="border-radius:0 0 16px 16px;">
    <span class="vq">QUERY</span> /productos HTTP/1.1<br>{ <span class="dim">"color"</span>: "azul", <span class="dim">"precio_max"</span>: 50 }<br><br>
    <span class="cm"># ahora es cacheable</span>
  </div>
</div>
''' + navs())

# ─────────────────────────── SLIDE 7 — qué viaja por el cable ───────────────────────────
S.append(TOP + f'''
<div class="wrap">
  <h1 style="font-size:82px;">Qu&eacute; viaja de verdad<br>por el <span class="hl">cable</span></h1>
  <div class="sub" style="margin-top:34px;"><b>GET</b>: los filtros van pegados a la URL, visibles y con l&iacute;mite.<br>
   <b>QUERY</b>: la direcci&oacute;n queda limpia y la consulta viaja <b>dentro del sobre</b> (el body).</div>
</div>
<div style="position:absolute;left:84px;top:716px;z-index:5;">{penguin(78)}</div>
<div class="net-line" style="left:170px;top:760px;width:120px;"></div>
<div style="position:absolute;left:290px;top:700px;width:560px;z-index:5;text-align:left;">
  <div class="net-lab" style="color:#c23a12;">GET &middot; URL</div>
  <div class="net-pill" style="margin-top:8px;background:#fff4ef;border:2.5px solid #ffb59d;color:#8a3315;">
    /search?q=&amp;f=&amp;orden=&amp;pag=999&hellip;</div>
</div>
<div class="net-line" style="left:862px;top:760px;width:96px;"></div>
<div style="position:absolute;right:84px;top:712px;z-index:5;">{server(100)}</div>

<div style="position:absolute;left:84px;top:986px;z-index:5;">{penguin(78)}</div>
<div class="net-line" style="left:170px;top:1030px;width:120px;"></div>
<div style="position:absolute;left:290px;top:938px;width:560px;z-index:5;text-align:left;">
  <div class="net-lab" style="color:#00795a;">QUERY &middot; body</div>
  <div class="net-pill" style="margin-top:8px;background:rgba(0,255,178,.12);border:2.5px solid rgba(0,170,118,.55);color:#0A0A0A;">
    /search <span style="color:#00795a;">&middot; safe</span><br>
    <span style="display:inline-block;margin-top:8px;background:#101418;color:#cfd6cf;border-radius:10px;padding:8px 16px;">{{ "filtros": {{&hellip;}} }}</span></div>
</div>
<div class="net-line" style="left:862px;top:1030px;width:96px;"></div>
<div style="position:absolute;right:84px;top:982px;z-index:5;">{server(100)}</div>
''' + navs())

# ─────────────────────────── SLIDE 8 — cache y reintentos ───────────────────────────
S.append(TOP + f'''
<div class="wrap">
  <h1>Gratis: <span class="hl">cache</span> y<br>reintentos seguros</h1>
  <div class="sub" style="margin-top:34px;">Como es <b>safe</b>, el CDN cachea la respuesta:
   misma consulta &rarr; respuesta guardada.<br>Como es <b>idempotente</b>, si la red falla el cliente
   <b>reintenta sin miedo</b>.</div>
</div>
<div style="position:absolute;left:96px;top:756px;z-index:5;text-align:center;">{penguin(84)}
  <div class="net-lab" style="margin-top:10px;color:#3c403d;">cliente</div></div>
<div style="position:absolute;left:238px;top:770px;z-index:5;font-family:var(--mono);font-weight:600;font-size:24px;color:#00795a;">QUERY +<br>body &rarr;</div>
<div style="position:absolute;left:434px;top:726px;z-index:5;">{cloud(226)}</div>
<div style="position:absolute;left:706px;top:770px;z-index:5;font-family:var(--mono);font-weight:600;font-size:24px;color:#565b57;">solo la 1&ordf;<br>&rarr;</div>
<div style="position:absolute;right:88px;top:742px;z-index:5;text-align:center;">{server(104)}
  <div class="net-lab" style="margin-top:10px;color:#3c403d;">servidor</div></div>
<div class="dotline" style="position:absolute;left:238px;right:240px;top:914px;z-index:4;"></div>
<div style="position:absolute;left:238px;top:930px;z-index:5;font-family:var(--mono);font-weight:600;font-size:25px;color:#00795a;">&larr; 200 OK &middot; respuesta cacheable</div>
<div style="position:absolute;left:84px;top:1020px;z-index:5;"><span class="chip pos">2&ordf; petici&oacute;n id&eacute;ntica &rarr; cache HIT</span></div>
<div style="position:absolute;left:84px;top:1096px;z-index:5;"><span class="chip"><span style="color:#00795a;">&#8635; idempotente</span>: reintenta sin miedo</span></div>
''' + navs())

# ─────────────────────────── SLIDE 9 — seamos honestos ───────────────────────────
S.append(TOP + '''
<div class="wrap">
  <h1 style="font-size:68px;">Seamos <span class="hl amb">honestos</span>:<br>no es &laquo;el primero en 20 a&ntilde;os&raquo;</h1>
  <div class="sub" style="margin-top:34px;">Vas a leer que QUERY es &laquo;el primer m&eacute;todo en 20 a&ntilde;os&raquo;.
   <b>No es exacto:</b> PATCH lleg&oacute; en 2010. Es el primer verbo <b>seguro con body</b> en una d&eacute;cada.</div>
</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:730px;z-index:5;">
  <div class="paper9">
    <div class="mast">THE PROTOCOL TIMES &middot; A&Ntilde;O 2002</div>
    <h4>Primer m&eacute;todo nuevo <span class="tach">en 20 a&ntilde;os</span></h4>
    <div class="cuerpo">Sin novedades en el cable.</div>
    <div class="stamp">FE DE ERRATAS</div>
    <div class="sticky">PATCH<br>RFC 5789<br>2010</div>
  </div>
</div>
''' + navs())

# ─────────────────────────── SLIDE 10 — adopción ───────────────────────────
S.append(TOP + f'''
<div class="wrap">
  <h1>El siguiente desaf&iacute;o es<br>la <span class="hl">adopci&oacute;n</span></h1>
  <div class="sub" style="margin-top:34px;">El m&eacute;todo ya est&aacute; aprobado, pero para producci&oacute;n
   falta que <b>todo el stack</b> lo soporte. Y eso no pasa de un d&iacute;a para el otro.</div>
</div>
<div style="position:absolute;left:110px;top:756px;z-index:5;">{robot("query", 190)}</div>
<div style="position:absolute;left:380px;top:706px;width:600px;z-index:5;display:grid;grid-template-columns:1fr 1fr;gap:18px;">
  <div class="stackbox">servidores</div><div class="stackbox">frameworks</div>
  <div class="stackbox">proxies</div><div class="stackbox">CDNs</div>
  <div class="stackbox" style="grid-column:1/3;width:60%;justify-self:center;">tooling</div>
</div>
<div style="position:absolute;left:380px;top:1016px;width:600px;z-index:5;text-align:left;">
  <div class="net-lab" style="color:#0A0A0A;">15% soportado</div>
  <div class="adopbar" style="margin-top:10px;"><span></span></div>
</div>
<div class="bub" style="left:50%;transform:translateX(-50%);top:1124px;width:740px;font-size:26px;">GET, a medias:
 &laquo;bienvenido&hellip; cuando servidores y CDNs te soporten, hablamos&raquo;.</div>
''' + navs())

# ─────────────────────────── SLIDE 11 — junior vs senior ───────────────────────────
S.append(TOP + '''
<div class="wrap">
  <h1>El verbo correcto <span class="hl">separa</span><br>al junior del senior</h1>
</div>
<div style="position:absolute;left:0;right:0;top:520px;z-index:5;">
  <div class="rol" style="color:#8a8f8b;">un junior</div>
  <div class="rol-sub">memoriza: &laquo;para mandar datos, POST&raquo;</div>
</div>
<div class="code" style="position:absolute;left:50%;transform:translateX(-50%);top:686px;width:520px;z-index:5;font-size:30px;">
  <span class="vg">GET</span>   <span class="dim">&rarr;</span> lee<br>
  <span class="vp">POST</span>  <span class="dim">&rarr;</span> crea<br>
  <span class="va">PATCH</span> <span class="dim">&rarr;</span> modifica<br>
  <span class="vq">QUERY</span> <span class="dim">&rarr;</span> lee + body
</div>
<div style="position:absolute;left:0;right:0;top:986px;z-index:5;">
  <div class="rol" style="color:#00795a;">un senior</div>
  <div class="rol-sub" style="color:#3c403d;">entiende qu&eacute; le promete a la red cada verbo</div>
</div>
<div style="position:absolute;left:0;right:0;top:1136px;text-align:center;z-index:5;">
  <span class="chip" style="font-family:var(--cond);font-weight:700;font-size:29px;color:#0A0A0A;">
    Entender el mecanismo &gt; memorizar la receta.</span>
</div>
''' + navs())

# ─────────────────────────── SLIDE 12 — CTA final ───────────────────────────
S.append(f'''
<div class="arrowup"><svg width="90" viewBox="0 0 50 50" fill="none">
  <path d="M42 44 C 20 40, 10 28, 12 8" stroke="{VERDE}" stroke-width="4" stroke-linecap="round"/>
  <path d="M5 16 L12 6 L20 14" stroke="{VERDE}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg></div>
<div style="position:absolute;left:230px;top:118px;font-family:var(--cond);font-weight:600;font-size:30px;color:#3c403d;z-index:5;">Seguime para m&aacute;s<br>contenido as&iacute;</div>
<div class="wrap" style="padding-top:300px;text-align:center;">
  <h1 style="text-align:center;font-size:86px;">Coment&aacute; <span class="hl">QUERY</span> y<br>te mando la <span style="font-family:var(--mono);font-weight:600;">gu&iacute;a</span></h1>
  <div class="sub" style="margin:30px auto 0;text-align:center;">La ficha t&eacute;cnica completa, los ejemplos
   y <b>cu&aacute;ndo conviene usarlo</b>, en un solo recurso.</div>
  <div style="margin-top:46px;"><span class="pill12">Link en el perfil</span></div>
</div>
<div style="position:absolute;left:50%;transform:translateX(-50%);top:876px;z-index:5;">{robot("query", 300)}</div>
<div class="share nav-l" style="left:84px;">&#10148; Compartilo con tus colegas</div>
<div class="share nav-r" style="right:84px;">Guardalo</div>
''')

slides = [chrome(i + 1, inner, total=12, bridges=None, footer=True) for i, inner in enumerate(S)]
write_html(slides, f"{BUILD}/carrusel.html", extra_css=CSS)
print(f"HTML escrito: {BUILD}/carrusel.html — {len(slides)} slides")
