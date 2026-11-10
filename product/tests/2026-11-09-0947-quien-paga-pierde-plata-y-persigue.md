---
opportunity: quien-paga-pierde-plata-y-persigue
solutions: product/solutions/2026-11-09-0939-quien-paga-pierde-plata-y-persigue.md
status: designed
---

# Pruebas de solución para: Quien paga por el grupo pierde plata y desgaste recuperándola

## Por qué probar
Bajo prueba: A3, la organizadora trae Splitwise al viaje (`splitwise-traido-por-organizadora`). El dolor del pagador está evidenciado (real). Sobre la solución hay un caso real donde funcionó, el viaje de Juan Pablo: todos registraron, incluso lo chico, y se pagó el día del regreso. Pero falló en 2 de 3 intentos por adopción, y nunca se ha visto con el grupo de Lina ni con Lina como organizadora. Las tres pruebas corren en el viaje del 14 nov.

**Reglas comunes a T1, T2 y T3:**
- Lina invita y registra solo lo que ella paga, como cualquier organizadora que usa la app.
- No le recuerda a nadie que entre ni que registre, salvo una vez a quien no haya entrado, como hizo Ricardo con Mateo. Cada recordatorio adicional se anota en la hoja de captura, porque contamina la señal.
- A quienes van al viaje no se les entrevista antes de que termine (regla de la guía de entrevistas). Las preguntas de cierre se hacen el 21 nov.
- Sesgo declarado: Lina es organizadora, sponsor y observadora a la vez.
- Si la adopción falla, A4 (bolsa de gastos chicos) no se activa en este viaje sin diseñarla antes como prueba propia.

Definición de **gasto chico**: un gasto por el grupo cuya cuota por persona es menor a 20.000 (los casos reales fueron 9.000 y 15.000).

## T1. splitwise-traido-por-organizadora: adopción con Lina como organizadora
- **Test status:** ready
- **Belief under test:** "Si Lina, como organizadora, trae una app gratuita para dividir gastos al viaje del 14 nov, todo el grupo entra y la usa hasta cerrar las cuentas." — overview #11
- **Risk:** [viability]
- **Test type:** field-trial
- **What we do:** 1) Antes del viaje (10 a 13 nov), Lina crea el grupo en Splitwise y manda el link al chat del viaje con su mensaje normal de organizadora. 2) Anota cuándo entra cada integrante. 3) Durante el viaje, cada quien registra lo que paga y Lina no carga gastos ajenos. 4) Al volver, el grupo cierra con el neto de la app. Lina anota si alguien recurre al Excel o a un cálculo propio en el chat.
- **With whom:** todo el grupo de amigos de Lina que va al viaje del 14 nov (segmento: 20 a 26 años, solo amigos, varios pagadores). No hay reclutamiento: es el viaje real.
- **Material needed:** 1) El mensaje de invitación: link, una línea de por qué ("para no hacer Excel") y nada más; deja fuera tutoriales, reglas sobre qué registrar e incentivos. 2) La hoja de captura por integrante: fecha y hora de entrada, número de gastos que registró, si su deuda se cerró con el neto de la app (sí/no), si se usó un cálculo paralelo (sí/no y dónde) y los recordatorios que Lina tuvo que dar.
- **Material:** [mensaje-invitacion.md](materials/t1-splitwise-traido-por-organizadora/mensaje-invitacion.md) · [hoja-captura.md](materials/t1-splitwise-traido-por-organizadora/hoja-captura.md)
- **Duration:** del envío del link (10 a 13 nov) al 21 nov.
- **Signal and threshold:** a) todos los integrantes entraron a la app antes de terminar el día 2 (15 nov, 23:59); b) al 21 nov, todas las deudas se calcularon con el neto de la app, sin Excel ni un cálculo paralelo en el chat. Pasa solo si se cumplen a y b.
- **Decision rule:** continue si se cumplen a y b · change si una sola persona no entró o hubo un solo cálculo paralelo, y el resto cerró en la app (la versión cambiada, por ejemplo armar el grupo en persona al salir, necesita su propia prueba) · discard si dos o más no entraron antes del día 2, o si el grupo cerró con Excel o con el chat. En ese caso se activa la evaluación de A4 y A5 según la causa (no quisieron instalar → A5; no registraron → A4).
- **Expected provenance:** real
- **Next step if it passes:** repetir en una segunda salida del grupo donde Lina no cree el grupo en la app, para ver si el uso se sostiene sin ella y si deja de depender de quién organiza.

## T2. splitwise-traido-por-organizadora: los gastos chicos entran a la app
- **Test status:** designed
- **Belief under test:** "Con la app en el viaje, los gastos chicos se registran y se recuperan dentro del neto: al 21 nov, al menos 3 de cada 4 gastos chicos pagados por el grupo están en la app, y ningún pagador dice haber dejado uno sin cobrar por pena." — overview #12
- **Risk:** [value]
- **Test type:** field-trial
- **What we do:** 1) Durante el viaje, Lina lleva una bitácora de cada gasto chico que vea pagar por el grupo, sin decirle a nadie que lo registre. 2) Al cierre, cruza la bitácora con los gastos de la app. 3) El 21 nov, a cada persona que pagó algo por el grupo le hace una sola pregunta, por privado: "¿Pagaste algo por el grupo que no quedó en la app? ¿Qué fue y por qué no lo metiste?". Los gastos que salgan de ahí se suman al total de gastos chicos.
- **With whom:** los mismos del T1. Todos los que pagaron algo por el grupo responden la pregunta de cierre.
- **Material needed:** 1) Bitácora de gastos chicos: quién pagó, qué, monto, número de personas, cuota por persona, día, y si quedó en la app (se llena al cierre). 2) La tarjeta con la pregunta de cierre, textual, y una columna para la razón, codificada después como pena, olvido, "no valía la pena" u otra. Quedan fuera las preguntas de opinión sobre la app.
- **Material:**
- **Duration:** del 14 nov al 21 nov.
- **Signal and threshold:** a) gastos chicos en la app ÷ gastos chicos totales (bitácora más los que reporten en la pregunta de cierre) ≥ 3/4; b) cero pagadores dicen haber dejado un gasto chico fuera por pena. Pasa solo si se cumplen a y b.
- **Decision rule:** continue si se cumplen a y b · change si a queda entre 1/2 y 3/4, o si un solo pagador lo dejó por pena (la versión cambiada, por ejemplo con un cierre diario de "anoten lo de hoy" a cargo de otro integrante, necesita su propia prueba) · discard si a < 1/2: la #12 cae y también se debilita la #9 (el pagador no registra lo chico ni con la app). En ese caso se reconsidera A4 o se vuelve a investigación.
- **Expected provenance:** real
- **Next step if it passes:** ver si el resultado se repite en la salida del paso siguiente del T1.

## T3. splitwise-traido-por-organizadora: nadie cobra dos veces
- **Test status:** designed
- **Belief under test:** "Con el neto y los recordatorios de la app, ningún pagador tiene que escribir más de un cobro a un mismo deudor: al 21 nov, todos los deudores pagaron sin un segundo mensaje escrito por el pagador." — overview #13
- **Risk:** [value]
- **Test type:** field-trial
- **What we do:** 1) Al cierre en la app, Lina anota cada par acreedor–deudor del neto y su monto. 2) Cuenta los mensajes de cobro que cada acreedor escribe en el chat del grupo (los ve). 3) El 21 nov, en la misma conversación de la pregunta del T2, pregunta a cada acreedor: "¿A quién le tuviste que escribir para que te pagara, y cuántas veces?". 4) Anota la fecha de pago de cada par (marcado en la app o según el acreedor).
- **With whom:** todos los acreedores del neto final del viaje.
- **Material needed:** 1) Hoja por par acreedor–deudor: monto neto, fecha de cierre, mensajes de cobro escritos por el acreedor (en el grupo, por privado), fecha de pago y si estaba pagado al 21 nov. 2) La segunda pregunta de cierre, en la misma tarjeta del T2. Quedan fuera los recordatorios automáticos de la app, que no cuentan como mensajes escritos por el pagador.
- **Material:**
- **Duration:** del cierre en la app al 21 nov.
- **Signal and threshold:** a) todos los pares pagados al 21 nov; b) cero pares con un segundo mensaje de cobro escrito por el acreedor. Pasa solo si se cumplen a y b.
- **Decision rule:** continue si se cumplen a y b · change si a lo sumo 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar (la versión cambiada, por ejemplo con el cobro individual completo de A2 como plantilla al cerrar, necesita su propia prueba) · discard si más de 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar: la app no le quita la persecución al pagador frente a la línea base.
- **Expected provenance:** real
- **Next step if it passes:** ver si el resultado se repite en la salida del paso siguiente del T1.

## Resultados

## Decisión
