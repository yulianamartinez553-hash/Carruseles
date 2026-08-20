# Manifiesto de fuentes — Agente simplifica procesos

| Fuente | Peso / estilo | Rol | Origen | Código / comando |
|---|---|---|---|---|
| **Anton** | 400 | Títulos display (ultra-heavy) | Google Fonts `ofl/anton/` → `fonts/Anton-Regular.ttf` | `@font-face` embebido vía `stlabs_kit.embedded_fonts_css()` |
| **Impact** | 400 / 900 | Fallback display super-heavy | `fonts/Impact.ttf` | idem |
| Poppins | 700 / 800 | CTA pill | `fonts/Poppins-Bold.ttf` | idem |
| Barlow Condensed | 400–700 | Cuerpo, subtítulos | `fonts/BarlowCondensed-*.ttf` | idem |
| IBM Plex Mono | 400–600 | Badges, footer | `fonts/IBMPlexMono-*.ttf` | idem |
| Lora | 400–700 itálica | Palabras acento (`OPERATIVO`) | `fonts/Lora-Italic-Variable.ttf` | idem |

Referencia skeleton: `carrusel-studio/references/05-template-html.md` → `--f-display: 'Anton', Impact, …`
