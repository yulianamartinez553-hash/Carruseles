# Manifiesto de fuentes — Crear Una Web Con Claude Desde Cero

Clon (modo blanco) del carrusel de referencia. Todas las fuentes van **embebidas en base64** en `STLabs-CrearWebConClaude.html` (HTML standalone, sin CDN).

| Fuente | Peso / estilo | Rol | Origen | Código / comando de carga |
|---|---|---|---|---|
| Playfair Display | 900 (Black) normal + italic | Título display serif (portada + cada slide) y palabra-acento en verde | GitHub google/fonts (`ofl/playfairdisplay/PlayfairDisplay[wght].ttf` y `PlayfairDisplay-Italic[wght].ttf`) | `curl -LO https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf` → `@font-face{font-family:'Playfair Display';font-weight:400 900;src:url(data:font/ttf;base64,...) format('truetype');}` |
| Caveat | 700 | Líneas de acento manuscritas (verde): "esto es lo que haría", "tu diseñador UX en 5 min", "del mockup al código real", "sin saber nada técnico", "mi entrenamiento completo." | GitHub google/fonts (`ofl/caveat/Caveat[wght].ttf`) | `curl -LO https://raw.githubusercontent.com/google/fonts/main/ofl/caveat/Caveat%5Bwght%5D.ttf` → `@font-face{font-family:'Caveat';font-weight:400 700;src:url(data:font/ttf;base64,...) format('truetype');}` |
| Poppins | 700 / 800 | Labels de nodos (DISEÑO · CÓDIGO · DEPLOY), rótulo "SUPER PROMPT", "SUPERA AL 99%" | `fonts/Poppins-Bold.ttf`, `fonts/Poppins-ExtraBold.ttf` (stack STLabs) | `@font-face` base64 en el HTML |
| Barlow Condensed | 500 / 700 | Cuerpo, claims, texto de cajas | `fonts/BarlowCondensed-*.ttf` (stack STLabs) | `@font-face` base64 en el HTML |
| IBM Plex Mono | 400–600 | Footer `sebastian.stlabs.ar`, sublabels de nodos (Claude Design / Claude Code / Vercel), etiquetas "Fase 0–4" | `fonts/IBMPlexMono-*.ttf` (stack STLabs) | `@font-face` base64 en el HTML |

Modo: **blanco** · Textura: **retícula fina (versión clara)** · Familia visual: **blueprint / proceso en pasos**
Acento: verde `#00FFB2` (sin modificar). Logo/ráfaga de Claude: naranja `#D97757` (intacto). Indicador de error: ámbar `#FF9D3C` (énfasis negativo puntual).
Firma en todos los slides: `sebastian.stlabs.ar`. Sin @handle de Instagram · sin contador de slides · sin UI de la app.
