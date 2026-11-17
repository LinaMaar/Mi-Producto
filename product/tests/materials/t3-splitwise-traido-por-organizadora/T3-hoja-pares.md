---
source: real
ejercicio: prueba-de-revision
---

# T3 · Hoja por par acreedor–deudor

Prueba: product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md, T3
Creencia: overview #13 · Procedencia esperada: real

**Al cierre en la app:** copia cada par del neto final (pantalla "Saldos") con su monto.
**Durante los días siguientes:** cuenta los mensajes de cobro que cada acreedor
escribe en el chat del grupo. Los mensajes por privado salen de la pregunta 2 de la tarjeta (16 nov):
materials/t2-splitwise-traido-por-organizadora/tarjeta-preguntas-cierre.md.

Cómo contar:
- Un mensaje al grupo que nombra o le cobra a varios deudores cuenta como 1 mensaje para cada uno de esos pares.
- Los recordatorios automáticos de la app no cuentan.
- Un pantallazo de "Saldos" cuenta solo si lo manda el acreedor pidiendo que le paguen.

- Fecha de cierre en la app: 15 nov 2026, 20:30

| Acreedor | Deudor | Monto neto | Mensajes en el grupo (n.º, fechas) | Mensajes por privado (n.º, según el acreedor) | Total de mensajes | ¿Hubo un segundo mensaje? (sí/no) | Fecha de pago (app o según el acreedor) | ¿Pagado al 16 nov? (sí/no) |
|---|---|---|---|---|---|---|---|---|
| Lina | Felipe | 312.000 | 1 (15 nov, 21:00) | 1 (15 nov, 23:00) | 2 | sí | 15 nov, 23:35 | sí |
| Lina | Esteban | 180.000 | 0 | 0 | 0 | no | 15 nov, 21:50 | sí |
| Lina | Manuela | 126.000 | 0 | 0 | 0 | no | 15 nov, 22:00 | sí |
| Natalia | Manuela | 30.000 | 0 | 0 | 0 | no | 15 nov, 22:00 | sí |
| Natalia | Isabel | 6.000 | 0 | 0 | 0 | no | 15 nov, 21:40 | sí |
| | | | | | | | | |

## Lectura al 16 nov (única)
- Pares totales: **5**
- a) ¿Todos los pares pagados al 16 nov? **sí** · Pares sin pagar todavía: **0** (no cuentan como fallo)
- b) ¿Cero pares con un segundo mensaje? **no** · Pares con un segundo mensaje: **1 (Lina–Felipe)**
- Pares con un segundo mensaje o sin pagar: **1 de 5** (¿más de 1 de cada 4? **no**, 20 %)

**Regla de decisión (fijada en el diseño):**
- `continue`: se cumplen a y b.
- `change`: a lo sumo 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar.
- `discard`: más de 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar.
- El 16 nov los pares sin pagar no cuentan en estas cuentas, solo los segundos mensajes. Si quedan pares sin pagar y lo demás daría `continue`, el resultado es `inconclusive`.

Decisión: **change**. 1 de 5 pares (20 %) necesitó un segundo mensaje. Todos los pares quedaron pagados.

## Notas
- 15 nov, 21:00: mensaje de Lina en el grupo: "Felipe, cuando puedas lo tuyo 🙏". Nombra solo a Felipe, así que cuenta 1 para ese par.
- 15 nov, 21:30: Natalia mandó el pantallazo de "Saldos" con "para que vean cuánto quedó". **No cuenta** como mensaje de cobro, porque no pide que le paguen. Esteban, Manuela e Isabel pagaron después de ese pantallazo.
- Felipe era el que más debía (312.000), porque no pagó nada grande durante el viaje. Pagó tras el mensaje por privado: "uy perdón, ya".
