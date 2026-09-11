#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reel STLabs — Cómo funciona Turbo

Clona la secuencia de referencia:
- canvas ANCHO estilo n8n / multi-agente
- cámara que se mueve en HORIZONTAL parte por parte
- iconos con volumen / glow (más realistas)
"""
from __future__ import annotations

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BUILD = Path(__file__).resolve().parent
REPO = BUILD.parents[1]
FONTS_DIR = REPO / "fonts"
OUT = BUILD / "out"
FRAMES = BUILD / "frames"

VW, VH = 1080, 1920
FPS = 20
DURATION = 32.0
CW, CH = 5200, 1920

BG = (10, 10, 12)
GREEN = (0, 255, 178)
WHITE = (245, 245, 245)
GRAY = (160, 165, 175)
MUTED = (90, 95, 105)
ORANGE = (255, 145, 40)
BLUE = (70, 150, 255)
TEAL = (40, 210, 200)
CARD = (22, 24, 28)
CARD2 = (42, 46, 54)


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS_DIR / name), size)


def sh(cmd: list[str]) -> None:
    print("+", " ".join(map(str, cmd[:14])), "...")
    subprocess.run(cmd, check=True)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def ease(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def camera_x(t: float) -> float:
    keys = [
        (0.0, 40),
        (3.0, 40),
        (5.0, 480),
        (9.0, 1100),
        (13.5, 1900),
        (18.0, 2700),
        (23.0, 3450),
        (27.5, 4120),
        (32.0, 4120),
    ]
    for i in range(len(keys) - 1):
        t0, x0 = keys[i]
        t1, x1 = keys[i + 1]
        if t0 <= t <= t1:
            return lerp(x0, x1, ease((t - t0) / max(0.001, t1 - t0)))
    return keys[-1][1]


def glow_box(base: Image.Image, box, color, blur=18, alpha=80) -> Image.Image:
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(box, radius=24, fill=(*color, alpha))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    return Image.alpha_composite(base, layer)


def glow_dot(base: Image.Image, cx, cy, r, color, blur=12, alpha=120) -> Image.Image:
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, alpha))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    return Image.alpha_composite(base, layer)


def _fill_round(size, color_fn, radius=18):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i in range(size):
        d.line([(0, i), (size, i)], fill=color_fn(i))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([3, 3, size - 3, size - 3], radius=radius, fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def icon_trigger(size=88) -> Image.Image:
    out = _fill_round(size, lambda i: (255 - i // 3, 110 + i // 4, 25, 255), 18)
    d = ImageDraw.Draw(out)
    bolt = [(38, 14), (22, 46), (36, 46), (28, 74), (58, 36), (42, 36), (52, 14)]
    d.polygon(bolt, fill=(255, 255, 240, 255))
    d.rounded_rectangle([3, 3, size - 3, size - 3], radius=18, outline=(255, 200, 120, 230), width=3)
    return out


def icon_prompt(size=88) -> Image.Image:
    out = _fill_round(size, lambda i: (40, 100 + i // 3, 255 - i // 3, 255), 18)
    d = ImageDraw.Draw(out)
    d.polygon([(28, 58), (52, 20), (62, 28), (38, 66)], fill=(255, 255, 255, 245))
    d.polygon([(52, 20), (58, 14), (68, 24), (62, 28)], fill=(255, 210, 80, 255))
    d.polygon([(28, 58), (22, 70), (34, 64)], fill=(255, 160, 60, 255))
    d.rounded_rectangle([3, 3, size - 3, size - 3], radius=18, outline=(140, 190, 255, 230), width=3)
    return out


def icon_agent(size=96, accent=GREEN) -> Image.Image:
    out = _fill_round(size, lambda i: (30 + i // 5, 34 + i // 5, 40 + i // 5, 255), 20)
    d = ImageDraw.Draw(out)
    d.rounded_rectangle([22, 26, 74, 70], radius=14, fill=(245, 245, 250, 255), outline=(*accent, 255), width=3)
    d.ellipse([30, 38, 44, 52], fill=(*accent, 255))
    d.ellipse([52, 38, 66, 52], fill=(*accent, 255))
    d.ellipse([34, 42, 40, 48], fill=(10, 10, 12, 255))
    d.ellipse([56, 42, 62, 48], fill=(10, 10, 12, 255))
    d.rounded_rectangle([40, 56, 56, 62], radius=3, fill=(40, 45, 55, 255))
    d.line([(48, 26), (48, 16)], fill=(*accent, 255), width=3)
    d.ellipse([43, 10, 53, 20], fill=(*accent, 255))
    d.rounded_rectangle([3, 3, size - 3, size - 3], radius=20, outline=(*accent, 200), width=3)
    return out


def icon_llm(size=84) -> Image.Image:
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([2, 2, size - 2, size - 2], fill=(25, 55, 140, 255))
    d.ellipse([10, 10, size - 10, size - 10], outline=(120, 180, 255, 255), width=3)
    d.ellipse([22, 22, size - 22, size - 22], fill=(70, 140, 255, 255))
    d.rounded_rectangle([32, 32, 52, 52], radius=4, fill=(240, 248, 255, 255))
    for a, b in [((42, 28), (42, 32)), ((42, 52), (42, 56)), ((28, 42), (32, 42)), ((52, 42), (56, 42))]:
        d.line([a, b], fill=(200, 220, 255, 255), width=2)
    d.ellipse([2, 2, size - 2, size - 2], outline=(150, 200, 255, 220), width=3)
    return im


def icon_wave(size=84, color=GREEN) -> Image.Image:
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([2, 2, size - 2, size - 2], fill=(18, 40, 34, 255), outline=(*color, 230), width=3)
    cy = size // 2
    pts = [(16 + i, cy + int(14 * math.sin(i * 0.35))) for i in range(0, 53)]
    d.line(pts, fill=(*color, 255), width=4)
    return im


def icon_memory(size=88, accent=ORANGE) -> Image.Image:
    out = _fill_round(size, lambda i: (40 + i // 4, 38 + i // 5, 50 + i // 4, 255), 18)
    d = ImageDraw.Draw(out)
    d.ellipse([24, 18, 64, 34], fill=(*accent, 255))
    d.rectangle([24, 26, 64, 58], fill=(*accent, 220))
    d.ellipse(
        [24, 50, 64, 66],
        fill=(max(0, accent[0] - 40), max(0, accent[1] - 40), max(0, accent[2] - 20), 255),
    )
    d.ellipse([24, 18, 64, 34], outline=(255, 255, 255, 180), width=2)
    d.rounded_rectangle([3, 3, size - 3, size - 3], radius=18, outline=(*accent, 200), width=3)
    return out


def icon_processor(size=88, accent=ORANGE) -> Image.Image:
    out = _fill_round(
        size,
        lambda i: (min(255, accent[0] + i // 2), min(255, accent[1] + i // 4), accent[2] // 2 + 20, 255),
        18,
    )
    d = ImageDraw.Draw(out)
    d.polygon([(28, 28), (48, 44), (28, 60)], fill=(255, 255, 255, 245))
    d.polygon([(44, 28), (64, 44), (44, 60)], fill=(255, 255, 255, 245))
    d.rounded_rectangle([3, 3, size - 3, size - 3], radius=18, outline=(255, 220, 160, 220), width=3)
    return out


def icon_bundle(size=96) -> Image.Image:
    out = _fill_round(size, lambda i: (20, 70 + i // 3, 75 + i // 4, 255), 20)
    d = ImageDraw.Draw(out)
    pts = [(48, 28), (30, 55), (66, 55)]
    d.line([pts[0], pts[1], pts[2], pts[0]], fill=(220, 255, 240, 255), width=4)
    for x, y in pts:
        d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=(*GREEN, 255))
    d.rounded_rectangle([3, 3, size - 3, size - 3], radius=20, outline=(*TEAL, 220), width=3)
    return out


def icon_success(size=96) -> Image.Image:
    out = _fill_round(size, lambda i: (0, 120 + i // 2, 90 + i // 3, 255), 20)
    d = ImageDraw.Draw(out)
    d.line([(28, 50), (42, 64), (70, 32)], fill=(255, 255, 255, 255), width=7)
    d.rounded_rectangle([3, 3, size - 3, size - 3], radius=20, outline=(*GREEN, 255), width=4)
    return out


def paste_icon(base: Image.Image, icon: Image.Image, cx: float, cy: float) -> None:
    x = int(cx - icon.size[0] / 2)
    y = int(cy - icon.size[1] / 2)
    base.alpha_composite(icon, (x, y))


def draw_label(draw, cx, y, title, sub, f_title, f_sub):
    bb = draw.textbbox((0, 0), title, font=f_title)
    draw.text((cx - (bb[2] - bb[0]) / 2, y), title, font=f_title, fill=WHITE)
    if sub:
        bb2 = draw.textbbox((0, 0), sub, font=f_sub)
        draw.text((cx - (bb2[2] - bb2[0]) / 2, y + 32), sub, font=f_sub, fill=GRAY)


def draw_wire(draw, p0, p1, color=MUTED, width=3):
    pts = []
    steps = 30
    for i in range(steps + 1):
        t = i / steps
        x = lerp(p0[0], p1[0], t)
        y = lerp(p0[1], p1[1], t) + math.sin(t * math.pi) * ((p1[1] - p0[1]) * 0.04)
        pts.append((x, y))
    draw.line(pts, fill=color, width=width)
    r = 5
    draw.ellipse([p0[0] - r, p0[1] - r, p0[0] + r, p0[1] + r], fill=color)
    draw.ellipse([p1[0] - r, p1[1] - r, p1[0] + r, p1[1] + r], fill=color)
    return pts


def draw_pulse(draw, pts, phase, color=ORANGE, r=6):
    if not pts:
        return
    idx = int((phase % 1.0) * (len(pts) - 1))
    x, y = pts[idx]
    draw.ellipse([x - r - 3, y - r - 3, x + r + 3, y + r + 3], outline=color, width=2)
    draw.ellipse([x - r, y - r, x + r, y + r], fill=color)


def draw_card(base: Image.Image, cx, cy, w, h, active=False, accent=GREEN) -> Image.Image:
    x0, y0 = int(cx - w / 2), int(cy - h / 2)
    box = [x0, y0, x0 + w, y0 + h]
    if active:
        base = glow_box(base, [x0 - 8, y0 - 8, x0 + w + 8, y0 + h + 8], accent, 22, 75)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle(box, radius=22, fill=CARD, outline=accent if active else CARD2, width=3 if active else 2)
    return base


def tip_for(t: float) -> str:
    tips = [
        (0.0, 3.5, "Turbo recibe el disparador y arma el prompt"),
        (3.5, 9.0, "Un prompt → tres agentes en paralelo"),
        (9.0, 16.0, "Cada agente estructura y recupera datos"),
        (16.0, 22.5, "Procesa ventas, marketing y producto"),
        (22.5, 26.5, "Empaqueta todo en un solo resultado"),
        (26.5, 32.1, "Listo: Turbo entrega el estado de éxito"),
    ]
    for a, b, msg in tips:
        if a <= t < b:
            return msg
    return ""


def build_canvas(t: float, fonts: dict) -> Image.Image:
    img = Image.new("RGBA", (CW, CH), (*BG, 255))
    d = ImageDraw.Draw(img)

    for x in range(0, CW, 80):
        d.line([(x, 0), (x, CH)], fill=(18, 18, 22, 255), width=1)
    for y in range(0, CH, 80):
        d.line([(0, y), (CW, y)], fill=(18, 18, 22, 255), width=1)

    y_mid, y_top, y_bot = 820, 520, 1120
    x_trig, x_prompt, x_agents = 220, 560, 1100
    x_llm, x_out, x_mem = 1650, 2150, 2750
    x_proc, x_bundle, x_ok = 3400, 4100, 4700

    agents_y = [y_top, y_mid, y_bot]
    names = ["Agente Ventas", "Agente Marketing", "Agente Producto"]
    mem_names = ["Datos Ventas", "Datos Marketing", "Datos Producto"]
    proc_names = ["Procesar Ventas", "Procesar Marketing", "Procesar Producto"]
    accents = [ORANGE, GREEN, BLUE]
    phase = (t * 0.9) % 1.0
    wires = []

    if t >= 0.8:
        wires.append(draw_wire(d, (x_trig + 55, y_mid), (x_prompt - 55, y_mid), ORANGE if t < 5 else MUTED, 4))
    if t >= 3.5:
        for i, ay in enumerate(agents_y):
            if t >= 3.5 + i * 0.12:
                wires.append(draw_wire(d, (x_prompt + 55, y_mid), (x_agents - 70, ay), GREEN if t < 12 else MUTED, 3))
    if t >= 7.0:
        for i, ay in enumerate(agents_y):
            if t >= 7.0 + i * 0.1:
                wires.append(draw_wire(d, (x_agents + 70, ay), (x_llm - 50, ay), BLUE if t < 16 else MUTED, 3))
            if t >= 9.0 + i * 0.1:
                wires.append(draw_wire(d, (x_llm + 50, ay), (x_out - 50, ay), GREEN if t < 18 else MUTED, 3))
            if t >= 12.0 + i * 0.1:
                wires.append(draw_wire(d, (x_out + 50, ay), (x_mem - 55, ay), accents[i] if t < 22 else MUTED, 3))
            if t >= 16.5 + i * 0.1:
                wires.append(draw_wire(d, (x_mem + 55, ay), (x_proc - 55, ay), accents[i] if t < 26 else MUTED, 3))
    if t >= 22.0:
        for ay in agents_y:
            wires.append(draw_wire(d, (x_proc + 55, ay), (x_bundle - 60, y_mid), GREEN if t < 28 else MUTED, 3))
    if t >= 26.0:
        wires.append(draw_wire(d, (x_bundle + 60, y_mid), (x_ok - 60, y_mid), GREEN, 5))

    for i, pts in enumerate(wires):
        draw_pulse(d, pts, phase + i * 0.08, ORANGE if t < 26 else GREEN, 6)

    img = draw_card(img, x_trig, y_mid, 120, 120, t < 5, ORANGE)
    paste_icon(img, icon_trigger(), x_trig, y_mid)
    d = ImageDraw.Draw(img)
    draw_label(d, x_trig, y_mid + 78, "Activador", "del flujo", fonts["lab"], fonts["sub"])

    if t >= 1.0:
        img = draw_card(img, x_prompt, y_mid, 120, 120, 1 <= t < 8, BLUE)
        paste_icon(img, icon_prompt(), x_prompt, y_mid)
        d = ImageDraw.Draw(img)
        draw_label(d, x_prompt, y_mid + 78, "Crear prompt", "Disparador", fonts["lab"], fonts["sub"])

    if t >= 3.8:
        for i, ay in enumerate(agents_y):
            img = draw_card(img, x_agents, ay, 150, 110, t < 14, accents[i])
            paste_icon(img, icon_agent(96, accents[i]), x_agents, ay - 4)
            d = ImageDraw.Draw(img)
            draw_label(d, x_agents, ay + 70, names[i], "Agente IA", fonts["lab"], fonts["sub"])

    if t >= 7.2:
        for i, ay in enumerate(agents_y):
            if t < 16:
                img = glow_dot(img, x_llm, ay, 42, BLUE, 14, 70)
            paste_icon(img, icon_llm(), x_llm, ay)
            d = ImageDraw.Draw(img)
            draw_label(d, x_llm, ay + 58, "Modelo chat", "LLM", fonts["tiny"], fonts["sub"])

    if t >= 9.2:
        for ay in agents_y:
            paste_icon(img, icon_wave(84, GREEN), x_out, ay)
            d = ImageDraw.Draw(img)
            draw_label(d, x_out, ay + 58, "Salida estructurada", "", fonts["tiny"], fonts["sub"])

    if t >= 12.2:
        for i, ay in enumerate(agents_y):
            img = draw_card(img, x_mem, ay, 120, 110, t < 22, accents[i])
            paste_icon(img, icon_memory(88, accents[i]), x_mem, ay - 4)
            d = ImageDraw.Draw(img)
            draw_label(d, x_mem, ay + 70, mem_names[i], "Memoria", fonts["lab"], fonts["sub"])

    if t >= 16.8:
        for i, ay in enumerate(agents_y):
            img = draw_card(img, x_proc, ay, 120, 110, t < 26, accents[i])
            paste_icon(img, icon_processor(88, accents[i]), x_proc, ay - 4)
            d = ImageDraw.Draw(img)
            draw_label(d, x_proc, ay + 70, proc_names[i], "Procesador", fonts["lab"], fonts["sub"])

    if t >= 22.2:
        img = draw_card(img, x_bundle, y_mid, 140, 120, True, TEAL)
        paste_icon(img, icon_bundle(), x_bundle, y_mid - 4)
        d = ImageDraw.Draw(img)
        draw_label(d, x_bundle, y_mid + 78, "Empaquetar datos", "procesados", fonts["lab"], fonts["sub"])

    if t >= 26.2:
        img = glow_box(img, [x_ok - 90, y_mid - 90, x_ok + 90, y_mid + 90], GREEN, 28, 100)
        img = draw_card(img, x_ok, y_mid, 140, 120, True, GREEN)
        paste_icon(img, icon_success(), x_ok, y_mid - 4)
        d = ImageDraw.Draw(img)
        draw_label(d, x_ok, y_mid + 78, "Estado de éxito", "Listo", fonts["lab"], fonts["sub"])

    return img


def compose_frame(t: float, fonts: dict) -> Image.Image:
    canvas = build_canvas(t, fonts)
    x0 = int(max(0, min(CW - VW, camera_x(t))))
    view = canvas.crop((x0, 0, x0 + VW, VH)).convert("RGBA")

    hud = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    d = ImageDraw.Draw(hud)
    for i in range(220):
        a = int(200 * (1 - i / 220))
        d.line([(0, i), (VW, i)], fill=(8, 8, 10, a))
    for i in range(160):
        a = int(210 * (i / 160))
        d.line([(0, VH - 160 + i), (VW, VH - 160 + i)], fill=(8, 8, 10, a))

    d.text((VW / 2, 70), "CÓMO FUNCIONA TURBO", font=fonts["title"], fill=WHITE, anchor="mm")
    d.text((VW / 2, 118), "Flujo multi-agente en paralelo", font=fonts["sub_g"], fill=GREEN, anchor="mm")

    tip = tip_for(t)
    if tip:
        bb = d.textbbox((0, 0), tip, font=fonts["tip"])
        tw = bb[2] - bb[0]
        x0b = (VW - tw) // 2 - 24
        d.rounded_rectangle([x0b, 150, x0b + tw + 48, 198], radius=14, fill=(0, 0, 0, 210), outline=GREEN, width=2)
        d.text((VW / 2, 174), tip, font=fonts["tip"], fill=WHITE, anchor="mm")

    d.text((VW / 2, VH - 70), "sebastian.stlabs.ar", font=fonts["foot"], fill=GREEN, anchor="mm")
    return Image.alpha_composite(view, hud).convert("RGB")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    for p in FRAMES.glob("f_*.png"):
        p.unlink()

    fonts = {
        "title": load_font("Poppins-Bold.ttf", 42),
        "sub_g": load_font("IBMPlexMono-Medium.ttf", 22),
        "lab": load_font("Poppins-Bold.ttf", 22),
        "sub": load_font("IBMPlexMono-Medium.ttf", 16),
        "tiny": load_font("Poppins-Bold.ttf", 18),
        "tip": load_font("Poppins-Bold.ttf", 24),
        "foot": load_font("IBMPlexMono-Medium.ttf", 30),
    }

    n = int(DURATION * FPS)
    for i in range(n):
        compose_frame(i / FPS, fonts).save(FRAMES / f"f_{i:05d}.png")
        if i % 48 == 0:
            print(f"frame {i}/{n}")

    mp4 = OUT / "STLabs-Reel-Turbo-Flujo.mp4"
    sh([
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(FRAMES / "f_%05d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17",
        "-movflags", "+faststart",
        str(mp4),
    ])
    for ss, name in [(1.5, "preview-01"), (6, "preview-05"), (14, "preview-13"), (24, "preview-24"), (29, "preview-29")]:
        sh([
            "ffmpeg", "-y", "-ss", str(ss), "-i", str(mp4),
            "-frames:v", "1", "-update", "1", str(OUT / f"{name}.png"),
        ])

    (BUILD / "caption.txt").write_text(
        "Así funciona Turbo.\n\n"
        "Un disparador. Un prompt.\n"
        "Tres agentes en paralelo: ventas, marketing y producto.\n"
        "Cada uno estructura, recupera y procesa.\n"
        "Todo se empaqueta en un solo resultado.\n\n"
        "Menos ida y vuelta. Más ejecución.\n\n"
        "Comentá TURBO y te muestro cómo aplicarlo a tu operación.\n\n"
        "#turbo #automatizacion #agentes #stlabs #revops\n",
        encoding="utf-8",
    )
    (BUILD / "index.json").write_text(
        "{\n"
        '  "id": "2026-09-11-reel-turbo-flujo",\n'
        '  "titulo": "Cómo funciona Turbo — pan horizontal multi-agente",\n'
        '  "tipo": "reel",\n'
        f'  "duracion_s": {int(DURATION)},\n'
        '  "formato": "1080x1920",\n'
        '  "fondo": "canvas_n8n_pan",\n'
        '  "familia_visual": "manifiesto",\n'
        '  "origen": "screenshot",\n'
        '  "keyword_portada": "TURBO"\n'
        "}\n",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        "# Manifiesto de fuentes — Reel Turbo flujo\n\n"
        "| Familia | Peso | Rol | Origen |\n|---|---|---|---|\n"
        "| Poppins | 700 | Título / tips / nodos | `/workspace/fonts/Poppins-Bold.ttf` |\n"
        "| IBM Plex Mono | 500 | Labels / firma | `/workspace/fonts/IBMPlexMono-Medium.ttf` |\n",
        encoding="utf-8",
    )
    print("DONE →", mp4)


if __name__ == "__main__":
    main()
