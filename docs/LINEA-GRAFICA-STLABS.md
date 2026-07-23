# Línea gráfica STLabs — Sebastián García

> **Documento maestro de identidad visual.**  
> Uso: YouTube, Shorts, banners, posts, thumbnails y **cualquier** pieza de marca.  
> Fuente: sistema STLabs del repo + correcciones de todos los chats del canal Carruseles.  
> Prioridad: ante duda, este documento + las referencias visuales aprobadas ganan sobre improvisación.

---

## 0. Brief para cualquier agente (copiar/pegar)

```
Marca: Sebastián García / STLabs · Firma: sebastian.stlabs.ar (IBM Plex Mono, #00FFB2)
Acento único: verde neón #00FFB2 (barras, líneas tech, glows, nodos, CTAs, URL)
Títulos: Impact / Anton — monumentales, creativos, variables (rectos / inclinados / grandes / chicos)
Tipografía código: IBM Plex Mono en labels, UI, terminales, firma
Fondo vigente: blanco + retícula/líneas sutiles + textura física + glow verde en esquinas inferiores
Mecánicas: flechas, cuadros/cards, corchetes, nodos verdes, números/flechas partidos por costura,
  barras verdes detrás de keywords, ventanas de código, before/after, badges, pipeline
Foto: Sebastián real (seb.jpg). Claude: bichito naranja EXACTO (nunca regenerar ni teñir de verde)
Voz: español AR voseo · sin emojis · “IA” no “Inteligencia Artificial” · sin @handles
Regla #1: NADA tapa texto, logos ni firma. Si no entra, achicar o dividir.
```

---

## 1. Identidad

| Campo | Valor |
|---|---|
| Marca personal | **Sebastián García** |
| Firma / dominio | **sebastian.stlabs.ar** |
| Territorio | RevOps · CRM · IA |
| Posicionamiento | Arquitecto de soluciones de IA: sistemas, agentes, automatización, soluciones escalables |
| Personalidad | Contraste fuerte · tipografía monumental · verde neón tecnológico · textura física · asimetría · look de código/ops · impacto creativo sin estética SaaS genérica |

La marca **no depende de un logo ilustrado**. Se construye con:

1. URL `sebastian.stlabs.ar` en mono verde  
2. Verde neón `#00FFB2`  
3. Títulos Impact / Anton  
4. Foto real de Sebastián  
5. Elementos UI/tech (líneas, flechas, cuadros, código, nodos)  
6. Alto contraste negro/blanco  

---

## 2. Paleta (definitiva)

> **Corrección de chats:** el verde oficial es `#00FFB2`.  
> Valores antiguos tipo `#7DF0AE` quedan **obsoletos**.

| Token | HEX | Uso |
|---|---|---|
| **Verde STLabs / neón** | `#00FFB2` | Acento único. Barras de título, líneas tech, subrayados, bordes, glows, nodos, chips, CTAs, URL, palabras display |
| **Tinta sobre verde** | `#04130b` | Texto sobre botones/barras verdes |
| **Negro mineral** | `#0A0A0A` | Texto en modo claro · fondo en modo oscuro |
| **Grafito** | `#141414` | Paneles, cards oscuras |
| **Grafito medio** | `#1E1E1E` | Cards secundarias, ventanas de código |
| **Borde panel** | `#2A2A2A` | Bordes sutiles de UI |
| **Blanco** | `#FFFFFF` | Fondo principal (modo vigente) |
| **Blanco cálido** | `#F2F2F2` | Texto sobre negro · fondos cálidos |
| **Gris** | `#9aa39c` | Texto secundario, meta, timestamps |
| **Rojo** | `#FF5247` | Solo riesgo / ANTES / error. Nunca decorativo |
| **Ámbar** | `#FF9D3C` | Énfasis negativo puntual (raro) |
| **Naranja Claude** | `#D97757` / naranja del asset | Solo mascot Claude — **nunca teñir a verde** |
| **Dots mac (código)** | `#FF5F57` `#FEBC2E` `#28C840` | Ventanas terminal |

### Reglas de color

- `#00FFB2` **no se modifica** (ni más oscuro, ni más claro, ni otro verde).
- En fondos claros: verde **no** es texto de párrafo. Sí barras, bordes, labels, URL, display, líneas neón.
- Máximo **1–2 usos fuertes** de verde por frame (más glows/líneas sutiles).
- Glow neón permitido pero **controlado** (esquinas, nodos, barras) — no “todo brilla”.
- Claude permanece **naranja**.

### Modos

| Modo | Fondo | Texto | Cuándo |
|---|---|---|---|
| **Claro (vigente)** | `#FFFFFF` / `#F7F7F5` + retícula/textura | `#0A0A0A` | YouTube, educación, piezas actuales |
| **Oscuro** | `#0A0A0A` + textura | `#F2F2F2` | Autoridad, intros, night |

---

## 3. Tipografía

### Stack

| Rol | Familia | Peso | Uso |
|---|---|---|---|
| **Título display (default)** | **Impact** · **Anton** | Super/Ultra Heavy | Portadas, thumbnails, claims, CTAs |
| Display alternativo | Bebas Neue | 400 | Números gigantes, countdowns |
| Subtítulo / paso | Poppins | 700–800 | Subheads, pasos, flecha del nodo |
| Cuerpo | Barlow Condensed | 400–700 | Párrafos, bullets — **jamás título** |
| **Código / UI / firma** | **IBM Plex Mono** | 400–600 | `sebastian.stlabs.ar`, tags, terminal, labels, timestamps — **jamás título** |
| Acento editorial | Lora Italic | 400–700 | Una palabra énfasis, siempre en verde |

### REGLA DE TÍTULOS (crítica — pedida en múltiples chats)

Los títulos son el **héroe visual**. Deben verse creativos e impactantes.

| Variante | Cómo | Cuándo |
|---|---|---|
| **Monumental** | Impact/Anton ~100–132px+ · mayúsculas | Portada, thumbnail, claim principal |
| **Inclinado / tech** | `italic` + `skewX(-6° a -10°)` · más alto y grueso | Urgencia, clones estilo Brody, energía |
| **Recto** | sin skew · Impact pesado | Autoridad, tutoriales sobrios |
| **Horizontal / barra** | 1 línea dentro de rectángulo `#00FFB2` | Keyword / punchline |
| **Jerarquía creativa** | 1 línea enorme + 1 línea chica abajo | Contraste tipográfico impactante |
| **Split creativo** | línea 1 negra + línea 2 blanca sobre barra verde | Firma visual STLabs |
| **Degradé en letras** | gradiente mint→`#00FFB2`→oscuro (clip text) | Solo display gigante, nunca cuerpo |
| **Slash / código** | `/nombre-comando` en display + underline verde | Skills, comandos, reglas |

**Defaults de tamaño (referencia canvas 1080×1350; escalar a YouTube 16:9)**

- Título principal: **~100–132px** (o equivalente proporcional)
- Subtítulo: **42–52px** Poppins
- Cuerpo: **30–36px** Barlow
- Label mono: **20–24px**

**Prohibido en títulos:** Barlow Condensed, IBM Plex Mono, Inter fino, Roboto/Arial/system, títulos “de blog”.

---

## 4. Catálogo completo de elementos visuales

> Pedido explícito: **líneas, flechas, cuadros, todo**.  
> Estos elementos forman parte de la marca y deben estar disponibles siempre.

### 4.1 Líneas y neón tecnológico

| Elemento | Spec |
|---|---|
| **Retícula sutil** | Grid ~48–60px · `rgba(10,10,10,.03–.05)` en claro · equivalente en oscuro |
| **Líneas tech verdes** | 1–3px `#00FFB2` · subrayados, divisores, acentos de layout |
| **Barra rectangular de título** | Rectángulo sólido `#00FFB2` detrás de la frase clave · padding generoso · texto blanco o `#04130b` |
| **Underline grueso** | 6–10px verde bajo palabra/slash |
| **Glow / luz neón** | `radial-gradient` verde en esquinas inferiores · `box-shadow` suave en nodos/barras · nunca glow púrpura |
| **Barra de progreso** | Track oscuro + fill `#00FFB2` |

### 4.2 Flechas y continuidad

| Elemento | Spec |
|---|---|
| **Flecha de flujo `→`** | Entre pasos/logos · gris `#9aa39c` o verde · nunca sobre texto |
| **Nodo-flecha partido** | Círculo Ø156 · borde 2px verde · `→` Poppins 800 74px · mitad en un frame, mitad en el siguiente · `top≈597` en canvas 1080×1350 |
| **Nodo-número partido** | Círculo Ø168 · fondo `#00FFB2` · número Impact italic · posición **alternada** (arriba / medio / abajo) · se completa al pasar de slide/frame |
| **Deslizá →** | Prompt opcional mono gris (solo si aporta UX) |

### 4.3 Cuadros, marcos, paneles

| Elemento | Spec |
|---|---|
| **Card clara** | Blanco · borde `1.5px rgba(10,10,10,.10)` · radius 16–20 · sombra suave |
| **Card oscura** | `#141414` / `#1E1E1E` · borde `#2A2A2A` · radius ~20 |
| **Pill / badge** | Negro o verde · mono uppercase · tags tipo `HABILIDAD 01` / `PASO 1` |
| **CTA pill** | Fondo `#00FFB2` · texto `#04130b` · mono |
| **CTA outline** | Borde 3px verde · fondo blanco · underline verde en keyword |
| **Corchetes / escuadras L** | Esquinas (preferencia inferiores) · 3px `#00FFB2` |
| **Ventana de código** | Oscura · dots mac · mono · look terminal |
| **Tape / cinta** | Overlay físico opcional (editorial) |
| **Before / After** | Dos columnas · ANTES con rojo tipográfico · DESPUÉS con borde/acento verde · flecha central |
| **Badge numérico** | Círculo/cuadrado redondeado negro o verde · número blanco/verde |
| **Checklist** | Check en verde |
| **Pipeline / barras** | Embudo o barras métricas · acento verde en la hero |
| **VS circular** | Divisor entre comparativas |
| **iPhone CSS** | Mockup titanio con tilt (cuando el contenido lo pida) |
| **Donas %** | Verde = IA · gris = resto |

### 4.4 Logos e iconos de producto

- Logos reales (GitHub, Slack, Gmail, etc.): **exactos**, nunca reinventados.  
- Si se ven chicos: **agrandar** (corrección reiterada).  
- Claude: solo el **bichito naranja aprobado** (asset del repo / recorte de referencia). Prohibido regenerar.

---

## 5. Fondos y atmósfera

### Modo claro vigente

```
blanco #FFFFFF
+ retícula / líneas muy sutiles
+ textura física atenuada (piedra, papel, lino…)
+ glow verde en esquinas inferiores
+ escuadras L verdes (opcionales pero de marca)
```

### Texturas a rotar

| Token | Sensación |
|---|---|
| `piedra_roca` | Grano mineral |
| `papel_corrugado` | Surcos verticales |
| `concreto_industrial` | Ruido industrial |
| `reticula_fina` | Grid técnico |
| `lino_tela` | Tejido cruzado |
| `roca_volcanica` | Alto contraste + glow |
| `gradiente_profundo` | Negro con foco verde |

**Regla:** no repetir siempre la misma textura/composición. Rotar.

### Familias de composición

1. Manifiesto — título enorme + badge  
2. Blueprint — pasos / grid  
3. Operator log — flujo + microprueba  
4. Dossier editorial — foto full + texto monumental  
5. Before/After — dos columnas  
6. Dashboard mínimo — métricas / donas / barras  
7. Guía editorial — número de capítulo + progreso  

---

## 6. Fotografía e imagen

### Sebastián

- Asset: `seb.jpg` (referencia permanente de perfil)  
- Preferir **foto real**  
- Claro: brightness ~0.9 · Oscuro: ~0.5–0.6 + scrim + glow verde  
- **Nunca** tipografía sobre la cara  

### Claude (bichito)

- Asset exacto: `assets/claude.png` / `bichito-*.png` / recorte de referencia  
- **Recortar y pegar** — no recrear  
- Color naranja **inmutable**  
- Solo en contenido Claude  

### Héroes técnicos

- `assets/slide1-hero.png`, `assets/slide6-hero.png`  

### Prohibido como idea principal

Robots/cerebros/circuitos inventados · 3D plástico SaaS · glow púrpura · stock genérico sin contexto · solapar texto.

---

## 7. Voz y copy

| Sí | No |
|---|---|
| Español argentino **voseo** | Tuteo ES / inglés decorativo |
| Punchy, corto | Párrafos largos |
| “IA” | “Inteligencia Artificial” |
| Keyword CTA (`Comentá CLAUDE…`) | CTA vacío |
| Firma `sebastian.stlabs.ar` | @handles IG u otras redes |
| Sin emojis | Emojis |

Caption / BytePost: máximo ~500 caracteres cuando se pida post social.

---

## 8. Regla #1 de layout (corrección más repetida)

> **NINGÚN elemento tapa texto, títulos, logos ni firma.**  
> Cero solapamiento. Si no entra: achicar, mover o dividir contenido.  
> Nada se sale del margen seguro.

Márgenes de referencia (canvas 1080×1350): top ~90 · bottom ~110 · laterales ~72.  
Escalables a YouTube 16:9.

---

## 9. Aplicación YouTube

### Thumbnail 1280×720

1. Claim Impact creativo (recto **o** inclinado; grande + línea chica opcional)  
2. Barra verde / líneas neón en la keyword  
3. Una imagen dominante: Sebastián **o** tema/bichito  
4. Retícula + glow inferior  
5. Legible en celular  

### Banner canal

Foto Sebastián derecha · scrim izquierda · chips de servicio · URL verde · retícula/glow.

### Intro / end / Shorts / community

Misma tipografía, misma barra/líneas verdes, mismos nodos/números si hay capítulos.  
Menos clutter, mismo ADN.

| Pieza | Ratio |
|---|---|
| Thumbnail | 16:9 · 1280×720 |
| Banner | 16:9 wide |
| Shorts | 9:16 |
| Post | 1:1 |

---

## 10. Firma obligatoria

```
sebastian.stlabs.ar
```

IBM Plex Mono · `#00FFB2` · visible · nunca tapada · nunca reemplazada por @usuario.

---

## 11. Limpieza de piezas ajenas

Eliminar siempre:

- Firmas / créditos de terceros (`Hecho por…`, watermarks)  
- UI de captura de Instagram (contadores 02/07, Follow, handles ajenos)  
- Texto inglés si el brief es español  
- Elementos que pisen títulos  

---

## 12. Checklist final

1. Verde = `#00FFB2` exacto  
2. Título Impact/Anton grande y creativo (recto/inclinado/jerárquico según pieza)  
3. Barra o líneas verdes tech donde aporten impacto  
4. Tipografía mono en look código/firma  
5. Flechas / cuadros / nodos disponibles y legibles  
6. Fondo con atmósfera (no flat muerto)  
7. Glow/escuadras verdes inferiores si aplica  
8. Sebastián foto real si hay persona  
9. Claude naranja exacto si aparece  
10. Nada tapa nada  
11. `sebastian.stlabs.ar` visible  
12. Voseo · sin emojis · “IA”  
13. Pieza distinta a la anterior (rotar textura/composición)  
14. Funciona en celular  

---

## 13. Inventario de activos

| Activo | Ruta |
|---|---|
| Foto Sebastián | `seb.jpg` |
| Claude sticker | `assets/claude.png` |
| Bichitos voxel | `Word/bichito-*.png` / builds |
| Héroes | `assets/slide1-hero.png`, `slide6-hero.png` |
| Kit CSS/tokens | `stlabs_kit.py` |
| Sistema carruseles (histórico) | `SISTEMA-DISENO-CARRUSELES-STLABS.md` |
| Skill mecánicas | `.claude/skills/carrusel-stlabs/references/` |
| Memoria fondos | `stlabs_memory.py`, `historial/` |

---

## 14. Correcciones de chats incorporadas (historial)

| Pedido de Yuli | Cómo quedó en la marca |
|---|---|
| Fondo blanco en piezas | Modo claro vigente |
| Verde `00FFB2` reemplaza color principal de refs | Paleta oficial |
| Títulos más gruesos / Impact+Anton ~100px | Stack display |
| Fuente de referencia más inclinada, gruesa y alta | Variante inclinada + skew |
| Barra rectangular detrás de letras (naranja→verde) | Barra `#00FFB2` |
| Bichito Claude exacto, recortar no recrear | Asset naranja inmutable |
| Foto perfil Sebastián siempre | `seb.jpg` |
| Líneas sutiles en fondo | Retícula |
| Verde en esquinas inferiores | Glow + escuadras |
| Números mitad/mitad entre hojas, posición alternada | Nodos número |
| Flechas, cuadros, todo el kit UI | Catálogo §4 |
| Tipografía que parece código | IBM Plex Mono |
| Luces / neón tecnológicos | Glow + líneas verdes |
| Títulos creativos: rectos, inclinados, grandes, chicos | Variantes §3 |
| Apps/íconos más grandes, legibles | Regla logos |
| Nada tape textos | Regla #1 |
| Quitar créditos ajenos | Limpieza §11 |
| Español (no inglés salvo pedido) | Voz |
| Línea gráfica para YouTube / marca completa | Este documento |

---

## 15. Resumen ejecutivo

> **STLabs / Sebastián García.** Firma `sebastian.stlabs.ar`.  
> Acento neón `#00FFB2`. Títulos Impact/Anton monumentales y creativos (rectos o inclinados, con barra/líneas verdes).  
> Look tecnológico: retícula, glows, flechas, cuadros, nodos, ventanas de código, mono.  
> Fondo claro + textura. Foto real. Claude naranja exacto.  
> Cero solapes. Voseo. Sin emojis. Sin handles.  
> Esta es la **única referencia de línea gráfica** para YouTube y contenido de marca a futuro.
