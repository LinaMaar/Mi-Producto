---
feature: splitwise-traido-por-organizadora
opportunity: product/opportunities/2026-11-09-0901-quien-paga-pierde-plata-y-persigue.md
solutions: product/solutions/2026-11-09-0939-quien-paga-pierde-plata-y-persigue.md
tests: product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md
status: ready
critique: product/insights/2026-11-17-1703-critique-splitwise-traido-por-organizadora.md
---

# Splitwise traído por la organizadora

## Problema
En los viajes del grupo, quien pone plata por los demás no la recupera completa ni a tiempo. Lo chico no lo cobra por pena, lo grande tiene que perseguirlo, y hay quien termina diciendo "nunca más pago el hospedaje". Para Lina, como sponsor, el riesgo es otro: si le toca cargar todo y revisar quién actualizó, lo suelta. Es el momento porque el T4, con el grupo real, mostró que una app gratuita traída por la organizadora cierra todas las deudas con un solo neto aunque no todos la instalen. Pero lo chico y el segundo cobro siguieron fallando (T2 y T3).

> Evidencia: "Me daba más pena cobrar eso que perderlo." — Mariana (Luisa Ríos), product/insights/2026-11-09-0847-entrevistas-deudor-reales.md
> Evidencia: "Simón. Hizo tres cuentas. En el grupo dijo 'nunca más pago el hospedaje'." — Julián (Luisa Ríos), product/interviews/2026-11-09-1100-julian.md
> Evidencia: "Si el que organiza ya usa algo, todos entran. Si lo propone uno cualquiera, no." — Juan Pablo, product/interviews/2026-11-09-1300-juan-pablo.md
> Evidencia: "Qué oso cobrar helados, eran como 9 mil por cabeza." — Isabel, T2 (real), product/tests/materials/t2-splitwise-traido-por-organizadora/T2-T3-tarjeta-preguntas-cierre.md

Propuesta de valor y lo que reemplaza: ver product/solutions/2026-11-09-0939-quien-paga-pierde-plata-y-persigue.md, sección "Propuesta de valor". No se reescribe aquí.

## Para quién
- **Luisa Ríos (primary):** pone plata por el grupo y quiere recuperarla sin cobrar dos veces. Es quien tiene motivo para registrar. (product/personas/luisa-rios.md)
- **Camilo Restrepo (secondary):** es deudor. Recibe el neto y paga, y puede no instalar la app, como Esteban en el T1 y el T4. (product/personas/camilo-restrepo.md)
- **Lina, organizadora y sponsor:** arma el grupo y registra solo lo que ella paga.
- Fuera de foco: grupos mixtos con familia.

## Recorrido de Luisa
1. **Disparador.** Se arma el viaje. Antes de salir, la organizadora manda al chat el link del grupo en Splitwise con una sola línea: "para no hacer Excel". (T1, T4)
2. **Entrar.** Luisa entra desde el link. A quien no ha entrado le llega un solo recordatorio por privado. Si no quiere instalar, nadie insiste. (T4: 5 de 6 entraron)
3. **Lo grande.** Luisa paga el mercado y lo registra en el momento. Si quien paga algo, grande o chico, no tiene la app, lo manda al chat y lo registra alguien que sí la tenga, y ese alguien no es la organizadora. (T4 lo vio con un gasto grande: Esteban le pidió a Natalia; con lo chico, no probado)
4. **Lo chico.** Luisa paga el hielo. Aquí es donde hoy se pierde: 3 de 7 gastos chicos quedaron fuera (T2). Cada noche, el integrante que quedó nombrado antes del viaje, que nunca es la organizadora, escribe en el chat "anoten lo de hoy", y Luisa mete lo chico. *(no probado)*
5. **Cierre.** El día del regreso, el grupo cierra en la app. Alguien manda al chat el pantallazo de "Saldos", y si nadie lo hace en 24 h, la organizadora lo manda una vez. Quien no tiene la app conoce su neto por ese pantallazo. (T4)
6. **Cobro.** Como acreedora, Luisa le manda a cada deudor por privado un solo cobro completo, con nombre, monto del neto y cuenta. Lo copia de un mensaje armado con lo que sale en "Saldos", sin escribirlo desde cero. *(no probado; viene del insight 2 de las entrevistas reales)*
7. **Resultado.** Aquí está el valor: Luisa recupera todo, incluido lo chico, el mismo día o al siguiente, sin escribirle dos veces a nadie y sin Excel. La organizadora no cargó gastos ajenos.

## Historias críticas

### 1. Entrar al grupo antes del viaje
Como Luisa, quiero entrar al grupo del viaje desde un link antes de salir, para registrar lo mío desde el primer gasto.

Criterios de aceptación:
- [ ] La organizadora crea el grupo en la app y manda el link al chat antes del día de salida.
- [ ] El mensaje trae solo el link y una línea de por qué. No trae tutorial, reglas ni incentivos.
- [ ] Quien no ha entrado recibe a lo sumo un recordatorio por privado.
- [ ] Caso borde: si alguien no instala, el viaje sigue sin esa persona en la app y su parte sale igual en el neto.

Traza a: insight 3 de product/insights/2026-11-09-0847-entrevistas-deudor-reales.md; T1 y T4 (real).

### 2. El gasto de quien no tiene la app entra igual
Como Luisa, quiero que lo que paga alguien sin la app quede en el neto, para que la cuenta salga completa.

Criterios de aceptación:
- [ ] Todo gasto con cuota por persona ≥ 20.000 queda registrado en la app el mismo día.
- [ ] Quien no tiene la app manda al chat cualquier gasto que pagó por el grupo, grande o chico.
- [ ] Ese gasto lo registra otro integrante con la app, con "pagado por" a nombre de quien pagó.
- [ ] La organizadora no registra gastos pagados por otros.
- [ ] Caso borde: un gasto pagado entre dos se registra con los dos como pagadores.

Traza a: T4 (real, passed, con un gasto grande); overview #14 y #15; crítica sintética (lo chico de quien no tiene la app).

### 3. Lo chico entra el mismo día
Como Luisa, quiero que lo chico que pago entre al neto sin tener que cobrarlo aparte, para no perderlo por pena.

Criterios de aceptación:
- [ ] Antes del viaje queda nombrado quién manda cada noche "anoten lo de hoy", y no es la organizadora.
- [ ] Cada noche del viaje, esa persona manda el mensaje al chat.
- [ ] Los gastos con cuota por persona menor a 20.000 se registran en la app el día en que se pagaron.
- [ ] Al cierre, al menos 3 de cada 4 gastos chicos están en la app.
- [ ] Caso borde: un gasto que quien lo paga anuncia en el momento como invitación ("van por mí") no se registra y no cuenta.

Traza a: insight 4 de product/insights/2026-11-09-0847-entrevistas-deudor-reales.md; T2 (real, `change`).

### 4. Cierre y un solo cobro por deudor
Como Luisa, quiero que al regresar cada deudor sepa cuánto me debe y reciba un solo cobro completo, para no tener que escribirle dos veces.

Criterios de aceptación:
- [ ] El día del regreso, el grupo se cierra en la app y el pantallazo de "Saldos" llega al chat en menos de 24 h. Si nadie lo manda, la organizadora lo manda una vez.
- [ ] Cada acreedor le manda a cada deudor por privado un mensaje con nombre, monto del neto y cuenta.
- [ ] El acreedor no escribe ese mensaje desde cero: copia la plantilla y cambia nombre, monto y cuenta según lo que sale en "Saldos".
- [ ] Ningún acreedor escribe un segundo mensaje de cobro a un mismo deudor.
- [ ] Nadie calcula las deudas en Excel ni en el chat.
- [ ] Caso borde: quien no tiene la app paga con el pantallazo y el cobro privado, sin instalar nada.

Traza a: insight 2 de product/insights/2026-11-09-0847-entrevistas-deudor-reales.md; T3 (real, `change`) y T4 (real, passed).

## Hipótesis
Creemos que, en un viaje del grupo, quienes pagan (Luisa) registrarán lo suyo, incluido lo chico, y recuperarán todo con un solo cobro por deudor, aunque no todos instalen la app. La razón: la organizadora trae la app, un integrante recuerda cada noche anotar lo del día, y el neto y el cobro privado le llegan completos a cada deudor.
Estamos equivocados si, en un viaje del grupo, pasa cualquiera de estas cosas: menos de 3 de cada 4 gastos chicos quedan en la app; algún pagador deja uno fuera por pena; más de 1 de cada 4 pares acreedor–deudor necesita un segundo cobro; alguna deuda se calcula fuera del neto de la app; o la organizadora termina registrando gastos ajenos.

## Alternativas consideradas
Exploradas en: product/solutions/2026-11-09-0939-quien-paga-pierde-plata-y-persigue.md
- A1 `fondo-comun-previo` — parked: pide plata por adelantado y traslada la persecución a antes del viaje.
- A2 `cobro-individual-completo` — parked como alternativa propia. Su plantilla entra en este spec para el cobro al cerrar (historia 4).
- A4 `bolsa-de-gastos-chicos` — parked: es el plan B sin app. No se activó porque en el T2 entraron 4 de 7 gastos chicos, por encima del corte de 1/2.
- A5 `cobrador-del-pagador` — parked: solo tendría sentido si los deudores no instalan. El T4 mostró que quien no instala paga con el pantallazo.

## Probado antes del spec
Probado en: product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md
- T1 adopción con Lina como organizadora — failed → change (real, n=6) · #11
- T2 los gastos chicos entran a la app — failed → change (real, n=6, 7 gastos chicos) · #12
- T3 nadie cobra dos veces — failed → change (real, 5 pares) · #13
- T4 no todos instalan, el neto va al chat — passed → continue (real, n=6; un caso sin app) · #15
- Cierre diario de "anoten lo de hoy" (historia 3) — not tested (declared). Es el `change` del T2.
- Cobro individual completo al cerrar (historia 4) — not tested (declared). Es el `change` del T3.
- Una salida en la que Lina no crea el grupo — not tested (declared). Es el paso siguiente del T4.
- Gastos chicos de quien no tiene la app (historia 2) — not tested (declared). Amplía lo que probó el T4, que solo lo vio con un gasto grande; no cambia su mecanismo. Viene de la crítica sintética.
- Lo que probó el T4 (mecanismo, quién hace qué, segmento) no cambia en este spec, así que su resultado sigue aplicando.
- Decisión de Lina (2026-11-17): no habrá más salidas de prueba. El spec queda con la evidencia del viaje del 14 al 15 nov, y las piezas no probadas siguen como supuestos abiertos (#16, #17 y #18).

## Supuestos
Referencias a product/overview.md (registro único).
- [opportunity: quien-paga-pierde-plata-y-persigue] [viability] Quien pagó por el grupo sí registrará lo que puso. — overview #9
- [product] [viability] Si Lina trae la app, todo el grupo entra y la usa hasta cerrar las cuentas. — overview #11 (weakened)
- [feature: splitwise-traido-por-organizadora] [value] Los gastos chicos se registran y se recuperan dentro del neto. — overview #12 (weakened, en la versión sin cierre diario)
- [feature: splitwise-traido-por-organizadora] [value] Ningún pagador escribe más de un cobro a un mismo deudor. — overview #13 (weakened, en la versión sin cobro privado)
- [feature: splitwise-traido-por-organizadora] [viability] Lina solo registra lo que ella pagó. — overview #14
- [feature: splitwise-traido-por-organizadora] [viability] Aunque no todos instalen, todas las deudas cierran con el neto. — overview #15 (confirmed, un caso)
- [feature: splitwise-traido-por-organizadora] [value] Cierre diario de "anoten lo de hoy" → al menos 3 de cada 4 gastos chicos en la app, sin pena. — overview #16
- [feature: splitwise-traido-por-organizadora] [value] Un solo cobro privado completo por deudor → nadie necesita un segundo mensaje. — overview #17
- [feature: splitwise-traido-por-organizadora] [viability] Sin Lina armando el grupo, el uso se sostiene. — overview #18
