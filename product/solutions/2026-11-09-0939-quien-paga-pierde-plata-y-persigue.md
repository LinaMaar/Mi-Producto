---
opportunity: quien-paga-pierde-plata-y-persigue
status: chosen
chosen: splitwise-traido-por-organizadora
tests: product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md
---

# Soluciones para: Quien paga por el grupo pierde plata y desgaste recuperándola

## Lo que dice hoy la evidencia
- #8 [value] (1 de cada 2 pagadores deja algo sin cobrar o cobra más de una vez): abierta. Las señales reales la apoyan (4 de 6 entrevistas con gastos chicos sin cobrar; Kevin, Simón y Andrea persiguieron), pero todas se contaron desde el deudor. Ninguna entrevista se le hizo a un acreedor.
- #9 [viability] (quien paga registra lo que puso): abierta, sin evidencia directa. Hay un indicio en contra: el pagador anuncia lo grande y no lo chico. Solo Juan Pablo registró lo chico (las cervezas), y fue porque tenía Splitwise (real).
- #11 (Splitwise traído por la organizadora): abierta; se observa en el viaje del 14 nov. La #3 quedó contradicted y la #1 sigue debilitada.
- Persona primary con más evidencia: Luisa Ríos (derivada de entrevistas reales). Valentina Ospina (sintética) la valida.

## Línea base: lo que hace hoy quien paga
Lo grande se cobra con un mensaje al grupo con el monto por persona y, a veces, la cuenta ("casa 95 por cabeza" y el Nequi). Cuando alguien falta, se insiste por privado. Lo chico se absorbe por pena y cada pagador lleva una nota solo de lo suyo (product/personas/luisa-rios.md, real). Cuando el organizador trae una app (Splitwise), el grupo la usa; esto funcionó en 1 de 3 intentos (product/insights/2026-11-09-0847-entrevistas-deudor-reales.md, real).

## Alternativas
### A1. Fondo común antes del viaje (`fondo-comun-previo`)
Se acuerda un aporte por persona, se recoge antes de salir y los gastos se pagan de esa bolsa; al final se reparte lo que sobre. Mecanismo: quita la necesidad de cobrar, porque nadie adelanta plata. Para Luisa Ríos y Valentina Ospina (primary). Reemplaza el cobro posterior. No es software.

### A2. Cobro completo por privado (`cobro-individual-completo`)
El pagador manda a cada deudor, por privado, un solo mensaje con nombre, monto y cuenta (con una plantilla), en lugar de un mensaje en el grupo. Incluye el arreglo de pedir las llaves de pago antes del viaje (fusionado: mismo mecanismo, que el cobro llegue completo). Ataca la persecución. Para Luisa y Valentina. Reemplaza el cobro en el grupo. No es software.

### A3. La organizadora trae Splitwise al viaje (`splitwise-traido-por-organizadora`)
Lina, como organizadora, crea el grupo antes del viaje y mete a todos. Cada pagador registra lo suyo, la app calcula el neto y manda recordatorios. Ataca el registro, el cálculo y el cobro, incluido lo chico. Para Luisa y Valentina (pagadoras) y Camilo Restrepo (secondary, deudor). Reemplaza el chat y el Excel.

### A4. Bolsa de gastos chicos (`bolsa-de-gastos-chicos`)
Un mensaje fijado en el chat del viaje donde cada quien anota lo chico que pone (taxi, hielo, desayuno). Al final se suma y se cobra en un solo neto por persona, junto con lo grande. Ataca la pena: nadie cobra 9.000, se cobra un total. Para Luisa y Valentina. Es lo más pequeño que podría funcionar. No es software.

### A5. Cobrador del pagador (`cobrador-del-pagador`)
Herramienta propia que usa solo el pagador: anota el gasto y la herramienta manda a cada deudor un cobro individual (monto y cuenta), con recordatorios automáticos, sin que el deudor instale nada. Automatiza la persecución. Para Luisa y Valentina; Camilo lo recibe.

## Comparación
| Alternativa | Desirable | Feasible | Viable | Creencia más riesgosa |
|---|---|---|---|---|
| A1 | mixed: pain evidenced, relief not tested. Traslada la persecución a antes del viaje (product/personas/patricia-gomez.md, synthetic) y pide plata por adelantado: 2 de 17 retrasos fueron por falta de plata (product/insights/2026-11-09-0807-encuesta-deudor-real.md, survey) | strong: nada que construir; 3 de 45 encuestados ya lo usan (survey) | mixed: elimina el cobro, pero alguien queda de tesorero; si es Lina, cae en "le toca a ella cargar todo" (product/overview.md) | Si se propone un aporte fijo para el 14 nov, todos lo ponen antes de salir sin que haya que recordarlo más de una vez |
| A2 | mixed: con lo grande, lo que llega por privado se paga en el momento (Julián D1, Ricardo D1; entrevistas-deudor-reales, real), pero multiplica la queja del pagador ("tocó cobrar uno por uno", survey) y en lo chico la pena crece | strong: es una plantilla de mensaje | weak: evita cobros repetidos, no toca lo chico ni el criterio de la sponsor | Un pagador que cobra por privado a cada deudor recupera todo con un solo mensaje por persona y no lo vive como más trabajo |
| A3 | mixed: única con evidencia sobre la solución. En el viaje de Juan Pablo todos registraron, incluido lo chico, y se pagó el día del regreso; falló en 2 de 3 intentos por adopción (product/interviews/2026-11-09-1300-juan-pablo.md, -1100-julian.md, real). Prueba T1 (viaje 5–10 nov, 6 personas): 5 de 6 entraron; las 6 deudas cerraron con el neto de la app, sin Excel; el que no instaló pagó con un pantallazo del neto (product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md, real) | strong: la app existe y es gratis, y un grupo del segmento la usó (real); `/research-market` de la #3 pendiente | strong: cuando se adopta, cumple el criterio de la sponsor, cada quien registra y se cierra sin Excel (juan-pablo, real) | #15: aunque no todos instalen, quienes pagan registran y quien no tiene la app paga el neto compartido en el chat; todas las deudas cierran con la app y ningún gasto queda fuera por falta de app |
| A4 | mixed: pain evidenced, relief not tested. Que juntar lo chico quite la pena es assumption | strong: un mensaje fijado en WhatsApp | mixed: recupera lo que hoy se pierde (80.000 y 90.000, real), pero alguien tiene que sumar al final | Durante el viaje, quien paga algo chico lo anota en el momento: al menos 3 de cada 4 gastos chicos quedan anotados |
| A5 | mixed: pain evidenced, relief not tested; nadie ha reaccionado a un cobro automático | to check with tech: mensajes automáticos por WhatsApp sin presupuesto; cuentas y teléfonos de terceros | mixed: depende de la #9; la #3 (contradicted) le exige ganarle a una app gratuita (aquí, en que el deudor no instala nada) | Un cobro automático por privado se paga al primer o segundo aviso en al menos 2 de cada 3 deudores, sin que el pagador escriba nada |

## Decisión
Lina eligió A3 para probar el 2026-11-09, igual que la recomendación. Razones: es la única alternativa con evidencia real sobre la solución y no solo sobre el dolor; cuando se adopta, cumple el criterio de continuidad de la sponsor; y el viaje del 14 nov ya estaba planeado para probar la #11. De paso prueba la #9 y si juntar lo chico en un neto quita la pena. Qué cambiaría la decisión: si el grupo no entra a la app, A4 es el plan B sin app; si falla porque los deudores no quieren instalar, A5 gana sentido; si los pagadores no registran lo chico ni con la app, la #9 cae y se vuelve a investigación.

## Por probar
- A3 — #11 (adopción, la que la mata), #12 (gastos chicos) y #13 (nadie cobra dos veces): diseñadas como T1, T2 y T3 en [product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md](../tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md). La #14 queda para después.
- A3 (versión cambiada) — #15: diseñada como T4 en el mismo archivo de pruebas.

## Propuesta de valor: Splitwise traído por la organizadora
- Dolor que alivia: lo chico se pierde por pena (80.000 en taxis, 90.000 de un desayuno) y lo grande hay que perseguirlo (Kevin, 2 semanas; Simón, 3 cobros; Andrea, 3 semanas pagando intereses) (product/personas/luisa-rios.md, real).
- Ganancia: quien paga anota en el momento y se olvida. Lo chico entra al neto sin que nadie tenga que cobrarle 9.000 a un amigo, y el cobro y los recordatorios salen de la app, no de ella.
- Reemplaza: el mensaje al grupo que "se va para arriba", la insistencia por privado y la nota propia de cada pagador. Se cambiaría porque hoy la pena cuesta plata y perseguir cuesta la relación ("nunca más pago el hospedaje").
- Deliberadamente no hace: no construye nada propio, no resuelve el efectivo ni la falta de plata del deudor, no maneja el presupuesto previo (#7) y no incluye grupos mixtos con familia.

## Creencias
- [opportunity: quien-paga-pierde-plata-y-persigue] [value] En un viaje típico, al menos 1 de cada 2 personas que pagan por el grupo deja algún gasto sin cobrar o tiene que cobrarle más de una vez a algún deudor. — overview #8
- [opportunity: quien-paga-pierde-plata-y-persigue] [viability] Quien pagó por el grupo sí registrará lo que puso, porque es quien quiere recuperarlo, sin que Lina tenga que cargarlo; el deudor no tiene ese motivo. — overview #9
- [product] [viability] Si Lina, como organizadora, trae una app gratuita para dividir gastos al viaje del 14 nov, todo el grupo entra y la usa hasta cerrar las cuentas. — overview #11
- [feature: splitwise-traido-por-organizadora] [value] Con la app en el viaje, los gastos chicos se registran y se recuperan dentro del neto: al 21 nov, al menos 3 de cada 4 gastos chicos pagados por el grupo están en la app, y ningún pagador dice haber dejado uno sin cobrar por pena. — overview #12
- [feature: splitwise-traido-por-organizadora] [value] Con el neto y los recordatorios de la app, ningún pagador tiene que escribir más de un cobro a un mismo deudor: al 21 nov, todos los deudores pagaron sin un segundo mensaje escrito por el pagador. — overview #13
- [feature: splitwise-traido-por-organizadora] [viability] Lina solo registra lo que ella pagó: no carga gastos ajenos ni revisa quién actualizó. — overview #14

## Descartadas o estacionadas
- A1 — parked: pide plata por adelantado y traslada la persecución a antes del viaje; no hay evidencia del segmento sobre cómo le va a quien lo usa. Volvería si en el viaje del 14 nov la falta de plata explica la mayoría de los retrasos.
- A2 — parked: multiplica el trabajo "uno por uno" del que se queja el pagador y no toca lo chico; su mecanismo (cobro individual completo) vive dentro de A3 y A5. Volvería como plantilla si A3 y A5 se descartan.
- A4 — parked: plan B sin app. Volvería si el grupo no adopta Splitwise en el viaje del 14 nov.
- A5 — parked: herramienta propia que solo tiene sentido si Splitwise falla porque los deudores no instalan. Volvería con ese resultado y tras revisar la factibilidad con tech.

## Resultado
- A3 — chosen, con cambio (2026-11-10): T1 `failed` porque 1 de 6 no instaló, aunque las 6 deudas cerraron con el neto de la app. La versión cambiada (no todos instalan; el neto se comparte en el chat) necesita su propia prueba. T2 y T3 no corrieron. Ver [product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md](../tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md).
- A5 — parked, con un indicio: un deudor no quiso instalar ("yo no me bajo más apps") y aun así pagó con el pantallazo del neto.
