# -*- coding: utf-8 -*-
"""Render a clean Space Gray MacBook Pro — product shot, code flush on screen."""
from __future__ import annotations

import base64
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
CODE = Path("/tmp/code_hires.png")
OUT = HERE / "macbook-code.png"


def b64(path: Path) -> str:
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


HTML = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  html,body{{
    margin:0;padding:0;background:transparent;
    width:1800px;height:1400px;overflow:hidden;
  }}
  .stage{{
    width:1800px;height:1400px;
    display:flex;align-items:center;justify-content:center;
    background:transparent;
    perspective:1800px;
    perspective-origin:50% 40%;
  }}
  .laptop{{
    position:relative;
    width:1100px;height:820px;
    transform-style:preserve-3d;
    /* Vista producto: ligeramente desde arriba y a la derecha */
    transform: rotateX(28deg) rotateY(-22deg) rotateZ(-6deg) scale(1.02);
    filter: drop-shadow(0 60px 80px rgba(0,0,0,.65));
  }}

  /* ── LID ── */
  .lid{{
    position:absolute;left:90px;top:20px;width:920px;height:560px;
    transform-style:preserve-3d;
  }}
  .lid-back{{
    position:absolute;inset:0;
    border-radius:22px 22px 8px 8px;
    background:linear-gradient(165deg,#4a4e56 0%,#32363c 45%,#22252a 100%);
    box-shadow:
      inset 0 1px 0 rgba(255,255,255,.25),
      inset 0 -1px 0 rgba(0,0,0,.45),
      0 1px 2px rgba(0,0,0,.4);
  }}
  .bezel{{
    position:absolute;left:16px;top:14px;right:16px;bottom:36px;
    border-radius:12px;
    background:#030405;
    overflow:hidden;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,.05);
  }}
  .cam{{
    position:absolute;left:50%;top:5px;width:9px;height:9px;margin-left:-4.5px;z-index:4;
    border-radius:50%;background:#0c0d0f;
    box-shadow: inset 0 0 0 1.5px #1a1c20, 0 0 0 1px #050505;
  }}
  .cam i{{
    position:absolute;left:3px;top:3px;width:3px;height:3px;border-radius:50%;background:#163040;
  }}
  .screen{{
    position:absolute;inset:0;background:#07090c;overflow:hidden;
  }}
  .screen img{{
    width:100%;height:100%;object-fit:cover;display:block;
    filter:contrast(1.05) saturate(1.06) brightness(1.03);
  }}
  .glass{{
    position:absolute;inset:0;pointer-events:none;z-index:2;
    background:linear-gradient(125deg,
      rgba(255,255,255,.09) 0%,
      rgba(255,255,255,.02) 28%,
      rgba(255,255,255,0) 52%,
      rgba(0,0,0,.18) 100%);
  }}
  .chin{{
    position:absolute;left:0;right:0;bottom:10px;height:20px;
    display:flex;align-items:center;justify-content:center;
    font:600 12px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    letter-spacing:.28em;color:rgba(190,195,200,.5);text-transform:uppercase;
  }}

  /* ── BASE ── */
  .base{{
    position:absolute;left:40px;top:565px;width:1020px;height:210px;
    transform-style:preserve-3d;
  }}
  .deck{{
    position:absolute;inset:0;
    border-radius:6px 6px 16px 16px;
    background:
      linear-gradient(180deg,#565b64 0%,#3d4148 14%,#2f3339 50%,#262a30 100%);
    box-shadow:
      inset 0 1px 0 rgba(255,255,255,.28),
      inset 0 -3px 0 rgba(0,0,0,.35),
      0 10px 24px rgba(0,0,0,.4);
  }}
  .hinge{{
    position:absolute;left:100px;top:-8px;width:820px;height:12px;
    border-radius:5px;
    background:linear-gradient(180deg,#1c1e22,#383c43 45%,#1c1e22);
    box-shadow:0 1px 0 rgba(255,255,255,.1);
  }}
  .kb{{
    position:absolute;left:78px;top:22px;right:78px;height:88px;
    border-radius:6px;
    background:#1b1e23;
    box-shadow: inset 0 0 0 1px rgba(0,0,0,.5), inset 0 3px 10px rgba(0,0,0,.4);
    overflow:hidden;
    padding:6px 8px;
    display:grid;
    grid-template-rows:repeat(5,1fr);
    gap:3px;
  }}
  .kb-row{{
    display:grid;gap:3px;height:100%;
  }}
  .kb-row:nth-child(1){{grid-template-columns:repeat(14,1fr);}}
  .kb-row:nth-child(2){{grid-template-columns:1.4fr repeat(12,1fr) 1.6fr;}}
  .kb-row:nth-child(3){{grid-template-columns:1.7fr repeat(11,1fr) 1.9fr;}}
  .kb-row:nth-child(4){{grid-template-columns:2.1fr repeat(10,1fr) 2.3fr;}}
  .kb-row:nth-child(5){{grid-template-columns:1.2fr 1.2fr 1.2fr 6fr 1.2fr 1.2fr 1.2fr 1.2fr;}}
  .key{{
    background:linear-gradient(180deg,#2a2e34,#1e2126);
    border-radius:3px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 1px 0 rgba(0,0,0,.5);
  }}
  .trackpad{{
    position:absolute;left:50%;bottom:18px;width:280px;height:62px;margin-left:-140px;
    border-radius:8px;
    background:linear-gradient(180deg,#454950,#32363c);
    box-shadow:
      inset 0 0 0 1px rgba(255,255,255,.1),
      inset 0 2px 3px rgba(0,0,0,.25);
  }}
  .lip{{
    position:absolute;left:12px;right:12px;bottom:-8px;height:14px;
    border-radius:0 0 10px 10px;
    background:linear-gradient(180deg,#2c3036,#15171a);
    box-shadow:0 6px 14px rgba(0,0,0,.45);
  }}
</style>
</head>
<body>
  <div class="stage">
    <div class="laptop">
      <div class="lid">
        <div class="lid-back"></div>
        <div class="cam"><i></i></div>
        <div class="bezel">
          <div class="screen">
            <img src="{b64(CODE)}" alt=""/>
            <div class="glass"></div>
          </div>
        </div>
        <div class="chin">MacBook Pro</div>
      </div>
      <div class="base">
        <div class="hinge"></div>
        <div class="deck">
          <div class="kb" id="kb"></div>
          <div class="trackpad"></div>
        </div>
        <div class="lip"></div>
      </div>
    </div>
  </div>
  <script>
    const kb=document.getElementById('kb');
    const rows=[14,14,13,12,8];
    rows.forEach((n,i)=>{{
      const r=document.createElement('div');
      r.className='kb-row';
      for(let k=0;k<n;k++){{
        const key=document.createElement('div');
        key.className='key';
        r.appendChild(key);
      }}
      kb.appendChild(r);
    }});
  </script>
</body>
</html>
"""


def main():
    html_path = HERE / "_macbook_mockup.html"
    html_path.write_text(HTML, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": 1800, "height": 1400},
            device_scale_factor=2,
        )
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(500)
        page.screenshot(path=str(HERE / "_mac_raw.png"), omit_background=True)
        browser.close()

    im = Image.open(HERE / "_mac_raw.png").convert("RGBA")
    a = np.array(im)
    ys, xs = np.where(a[:, :, 3] > 10)
    pad = 48
    crop = im.crop(
        (
            max(0, xs.min() - pad),
            max(0, ys.min() - pad),
            min(im.width, xs.max() + pad),
            min(im.height, ys.max() + pad),
        )
    )
    crop.save(OUT)
    print(f"✓ {OUT} {crop.size} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
