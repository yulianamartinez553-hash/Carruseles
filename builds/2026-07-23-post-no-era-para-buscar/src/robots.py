# -*- coding: utf-8 -*-
"""Robots pixel-art del carrusel QUERY — recreados fielmente de la referencia.
POST = naranja exacto de la referencia (enojado). QUERY = verde STLabs (anteojos negros,
sonrisa). GET = azul (triste). Dibujados como SVG con shape-rendering crispEdges."""

OUT = "#0f1218"          # contorno / oscuro
NARANJA = "#FF5A2E"      # bichito POST — igual a la referencia
VERDE = "#00FFB2"        # QUERY con verde de marca
AZUL = "#2F7BFF"         # GET
BAND = "#12161d"         # placa del nombre
EYE = "#ffffff"


def px(x, y, w, h, c, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" {extra}/>'


def _head(color):
    p = []
    # antena
    p.append(px(14, 2, 2, 2, OUT))
    p.append(px(13, 0, 4, 2, color))
    p.append(px(13.4, .4, 3.2, 1.2, "rgba(0,0,0,.25)"))
    # orejas
    p.append(px(1, 9, 2, 5, OUT))
    p.append(px(27, 9, 2, 5, OUT))
    # cabeza: contorno redondeado pixel + relleno
    p.append(px(4, 4, 22, 14, OUT))
    p.append(px(3, 5, 24, 12, OUT))
    p.append(px(5, 5, 20, 12, color))
    p.append(px(4, 6, 22, 10, color))
    # sombra inferior
    p.append(px(4, 15, 22, 1, "rgba(0,0,0,.16)"))
    return p


def _visor():
    return [px(7, 7, 16, 8, OUT), px(6, 8, 18, 6, OUT)]


def _body(color, label, label_size, band_pad=0):
    p = []
    # brazos
    p.append(px(4, 19, 4, 5, OUT))
    p.append(px(5, 20, 2, 3, color))
    p.append(px(22, 19, 4, 5, OUT))
    p.append(px(23, 20, 2, 3, color))
    # torso
    p.append(px(9, 18, 12, 9, OUT))
    p.append(px(10, 19, 10, 7, color))
    # placa con nombre
    p.append(px(10, 20.5, 10, 3.6, BAND))
    p.append(
        f'<text x="15" y="23.15" text-anchor="middle" fill="#fff" '
        f'font-family="\'Press Start 2P\',monospace" font-size="{label_size}">{label}</text>'
    )
    # patas + pies
    p.append(px(11, 27, 3, 3, OUT))
    p.append(px(16, 27, 3, 3, OUT))
    p.append(px(9, 30, 5, 2, OUT))
    p.append(px(16, 30, 5, 2, OUT))
    return p


def _face_query():
    p = []
    # anteojos negros: patillas + lentes redondeados + puente
    p.append(px(3, 9, 4, 1.6, "#000"))
    p.append(px(23, 9, 4, 1.6, "#000"))
    for lx in (7, 17):
        p.append(px(lx, 8, 6, 4, "#000"))
        for cx, cy in ((lx, 8), (lx + 5, 8), (lx, 11), (lx + 5, 11)):
            p.append(px(cx, cy, 1, 1, "rgba(255,255,255,0)"))
    p.append(px(13, 9, 4, 1.4, "#000"))
    # brillo de lentes
    p.append(px(8, 9, 1, 1, "#3a3f4a"))
    p.append(px(18, 9, 1, 1, "#3a3f4a"))
    # sonrisa blanca
    p.append(px(11, 13, 1, 1, EYE))
    p.append(px(12, 14, 6, 1, EYE))
    p.append(px(18, 13, 1, 1, EYE))
    return p


def _face_get():
    p = _visor()
    # ojos tristes: caídos hacia afuera
    p.append(px(9, 9, 3, 4, EYE))
    p.append(px(18, 9, 3, 4, EYE))
    p.append(px(9, 9, 1, 1, OUT))    # párpado externo izq
    p.append(px(20, 9, 1, 1, OUT))   # párpado externo der
    p.append(px(9, 9, 3, 1, "rgba(0,0,0,.28)"))
    p.append(px(18, 9, 3, 1, "rgba(0,0,0,.28)"))
    return p


def _face_post():
    p = _visor()
    # ojos enojados: ceja que baja hacia el centro
    p.append(px(9, 9, 4, 3, EYE))
    p.append(px(17, 9, 4, 3, EYE))
    p.append(px(11, 9, 2, 1, OUT))
    p.append(px(17, 9, 2, 1, OUT))
    # mueca zigzag
    for i, x in enumerate(range(11, 20)):
        p.append(px(x, 14 if i % 2 == 0 else 13, 1, 1, EYE))
    return p


def robot(kind, width, cls=""):
    color = {"query": VERDE, "get": AZUL, "post": NARANJA}[kind]
    label = {"query": "QUERY", "get": "GET", "post": "POST"}[kind]
    size = 1.75 if kind == "query" else 2.3
    face = {"query": _face_query, "get": _face_get, "post": _face_post}[kind]()
    parts = _head(color) + face + _body(color, label, size)
    return (
        f'<svg class="{cls}" width="{width}" viewBox="0 0 30 32.5" '
        f'shape-rendering="crispEdges" xmlns="http://www.w3.org/2000/svg">'
        + "".join(parts) + "</svg>"
    )


def penguin(width, cls=""):
    """Pingüino pixel chiquito (cliente en los diagramas de red)."""
    B = "#14181f"; W = "#f4f4ef"; O = "#FF9D3C"
    p = [
        px(3, 0, 6, 2, B), px(2, 1, 8, 9, B), px(1, 3, 10, 6, B),
        px(4, 4, 4, 5, W), px(3, 5, 6, 4, W),
        px(3.4, 1.8, 1.4, 1.4, W), px(7.2, 1.8, 1.4, 1.4, W),
        px(3.9, 2.2, .7, .7, B), px(7.7, 2.2, .7, .7, B),
        px(5, 3.1, 2, 1.2, O),
        px(2.4, 10, 2.6, 1.4, O), px(7, 10, 2.6, 1.4, O),
    ]
    return (
        f'<svg class="{cls}" width="{width}" viewBox="0 0 12 11.6" '
        f'shape-rendering="crispEdges" xmlns="http://www.w3.org/2000/svg">'
        + "".join(p) + "</svg>"
    )


def squiggle(width=120, color=VERDE, cls="sq"):
    return (
        f'<svg class="{cls}" width="{width}" viewBox="0 0 60 14" fill="none" '
        f'xmlns="http://www.w3.org/2000/svg"><path d="M2 10 C 12 2, 20 13, 30 7 S 50 2, 58 8" '
        f'stroke="{color}" stroke-width="3.4" stroke-linecap="round"/></svg>'
    )


def cloud(width=210, color=VERDE):
    return (
        f'<svg width="{width}" viewBox="0 0 100 62" fill="none" xmlns="http://www.w3.org/2000/svg">'
        f'<path d="M25 52 h50 a14 14 0 0 0 4 -27.5 A20 20 0 0 0 41 15 A16 16 0 0 0 12 27 '
        f'a13 13 0 0 0 13 25 Z" stroke="{color}" stroke-width="3.4" fill="rgba(0,255,178,.06)"/>'
        f'<text x="50" y="37" text-anchor="middle" fill="#0A0A0A" '
        f'font-family="\'IBM Plex Mono\',monospace" font-weight="600" font-size="12">CDN</text>'
        f'<text x="50" y="49" text-anchor="middle" fill="#5a5f5b" '
        f'font-family="\'IBM Plex Mono\',monospace" font-size="9">proxy</text></svg>'
    )


def server(height=96, cls=""):
    bars = "".join(
        f'<div class="srv-bar"><i></i><i></i></div>' for _ in range(3)
    )
    return f'<div class="srv {cls}" style="height:{height}px">{bars}</div>'
