---
status: framed
segment: Personas de 20 a 26 años que, en viajes entre amigos donde varios pagan cosas distintas, ponen plata por el grupo (sea o no quien organiza)
personas: valentina-ospina, santiago-mejia, camilo-restrepo, patricia-gomez
---

# Oportunidad: Quien paga por el grupo pierde plata y desgaste recuperándola

En los viajes entre amigos, quien pone plata por el grupo no la recupera completa
ni a tiempo: lo chico no lo cobra por pena y lo grande tiene que perseguirlo, y
algunos terminan negándose a volver a pagar; ahora, porque la evidencia real
(encuesta y entrevistas del 9 nov) mostró que parte del retraso no depende de la
información del deudor, y el viaje del 14 nov permite observarlo desde quien cobra.

## Segmento y personas

- Valentina Ospina (primary) — lo sufre: cobra uno por uno, vuelve a escribir con pena y pierde más de 50.000 por viaje en gastos chicos que no cobra
- Santiago Mejía (tertiary) — no lo sufre según su ficha: paga cosas grandes y las cobra con un audio, que es justo el tipo de cobro que otro deudor no entendió (Sebastián, entrevista simulada)
- Camilo Restrepo (secondary) — no lo sufre: es deudor; con sus olvidos genera la persecución que sufre quien cobra
- Patricia Gómez (negative) — no lo sufre: los aportes se acuerdan y recogen antes del viaje, así que nadie queda adelantando plata
- Faltante: ninguna (Valentina lo sufre)

## Señales

| Señal | Procedencia | Fuente |
|---|---|---|
| Pagadores que dicen "nunca más": "nunca más pago el hospedaje" (Simón, tras recalcular 3 veces); "la próxima la reserva otra, que yo siempre pongo la tarjeta" (Valeria) | real | product/interviews/2026-11-09-1100-julian.md, product/interviews/2026-11-09-1500-ana-maria.md |
| Andrea esperó 3 semanas a Lorena mientras pagaba intereses de la tarjeta | real | product/interviews/2026-11-09-1200-lorena.md |
| Gastos chicos que no se cobran por pena: taxis por 80.000 ("me daba más pena cobrar eso que perderlo") y un desayuno por 90.000 (15.000 por persona) | real | product/interviews/2026-11-09-1000-mariana.md, product/interviews/2026-11-09-1500-ana-maria.md |
| Deudas en "no sé si pagué" porque quien pagó nunca cobró (la comida de Jefferson, una cena) | real | product/interviews/2026-11-09-1400-ricardo.md, product/interviews/2026-11-09-1500-ana-maria.md |
| Kevin persiguió 2 semanas; Simón cobró 3 veces; Ricardo (en el viaje de Juan Pablo) persiguió a Mateo para que entrara a la app | real | product/interviews/2026-11-09-1400-ricardo.md, product/interviews/2026-11-09-1100-julian.md, product/interviews/2026-11-09-1300-juan-pablo.md |
| Los montos pequeños quedan sin cobrar y se cobra días después | real | product/overview.md (observado por Lina) |
| Perseguir a los deudores: 4 menciones en "lo más molesto"; 3 de 13 acreedores tuvieron que cobrar uno por uno porque nadie preguntó | survey (n = 13 acreedores) | product/insights/2026-11-09-0807-encuesta-deudor-real.md |
| Laura: "la próxima la reserva otro"; Daniela ya no paga nada grande para no tener que cobrar; 3 de 4 dejaron gastos propios sin cobrar | synthetic | product/insights/2026-11-09-0836-entrevistas-deudor-sinteticas.md |
| "El problema es tener que cobrarle a cada uno después, uno por uno"; pierde más de 50.000 en gastos chicos por viaje | synthetic | product/personas/valentina-ospina.md |

Límite: las entrevistas fueron a deudores. La voz de quien paga llega de segunda mano, salvo en la encuesta.

## Resultado de negocio

Interno (sponsor: Lina). Mueve la otra mitad de su criterio de continuidad: lo
suelta "si le toca a ella cargar todo y revisar si los demás actualizaron".
Costo evitado: plata que nunca se recupera, cobros repetidos y pagadores que
dejan de poner la tarjeta por el grupo.

## Restricciones

- Presupuesto: proyecto personal, con el tiempo de Lina; sin dinero asignado.
- Datos sensibles: números de cuenta, teléfonos y montos de terceros.
- El segmento vive en el celular durante el viaje.
- Poca tolerancia a la fricción: el grupo no adopta lo que no usan todos y abandona los registros largos.
- Fecha: viaje del grupo el 14 nov 2026; la observación cierra el 21 nov.

## Creencias

Referencias a product/overview.md (registro único).

- [opportunity: quien-paga-pierde-plata-y-persigue] [value] En un viaje típico, al menos 1 de cada 2 personas que pagan por el grupo deja algún gasto sin cobrar o tiene que cobrarle más de una vez a algún deudor. — overview #8
- [opportunity: quien-paga-pierde-plata-y-persigue] [viability] Quien pagó por el grupo sí registrará lo que puso, porque es quien quiere recuperarlo, sin que Lina tenga que cargarlo; el deudor no tiene ese motivo. — overview #9
- Relacionada: [product] [value] overview #1 (cada amigo registra lo suyo, hoy debilitada); la #9 la acota al único que tiene motivo para registrar.

## Agenda de investigación

| Creencia | Instrumento | Decisión que desbloquea | Para cuándo |
|---|---|---|---|
| [value] 1 de cada 2 pagadores deja algo sin cobrar o cobra más de una vez | 1) Datos que ya existen: revisar los chats de 2 o 3 viajes pasados y contar, por pagador, cobros repetidos y gastos que se mencionaron pero nunca se cobraron. 2) Observar el viaje del 14 nov: por pagador, qué puso, qué cobró, cuántas veces y qué recuperó al 21 nov | Si no se cumple, el costo de quien cobra no es central y el foco sigue en las oportunidades del deudor | Chats: 13 nov; viaje: 21 nov 2026 |
| [viability] quien pagó sí registra lo que puso | 1) En los mismos chats y en el viaje: ¿quien paga anuncia lo que puso, incluido lo chico, o solo lo grande? 2) `/design-interview` con pagadores (hoy no hay ninguna entrevista a acreedores): qué anotaron, qué dejaron sin cobrar y por qué | Si los pagadores tampoco registran lo chico, ninguna solución puede depender del registro del pagador, y la #1 queda sin salida por este lado | Viaje: 21 nov; entrevistas: 30 nov 2026 |
| [product] [viability] overview #3 (contradicha 9 nov) | `/research-market`: en las apps gratuitas, ¿quién registra los gastos y qué pasa con lo chico? | Si una app ya resuelve el lado del pagador, la pregunta pasa a ser qué impide adoptarla en este grupo | 13 nov 2026 |

## Ideas candidatas (no evaluadas)

- Fondo común previo (ya estaba en la oportunidad del deudor): nadie adelanta plata, como en el caso de Patricia.
- Cobro individual a cada deudor en vez de un mensaje en el grupo (de los insights reales 9 nov).
- Pedir las llaves de pago de todos antes del viaje (el arreglo de Carolina y de Mariana).
- Que el organizador traiga Splitwise al grupo (el caso de Juan Pablo).
