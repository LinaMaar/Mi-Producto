---
source: synthetic
generado: 2026-11-19 por Claude, a pedido de Lina, para ensayar /analyze-metrics
metricas: product/metrics/2026-11-18-1709-splitwise-traido-por-organizadora.md
nivel: 2 — + "Anoten lo de hoy"
---

# Viaje simulado (synthetic) — nivel 2

Ensayo del cálculo. No es evidencia sobre el segmento y no anota creencias del overview.
Los nombres son inventados para no confundirlos con el grupo real.

- Viaje: 5 al 7 dic 2026 (3 días). Regreso y cierre = 7 dic.
- Grupo: Laura (organizadora), Tomás (manda "anoten lo de hoy"), Sara, Andrés, Valeria, Diego (no instaló la app).
- Gasto chico = cuota por persona < 20.000 (6 personas → monto < 120.000).

Archivos:
- `actividad_splitwise.csv` — un gasto por fila, del historial de actividad (creado_en = fecha y hora de creación).
- `bitacora_gastos_chicos.csv` — gastos chicos vistos por la observadora + los de la pregunta de cierre; `id_app` enlaza con la actividad.
- `pregunta_cierre.csv` — respuestas a "¿Pagaste algo por el grupo que no quedó en la app? ¿Qué fue y por qué no lo metiste?".
- `chat.csv` — mensajes de proceso: "anoten lo de hoy", pantallazo de Saldos, link del formulario.
- `satisfaccion.csv` — respuestas del formulario CSAT.
- `pagos.csv` — pago de cada neto.
