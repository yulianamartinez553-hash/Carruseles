# -*- coding: utf-8 -*-
"""
Carrusel panorámico continuo STLabs — Claude × WhatsApp × Multinivel
4 slides · reticula_fina · dossier_editorial · continuidad gráfica + copy voseo
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import embedded_fonts_css

N = 4
W = 1080
H = 1350
PANO_W = N * W


def b64(path: Path, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


URI_SEB = b64(REPO / "seb.jpg", "image/jpeg")

# Claude mark — naranja Anthropic (regla: logo Claude siempre naranja)
CLAUDE_SVG = (
    "data:image/svg+xml,"
    + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    + "%3Crect width='64' height='64' rx='14' fill='%23D97757'/%3E"
    + "%3Cpath fill='%23fff' d='M32 14c-2.2 8.4-6.8 14.2-14 18 7.2 3.8 11.8 9.6 14 18 "
    + "2.2-8.4 6.8-14.2 14-18-7.2-3.8-11.8-9.6-14-18z'/%3E%3C/svg%3E"
)

EXTRA_CSS = f"""
:root{{
  --verde:#00FFB2;--neg:#0A0A0A;--blanco:#F2F2F2;--gray:#9aa39c;
  --claude:#D97757;
  --mono:'IBM Plex Mono',monospace;
  --cond:'Barlow Condensed',sans-serif;
  --disp:'Bebas Neue',sans-serif;
  --pop:'Poppins',sans-serif;
  --serif:'Lora',serif;
}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:40px;padding:40px;background:#000;}}
.slide{{
  position:relative;width:{W}px;height:{H}px;overflow:hidden;
  background:var(--neg);color:var(--blanco);
}}

.pano{{
  position:absolute;top:0;left:0;width:{PANO_W}px;height:{H}px;z-index:1;
  pointer-events:none;
}}
.s1 .pano{{transform:translateX(0);}}
.s2 .pano{{transform:translateX(-{W}px);}}
.s3 .pano{{transform:translateX(-{2*W}px);}}
.s4 .pano{{transform:translateX(-{3*W}px);}}

.pano-base{{
  position:absolute;inset:0;
  background:
    radial-gradient(36% 42% at 18% 22%, rgba(0,255,178,.09), transparent 62%),
    radial-gradient(40% 36% at 72% 78%, rgba(0,255,178,.06), transparent 65%),
    radial-gradient(50% 50% at 48% 48%, #121212, transparent 70%),
    linear-gradient(112deg, #0c0c0c 0%, #080808 42%, #0b0b0b 68%, #0a0a0a 100%);
}}
.pano-grid{{
  position:absolute;inset:0;opacity:.5;z-index:1;
  background-image:
    linear-gradient(rgba(255,255,255,.022) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.022) 1px, transparent 1px);
  background-size:60px 60px;
}}
.pano-noise{{
  position:absolute;inset:0;opacity:.38;mix-blend-mode:overlay;z-index:1;pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.5'/%3E%3C/svg%3E");
}}
.shadow-band{{
  position:absolute;height:380px;width:170%;left:-12%;z-index:2;
  background:linear-gradient(180deg, rgba(255,255,255,.035), rgba(255,255,255,.01) 50%, transparent);
  transform-origin:left center;
}}
.sb-a{{top:60px;transform:rotate(-16deg);}}
.sb-b{{top:480px;transform:rotate(-16deg);opacity:.7;}}
.sb-c{{top:920px;transform:rotate(-16deg);opacity:.45;}}
.beam{{
  position:absolute;left:-220px;top:40px;width:4800px;height:220px;z-index:2;
  background:linear-gradient(180deg, rgba(0,255,178,0), rgba(0,255,178,.10) 42%, rgba(0,255,178,.03) 72%, transparent);
  transform:rotate(12.6deg);transform-origin:left center;filter:blur(22px);
}}
.diag-master{{
  position:absolute;left:-100px;top:150px;width:4600px;height:5px;z-index:8;
  background:linear-gradient(90deg, rgba(0,255,178,0), #00FFB2 8%, #00FFB2 92%, rgba(0,255,178,0));
  transform:rotate(12.6deg);transform-origin:left center;
  box-shadow:0 0 26px rgba(0,255,178,.55);border-radius:3px;
}}
.diag-thin{{
  position:absolute;left:-60px;top:220px;width:4550px;height:1.5px;z-index:8;
  background:linear-gradient(90deg, transparent, rgba(0,255,178,.65) 10%, rgba(0,255,178,.4) 90%, transparent);
  transform:rotate(12.6deg);transform-origin:left center;
}}
.diag-ghost{{
  position:absolute;left:80px;top:70px;width:4400px;height:1px;z-index:7;
  background:linear-gradient(90deg, transparent, rgba(255,255,255,.14) 20%, transparent);
  transform:rotate(12.6deg);transform-origin:left center;
}}
.cable{{
  position:absolute;left:160px;top:1090px;width:4100px;height:1.5px;z-index:7;
  background:linear-gradient(90deg, transparent, rgba(255,255,255,.2) 10%, rgba(0,255,178,.3) 50%, transparent);
  transform:rotate(-2.8deg);transform-origin:left center;
}}
.metal-rail{{
  position:absolute;left:20px;top:1195px;width:4300px;height:12px;z-index:9;
  background:linear-gradient(180deg,#5a5e64 0%,#22252a 32%,#0a0b0c 58%,#3a3e44 100%);
  box-shadow:0 10px 28px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.28);
}}
.metal-rail::after{{
  content:'';position:absolute;left:0;right:0;top:3px;height:2px;
  background:linear-gradient(90deg, transparent, rgba(0,255,178,.65) 20%, transparent);
}}
.ticks{{position:absolute;left:60px;top:1176px;width:4220px;height:12px;z-index:10;display:flex;gap:46px;}}
.ticks i{{display:block;width:2px;height:10px;background:rgba(255,255,255,.22);}}
.ticks i:nth-child(5n){{background:#00FFB2;height:14px;box-shadow:0 0 8px rgba(0,255,178,.55);}}
.anchor{{
  position:absolute;width:16px;height:16px;border-radius:50%;z-index:11;
  background:#0A0A0A;border:2px solid #00FFB2;box-shadow:0 0 18px rgba(0,255,178,.65);
}}
.a1{{left:900px;top:368px;}}
.a2{{left:1960px;top:605px;}}
.a3{{left:3020px;top:842px;}}
.a4{{left:3900px;top:1040px;}}

.glass{{
  position:absolute;border-radius:16px;z-index:6;overflow:hidden;
  background:linear-gradient(145deg, rgba(255,255,255,.09), rgba(255,255,255,.02) 38%, rgba(0,255,178,.04));
  border:1px solid rgba(255,255,255,.12);
  box-shadow:0 28px 60px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.18);
}}
.glass::before{{
  content:'';position:absolute;inset:0;
  background:linear-gradient(118deg, rgba(255,255,255,.16) 0%, transparent 26%, transparent 70%, rgba(0,255,178,.10) 100%);
}}
.g1{{left:60px;top:160px;width:360px;height:420px;transform:rotate(-7deg);opacity:.55;}}
.g2{{left:1180px;top:70px;width:280px;height:220px;transform:rotate(5deg);opacity:.5;}}
.g3{{left:2280px;top:100px;width:260px;height:300px;transform:rotate(-3deg);opacity:.45;}}
.g4{{left:3400px;top:160px;width:420px;height:520px;transform:rotate(-4deg);opacity:.7;}}
.g5{{left:3860px;top:580px;width:300px;height:240px;transform:rotate(6deg);opacity:.65;}}

.plate{{
  position:absolute;z-index:6;border-radius:10px;
  background:linear-gradient(160deg,#4a4e54 0%,#1b1d20 40%,#0b0c0e 70%,#2a2e33 100%);
  box-shadow:0 24px 48px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.25);
}}
.p1{{left:480px;top:900px;width:220px;height:130px;transform:rotate(11deg);opacity:.7;}}
.p2{{left:2500px;top:160px;width:190px;height:110px;transform:rotate(-12deg);}}
.p3{{left:3600px;top:900px;width:260px;height:120px;transform:rotate(-6deg);}}
.plate .edge{{
  position:absolute;left:12px;right:12px;top:14px;height:3px;border-radius:2px;
  background:linear-gradient(90deg, #00FFB2, rgba(0,255,178,.12));
  box-shadow:0 0 12px rgba(0,255,178,.5);
}}
.block{{position:absolute;z-index:5;}}
.b1{{
  left:160px;top:1020px;width:130px;height:130px;transform:skewY(-8deg);
  background:linear-gradient(135deg,#2e3238,#121416);
  box-shadow:14px 16px 0 rgba(0,255,178,.07), 0 24px 40px rgba(0,0,0,.5);
}}
.b2{{
  left:2140px;top:1000px;width:100px;height:160px;transform:skewY(-8deg);
  background:linear-gradient(135deg,#1a1d22,#070809);
}}
.b3{{
  left:3480px;top:90px;width:78px;height:78px;transform:rotate(18deg);
  background:linear-gradient(135deg,#00FFB2,#009e6e);
  box-shadow:0 18px 40px rgba(0,255,178,.4);
}}
.ring{{
  position:absolute;border-radius:50%;border:1.5px solid rgba(0,255,178,.3);z-index:5;
}}
.r1{{left:620px;top:420px;width:220px;height:220px;opacity:.5;}}
.r2{{left:1680px;top:760px;width:320px;height:320px;border-color:rgba(255,255,255,.08);}}
.r3{{left:3700px;top:420px;width:280px;height:280px;}}

/* ── iMac realista CSS (puente continuo slides 1↔2) — sin imagen del repo ── */
.imac-wrap{{
  position:absolute;left:680px;top:380px;width:820px;height:860px;z-index:14;
  transform:perspective(2400px) rotateY(-14deg) rotateX(5deg) rotateZ(-1deg);
  transform-origin:center bottom;
  filter:drop-shadow(0 60px 80px rgba(0,0,0,.82));
}}
.imac{{position:relative;width:100%;height:100%;}}
.imac-body{{
  position:relative;width:700px;margin:0 auto;
}}
.imac-edge{{
  position:absolute;top:10px;right:-10px;width:12px;height:470px;
  border-radius:0 10px 10px 0;
  background:linear-gradient(180deg,#f4f5f7 0%,#9aa0a6 35%,#5c6168 70%,#c9ccd1 100%);
  box-shadow:2px 0 8px rgba(0,0,0,.35);
}}
.imac-bezel{{
  position:relative;width:100%;
  padding:16px 16px 0;
  border-radius:26px 26px 4px 4px;
  background:
    linear-gradient(145deg, rgba(255,255,255,.55) 0%, transparent 28%),
    linear-gradient(160deg,#f3f4f6 0%,#c2c6cb 16%,#8a8f96 40%,#bec0c4 62%,#e9ebef 88%,#f7f8fa 100%);
  box-shadow:
    inset 0 2px 0 rgba(255,255,255,.9),
    inset 0 -2px 0 rgba(0,0,0,.18),
    inset 2px 0 0 rgba(255,255,255,.35),
    inset -2px 0 0 rgba(0,0,0,.12),
    0 0 0 1px rgba(30,30,30,.45);
}}
.imac-screen{{
  position:relative;width:100%;height:448px;border-radius:8px;overflow:hidden;
  background:#030405;
  box-shadow:
    inset 0 0 0 2px #0a0a0a,
    inset 0 0 40px rgba(0,0,0,.85),
    0 0 40px rgba(0,255,178,.08);
}}
.imac-ui{{
  position:absolute;inset:0;display:grid;
  grid-template-columns:78px 1.05fr 1fr;gap:0;
  background:
    radial-gradient(70% 55% at 75% 18%, rgba(0,255,178,.07), transparent 55%),
    linear-gradient(165deg,#0c100e 0%,#070807 48%,#050505 100%);
}}
.imac-side{{
  background:linear-gradient(180deg,#101411,#080a09);
  border-right:1px solid #1c221e;
  padding:20px 0;display:flex;flex-direction:column;align-items:center;gap:16px;
}}
.imac-side i{{
  display:block;width:30px;height:30px;border-radius:9px;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);
}}
.imac-side i.on{{
  background:rgba(0,255,178,.2);border-color:rgba(0,255,178,.6);
  box-shadow:0 0 16px rgba(0,255,178,.4);
}}
.imac-mid{{padding:18px 14px;display:flex;flex-direction:column;gap:11px;}}
.imac-row{{
  height:48px;border-radius:11px;background:#121612;border:1px solid #1f2621;
  position:relative;overflow:hidden;
}}
.imac-row::after{{
  content:'';position:absolute;left:14px;top:18px;width:42%;height:10px;border-radius:5px;
  background:rgba(255,255,255,.08);
}}
.imac-row.tall{{height:132px;}}
.imac-row.tall::after{{display:none;}}
.imac-wave{{
  position:absolute;left:10px;right:10px;bottom:12px;height:72px;
  background:
    linear-gradient(180deg, transparent 35%, rgba(0,255,178,.12)),
    radial-gradient(55% 80% at 18% 72%, rgba(0,255,178,.65), transparent 58%),
    radial-gradient(48% 70% at 48% 38%, rgba(0,255,178,.45), transparent 55%),
    radial-gradient(42% 65% at 82% 68%, rgba(0,255,178,.55), transparent 55%);
  border-bottom:2px solid rgba(0,255,178,.65);opacity:.95;
  filter:drop-shadow(0 0 10px rgba(0,255,178,.25));
}}
.imac-right{{padding:18px 14px;display:flex;flex-direction:column;gap:12px;}}
.imac-donut{{
  width:92px;height:92px;border-radius:50%;margin:4px auto 0;
  background:conic-gradient(from -40deg, #00FFB2 0 72%, #1a1f1c 72% 100%);
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 28px rgba(0,255,178,.3), inset 0 0 0 1px rgba(0,255,178,.2);
}}
.imac-donut span{{
  width:52px;height:52px;border-radius:50%;background:#080a09;
  display:flex;align-items:center;justify-content:center;
  font-family:var(--mono);font-size:14px;color:#00FFB2;font-weight:600;
}}
.imac-bars{{display:flex;align-items:flex-end;gap:7px;height:78px;padding:0 6px;}}
.imac-bars b{{
  flex:1;border-radius:4px 4px 0 0;
  background:linear-gradient(180deg,#6dffd0,#00FFB2 40%,#007a52);
  box-shadow:0 0 12px rgba(0,255,178,.3);
}}
.imac-bars b:nth-child(1){{height:32%;opacity:.5;}}
.imac-bars b:nth-child(2){{height:55%;opacity:.7;}}
.imac-bars b:nth-child(3){{height:88%;}}
.imac-bars b:nth-child(4){{height:44%;opacity:.65;}}
.imac-bars b:nth-child(5){{height:70%;opacity:.85;}}
.imac-wa{{
  margin-top:auto;border-radius:14px;padding:12px;
  background:linear-gradient(145deg,#102018,#0a120e);
  border:1px solid rgba(37,211,102,.4);
  box-shadow:0 0 18px rgba(37,211,102,.12);
}}
.imac-wa .line{{
  height:8px;border-radius:4px;background:rgba(255,255,255,.07);margin-bottom:8px;
}}
.imac-wa .line.g{{width:64%;background:rgba(0,255,178,.4);}}
.imac-wa .line.s{{width:42%;background:rgba(37,211,102,.45);}}
.imac-glare{{
  position:absolute;inset:0;pointer-events:none;z-index:3;
  background:
    linear-gradient(115deg, rgba(255,255,255,.22) 0%, rgba(255,255,255,0) 18%, transparent 55%, rgba(255,255,255,.05) 100%),
    radial-gradient(40% 30% at 80% 10%, rgba(0,255,178,.08), transparent 70%);
}}
.imac-chin{{
  height:56px;display:flex;align-items:center;justify-content:center;position:relative;
  background:
    linear-gradient(180deg, rgba(255,255,255,.35) 0%, transparent 40%),
    linear-gradient(180deg,#e4e6ea 0%,#a8adb4 48%,#d5d8dd 100%);
  border-radius:0 0 6px 6px;
}}
.imac-cam{{
  width:9px;height:9px;border-radius:50%;
  background:radial-gradient(circle at 35% 28%,#4a5562,#0b0d10 68%);
  box-shadow:0 0 0 3px rgba(0,0,0,.18), inset 0 0 2px #7a8899;
}}
.imac-logo{{
  position:absolute;bottom:10px;left:50%;transform:translateX(-50%);
  width:18px;height:18px;opacity:.28;
  background:radial-gradient(circle at 40% 35%,#555,#222);
  border-radius:50%;
}}
.imac-neck{{
  width:98px;height:78px;margin:-1px auto 0;
  background:
    linear-gradient(90deg, transparent 0%, rgba(255,255,255,.35) 35%, transparent 55%),
    linear-gradient(90deg,#5a5e64 0%,#d8dade 26%,#8e9399 50%,#eef0f2 76%,#4e5258 100%);
  clip-path:polygon(30% 0, 70% 0, 100% 100%, 0 100%);
  box-shadow:inset 0 0 14px rgba(0,0,0,.28);
}}
.imac-base{{
  position:relative;width:300px;height:16px;margin:0 auto;
  border-radius:0 0 48% 48% / 0 0 100% 100%;
  background:linear-gradient(180deg,#f5f6f8 0%,#b0b4ba 38%,#6a6f75 100%);
  box-shadow:
    0 10px 22px rgba(0,0,0,.5),
    inset 0 1px 0 rgba(255,255,255,.75);
}}
.imac-base::after{{
  content:'';position:absolute;left:50%;bottom:-10px;transform:translateX(-50%);
  width:240px;height:10px;border-radius:50%;
  background:rgba(0,0,0,.35);filter:blur(6px);
}}
.imac-kb{{
  position:absolute;left:90px;bottom:48px;width:520px;height:28px;z-index:12;
  border-radius:6px;
  background:
    linear-gradient(180deg,#3a3d42 0%,#1a1c1f 45%,#2c2f34 100%);
  box-shadow:
    0 14px 28px rgba(0,0,0,.55),
    inset 0 1px 0 rgba(255,255,255,.12);
  transform:perspective(800px) rotateX(55deg);
  transform-origin:center top;
}}
.imac-kb::before{{
  content:'';position:absolute;inset:4px 8px;border-radius:3px;
  background:repeating-linear-gradient(90deg,
    rgba(255,255,255,.06) 0 10px,
    transparent 10px 14px);
  opacity:.55;
}}
.imac-pad{{
  position:absolute;left:280px;bottom:18px;width:140px;height:22px;z-index:11;
  border-radius:8px;
  background:linear-gradient(180deg,#2a2d31,#121416);
  box-shadow:0 10px 20px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.1);
  transform:perspective(700px) rotateX(50deg);
}}
.imac-cursor{{
  position:absolute;right:95px;bottom:250px;width:58px;height:58px;z-index:16;
  filter:drop-shadow(0 12px 16px rgba(0,0,0,.6));
  transform:rotate(-10deg);
}}
.imac-cursor svg{{width:100%;height:100%;display:block;}}

.obj-portrait{{
  position:absolute;left:2000px;top:980px;width:160px;height:160px;z-index:13;
  border-radius:50%;overflow:hidden;border:3px solid #00FFB2;
  box-shadow:0 0 0 8px rgba(0,255,178,.08), 0 20px 40px rgba(0,0,0,.55), 0 0 28px rgba(0,255,178,.35);
}}
.obj-portrait img{{width:100%;height:100%;object-fit:cover;filter:grayscale(.2) contrast(1.06) brightness(.92);}}

.chip{{
  position:absolute;z-index:11;border-radius:12px;overflow:hidden;
  border:1px solid rgba(255,255,255,.14);box-shadow:0 20px 40px rgba(0,0,0,.5);
}}
.chip img{{width:100%;height:100%;object-fit:cover;filter:brightness(.55) contrast(1.08) saturate(.7);}}
.chip-a{{left:200px;top:700px;width:150px;height:180px;transform:rotate(-6deg);opacity:.85;}}

.orb{{
  position:absolute;border-radius:50%;z-index:4;filter:blur(40px);
  background:radial-gradient(circle, rgba(0,255,178,.35), transparent 70%);
}}
.o1{{left:700px;top:180px;width:220px;height:220px;}}
.o2{{left:2500px;top:900px;width:240px;height:240px;opacity:.65;}}
.o3{{left:3800px;top:260px;width:240px;height:240px;}}

/* ── Copy overlays (por slide) ── */
.copy{{position:absolute;inset:0;z-index:20;pointer-events:none;}}
.copy *{{pointer-events:none;}}
.kicker{{
  font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--verde);
  text-transform:uppercase;margin-bottom:18px;
}}
.h-bebas{{
  font-family:var(--disp);font-weight:400;line-height:.88;color:#fff;
  text-align:left;letter-spacing:1px;
}}
.h-pop{{
  font-family:var(--pop);font-weight:800;line-height:1.05;color:#fff;text-align:left;
}}
.body{{
  font-family:var(--cond);font-weight:500;font-size:34px;line-height:1.28;color:var(--gray);
  text-align:left;max-width:860px;
}}
.body b,.body .w{{color:#fff;font-weight:700;}}
.body .gr{{color:var(--verde);font-weight:600;}}
.ac{{font-family:var(--serif);font-style:italic;font-weight:600;color:var(--verde);}}

/* Slide 1 */
.s1-box{{position:absolute;left:72px;right:72px;top:88px;z-index:21;}}
.s1-box .h-bebas{{font-size:118px;max-width:920px;}}
.s1-box .h-bebas .gr{{color:var(--verde);}}
.s1-box .body{{margin-top:28px;font-size:36px;max-width:680px;}}
.s1-scrim{{
  position:absolute;left:0;right:0;top:0;height:520px;z-index:15;pointer-events:none;
  background:linear-gradient(180deg, rgba(7,7,7,.72) 0%, rgba(7,7,7,.35) 55%, transparent 100%);
}}

/* Slide 2 */
.s2-box{{position:absolute;left:400px;right:72px;top:72px;z-index:21;}}
.s2-box .h-pop{{font-size:58px;max-width:620px;}}
.s2-box .body{{margin-top:22px;font-size:33px;max-width:600px;}}
.s2-box .body + .body{{margin-top:16px;}}
.claude-row{{
  display:flex;align-items:center;gap:18px;margin-top:28px;
}}
.claude-mark{{
  width:64px;height:64px;border-radius:14px;overflow:hidden;
  box-shadow:0 12px 28px rgba(217,119,87,.45);
}}
.claude-mark img{{width:100%;height:100%;display:block;}}
.claude-lab{{
  font-family:var(--mono);font-size:22px;color:var(--claude);letter-spacing:1px;
}}
.s2-scrim{{
  position:absolute;left:42%;right:0;top:0;height:520px;z-index:15;pointer-events:none;
  background:linear-gradient(270deg, rgba(7,7,7,.65) 0%, rgba(7,7,7,.25) 60%, transparent 100%);
}}

/* Slide 3 */
.s3-box{{position:absolute;left:64px;right:64px;top:64px;z-index:21;}}
.s3-box .h-pop{{font-size:48px;max-width:920px;}}
.bullets{{margin-top:22px;display:flex;flex-direction:column;gap:10px;max-width:980px;}}
.bullets li{{
  list-style:none;display:flex;gap:14px;align-items:flex-start;
  font-family:var(--cond);font-size:28px;line-height:1.2;color:var(--blanco);
}}
.bullets li::before{{
  content:'';flex:0 0 10px;height:10px;margin-top:10px;border-radius:50%;
  background:var(--verde);box-shadow:0 0 10px rgba(0,255,178,.55);
}}
.chat{{
  margin-top:22px;width:100%;max-width:980px;
  background:#0e1410;border:1px solid rgba(0,255,178,.22);border-radius:22px;
  padding:18px 18px 16px;box-shadow:0 24px 48px rgba(0,0,0,.45);
}}
.chat-head{{
  display:flex;align-items:center;gap:12px;margin-bottom:14px;
  font-family:var(--mono);font-size:16px;color:var(--verde);letter-spacing:1px;
}}
.chat-dot{{width:10px;height:10px;border-radius:50%;background:#25D366;box-shadow:0 0 8px rgba(37,211,102,.6);}}
.msg{{display:flex;margin-bottom:10px;}}
.msg.me{{justify-content:flex-end;}}
.msg.bot{{justify-content:flex-start;}}
.bubble{{
  max-width:78%;padding:12px 16px;border-radius:16px;
  font-family:var(--cond);font-size:24px;line-height:1.25;
}}
.msg.me .bubble{{background:#005c4b;color:#eafff6;border-bottom-right-radius:5px;}}
.msg.bot .bubble{{background:#1a1f1c;color:#e8eee9;border:1px solid #2a332e;border-bottom-left-radius:5px;}}
.bubble .who{{display:block;font-family:var(--mono);font-size:13px;color:var(--verde);margin-bottom:4px;letter-spacing:1px;}}
.desliza{{
  margin-top:14px;text-align:right;
  font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--verde);
}}
.s3-scrim{{
  position:absolute;inset:0;z-index:15;pointer-events:none;
  background:linear-gradient(180deg, rgba(7,7,7,.82) 0%, rgba(7,7,7,.55) 48%, rgba(7,7,7,.75) 100%);
}}

/* Slide 4 CTA */
.s4-box{{
  position:absolute;left:72px;right:72px;top:160px;z-index:21;
  display:flex;flex-direction:column;align-items:flex-start;
}}
.s4-box .h-pop{{font-size:56px;max-width:920px;}}
.s4-box .h-pop .gr{{color:var(--verde);}}
.s4-box .body{{margin-top:28px;font-size:34px;max-width:860px;}}
.cta-pill{{
  margin-top:40px;display:inline-flex;align-items:center;gap:14px;
  background:rgba(0,255,178,.1);border:1.5px solid rgba(0,255,178,.65);
  border-radius:999px;padding:18px 34px;
  font-family:var(--pop);font-weight:800;font-size:36px;color:var(--verde);
  box-shadow:0 0 30px rgba(0,255,178,.25);
}}
.cta-pill span{{
  font-family:var(--mono);font-weight:600;font-size:28px;letter-spacing:2px;
  color:#04130b;background:var(--verde);border-radius:10px;padding:8px 14px;
}}
.s4-scrim{{
  position:absolute;inset:0;z-index:15;pointer-events:none;
  background:radial-gradient(60% 50% at 40% 35%, rgba(7,7,7,.35), rgba(7,7,7,.78) 70%);
}}

.web{{
  position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:30;
  font-family:var(--mono);font-size:25px;letter-spacing:2px;color:#00FFB2;
  text-shadow:0 0 20px rgba(0,255,178,.35);opacity:.95;
}}
"""


def pano_html() -> str:
    ticks = "".join("<i></i>" for _ in range(90))
    return f"""
<div class="pano-base"></div>
<div class="pano-grid"></div>
<div class="pano-noise"></div>
<div class="shadow-band sb-a"></div>
<div class="shadow-band sb-b"></div>
<div class="shadow-band sb-c"></div>
<div class="beam"></div>
<div class="orb o1"></div>
<div class="orb o2"></div>
<div class="orb o3"></div>
<div class="diag-ghost"></div>
<div class="diag-master"></div>
<div class="diag-thin"></div>
<div class="cable"></div>
<div class="metal-rail"></div>
<div class="ticks">{ticks}</div>
<span class="anchor a1"></span>
<span class="anchor a2"></span>
<span class="anchor a3"></span>
<span class="anchor a4"></span>
<div class="glass g1"></div>
<div class="glass g2"></div>
<div class="glass g3"></div>
<div class="glass g4"></div>
<div class="glass g5"></div>
<div class="plate p1"><span class="edge"></span></div>
<div class="plate p2"><span class="edge"></span></div>
<div class="plate p3"><span class="edge"></span></div>
<div class="block b1"></div>
<div class="block b2"></div>
<div class="block b3"></div>
<div class="ring r1"></div>
<div class="ring r2"></div>
<div class="ring r3"></div>
<div class="chip chip-a"><img src="{URI_SEB}" alt=""></div>
<div class="imac-wrap">
  <div class="imac">
    <div class="imac-body">
      <div class="imac-edge"></div>
      <div class="imac-bezel">
        <div class="imac-screen">
          <div class="imac-ui">
            <div class="imac-side">
              <i class="on"></i><i></i><i></i><i></i><i></i>
            </div>
            <div class="imac-mid">
              <div class="imac-row"></div>
              <div class="imac-row tall"><div class="imac-wave"></div></div>
              <div class="imac-row"></div>
              <div class="imac-wa">
                <div class="line g"></div>
                <div class="line s"></div>
                <div class="line"></div>
              </div>
            </div>
            <div class="imac-right">
              <div class="imac-donut"><span>68%</span></div>
              <div class="imac-bars"><b></b><b></b><b></b><b></b><b></b></div>
              <div class="imac-row"></div>
            </div>
          </div>
          <div class="imac-glare"></div>
        </div>
        <div class="imac-chin">
          <div class="imac-cam"></div>
          <div class="imac-logo"></div>
        </div>
      </div>
      <div class="imac-neck"></div>
      <div class="imac-base"></div>
    </div>
    <div class="imac-kb"></div>
    <div class="imac-pad"></div>
    <div class="imac-cursor">
      <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="cg" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#f5f6f8"/>
            <stop offset="100%" stop-color="#9aa0a6"/>
          </linearGradient>
        </defs>
        <path fill="url(#cg)" stroke="#1a1a1a" stroke-width="2.2"
          d="M12 8 L12 50 L25 39 L34 58 L42 54 L31 35 L50 35 Z"/>
      </svg>
    </div>
  </div>
</div>
<div class="obj-portrait"><img src="{URI_SEB}" alt=""></div>
"""


def slide1() -> str:
    return f"""
<section class="slide s1">
  <div class="pano">{pano_html()}</div>
  <div class="s1-scrim"></div>
  <div class="copy s1-box">
    <div class="kicker">WhatsApp · Claude · Multinivel</div>
    <h1 class="h-bebas">ÚLTIMO<br><span class="gr">MOMENTO</span></h1>
    <p class="body">Ahora podés usar <span class="gr">Claude</span> directo desde WhatsApp,
    y dejar de ser <b>vos</b> el que contesta todo en tu multinivel.</p>
  </div>
  <div class="web">sebastian.stlabs.ar</div>
</section>
"""


def slide2() -> str:
    return f"""
<section class="slide s2">
  <div class="pano">{pano_html()}</div>
  <div class="s2-scrim"></div>
  <div class="copy s2-box">
    <div class="kicker">100% oficial</div>
    <h2 class="h-pop">Ya es <span class="ac">100% oficial</span></h2>
    <p class="body">Podés conectar <b>Claude</b> a tu WhatsApp y darle todo el
    trabajo operativo de tu red multinivel.</p>
    <p class="body">Y ponerlo a trabajar como un <span class="gr">miembro más</span>
    de tu equipo.</p>
    <div class="claude-row">
      <div class="claude-mark"><img src="{CLAUDE_SVG}" alt="Claude"></div>
      <div class="claude-lab">Claude · conectado</div>
    </div>
  </div>
  <div class="web">sebastian.stlabs.ar</div>
</section>
"""


def slide3() -> str:
    return f"""
<section class="slide s3">
  <div class="pano">{pano_html()}</div>
  <div class="s3-scrim"></div>
  <div class="copy s3-box">
    <h2 class="h-pop">¿Qué puede hacer<br>por tu <span class="ac">multinivel</span>?</h2>
    <ul class="bullets">
      <li>Publicar tu contenido sin que vos abras Instagram.</li>
      <li>Manejar los grupos de WhatsApp de tu equipo.</li>
      <li>Recordarle a tu red sus tareas, sus citas y sus cierres.</li>
      <li>Armarte la landing de tu próximo evento o registro.</li>
      <li>Programarte lo que necesites, aunque no sepas programar.</li>
      <li>Y todo lo que ya hacías con Claude, ahora desde WhatsApp.</li>
    </ul>
    <div class="chat">
      <div class="chat-head"><span class="chat-dot"></span> WhatsApp · Claude en tu red</div>
      <div class="msg me"><div class="bubble"><span class="who">RAFA</span>
        Publicá el carrusel de hoy y recordale la junta a mi equipo</div></div>
      <div class="msg bot"><div class="bubble"><span class="who">CLAUDE</span>
        Listo. Publicado y recordatorio enviado a los 14 del grupo · 13:30</div></div>
      <div class="msg me"><div class="bubble"><span class="who">RAFA</span>
        ¿Le doy seguimiento a los 3 que no contestaron?</div></div>
      <div class="msg bot"><div class="bubble"><span class="who">CLAUDE</span>
        Sí. ¿Arranco el seguimiento ahora?</div></div>
    </div>
    <div class="desliza">DESLIZÁ →</div>
  </div>
  <div class="web">sebastian.stlabs.ar</div>
</section>
"""


def slide4() -> str:
    return f"""
<section class="slide s4">
  <div class="pano">{pano_html()}</div>
  <div class="s4-scrim"></div>
  <div class="copy s4-box">
    <div class="kicker">Manual · Claude × WhatsApp</div>
    <h2 class="h-pop">Manual completo de<br>conexión de Claude con<br><span class="gr">WhatsApp</span><br>
    <span style="font-size:42px;color:#9aa39c;font-weight:700;">para tu multinivel</span></h2>
    <p class="body">Comentá <b class="gr">PDF</b> y te mando el manual completo
    con el que conecté Claude a mi WhatsApp y se lo pasé a mi equipo.</p>
    <div class="cta-pill">Comentá <span>PDF</span></div>
  </div>
  <div class="web">sebastian.stlabs.ar</div>
</section>
"""


def main():
    slides = [slide1(), slide2(), slide3(), slide4()]
    html = (
        '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
        f"<style>{embedded_fonts_css()}{EXTRA_CSS}</style></head>"
        f'<body><div class="sheet">{"".join(slides)}</div></body></html>'
    )
    out = BUILD / "carrusel.html"
    out.write_text(html, encoding="utf-8")
    print(f"✓ HTML escrito: {out} ({out.stat().st_size // 1024} KB)")
    return out


if __name__ == "__main__":
    main()
