---
name: video-stlabs
description: Editor y productor de Reels/TikTok/Shorts talking-head para la marca Sebastián García / STLabs (sebastian.stlabs.ar). Actívalo SIEMPRE que Yuli pida editar un video, Reel, TikTok, Short, talking-head, quitar ruido de cafetería, palabras neón, keywords on-screen, o cambios sobre un video ya entregado. Aplica el preset bloqueado de edición (grade profesional, solo voz, keywords verdes robóticas grandes y densas, framing estable). No pregunta por la marca; ya está definida.
---

# Video STLabs — Edición talking-head bloqueada

Producís videos cortos (Reels / TikTok / Shorts) para **Sebastián García · STLabs**, firma **sebastian.stlabs.ar**.

**Fuente de verdad del preset:** `references/sistema-video-edicion-stlabs.json` (también en `/workspace/sistema-video-edicion-stlabs.json`).  
ADN visual amplio: `/workspace/sistema-video-stlabs.json`.

No improvisar colores, tipografías ni modelo de texto. Verde oficial **siempre `#00FFB2`**.

## Modelo de texto (obligatorio)

- **Palabras sueltas** (1–3 palabras), UPPERCASE, estilo **robótico** → **Bebas Neue**
- Color **`#00FFB2`**, outline negro, sombra
- **Muchas** keywords (≈18+/min), tamaños **variados**:
  - Huge **190px** (golpes)
  - Mid **130px** (secundarias)
  - CTA barra verde **82px** (`COMENTÁ {KEYWORD}`)
- Alternar posición arriba/abajo
- Firma siempre: `sebastian.stlabs.ar` · IBM Plex Mono · verde
- **PROHIBIDO:** subtítulos de frases completas / karaoke del monólogo entero (salvo que Yuli lo pida explícito como variante aparte)

## Look / color (obligatorio)

Usar el grade profesional del JSON (`grade_profesional.ffmpeg_chain`):

- `colorlevels` + `eq` (sat ~1.14, contraste 1.07) + `colorbalance` neutro-cálido + `unsharp` suave
- **Sin** teñir la imagen de verde; el verde vive en overlays
- **Sin** vignette en este preset

## Framing (obligatorio)

- Crop **centrado fijo**: `(iw-1080)/2:(ih-1920)/2` sobre canvas 1620×2880
- **PROHIBIDO** saltar el crop en Y entre beats (se ve como corte desalineado)

## Audio (obligatorio)

- Bajar ruido de fondo; **solo voz de Sebastián**
- Cadena: `highpass` → `arnndn` (rnnoise) → `afftdn` → `speechnorm` → `loudnorm` → gain
- Medir lag vs labios del master y compensar (`atrim`/`adelay`)
- Cortes de video = mismos cortes de audio
- SFX hit/tick en onsets de keywords Huge + CTA

## Cortes / duración

- Objetivo **35–55s** (máx 60s)
- Recortar silencios > ~0.7s (dejar ~0.25s)
- Recortar muletillas / relleno que no aportan al claim
- Concat A/V sincronizado; hold final con `tpad` para CTA

## Workflow

1. Leer `references/sistema-video-edicion-stlabs.json`
2. Tomar master (Drive/local) → limpiar voz → Whisper word-level (es)
3. Definir keep-segments + lista densa de keywords con timestamps
4. Generar ASS (estilos del JSON) + SFX
5. Concat cortes → grade + framing + ass → export 1080×1920
6. QA checklist del JSON
7. Entregar MP4 + brief JSON + caption voseo si aplica + link de descarga

## Variantes (solo si Yuli lo pide)

| Pedido | Qué hacer |
|---|---|
| Default / “como siempre” | Este preset keywords |
| “Frases completas” | Variante captions (Poppins) — **no** es el default |
| “Más grande / más palabras” | Subir densidad o Huge; no cambiar color ni fuente |

## Entrega

- `/opt/cursor/artifacts/STLabs-{slug}-edit.mp4`
- Brief con: duración, cortes, keywords, grade, audio
- Caption social en voseo si se pide `@caption`
