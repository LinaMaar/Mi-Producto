---
source: real
ejercicio: prueba-de-revision
---

# T2 · Bitácora de gastos chicos

Prueba: product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md, T2
Creencia: overview #12 · Procedencia esperada: real

Gasto chico = un gasto por el grupo con cuota por persona menor a 20.000.

**Invitaciones:** si quien paga dice en el momento que lo invita ("van por mí"), no va en
la tabla, sino en la sección "Invitaciones" de abajo, y no cuenta en el total.

**Durante el viaje:** anota cada gasto chico que veas pagar por el grupo. No le digas
a nadie que lo registre, ni le preguntes si lo hizo. La última columna se llena al
cierre, cruzando con los gastos de la app.

| # | Día | Quién pagó | Qué | Monto | N.º de personas | Cuota por persona | Origen (bitácora / pregunta de cierre) | ¿Quedó en la app? (sí/no) |
|---|---|---|---|---|---|---|---|---|
| 1 | 14 nov | Felipe | Hielo y agua en la estación de gasolina | 24.000 | 6 | 4.000 | bitácora | no |
| 2 | 14 nov | Lina | Parqueadero en el pueblo | 30.000 | 6 | 5.000 | bitácora | sí |
| 3 | 15 nov | Natalia | Pan y huevos para el desayuno | 18.000 | 6 | 3.000 | bitácora | sí |
| 4 | 15 nov | Manuela | Mecato en la tienda | 36.000 | 6 | 6.000 | bitácora | sí |
| 5 | 15 nov | Natalia | Propina del lanchero | 60.000 | 6 | 10.000 | bitácora | sí |
| 6 | 15 nov | Isabel | Helados después del almuerzo | 54.000 | 6 | 9.000 | bitácora | no |
| 7 | 14 nov | Manuela | Dos bolsas de hielo en la noche | 12.000 | 6 | 2.000 | pregunta de cierre | no |
| 8 | | | | | | | | |

El 16 nov, agrega abajo los gastos chicos que salgan de la pregunta de cierre
(origen: "pregunta de cierre"), si no estaban ya en la tabla.

- El #7 salió de la pregunta de cierre a Manuela (15 nov). No lo vi pagar durante el viaje.

## Invitaciones (anunciadas en el momento; no cuentan en el total)

| Día | Quién invitó | Qué | Monto aprox. | Qué dijo (textual) |
|---|---|---|---|---|
| 15 nov | Felipe | Cervezas en la playa | 48.000 | "Estas van por mí" |
| | | | | |

## Lectura al 16 nov
- Gastos chicos en la app: **4** · Gastos chicos totales: **7** · a) proporción: **4/7 ≈ 0,57** (¿≥ 3/4? **no**)
- b) Pagadores que dijeron haber dejado un gasto chico por fuera **por pena**: **1 (Isabel)** (¿cero? **no**)

**Regla de decisión (fijada en el diseño):**
- `continue`: se cumplen a y b.
- `change`: a queda entre 1/2 y 3/4, o un solo pagador dejó un gasto por pena.
- `discard`: a < 1/2. Cae la #12 y se debilita la #9.

Decisión: **change**. a = 0,57 (entre 1/2 y 3/4), y un solo pagador dejó un gasto por fuera por pena.

## Notas
(gastos dudosos, recordatorios que hayas dado sin querer)

- Ningún recordatorio para registrar. Nadie preguntó si había que meter lo chico.
- #1: Felipe nunca entró a registrar nada (0 gastos en la app). En el cierre dijo que "no valía la pena".
- #5: la propina la registró Natalia el mismo día, con la foto del recibo de la lancha.
- Las cervezas de Felipe quedaron como invitación porque lo dijo en el momento.
