# -*- coding: utf-8 -*-
"""Recrea gráficos Turbo: mismos dibujos, textos ES sobre Turbo.

Fase 1 — tapa TODO el inglés con rects amplios (sin tocar íconos).
Fase 2 — escribe español en el mismo lugar.
"""
from __future__ import annotations

import colorsys
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

B = Path(__file__).resolve().parent
ASSETS = B / "assets"
FONTS = Path("/tmp/stlabs-fonts")
V = (0, 255, 178)
W = (242, 242, 242)
RED = (255, 90, 90)
GY = (180, 180, 180)
YEL = (255, 210, 80)
BG = (10, 10, 10)
TARGET_H = colorsys.rgb_to_hsv(0, 1, 178 / 255)[0]

# Recortes limpios (coords en imagen fuente)
CROPS: dict[int, tuple[str, tuple[int, int, int, int]]] = {
    1: ("orig", (40, 140, 1095, 900)),
    2: ("raw", (0, 335, 1170, 1035)),
    3: ("orig", (8, 130, 1065, 840)),
    4: ("orig", (8, 115, 1055, 810)),
    5: ("orig", (8, 115, 1065, 840)),
    6: ("orig", (8, 70, 1065, 840)),
    7: ("raw", (0, 315, 1170, 1265)),
    8: ("orig", (60, 20, 1005, 540)),
}


@dataclass
class L:
    x: int
    y: int
    w: int
    h: int
    text: str = ""
    size: int = 18
    color: tuple[int, int, int] = W
    align: str = "left"
    font: str = "poppins"
    lines: list[str] = field(default_factory=list)


def get_font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    paths = {
        "mono": FONTS / "IBMPlexMono-SemiBold.ttf",
        "barlow": FONTS / "BarlowCondensed-Bold.ttf",
        "barlow-m": FONTS / "BarlowCondensed-Medium.ttf",
    }
    return ImageFont.truetype(str(paths.get(kind, FONTS / "Poppins-Bold.ttf")), size)


def boost_green(img: Image.Image, strength: float = 0.42) -> Image.Image:
    arr = np.array(img.convert("RGBA"), dtype=np.float32)
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    mask = (a > 20) & (g > 55) & (g >= r * 0.95) & (g >= b * 0.85) & (lum > 35)
    ys, xs = np.where(mask)
    for y, x in zip(ys.tolist(), xs.tolist()):
        rv, gv, bv = r[y, x] / 255, g[y, x] / 255, b[y, x] / 255
        h, s, v = colorsys.rgb_to_hsv(rv, gv, bv)
        h = h * (1 - strength) + TARGET_H * strength
        s = min(1.0, s * (1 + strength * 0.55))
        v = min(1.0, v * (1 + strength * 0.12))
        nr, ng, nb = colorsys.hsv_to_rgb(h, s, v)
        ng = ng * (1 - strength * 0.25) + (strength * 0.25)
        nr *= 1 - strength * 0.15
        nb *= 1 - strength * 0.2
        arr[y, x, 0] = min(255, nr * 255)
        arr[y, x, 1] = min(255, ng * 255)
        arr[y, x, 2] = min(255, nb * 255)
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def load_base(n: int) -> Image.Image:
    kind, box = CROPS[n]
    if kind == "raw":
        im = Image.open(ASSETS / f"ref-slide-{n:02d}-raw.jpg").convert("RGBA")
    else:
        im = Image.open(ASSETS / f"graphic-{n:02d}.orig.png").convert("RGBA")
    return im.crop(box)


def scale_rects(rects: list[tuple[int, int, int, int]], ref: tuple[int, int], size: tuple[int, int]):
    rw, rh = ref
    w, h = size
    sx, sy = w / rw, h / rh
    out = []
    for x, y, rw2, rh2 in rects:
        out.append((int(x * sx), int(y * sy), max(4, int(rw2 * sx)), max(4, int(rh2 * sy))))
    return out


def scale_labels(labels: list[L], ref: tuple[int, int], size: tuple[int, int]) -> list[L]:
    rw, rh = ref
    w, h = size
    sx, sy = w / rw, h / rh
    out = []
    for t in labels:
        out.append(
            L(
                int(t.x * sx),
                int(t.y * sy),
                max(8, int(t.w * sx)),
                max(8, int(t.h * sy)),
                t.text,
                max(9, int(t.size * min(sx, sy))),
                t.color,
                t.align,
                t.font,
                t.lines,
            )
        )
    return out


def cover(img: Image.Image, x: int, y: int, w: int, h: int) -> None:
    ImageDraw.Draw(img).rectangle([x, y, x + w, y + h], fill=BG + (255,))


def apply_covers(img: Image.Image, rects: list[tuple[int, int, int, int]]) -> None:
    for x, y, w, h in rects:
        cover(img, x, y, w, h)


def fit_size(text: str, max_w: int, start: int, kind: str) -> int:
    size = start
    while size > 8:
        f = get_font(kind, size)
        bb = f.getbbox(text)
        if bb[2] - bb[0] <= max_w:
            return size
        size -= 1
    return 8


def draw_lbl(draw: ImageDraw.ImageDraw, t: L) -> None:
    lines = t.lines if t.lines else ([t.text] if t.text else [])
    if not lines:
        return
    size = t.size
    for line in lines:
        size = min(size, fit_size(line, max(6, t.w - 4), size, t.font))
    font = get_font(t.font, size)
    lh = size + 2
    th = lh * len(lines) - 2
    y0 = t.y + max(0, (t.h - th) // 2)
    for i, line in enumerate(lines):
        bb = font.getbbox(line)
        tw = bb[2] - bb[0]
        tx = t.x + (t.w - tw) // 2 if t.align == "center" else t.x + 2
        ty = y0 + i * lh - bb[1]
        draw.text((tx, ty), line, fill=t.color + (255,), font=font)


def apply_labels(img: Image.Image, labels: list[L]) -> Image.Image:
    out = img.copy()
    draw = ImageDraw.Draw(out)
    for t in labels:
        draw_lbl(draw, t)
    return out


def auto_cover_english(img: Image.Image) -> None:
    """Tapa restos de texto EN (blanco/verde, blobs horizontales)."""
    arr = np.array(img.convert("RGB"))
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    white = (lum > 130) & (r > 90) & (g > 90)
    green = (g > 85) & (g > r * 1.08) & (lum > 45)
    mask = white | green
    h, w = mask.shape
    visited = np.zeros_like(mask, dtype=bool)
    pad = 5
    for y in range(h):
        for x in range(w):
            if not mask[y, x] or visited[y, x]:
                continue
            stack = [(x, y)]
            minx = maxx = x
            miny = maxy = y
            n = 0
            while stack:
                cx, cy = stack.pop()
                if cx < 0 or cy < 0 or cx >= w or cy >= h:
                    continue
                if visited[cy, cx] or not mask[cy, cx]:
                    continue
                visited[cy, cx] = True
                n += 1
                minx = min(minx, cx)
                maxx = max(maxx, cx)
                miny = min(miny, cy)
                maxy = max(maxy, cy)
                stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])
            bw, bh = maxx - minx + 1, maxy - miny + 1
            if n < 90 or bh > 52 or bw > 420:
                continue
            if bh > 38 and bw < bh * 1.2:
                continue
            cover(img, max(0, minx - pad), max(0, miny - pad), bw + 2 * pad, bh + 2 * pad)


G1_REF = (1055, 760)
G1_COVERS = [
    (35, 0, 400, 58),
    (455, 0, 110, 52),
    (0, 268, 145, 62),
    (960, 268, 95, 62),
    (55, 628, 250, 95),
    (805, 628, 210, 95),
]
G1_LABELS = [
    L(35, 0, 400, 58, lines=["MEJORA SOLO.", "24/7."], size=16, align="center"),
    L(455, 0, 110, 52, "HACÉ", 26, W, "center"),
    L(0, 268, 145, 62, "PROBÁ", 24, W, "center"),
    L(960, 268, 95, 62, "MEDÍ", 22, W, "center"),
    L(55, 628, 225, 85, "MEJORÁ", 24, W, "center"),
    L(805, 628, 195, 85, "REFLEXIONÁ", 17, W, "center"),
]

G2_REF = (1170, 700)
G2_COVERS = [
    (468, 95, 320, 50),
    (40, 78, 140, 45),
    (980, 78, 140, 45),
    (130, 180, 170, 38),
    (130, 300, 170, 38),
    (130, 420, 170, 38),
    (130, 535, 170, 38),
    (860, 180, 300, 38),
    (860, 300, 300, 38),
    (860, 420, 300, 38),
    (860, 540, 300, 38),
]
G2_LABELS = [
    L(468, 95, 320, 50, "MEMORIA", 26, V, "center"),
    L(40, 78, 140, 45, "ENTRADA", 18, V, "center"),
    L(980, 78, 140, 45, "SALIDA", 18, V, "center"),
    L(130, 180, 170, 38, "TAREA", 17, W),
    L(130, 300, 170, 38, "ACCIÓN", 17, W),
    L(130, 420, 170, 38, "RESULTADO", 15, W),
    L(130, 535, 170, 38, "CONTEXTO", 15, W),
    L(860, 180, 110, 38, "ÉXITO", 14, W, "center"),
    L(860, 300, 110, 38, "FALLO", 14, W, "center"),
    L(860, 420, 110, 38, "MEJORA", 13, W, "center"),
    L(860, 540, 110, 38, "CAMBIO", 13, W, "center"),
]

G3_REF = (1057, 710)
G3_COVERS = [
    (95, 0, 180, 48),
    (395, 188, 190, 85),
    (648, 0, 130, 48),
    (648, 38, 195, 42),
    (648, 138, 185, 42),
    (648, 238, 175, 42),
    (648, 338, 320, 44),
    (548, 438, 430, 38),
    (578, 498, 400, 42),
]
G3_LABELS = [
    L(95, 0, 180, 48, "TURBO", 18, V, "center"),
    L(395, 188, 190, 85, lines=["EVALÚA", "CADA CORRIDA"], size=13, align="center"),
    L(648, 0, 130, 48, "PUNTAJE", 16, V, "center"),
    L(648, 38, 195, 42, "PRECISIÓN", 15, W),
    L(648, 138, 185, 42, "CALIDAD", 15, W),
    L(648, 238, 175, 42, "ERRORES", 15, W),
    L(648, 338, 320, 44, "OBJETIVO CUMPLIDO", 13, W),
    L(548, 438, 430, 38, "Basado en tus métricas.", 12, GY, font="barlow-m"),
    L(578, 498, 400, 42, "DATOS > ANÁLISIS > MEJORA", 12, V),
]

G4_REF = (1047, 695)
G4_COVERS = [
    (150, 68, 220, 58),
    (35, 360, 335, 145),
    (815, 0, 270, 75),
    (280, 245, 300, 105),
    (695, 365, 345, 45),
    (695, 415, 345, 45),
    (695, 468, 345, 45),
    (695, 522, 345, 45),
]
G4_LABELS = [
    L(150, 68, 220, 58, "TURBO", 18, V, "center"),
    L(40, 378, 320, 45, "TRABAJO ENTREGADO", 14, V, "center"),
    L(40, 425, 335, 72, lines=["Salida, acciones,", "decisiones y resultados."], size=12, font="barlow-m"),
    L(280, 245, 300, 105, lines=["ENVÍA TODO", "A REVISIÓN"], size=12, align="center"),
    L(815, 0, 270, 75, "CRÍTICO", 18, V, "center"),
    L(695, 365, 345, 45, "¿QUÉ FUNCIONÓ?", 14, W, font="mono"),
    L(695, 415, 345, 45, "¿QUÉ FALLÓ?", 14, W, font="mono"),
    L(695, 468, 345, 45, "¿POR QUÉ FALLÓ?", 12, W, font="mono"),
    L(695, 522, 345, 45, "¿QUÉ CAMBIAR?", 14, W, font="mono"),
]

G5_REF = (1057, 725)
G5_COVERS = [
    (70, 8, 320, 48),
    (5, 532, 295, 48),
    (275, 532, 175, 48),
    (605, 12, 400, 85),
    (605, 132, 400, 45),
    (570, 172, 440, 38),
    (605, 282, 400, 45),
    (575, 325, 430, 40),
    (625, 438, 370, 45),
    (605, 482, 420, 55),
]
G5_LABELS = [
    L(70, 8, 320, 48, "HISTORIAL DE TAREAS", 15, V, "center"),
    L(5, 532, 295, 48, "20 TAREAS EJECUTADAS", 12, W),
    L(275, 532, 175, 48, "6 FALLOS", 12, RED),
    L(605, 12, 390, 42, "6 FALLOS DETECTADOS", 14, W),
    L(605, 52, 390, 36, "Turbo no solo los registró.", 11, W, font="barlow-m"),
    L(605, 132, 390, 42, "ANALIZANDO CAUSAS", 14, W),
    L(570, 172, 440, 38, "Compara entradas, acciones y resultados.", 10, W, font="barlow-m"),
    L(605, 282, 390, 42, "4 CAUSAS RAÍZ IGUALES", 13, W),
    L(575, 325, 420, 36, "Tareas distintas. Mismo problema.", 10, W, font="barlow-m"),
    L(625, 438, 370, 42, "PATRÓN ENCONTRADO", 14, V),
    L(610, 482, 400, 48, "Turbo salta el Paso #3 del flujo.", 10, W, font="barlow-m"),
]

G6_REF = (1057, 770)
G6_COVERS = [
    (35, 5, 290, 68),
    (35, 338, 300, 145),
    (110, 330, 230, 160),
    (30, 595, 295, 60),
    (370, 0, 260, 78),
    (355, 275, 325, 55),
    (355, 330, 325, 240),
    (355, 555, 325, 65),
    (795, 0, 280, 68),
    (755, 338, 305, 185),
    (870, 335, 175, 190),
    (765, 595, 295, 60),
]
G6_LABELS = [
    L(35, 5, 290, 68, "TURBO V1", 20, W, "center"),
    L(45, 343, 285, 38, "PIERDE CONTEXTO", 13, W),
    L(45, 388, 290, 38, "OLVIDA PASOS CRÍTICOS", 12, W),
    L(45, 433, 290, 38, "RESULTADOS INCONSISTENTES", 11, W),
    L(30, 595, 295, 60, "PUNTAJE: 72/100", 14, W, "center"),
    L(375, 0, 250, 48, "REFLEXIÓN", 15, W, "center"),
    L(375, 290, 270, 32, "MEJORAS HECHAS:", 13, V),
    L(390, 335, 260, 30, "INSTRUCCIÓN ACTUALIZADA", 10, W),
    L(390, 380, 260, 30, "REGLAS REFINADAS", 12, W),
    L(390, 425, 260, 30, "MEMORIA EXPANDIDA", 12, W),
    L(390, 470, 260, 30, "FLUJO OPTIMIZADO", 12, W),
    L(390, 515, 260, 30, "HERRAMIENTAS MEJORADAS", 10, W),
    L(795, 0, 280, 68, "TURBO V2", 20, V, "center"),
    L(770, 343, 275, 34, "MEJOR CONTEXTO", 12, W),
    L(770, 388, 275, 34, "MENOS ERRORES", 12, W),
    L(770, 433, 275, 34, "MÁS CONSISTENTE", 12, W),
    L(770, 478, 275, 34, "MEJOR CALIDAD", 12, W),
    L(765, 595, 295, 60, "PUNTAJE: 91/100", 14, V, "center"),
]

G7_REF = (1170, 950)
G7_COVERS = [
    (15, 0, 330, 60),
    (255, 175, 195, 200),
    (45, 438, 295, 52),
    (630, 0, 330, 60),
    (725, 175, 195, 200),
    (668, 438, 295, 52),
    (5, 548, 255, 115),
    (305, 548, 255, 115),
    (610, 548, 310, 115),
    (270, 680, 420, 55),
    (1148, 530, 22, 120),
]
G7_LABELS = [
    L(15, 0, 330, 60, "VERSIÓN 1 (ANTERIOR)", 14, W, "center"),
    L(270, 180, 175, 34, "PRECISIÓN", 11, W),
    L(270, 228, 175, 34, "CALIDAD", 11, W),
    L(260, 276, 185, 34, "APROBADAS", 11, W),
    L(270, 324, 165, 34, "ERRORES", 11, W),
    L(45, 438, 295, 52, "PUNTAJE: 82/100", 14, W, "center"),
    L(630, 0, 330, 60, "VERSIÓN 2 (NUEVA)", 14, V, "center"),
    L(740, 180, 175, 34, "PRECISIÓN", 11, W),
    L(740, 228, 175, 34, "CALIDAD", 11, W),
    L(730, 276, 185, 34, "APROBADAS", 11, W),
    L(740, 324, 165, 34, "ERRORES", 11, W),
    L(668, 438, 295, 52, "PUNTAJE: 91/100", 14, V, "center"),
    L(10, 552, 245, 52, lines=["¿MEJOR?", "CONSERVÁLA."], size=12, align="center"),
    L(38, 628, 185, 38, "DESPLEGAR", 14, V, "center"),
    L(315, 552, 245, 52, lines=["¿PEOR?", "REVERTIR."], size=12, align="center"),
    L(338, 628, 185, 38, "DESCARTAR", 14, RED, "center"),
    L(620, 552, 290, 52, lines=["¿IGUAL?", "SEGUIR PROBANDO"], size=11, align="center"),
    L(668, 628, 185, 38, "ITERAR", 14, YEL, "center"),
    L(270, 680, 420, 55, "EL FLUJO DE PRUEBAS", 13, V, "center"),
]

G8_REF = (945, 520)
G8_COVERS = [
    (0, 0, 160, 125),       # Run. Learn. Evolve.
    (115, 0, 275, 82),      # DEPLOY
    (685, 0, 260, 82),      # MEASURE
    (48, 195, 275, 98),     # TEST
    (678, 190, 270, 98),    # REFLECT
    (325, 255, 310, 48),    # ALWAYS GETTING BETTER
    (325, 368, 295, 105),   # IMPROVE
    (735, 405, 210, 72),    # SELF-IMPROVING AI AGENT
]
G8_LABELS = [
    L(0, 0, 160, 125, lines=["Corré.", "Aprendé.", "Evolucioná.", "24/7."], size=14),
    L(125, 0, 265, 82),
    L(135, 2, 240, 32, "DESPLEGÁ", 17, V),
    L(135, 38, 250, 26, "Lanzá la mejor versión", 11, W, font="barlow-m"),
    L(695, 0, 250, 82),
    L(705, 2, 210, 32, "MEDÍ", 17, V),
    L(705, 38, 230, 26, "Puntuá cada resultado", 11, W, font="barlow-m"),
    L(58, 195, 260, 98),
    L(72, 200, 170, 32, "PROBÁ", 17, V),
    L(72, 237, 220, 26, "Demostrá que es mejor", 10, W, font="barlow-m"),
    L(688, 190, 260, 98),
    L(702, 195, 220, 32, "REFLEXIONÁ", 15, V),
    L(702, 232, 240, 26, "Criticá y encontrá fallos", 10, W, font="barlow-m"),
    L(325, 255, 310, 48, "SIEMPRE MEJORANDO.", 12, W, "center"),
    L(335, 368, 285, 105),
    L(365, 378, 220, 32, "MEJORÁ", 17, V, "center"),
    L(345, 418, 260, 26, "Mejorá el sistema", 11, W, "center", font="barlow-m"),
    L(735, 405, 210, 72, lines=["TURBO", "AUTOMEJORABLE"], size=12, color=V, align="center"),
]

ALL = {
    1: (G1_REF, G1_COVERS, G1_LABELS),
    2: (G2_REF, G2_COVERS, G2_LABELS),
    3: (G3_REF, G3_COVERS, G3_LABELS),
    4: (G4_REF, G4_COVERS, G4_LABELS),
    5: (G5_REF, G5_COVERS, G5_LABELS),
    6: (G6_REF, G6_COVERS, G6_LABELS),
    7: (G7_REF, G7_COVERS, G7_LABELS),
    8: (G8_REF, G8_COVERS, G8_LABELS),
}


def clean_edges(n: int, img: Image.Image) -> Image.Image:
    out = img.copy()
    w, h = out.size
    if n == 1:
        cover(out, w - 28, 0, 28, h)
    elif n == 2:
        cover(out, 0, h - 8, w, 8)
    elif n == 3:
        cover(out, w - 15, h - 80, 15, 80)
    elif n == 7:
        cover(out, w - 22, 548, 22, 110)
    elif n == 8:
        cover(out, w - 12, 0, 12, h)
    return out


def process(n: int) -> None:
    base = load_base(n)
    base = boost_green(base)
    base = clean_edges(n, base)
    ref, covers, labels = ALL[n]
    covers = scale_rects(covers, ref, base.size)
    labels = scale_labels(labels, ref, base.size)
    apply_covers(base, covers)
    out = apply_labels(base, labels)
    out.save(ASSETS / f"graphic-{n:02d}.png", optimize=True)
    print(f"OK graphic-{n:02d} → {out.size}")


def main() -> None:
    for i in range(1, 9):
        process(i)


if __name__ == "__main__":
    main()
