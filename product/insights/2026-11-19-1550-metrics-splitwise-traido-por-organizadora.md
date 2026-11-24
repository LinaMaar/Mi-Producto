---
metrics: product/metrics/2026-11-18-1709-splitwise-traido-por-organizadora.md (versión del nivel 2, commit 61af6c1)
level: 2 — + "Anoten lo de hoy"
data: product/data/2026-11-19-synthetic-nivel2/
period: 2026-12-05 a 2026-12-08 (viaje simulado de 3 días + formulario)
source: synthetic
script: product/insights/2026-11-19-1550-metrics-splitwise-traido-por-organizadora.py
---

> Ensayo con datos sintéticos: prueba el cálculo y las definiciones. No es evidencia sobre el segmento y no anota creencias del overview. El archivo de métricas sigue en `status: designed`. Desde el 2026-11-24 está revisado para el nivel 1; las definiciones con que se leyó este ensayo están en el commit 61af6c1 y se copian abajo.

# Métricas — Splitwise traído por la organizadora, nivel 2 (ensayo)

## Definiciones y metas con que se leyó
Audiencia = pagadores de gastos chicos (cuota < 20.000, sin invitaciones). Corte de cierre = pantallazo de "Saldos". Los registros que hizo la organizadora por otra persona no cuentan.
- `acquisition`: ≥ 1 gasto propio en la app · meta 100 %
- `activation`: ≥ 3/4 de sus gastos chicos en la app al cierre y ninguno fuera por pena · meta ≥ 75 % y 0 por pena
- `retention`: registró lo chico la misma noche (antes de las 06:00) todos los días en que pagó · meta ≥ 60 % y que la curva no baje
- `satisfaction`: CSAT ≥ 4 sobre la audiencia · meta ≥ 60 %, con respuesta ≥ 80 %

Audiencia: 6 (Andrés, Diego, Laura, Sara, Tomás, Valeria; nombres inventados). Diego no tiene la app. Cierre: 7 dic, 20:00.

## Resultados
| Métrica | Numerador / denominador | Ventana | Valor | Meta | Resultado |
|---|---|---|---|---|---|
| `acquisition` | 6 / 6 | link → cierre | 100 % | 100 % | `on target` |
| `activation` | 4 / 6 (1 no activado por pena: Valeria) | al cierre | 67 % | ≥ 75 % y 0 por pena | `below target` |
| `retention` | 4 / 6; curva 100 → 50 → 67 % | por día de viaje | 67 % | ≥ 60 % y que la curva no baje | `below target` (la curva baja) |
| `satisfaction` | 3 / 6; respuesta 5/6 (83 %); entre quienes respondieron 3/5 (60 %) | 8–9 dic | 50 % | ≥ 60 % | `below target` |

Lectura por gasto (plan): 9 / 11 = 82 % (≥ 3/4).
Activación por persona: Andrés 2/3 (olvidó el hielo del día 3) · Valeria 1/2 (helados, por pena) · Diego 1/1 (lo registró Sara) · Laura 2/2 · Sara 2/2 · Tomás 1/1.

## Embudo
De 6 que llegaron, 4 obtuvieron valor (67 %) y esos 4 volvieron (100 % de los activados). La caída está entre llegar y obtener valor.

## Curva de retención (por día del viaje)
| Día | Pagadores de gastos chicos | La misma noche | "Anoten lo de hoy" |
|---|---|---|---|
| 5 dic | Andrés, Diego, Laura, Valeria | 4/4 (100 %) | 21:30, Tomás |
| 6 dic | Andrés, Sara, Tomás, Valeria | 2/4 (50 %) | 23:50, Tomás |
| 7 dic (regreso) | Andrés, Laura, Sara | 2/3 (67 %) | sin mensaje (cierre) |
La curva baja de la primera noche a la última. Con 3 días y 6 personas, la lectura es direccional.

## Contra el plan de exposición
- ¿Al menos 3/4 de los gastos chicos en la app? Sí (82 %).
- ¿Ningún pagador dejó un gasto fuera por pena? No (Valeria). → No se avanza al nivel 3. Tampoco aplica "parar", porque 82 % ≥ 1/2.
- Vacío del plan: la regla de "ajustar" solo cubre el rango 1/2–3/4. No dice qué hacer si queda ≥ 3/4 con un caso de pena.
- Lo heredado del nivel 1 (ni Excel ni cálculo en el chat) queda `not computable`: los datos no traen esos registros.
- Proceso: 2 mensajes de "anoten lo de hoy", los dos de Tomás y con la línea del total. Ninguno lo mandó la organizadora.

## Métricas de negocio
- #14: Laura no registró gastos ajenos (0). Se cumple.
- Criterio de la sponsor: cada uno registró lo suyo (acquisition 100 %). Si cada uno "marcó su pago" queda `not computable`, y lo del Excel también.

## La métrica más baja frente a su meta
`satisfaction`: 50 % contra 60 % (−10 pp). Ojo, puede venir de la definición: la diferencia es exactamente una persona que no respondió. Entre quienes respondieron, el 60 % llega a la meta. La que decide frente al plan es `activation`, por el caso de pena.

## Hipótesis (ordenadas por cuánto de la brecha podrían explicar)
1. **El mensaje de la noche 2 llegó tarde (23:50) y el registro de ese día se cayó.** Lo apoya: la curva pasa de 100 % a 50 %, y Andrés registró la propina a las 10:00 del día siguiente. Se confirma si Andrés y Valeria no vieron el mensaje antes de dormir.
2. **La línea "lo chico se suma al total" no rompe la pena con los gastos que parecen un gusto (helados).** Lo apoya: Valeria dejó los helados por pena, igual que Isabel en el T2 real. Se confirma si quienes dejan algo por pena lo describen como casi una invitación.
3. **El día del regreso no hay "anoten lo de hoy" y lo chico de ese día se olvida.** Lo apoya: Andrés olvidó el hielo del día 3. También es una cuestión de definición de la curva.
4. **La pregunta de satisfacción no le aplica a quien no tiene la app.** Lo apoya: Diego puso un 3 con "no tengo la app, me da igual".

## Lo que deja el ensayo
- La regla del plan no cubre el caso de ≥ 3/4 de gastos en la app con un caso de pena.
- El día del regreso quizá no debería contar en la curva, o necesita su propio "anoten" antes del pantallazo de "Saldos".
- Para leer el criterio de la sponsor faltan registros: si cada uno marcó su pago y si hubo Excel.
