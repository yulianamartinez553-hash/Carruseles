# Línea gráfica STLabs — Sebastián García

> Documento maestro de identidad visual.
> Uso: YouTube y todo contenido de marca a partir de ahora.
> Fuente: síntesis del repositorio Carruseles + sistema de diseño STLabs.

---

## 1. Identidad

| Campo | Valor |
|---|---|
| Marca personal | **Sebastián García** |
| Firma / dominio | **sebastian.stlabs.ar** |
| Territorio | RevOps · CRM · IA |
| Posicionamiento | Arquitecto de soluciones de IA: sistemas, agentes, automatización, soluciones escalables |
| Personalidad visual | Contraste fuerte · tipografía monumental · acento verde puntual · textura física · composición asimétrica · autoridad técnica sin look SaaS genérico |

La marca **no depende de un logo ilustrado**. La identidad se construye con:

1. URL `sebastian.stlabs.ar` en IBM Plex Mono verde
2. Verde neón `#00FFB2` como único acento fuerte
3. Tipografía display Impact / Anton
4. Foto real de Sebastián
5. Alto contraste negro/blanco

---

## 2. Paleta

### Colores oficiales

| Token | HEX | Uso |
|---|---|---|
| **Verde STLabs** | `#00FFB2` | Acento único. Barras de título, subrayados, bordes, URL, chips, CTAs. Máximo 1–2 usos fuertes por frame. |
| **Negro mineral** | `#0A0A0A` | Texto principal en modo claro · fondo base en modo oscuro |
| **Grafito** | `#141414` | Paneles, cards, UI oscura |
| **Grafito medio** | `#1E1E1E` | Cards secundarias, ventanas de código |
| **Blanco** | `#FFFFFF` | Fondo principal (modo vigente) |
| **Blanco cálido** | `#F2F2F2` | Texto sobre negro · fondos cálidos opcionales |
| **Gris** | `#9aa39c` | Texto secundario, meta, timestamps |
| **Rojo** | `#FF5247` | Solo riesgo / urgencia / error. Nunca decorativo |
| **Ámbar** | `#FF9D3C` | Énfasis negativo puntual (muy raro) |

### Tinta sobre verde

| Token | HEX | Uso |
|---|---|---|
| Tinta sobre CTA verde | `#04130b` | Texto sobre botones/barras `#00FFB2` |

### Reglas de color

- `#00FFB2` **no se modifica** (ni más oscuro, ni más claro, ni saturado distinto).
- En fondos claros, el verde **no** se usa como texto de párrafo (poco contraste). Sí en barras, bordes, labels, URL y palabras display.
- El verde no se “esparce”: si todo brilla, deja de ser acento.
- El naranja del mascot Claude (cuando aparece) **permanece naranja**; no se tiñe de verde.

### Modos

| Modo | Fondo | Texto | Cuándo |
|---|---|---|---|
| **Claro (vigente)** | `#FFFFFF` / `#F7F7F5` | `#0A0A0A` | YouTube, thumbnails, educación, piezas actuales |
| **Oscuro** | `#0A0A0A` | `#F2F2F2` | Autoridad, night mode, intros cinematográficas |

---

## 3. Tipografía

### Jerarquía

| Rol | Familia | Peso | Uso |
|---|---|---|---|
| **Título display** | **Impact** (default) · Anton (fallback) | 900 / Ultra | Títulos de video, thumbnails, portadas, claims |
| **Display alternativo** | Bebas Neue | 400 | Números gigantes, countdowns, variantes |
| **Subtítulo / paso** | Poppins | 700–800 | Subheads, pasos, labels de sección |
| **Cuerpo** | Barlow Condensed | 400–700 | Párrafos, bullets, descripción |
| **UI / meta / URL** | IBM Plex Mono | 400–600 | `sebastian.stlabs.ar`, tags, timestamps, CTAs |
| **Acento editorial** | Lora Italic | 400–700 | Una palabra énfasis, siempre en verde |

### Tratamiento de título (firma visual)

Cuando el título necesita impacto de marca:

- Impact / Anton
- Mayúsculas
- Escala monumental (muy grande)
- Inclinado: `italic` + sesgo ~`skewX(-8deg)` cuando hay urgencia
- **Barra rectangular verde `#00FFB2`** detrás de la frase clave
- Texto sobre la barra: blanco o negro (`#04130b` / `#0A0A0A`), nunca gris

### Prohibido en títulos

- Barlow Condensed como título
- IBM Plex Mono como título
- Fuentes finas, system UI (Inter, Roboto, Arial) como display
- Títulos pequeños o “de blog”

---

## 4. Voz y copy

| Sí | No |
|---|---|
| Español argentino, **voseo** (Empezá, Comentá, Deslizá, Querés) | Tuteo español de España |
| Punchy, corto, concreto | Párrafos largos / humo |
| “IA” | “Inteligencia Artificial” |
| Keyword de CTA: `Comentá CLAUDE y te lo mando` | CTAs genéricos sin keyword |
| Técnico operacional (CRM, pipeline, lead) | Inglés decorativo / buzzwords vacíos |
| Firma `sebastian.stlabs.ar` | @handles de Instagram u otras redes |

Sin emojis en piezas de marca.

---

## 5. Lenguaje visual

### Elementos recurrentes

| Elemento | Descripción |
|---|---|
| **Barra verde de título** | Rectángulo `#00FFB2` detrás de 1 línea clave del título |
| **Escuadras / corchetes** | Ángulos L en esquinas (preferencia: inferiores) en verde |
| **Retícula sutil** | Grid fino `~48–60px`, opacidad baja (`.03–.05`) |
| **Glow de esquina** | Radial verde muy suave solo en 1–2 esquinas (abajo) |
| **Textura física** | Ruido/piedra/papel/lino — nunca fondo plano sin atmósfera |
| **Nodo verde** | Círculo `#00FFB2` con número o flecha (transiciones, capítulos) |
| **Cards técnicas** | Fondo blanco o `#141414` / `#1E1E1E`, radio ~16–18px, sombra suave |
| **Ventana de código** | Oscura, dots mac opcionales (`#FF5F57` `#FEBC2E` `#28C840`) |

### Texturas disponibles (rotar, no repetir siempre la misma)

| Token | Sensación |
|---|---|
| `piedra_roca` | Grano mineral sutil |
| `papel_corrugado` | Surcos verticales de cartón |
| `concreto_industrial` | Ruido industrial |
| `reticula_fina` | Grid técnico |
| `lino_tela` | Tejido cruzado suave |
| `roca_volcanica` | Alto contraste + glow verde puntual |
| `gradiente_profundo` | Negro con foco verde tenue |

### Familias de composición (rotar)

1. **Manifiesto** — título enorme + un dato/badge
2. **Blueprint** — proceso / pasos numerados
3. **Operator log** — flujo con microprueba
4. **Dossier editorial** — foto full + texto monumental
5. **Before / After** — dos columnas riesgo vs solución
6. **Dashboard mínimo** — barras, métricas, donas
7. **Guía editorial** — número de capítulo gigante + progreso

---

## 6. Fotografía e imagen

### Sebastián (activo principal)

- Archivo: `seb.jpg`
- Preferir **foto real** sobre render IA
- En modo claro: brillo ~0.9, contraste leve, saturación controlada
- En modo oscuro: brillo ~0.5–0.6 + scrim vertical + glow verde sutil
- Nunca tapar la cara con tipografía

### Mascot Claude (solo contenido Claude)

- Naranja original — **no recolorear a verde**
- Variantes voxel (`bichito-*.png`) o sticker plano (`assets/claude.png`)
- Usar solo cuando el tema es Claude / Claude Code

### Héroes técnicos

- `assets/slide1-hero.png` — monitor / dashboard
- `assets/slide6-hero.png` — Sebastián + paneles
- Válidos para thumbnails y portadas de sistemas/IA

### Prohibido como idea principal

- Robots / cerebros / circuitos genéricos inventados
- 3D plástico SaaS
- Collages de stock sin relación con el producto
- Glow púrpura / estética “AI purple”

---

## 7. Aplicación YouTube

### Thumbnail (1280×720)

Presupuesto visual del primer frame:

1. **Claim** Impact (1–2 líneas) — una con barra verde
2. **Una imagen dominante**: foto de Sebastián **o** mascot/tema (no ambos compitiendo)
3. **Cero clutter**: sin filas de stats, sin pills múltiples, sin badges flotantes sobre la cara
4. Verde solo en barra / 1 acento / URL opcional mínima
5. Contraste extremo: el título debe leerse a tamaño celular

Plantilla tipo:

```
[ Fondo blanco + retícula sutil + glow verde inferior ]
[ TÍTULO IMPACT INCLINADO ]
[ FRASE CLAVE EN BARRA #00FFB2 ]
[ Foto Sebastián a la derecha O bichito/tema a la izquierda ]
[ sebastian.stlabs.ar abajo, mono verde ]
```

### Banner del canal (~2560×1440, safe area central)

Patrón ya validado en cover Facebook del repo:

- Foto de Sebastián a la derecha (~45–55%)
- Scrim negro/verde a la izquierda
- Título de marca + 3–4 chips de servicio
- URL `sebastian.stlabs.ar` en verde
- Retícula / glow sutil

Chips sugeridos:

- Arquitectura de sistemas
- Agentes inteligentes
- Automatización con IA
- Soluciones escalables

### Intro / end screen / community post

| Pieza | Regla |
|---|---|
| Intro corta | Negro o blanco + 1 palabra Impact + flash verde |
| End screen | Fondo claro, barra verde en CTA, URL centrada |
| Community / Shorts cover | Misma tipografía y barra; menos elementos |
| Capítulos en video | Nodo verde con número (estilo costura) |

### Formatos de export

| Pieza | Ratio | Notas |
|---|---|---|
| Thumbnail | 16:9 · 1280×720 | Contraste máximo |
| Banner | 16:9 wide | Safe zone central |
| Shorts / Stories | 9:16 | Título arriba, visual abajo |
| Post cuadrado | 1:1 | Misma línea gráfica |

---

## 8. Firma obligatoria

En toda pieza publicada:

```
sebastian.stlabs.ar
```

- IBM Plex Mono
- Color `#00FFB2`
- Centrada o ancla inferior consistente
- Nunca reemplazar por @usuario de red social

---

## 9. Checklist rápido (cualquier pieza nueva)

1. ¿El verde es `#00FFB2` exacto y aparece 1–2 veces fuertes?
2. ¿El título es Impact/Anton grande (no Barlow/Mono)?
3. ¿Hay barra verde detrás de la frase clave (si aplica)?
4. ¿El fondo tiene atmósfera (retícula/textura), no flat muerto?
5. ¿La foto es real de Sebastián cuando hay persona?
6. ¿Claude (si aparece) sigue naranja?
7. ¿Está `sebastian.stlabs.ar` en mono verde?
8. ¿Copy en voseo, sin emojis, sin “Inteligencia Artificial”?
9. ¿Se ve distinto al último contenido (rotar textura/composición)?
10. ¿Funciona a tamaño celular?

---

## 10. Inventario de activos del repo

| Activo | Ruta |
|---|---|
| Foto Sebastián | `seb.jpg` |
| Claude sticker | `assets/claude.png` |
| Héroes dashboard | `assets/slide1-hero.png`, `assets/slide6-hero.png` |
| Bichitos voxel | `Word/bichito-*.png` (cuando existan en la rama de entrega) |
| Kit tokens/CSS | `stlabs_kit.py` |
| Sistema histórico carruseles | `SISTEMA-DISENO-CARRUSELES-STLABS.md` |
| Memoria de fondos/familias | `stlabs_memory.py`, `historial/` |
| Cover adaptables | `builds/facebook-cover/` |

---

## 11. Resumen ejecutivo (para briefear a otro agente)

> Marca Sebastián García / STLabs. Firma `sebastian.stlabs.ar`.
> Acento único `#00FFB2`. Fondos claros vigentes con retícula/textura sutil.
> Títulos Impact/Anton monumentales, a menudo inclinados, con barra verde detrás de la keyword.
> Cuerpo Barlow Condensed. Meta/URL IBM Plex Mono verde.
> Foto real de Sebastián. Claude siempre naranja si aparece.
> Sin emojis, sin handles, voseo argentino, “IA” no “Inteligencia Artificial”.
> Composición asimétrica, alto contraste, cero estética SaaS púrpura.

Este documento es la **única referencia de línea gráfica** para generar contenido de YouTube y piezas de marca a futuro.
