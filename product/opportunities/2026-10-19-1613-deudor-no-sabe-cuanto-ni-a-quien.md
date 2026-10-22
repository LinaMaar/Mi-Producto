---
status: framed
segment: Grupos de amigos de 20 a 26 años que viajan juntos y donde varias personas pagan cosas distintas
personas: camilo-restrepo, santiago-mejia, valentina-ospina, patricia-gomez
---

# Oportunidad: El deudor no sabe cuánto debe ni a quién

En los viajes de grupos de amigos donde varias personas pagan cosas distintas,
quien debe no sabe con claridad cuánto debe ni a quién, y por eso paga tarde,
paga "a ojo" o paga doble; ahora, porque el grupo tiene un viaje el 14 de
noviembre de 2026 donde el problema se puede observar en vivo.

## Segmento y personas

- Camilo Restrepo (secondary) — lo sufre: cobros fragmentados, pagó 60.000 dos veces, olvida pagar si el cobro llega tarde
- Santiago Mejía (tertiary) — lo sufre: paga "a ojo" y se queda corto o se pasa; además puede bloquear la adopción
- Valentina Ospina (primary) — no lo sufre directamente: es acreedora; recibe las consecuencias (pagos tardíos, 20 min por persona respondiendo "¿cuánto era?")
- Patricia Gómez (negative) — no lo sufre: aportes acordados y recogidos antes del viaje
- Faltante: ninguna
- Nota: la persona primary del producto no es quien sufre esta oportunidad; la creencia de valor depende de los deudores, que son quienes menos quieren "llenar nada"
- Fuera del segmento (decidido): grupos mixtos con familia, consistente con el overview

## Señales

| Señal | Procedencia | Fuente |
|---|---|---|
| Un deudor pregunta "¿cuánto tengo que enviar a este número?": tiene el número, no el monto | real | product/research/2026-04-07-chat-viaje-cuanto-enviar.md |
| El monto se corrige en un minuto (136.300 → 145.300 "contando lo del ceviche"): ni quien cobra lo tiene claro | real | ídem |
| Un deudor aplaza el pago "porque solo tengo efectivo": retraso por medio de pago, no por desconocer el monto | real | ídem |
| La búsqueda "cuanto" en el chat del viaje da 16 resultados | real | ídem |
| Se cobra días después del viaje y es difícil encontrar la información para pagar | real | product/overview.md (observado por Lina), reforzado por la captura |
| Cobros fragmentados, pago doble de 60.000, olvido si el cobro llega tarde | synthetic | product/personas/camilo-restrepo.md |
| Paga "a ojo" y se queda corto o se pasa | synthetic | product/personas/santiago-mejia.md |
| "¿A qué número te paso?" / "¿cuánto era?" (20 min por persona) | synthetic | product/personas/valentina-ospina.md |
| Existen apps gratuitas para dividir gastos | unverified | creencia 3 del overview; sin investigación aún |

## Resultado de negocio

Interno (sponsor: Lina). Mueve la mitad de su criterio de continuidad que
corresponde al deudor: que en un viaje cada deudor pague el monto correcto a la
persona correcta, al terminar el viaje o durante él, sin preguntar
"¿cuánto/a quién?" en el chat y sin que nadie lo persiga. Costo evitado:
preguntas repetidas, montos corregidos, pagos aplazados y pagos dobles.

## Restricciones

- Presupuesto: proyecto personal, con el tiempo de Lina; sin dinero asignado.
- Datos sensibles: el problema involucra números de cuenta, teléfonos y montos de terceros.
- El segmento vive en el celular durante el viaje.
- El segmento tolera poca fricción: no adopta lo que no usa todo el grupo y abandona registros largos.
- Fecha: próximo viaje del grupo el 14 de noviembre de 2026.

## Creencias

Referencias a product/overview.md (registro único).

- [opportunity: deudor-no-sabe-cuanto-ni-a-quien] [value] En un viaje típico del grupo, al menos 1 de cada 3 deudores pregunta en el chat cuánto o a quién pagar, o paga un monto distinto al que debe (de menos, de más o doble). — overview #4
- [opportunity: deudor-no-sabe-cuanto-ni-a-quien] [viability] El retraso en los pagos se explica sobre todo por no saber cuánto y a quién, y no por otras causas (falta de plata hasta la quincena, tener solo efectivo, simple olvido); si esas otras causas pesan más, aclarar el monto no hará que se pague a tiempo. — overview #5
- Relacionada: [product] [value] overview #6 (antes #4); la viabilidad de esta oportunidad la afina.

## Agenda de investigación

| Creencia | Instrumento | Decisión que desbloquea | Para cuándo |
|---|---|---|---|
| [value] 1 de cada 3 deudores pregunta o paga mal | Datos que ya existen: revisar los chats de WhatsApp de 2 o 3 viajes pasados y contar por deudor preguntas "¿cuánto/a quién/a qué número?", montos corregidos y pagos dobles | Si no se cumple, el problema del deudor es débil y conviene reabrir la variante del acreedor (cobro tarde, montos pequeños perdidos) antes de explorar soluciones | 31 oct 2026 |
| [viability] el retraso se debe a no saber cuánto/a quién | 1) La misma revisión de chats, anotando la causa de cada pago tardío (efectivo, plata, olvido, monto). 2) Observar el viaje del 14 nov: registrar cada deuda, cuándo se paga y por qué se demora | Si dominan otras causas (efectivo, liquidez), `/explore-solutions` debe priorizar alternativas que ataquen esas causas (p. ej. el fondo común) por encima de las que solo aclaran montos | Revisión: 31 oct; viaje: 21 nov 2026 |
| [product] [viability] overview #3 (herramienta propia vs. app gratuita) | `/research-market`: qué hacen las apps gratuitas existentes con el "¿cuánto/a quién?" y por qué el grupo no las usa | Si una app gratuita ya resuelve esto, la oportunidad sigue en pie pero cambia la pregunta: qué impide adoptarla | 31 oct 2026 |

## Ideas candidatas (no evaluadas)

- Una aplicación o página para llevar las cuentas del viaje (la idea con la que llegó la oportunidad).
- Fondo común previo: la herramienta estima cuánto costará el viaje, todos ponen ese valor al inicio, y al final se reparte lo que sobre (o se cobra lo que falte). Se cruza con la creencia de presupuesto estimado del overview (#7).
