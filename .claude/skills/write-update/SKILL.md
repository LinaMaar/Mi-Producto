---
name: write-update
description: Redacta un update del trabajo de producto para una persona de la empresa (CEO, Legal, Marketing, Ingeniería, etc.) a partir de lo guardado en product/. Pregunta audiencia, pedido y largo; arma el update en cuatro partes (qué creíamos, qué aprendimos, qué decidimos, qué pedimos) y lo guarda en product/comms/ solo después del OK. Usar cuando pida un update, un resumen para un stakeholder, un reporte de avance o "contale a X cómo vamos".
---

# write-update

Redacta un update de producto para **una** persona de la empresa que construye el producto, con lo que hay en `product/`. El update es para que esa persona decida o actúe, no un informe de todo lo que se hizo.

Escribe en el idioma de la conversación.

## Paso 1 — Preguntar antes de escribir

Hacé las tres preguntas **de a una**, con la herramienta de preguntas (AskUserQuestion), esperando cada respuesta antes de la siguiente. Cada pregunta trae 2–4 opciones de ejemplo; la opción de escribir la propia ya viene incluida ("Otro"), no la agregues.

1. **Para quién es y qué decide o qué le preocupa.**
   Opciones de ejemplo (ajustalas a lo que veas en `product/`):
   - CEO — si seguir invirtiendo en esta apuesta
   - Legal — riesgos de datos personales o de pagos
   - Marketing — qué mensaje y a qué segmento
   - Ingeniería — qué construir y qué tan firme está
2. **Qué le vas a pedir.**
   - Una decisión
   - Un recurso (tiempo, gente, presupuesto)
   - Una aprobación
   - Nada, es informativo
3. **Qué largo.**
   - Dos minutos de lectura, máximo 250 palabras (Recomendado)
   - Un minuto, máximo 120 palabras
   - Cinco minutos, máximo 600 palabras

Si la respuesta a la 2 es un pedido, y el plazo no quedó claro, preguntalo en la misma línea antes de escribir (por ejemplo: "¿para cuándo lo necesitás?"). No inventes el plazo.

## Paso 2 — Leer product/

Leé solo esto, y si algo no existe, omitilo sin comentarlo en el update:

| Qué | Dónde |
|---|---|
| Overview | `product/overview.md` |
| Oportunidad | `product/opportunities/` |
| Pruebas de solución | `product/tests/` (no hace falta abrir `tests/materials/`) |
| Spec | `product/specs/` |
| Plan de exposición | `product/exposure-plans/` |
| Análisis de métricas | `product/insights/*-metrics-*.md` |
| Análisis de feedback | `product/insights/*-feedback-*.md` |

Si hay varios archivos del mismo tipo, usá el más reciente (el nombre empieza con fecha) y los que se refieran a la misma apuesta. Si no sabés cuál es la apuesta vigente, preguntá.

**No inventes datos.** Cada número del update tiene que estar en alguno de esos archivos. Para cada dato, fijate en el archivo si es **real** (personas reales, uso real) o **sintético** (personas o datos simulados). Si el archivo no lo dice, decí "origen no indicado".

## Paso 3 — Escribir el update

Cuatro partes, con estos títulos:

1. **Qué creíamos** — la apuesta en una o dos líneas.
2. **Qué aprendimos** — solo los resultados que le importan a esa persona, según lo que decide o le preocupa. Con números cuando los hay, y marcando cada dato como *(real)* o *(sintético)*.
3. **Qué decidimos** — qué hacemos ahora y por qué, en función de lo aprendido.
4. **Qué pedimos** — un pedido concreto, a esta persona, con plazo. Si no hay pedido: "No te pedimos nada por ahora; es para que estés al tanto."

Reglas:
- **Para quien lo lee.** Incluí lo que necesita para decidir; dejá afuera el proceso, las herramientas y lo que no cambia su decisión.
- **Sin maquillar.** Si algo no funcionó, decilo con claridad y decí qué hacemos con eso. No escondas un resultado malo detrás de uno bueno ni lo suavices con adjetivos.
- **Sin jerga del equipo.** Nada de "T2", "nivel 2", "AARS", "OST", "exposure plan" o nombres internos sin explicarlos en palabras simples (o reemplazalos).
- **Respetá el largo** elegido. Contá las palabras antes de mostrarlo.
- Arriba, una línea con para quién es y la fecha.

## Paso 4 — Mostrar y esperar el OK

Mostrá el borrador **completo** en el chat, con el conteo de palabras, y preguntá si lo guardás o qué cambiar. **No guardes nada hasta que el usuario diga que sí.** Si pide cambios, aplicalos y volvé a mostrar el borrador completo.

## Paso 5 — Guardar

Con el OK, guardalo en `product/comms/` (creá la carpeta si no existe) con este nombre:

`AAAA-MM-DD-HHMM-update-<audiencia>.md`

donde `<audiencia>` es el rol en minúsculas y con guiones (por ejemplo `2026-11-25-1030-update-ceo.md`, `2026-11-25-1030-update-legal.md`). Usá la fecha y hora actuales.

Al final del archivo, agregá una sección corta **Fuentes** con los archivos de `product/` que usaste, para poder rastrear cada dato.
