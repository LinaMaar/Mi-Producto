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

- Fecha de cierre en la app: ____________

| Acreedor | Deudor | Monto neto | Mensajes en el grupo (n.º, fechas) | Mensajes por privado (n.º, según el acreedor) | Total de mensajes | ¿Hubo un segundo mensaje? (sí/no) | Fecha de pago (app o según el acreedor) | ¿Pagado al 16 nov? (sí/no) |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

## Lectura al 16 nov (única)
- Pares totales: ____
- a) ¿Todos los pares pagados al 16 nov? sí / no · Pares sin pagar todavía: ____ (no cuentan como fallo)
- b) ¿Cero pares con un segundo mensaje? sí / no · Pares con un segundo mensaje: ____
- Pares con un segundo mensaje o sin pagar: ____ de ____ (¿más de 1 de cada 4?)

**Regla de decisión (fijada en el diseño):**
- `continue`: se cumplen a y b.
- `change`: a lo sumo 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar.
- `discard`: más de 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar.
- El 16 nov los pares sin pagar no cuentan en estas cuentas, solo los segundos mensajes. Si quedan pares sin pagar y lo demás daría `continue`, el resultado es `inconclusive`.

Decisión: ____________

## Notas
