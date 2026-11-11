---
opportunity: quien-paga-pierde-plata-y-persigue
solutions: product/solutions/2026-11-09-0939-quien-paga-pierde-plata-y-persigue.md
status: ready
---

# Pruebas de solución para: Quien paga por el grupo pierde plata y desgaste recuperándola

## Por qué probar
Bajo prueba: A3, la organizadora trae Splitwise al viaje (`splitwise-traido-por-organizadora`). El dolor del pagador está evidenciado (real). Sobre la solución hay un caso real donde funcionó, el viaje de Juan Pablo: todos registraron, incluso lo chico, y se pagó el día del regreso. Pero falló en 2 de 3 intentos por adopción, y nunca se ha visto con el grupo de Lina ni con Lina como organizadora. Las tres pruebas corren en el viaje del 14 nov.

T4 (agregada el 2026-11-11) prueba la versión cambiada de A3 tras el `change` del T1: no se exige que todos instalen; el neto se comparte en el chat. Corre en el viaje del 14 nov junto con T2 y T3, bajo las mismas reglas comunes.

**Cambio de fechas (2026-11-11, antes del viaje, por decisión de Lina):** el viaje es del 14 al 15 nov (regreso = cierre, 15 nov). La lectura y las preguntas de cierre pasan del 21 al **16 nov** para T2, T3 y T4. Donde una creencia o un paso diga "al 21 nov", se lee "al 16 nov". Excepción en el T3: solo hay una lectura, la del 16 nov, un día después del regreso; no habrá otra después. Los pares sin pagar ese día no cuentan como fallo. Los segundos mensajes de cobro que ya hayan ocurrido sí cuentan, con la regla de decisión tal cual. Si quedan pares sin pagar y, por lo demás, el resultado sería `continue`, el T3 queda `inconclusive`: la parte a) no se pudo verificar.

**Reglas comunes a T1, T2 y T3:**
- Lina invita y registra solo lo que ella paga, como cualquier organizadora que usa la app.
- No le recuerda a nadie que entre ni que registre, salvo una vez a quien no haya entrado, como hizo Ricardo con Mateo. Cada recordatorio adicional se anota en la hoja de captura, porque contamina la señal.
- A quienes van al viaje no se les entrevista antes de que termine (regla de la guía de entrevistas). Las preguntas de cierre se hacen el 16 nov.
- Sesgo declarado: Lina es organizadora, sponsor y observadora a la vez.
- Si la adopción falla, A4 (bolsa de gastos chicos) no se activa en este viaje sin diseñarla antes como prueba propia.

Definición de **gasto chico**: un gasto por el grupo cuya cuota por persona es menor a 20.000 (los casos reales fueron 9.000 y 15.000).

Definición de **invitación** (aclarada el 2026-11-11, antes del viaje, por decisión de Lina): un gasto que quien lo paga anuncia en el momento como suyo (por ejemplo, "las cervezas van por mí", como Felipe en el T1). No es un gasto por el grupo para cobrar, así que no entra en el total del T2 ni en los gastos grandes del T4. Se anota aparte. Cuenta como invitación solo si se anunció antes del cierre. Si aparece por primera vez en la pregunta del 16 nov, se codifica por la razón que dé la persona y sigue contando.

## T1. splitwise-traido-por-organizadora: adopción con Lina como organizadora
- **Test status:** analyzed
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
- **Test status:** ready
- **Belief under test:** "Con la app en el viaje, los gastos chicos se registran y se recuperan dentro del neto: al 21 nov, al menos 3 de cada 4 gastos chicos pagados por el grupo están en la app, y ningún pagador dice haber dejado uno sin cobrar por pena." — overview #12
- **Risk:** [value]
- **Test type:** field-trial
- **What we do:** 1) Durante el viaje, Lina lleva una bitácora de cada gasto chico que vea pagar por el grupo, sin decirle a nadie que lo registre. 2) Al cierre, cruza la bitácora con los gastos de la app. 3) El 16 nov, a cada persona que pagó algo por el grupo le hace una sola pregunta, por privado: "¿Pagaste algo por el grupo que no quedó en la app? ¿Qué fue y por qué no lo metiste?". Los gastos que salgan de ahí se suman al total de gastos chicos.
- **With whom:** los mismos del T1. Todos los que pagaron algo por el grupo responden la pregunta de cierre.
- **Material needed:** 1) Bitácora de gastos chicos: quién pagó, qué, monto, número de personas, cuota por persona, día, y si quedó en la app (se llena al cierre). 2) La tarjeta con la pregunta de cierre, textual, y una columna para la razón, codificada después como pena, olvido, "no valía la pena" u otra. Quedan fuera las preguntas de opinión sobre la app.
- **Material:** [bitacora-gastos-chicos.md](materials/t2-splitwise-traido-por-organizadora/bitacora-gastos-chicos.md) · [tarjeta-preguntas-cierre.md](materials/t2-splitwise-traido-por-organizadora/tarjeta-preguntas-cierre.md) (compartida con T3)
- **Duration:** del 14 nov al 16 nov.
- **Signal and threshold:** a) gastos chicos en la app ÷ gastos chicos totales (bitácora más los que reporten en la pregunta de cierre) ≥ 3/4; b) cero pagadores dicen haber dejado un gasto chico fuera por pena. Pasa solo si se cumplen a y b.
- **Decision rule:** continue si se cumplen a y b · change si a queda entre 1/2 y 3/4, o si un solo pagador lo dejó por pena (la versión cambiada, por ejemplo con un cierre diario de "anoten lo de hoy" a cargo de otro integrante, necesita su propia prueba) · discard si a < 1/2: la #12 cae y también se debilita la #9 (el pagador no registra lo chico ni con la app). En ese caso se reconsidera A4 o se vuelve a investigación.
- **Expected provenance:** real
- **Next step if it passes:** ver si el resultado se repite en la salida del paso siguiente del T1.

## T3. splitwise-traido-por-organizadora: nadie cobra dos veces
- **Test status:** ready
- **Belief under test:** "Con el neto y los recordatorios de la app, ningún pagador tiene que escribir más de un cobro a un mismo deudor: al 21 nov, todos los deudores pagaron sin un segundo mensaje escrito por el pagador." — overview #13
- **Risk:** [value]
- **Test type:** field-trial
- **What we do:** 1) Al cierre en la app, Lina anota cada par acreedor–deudor del neto y su monto. 2) Cuenta los mensajes de cobro que cada acreedor escribe en el chat del grupo (los ve). 3) El 16 nov, en la misma conversación de la pregunta del T2, pregunta a cada acreedor: "¿A quién le tuviste que escribir para que te pagara, y cuántas veces?". 4) Anota la fecha de pago de cada par (marcado en la app o según el acreedor).
- **With whom:** todos los acreedores del neto final del viaje.
- **Material needed:** 1) Hoja por par acreedor–deudor: monto neto, fecha de cierre, mensajes de cobro escritos por el acreedor (en el grupo, por privado), fecha de pago y si estaba pagado al 16 nov. 2) La segunda pregunta de cierre, en la misma tarjeta del T2. Quedan fuera los recordatorios automáticos de la app, que no cuentan como mensajes escritos por el pagador.
- **Material:** [hoja-pares.md](materials/t3-splitwise-traido-por-organizadora/hoja-pares.md) · pregunta 2 en [tarjeta-preguntas-cierre.md](materials/t2-splitwise-traido-por-organizadora/tarjeta-preguntas-cierre.md)
- **Duration:** del cierre en la app (15 nov) al 16 nov (única lectura).
- **Signal and threshold:** a) todos los pares pagados al 16 nov (los pares sin pagar no cuentan como fallo; si quedan pares sin pagar y lo demás daría `continue`, el resultado es `inconclusive`); b) cero pares con un segundo mensaje de cobro escrito por el acreedor. Pasa solo si se cumplen a y b.
- **Decision rule:** continue si se cumplen a y b · change si a lo sumo 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar (la versión cambiada, por ejemplo con el cobro individual completo de A2 como plantilla al cerrar, necesita su propia prueba) · discard si más de 1 de cada 4 pares necesitó un segundo mensaje o quedó sin pagar: la app no le quita la persecución al pagador frente a la línea base.
- **Expected provenance:** real
- **Next step if it passes:** ver si el resultado se repite en la salida del paso siguiente del T1.

## T4. splitwise-traido-por-organizadora: no todos instalan, el neto va al chat
- **Test status:** ready
- **Belief under test:** "Aunque no todos instalen la app, quienes pagan registran lo suyo y quien no la tiene paga el neto que se comparte en el chat: todas las deudas cierran con el neto de la app, sin Excel ni cálculo paralelo, y ningún gasto del grupo queda fuera porque quien lo pagó no tenía la app." — overview #15
- **Risk:** [viability]
- **Test type:** field-trial
- **What we do:** 1) Antes del viaje (11 a 13 nov), Lina crea el grupo en Splitwise y manda el link al chat con el mismo mensaje de invitación del T1. El mensaje no dice que instalar sea opcional. 2) Anota quién entra y cuándo. Se permite un solo recordatorio a quien no haya entrado, como en el T1, y no se insiste más. 3) Durante el viaje, cada quien registra lo que paga y Lina no carga gastos ajenos. Si alguien sin la app paga un gasto grande, Lina anota qué pasa con ese gasto (lo registró otro, se cobró por fuera o quedó sin cobrar), sin intervenir. 4) Cierre = el día del regreso. Si en las 24 h siguientes nadie manda al chat el pantallazo de "Saldos", Lina lo manda una vez y lo anota. 5) Lina anota cómo conoció su neto cada persona (app o pantallazo) y si alguien recurrió al Excel o a un cálculo propio en el chat.
- **With whom:** todo el grupo que va al viaje del 14 nov (segmento: 20 a 26 años, solo amigos, varios pagadores). Es el viaje real, sin reclutamiento.
- **Material needed:** 1) El mensaje de invitación del T1, sin cambios ([mensaje-invitacion.md](materials/t1-splitwise-traido-por-organizadora/mensaje-invitacion.md)). 2) Hoja de captura por integrante: si entró (fecha y hora), recordatorios, gastos grandes que pagó por el grupo y, de cada uno, si quedó en la app y quién lo registró; cómo conoció su neto (app / pantallazo / otro); si su deuda se calculó con el neto de la app (sí/no) y si hubo cálculo paralelo (sí/no y dónde). 3) Registro del pantallazo de "Saldos": quién lo mandó, fecha y hora, y si lo tuvo que mandar Lina. Quedan fuera las preguntas de opinión sobre la app y cualquier pedido de instalar más allá del único recordatorio.
- **Material:** [mensaje-invitacion.md](materials/t1-splitwise-traido-por-organizadora/mensaje-invitacion.md) (el del T1) · [hoja-captura.md](materials/t4-splitwise-traido-por-organizadora/hoja-captura.md) (incluye el registro del pantallazo)
- **Duration:** del envío del link (11 a 13 nov) al 16 nov.
- **Signal and threshold:** a) todas las deudas del viaje se calcularon con el neto de la app, incluidas las de quienes no la tienen, sin Excel ni un cálculo paralelo en el chat; b) cero gastos grandes (cuota por persona ≥ 20.000) quedaron fuera del neto porque quien los pagó no tenía la app, y Lina no registró ningún gasto ajeno. Pasa solo si se cumplen a y b. Si ninguna persona sin la app pagó un gasto grande, b se cumple sin haberse puesto a prueba. Se anota así, y la #15 no puede pasar de promising.
- **Decision rule:** continue si se cumplen a y b · change si una sola deuda se calculó fuera del neto de la app, o si un solo gasto grande de alguien sin app quedó fuera o lo registró Lina, y el resto cerró en la app. La versión cambiada (por ejemplo, quien no tiene la app manda su gasto al chat y lo registra otro pagador que no sea Lina) necesita su propia prueba · discard si dos o más deudas quedaron fuera del neto de la app, si el grupo cerró con Excel o por el chat, o si dos o más gastos grandes quedaron fuera o los registró Lina. En ese caso se evalúa según la causa: gastos de quien no tenía la app que no entraron → A5; pagadores con la app que no registraron → A4, y se debilita la #9 · inconclusive si todos entraron a la app: no hubo nadie sin app y la #15 no se puso a prueba (el dato se anota para la #11).
- **Expected provenance:** real
- **Next step if it passes:** repetir en una segunda salida del grupo donde Lina no cree el grupo en la app, para ver si el uso se sostiene sin ella.

## Resultados

### T1 — `failed` · decisión: `change`
- **Observado:** 5 de 6 entraron a la app antes de terminar el día 2 (8 nov, 23:59). Esteban no entró, ni después del único recordatorio por privado (7 nov). Al cierre dijo: "yo no me bajo más apps, con el pantallazo me sirve". Las 6 deudas cerraron con el neto de la app: 0 cálculos paralelos, 0 Excel. Esteban pagó su neto (86.000) el mismo día en que Natalia mandó al chat, sin que nadie se lo pidiera, un pantallazo de "Saldos". Gastos registrados: Lina 4, Natalia 3, Manuela 2, Isabel 1, Felipe 0, Esteban 0. Lina no cargó gastos ajenos y respondió con lo mínimo dos preguntas sobre cómo funciona la app.
- **Con quién y cuántos:** el grupo completo del viaje, 6 personas del segmento. Del 5 nov (envío del link) al 10 nov (lectura).
- **Procedencia:** real.
- **Contra el umbral:** a) no se cumple (1 no entró); b) sí se cumple. La prueba pasa solo con a y b, así que es `failed`. La regla de decisión da `change`: una sola persona no entró y el resto cerró en la app.
- **Desviaciones del diseño:** corrió en un viaje anterior (link el 5 nov, lectura el 10 nov) y no en el del 14 nov. El corte del día 2 se movió con el viaje (8 nov). El mensaje de invitación no fue el del material, que se armó el 10 nov. La lectura se hizo el 10 nov y no el 21, pero todas las deudas ya estaban cerradas. Nada de esto cambia cómo se leen a y b.
- **Fuera de la señal (no cuenta para T2):** Felipe pagó unas cervezas (≈ 40.000, menos de 7.000 por persona, gasto chico) y no las registró: "las cervezas van por mí". Parece una invitación y no pena, pero T2 no corrió.
- **Hoja:** [T1-hoja-captura-completa.md](materials/t1-splitwise-traido-por-organizadora/T1-hoja-captura-completa.md)

### T2 — `not run`
No se armó el material ni se llevó la bitácora de gastos chicos.

### T3 — `not run`
No se armó la hoja por par acreedor–deudor ni se hizo la pregunta de cierre.

## Decisión
A3 (`splitwise-traido-por-organizadora`): `change` (2026-11-10). La app cerró todas las cuentas sin Excel, pero no todo el grupo entra. El único que no entró se negó a instalar; no fue un problema para unirse. Por eso el cambio no es armar el grupo en persona, sino no exigir que todos instalen: quienes pagan registran y el neto se comparte en el chat para quien no tenga la app. Esa versión cambia la #11 y necesita su propia prueba, porque el resultado aplica a lo que se probó. A4 y A5 siguen parked: la regla las activaba con dos o más personas fuera. A5 suma un indicio (un deudor que no instala) sin llegar a su condición. T2 y T3 quedan pendientes para el próximo viaje.
