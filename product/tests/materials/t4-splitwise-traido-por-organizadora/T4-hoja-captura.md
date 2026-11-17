---
source: real
ejercicio: prueba-de-revision
---

# T4 · Hoja de captura: no todos instalan, el neto va al chat

Prueba: product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md, T4
Creencia: overview #15 · Procedencia esperada: real
Mensaje de invitación: el mismo del T1 (materials/t1-splitwise-traido-por-organizadora/mensaje-invitacion.md), sin cambios.

## Antes de empezar
- Fecha y hora de envío del link: 13 nov 2026, 20:00
- Número de integrantes del viaje: 6
- Día del regreso (cierre): 15 nov
- Sesgo declarado: Lina es organizadora, sponsor y observadora.

## Por integrante

| Integrante | Procedencia | Entró (fecha y hora, o "no") | Recordatorios para que entrara (n.º y fecha) | ¿Cómo conoció su neto? (app / pantallazo / otro) | ¿Su deuda se calculó con el neto de la app? (sí/no) | ¿Cálculo paralelo? (sí/no · dónde: Excel / chat / otro) |
|---|---|---|---|---|---|---|
| Lina (organizadora) | miembro del segmento | 13 nov, 19:58 | n/a | app | sí | no |
| Natalia | miembro del segmento | 13 nov, 20:10 | 0 | app | sí | no |
| Isabel | miembro del segmento | 13 nov, 22:05 | 0 | pantallazo (lo vio en el chat antes de abrir la app) | sí | no |
| Manuela | miembro del segmento | 14 nov, 07:40 | 0 | app | sí | no |
| Felipe | miembro del segmento | 14 nov, 10:30 | 0 | otro (mensaje de Lina) | sí | no |
| Esteban | miembro del segmento | no | 1 · 14 nov, 18:05 | pantallazo | sí | no |

**Recordatorios:** se permite uno solo, a quien no haya entrado. No le digas a nadie que
instalar es opcional. Si das un segundo recordatorio, anótalo con fecha; eso contamina la señal.

## Gastos grandes (cuota por persona ≥ 20.000)

Anota cada gasto grande pagado por el grupo. Si quien lo pagó no tiene la app, **no intervengas**:
solo anota qué pasa con el gasto.

Las invitaciones (quien paga dice en el momento que va por su cuenta) no son gastos del grupo:
no van en esta tabla. Anótalas en "Notas".

| # | Día | Quién pagó | Qué | Monto | Cuota por persona | ¿Quien pagó tiene la app? (sí/no) | ¿Quedó en la app? (sí/no) | ¿Quién lo registró? | Si no quedó: ¿qué pasó? (se cobró por fuera / quedó sin cobrar / otro) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 14 nov | Lina | Alojamiento (2 noches) | 900.000 | 150.000 | sí | sí | Lina | n/a |
| 2 | 14 nov | Esteban | Gasolina y peajes | 132.000 | 22.000 | **no** | sí | **Natalia** | n/a |
| 3 | 14 nov | Natalia | Mercado | 270.000 | 45.000 | sí | sí | Natalia | n/a |
| 4 | 15 nov | Manuela e Isabel (120.000 cada una) | Lancha | 240.000 | 40.000 | sí | sí | Manuela | n/a |
| 5 | 15 nov | Isabel | Almuerzo | 186.000 | 31.000 | sí | sí | Isabel | n/a |
| 6 | | | | | | | | | |

**Gastos ajenos:** si Lina registra un gasto que pagó otra persona, se anota aquí con "Lina" en "¿Quién lo registró?".

## Pantallazo de "Saldos"
- ¿Alguien lo mandó al chat en las 24 h siguientes al regreso? **sí**
- Quién lo mandó: **Natalia** · Fecha y hora: **15 nov, 21:30**
- ¿Lo tuvo que mandar Lina porque nadie lo hizo? **no** · Fecha y hora: n/a

## Lectura al 16 nov
- ¿Hubo al menos una persona sin la app? **sí (Esteban)** → la #15 se puso a prueba
- a) ¿Todas las deudas se calcularon con el neto de la app, incluidas las de quienes no la tienen? **sí** · Deudas fuera del neto: **0**
- b) Gastos grandes fuera del neto porque quien los pagó no tenía la app: **0** · Gastos ajenos que registró Lina: **0** (¿ambos en cero? **sí**)
- ¿Alguna persona sin la app pagó un gasto grande? **sí** (Esteban, la gasolina) → b se puso a prueba

**Regla de decisión (fijada en el diseño):**
- `continue`: se cumplen a y b.
- `change`: una sola deuda fuera del neto de la app, o un solo gasto grande de alguien sin app quedó fuera o lo registró Lina, y el resto cerró en la app.
- `discard`: dos o más deudas fuera del neto, el grupo cerró con Excel o por el chat, o dos o más gastos grandes quedaron fuera o los registró Lina.
  Causa: gastos de quien no tenía la app que no entraron (→ A5) / pagadores con la app que no registraron (→ A4; se debilita la #9)
- `inconclusive`: todos entraron a la app.

Decisión: **continue**. Se cumplen a y b. El único gasto grande de alguien sin app entró al neto porque lo registró otra integrante (Natalia), no Lina.

## Notas
(preguntas sobre cómo funciona la app, quejas sobre instalar, cualquier cosa fuera del guion)

- 14 nov, 09:15: Esteban le pidió a Natalia en el carro que registrara la gasolina: "Nata, ¿tú metes lo de la gasolina, que yo no tengo eso?". Natalia lo hizo en el momento. Lina no intervino.
- 15 nov, 16:00: invitación de Felipe: cervezas, ≈ 48.000, "estas van por mí". No es gasto del grupo.
- 15 nov, 22:10: queja sobre instalar. Esteban, en el chat: "yo no me bajo más apps, con el pantallazo me sirve".
- Dato para revisar en el análisis: el gasto de Esteban entró porque **otra persona con la app lo registró por él**. La regla solo penaliza los gastos ajenos que registra Lina. Si nadie del grupo lo hubiera hecho, el resultado habría sido `change`.
