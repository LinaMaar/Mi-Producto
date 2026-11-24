---
spec: product/specs/2026-11-17-1645-splitwise-traido-por-organizadora.md
exposure-plan: product/exposure-plans/2026-11-17-1725-splitwise-traido-por-organizadora.md
level: 1 — La app y el neto en el chat
status: designed
---

# Métricas para: Splitwise traído por la organizadora

> Revisado el 2026-11-24 para el nivel 1. La versión del nivel 2 está en el commit 61af6c1.
> No hay software propio: los "eventos" son registros que se pueden revisar después (miembros y actividad del grupo en Splitwise, chat del viaje, hoja de captura, formulario de cierre). La audiencia es de ~6 personas por viaje: cada persona pesa ~17 % y toda lectura es direccional. El nivel 1 ya quedó validado por el T4 (real); sus resultados son la línea base.

## Audiencia objetivo
Todos los integrantes de un viaje que organiza Lina, contados por persona, tengan o no la app. Fuente: segmento del overview (grupo de amigos de Lina, 20 a 26 años, varios pagadores) y audiencia del nivel 1 del plan ("todo el grupo de un viaje que organiza Lina"). Tamaño: ~6 (T4: 6).
Quién inicia y quién participa: la organizadora inicia (crea el grupo y manda el link). Los participantes tienen dos papeles que se leen por separado en activation: el pagador (registra lo que puso) y el deudor (cierra su deuda con el neto, con o sin la app).

## Frecuencia esperada
- Dentro del viaje: diaria. En el T4 hubo 5 gastos grandes en 2 días (product/tests/2026-11-09-0947-quien-paga-pierde-plata-y-persigue.md, T4).
- Entre viajes: `assumption`. No hay medición real; hubo dos viajes en noviembre (T1 y el del 14–15), y "uno o dos al año" sale de una persona sintética (Camilo).
Ventana de retención: por día de viaje.

## Acquisition
- **Señal:** la persona entra al grupo de Splitwise desde el link o, si no tiene la app, conoce su neto por el pantallazo de "Saldos" que llega al chat.
- **Definición ampliada:** lo de la app cuenta si entró antes de terminar el día 2 del viaje (corte del T1); lo del pantallazo, si llegó al chat en las 24 h siguientes al regreso. Haber recibido el link no basta. Se reporta aparte cuántos llegaron por la app y cuántos solo por el pantallazo.
- **Cálculo:** integrantes que entraron a la app o recibieron su neto por el pantallazo / integrantes del viaje, del envío del link a 24 h después del regreso.
- **Meta:** 100 % (6 de 6) · **Por qué:** el nivel 1 acepta que no todos instalen, pero nadie puede quedarse sin su neto: su deuda quedaría fuera, que es la condición de parada del plan. Línea base T4: 6 de 6 (5 por la app, 1 por el pantallazo).
- **Registros necesarios:** miembros del grupo en Splitwise con fecha y hora de entrada; el recordatorio único por privado (a quién, cuándo); hora y autor del pantallazo de "Saldos" en el chat.

## Activation
- **Señal:** la deuda o el crédito de la persona se cerró con el neto de la app, sin Excel ni cálculo en el chat; si además es pagador, todos sus gastos grandes están en la app.
- **Definición ampliada:** gasto grande = cuota por persona ≥ 20.000. Cuenta el gasto registrado por el propio pagador o por otro integrante con "pagado por" a su nombre que no sea la organizadora (historia 2). Las invitaciones anunciadas en el momento no cuentan. Se leen por separado pagadores y deudores.
- **Umbral de la señal:** cerró con el neto de la app y, si pagó, sin gastos grandes fuera · **Por qué:** entrar a la app no es el valor; en el T4, Esteban no instaló y pagó con el pantallazo. El valor es que la cuenta salga completa del neto, y un gasto fuera daña el neto de todos. Viene de la cláusula de refutación del spec ("alguna deuda se calcula fuera del neto de la app") y del criterio de avance del plan · **Excluye:** a quien entró a la app pero cuya deuda se recalculó en el chat o en Excel; al pagador con un gasto grande fuera; los gastos que registró la organizadora por otra persona.
- **Cálculo:** integrantes que cumplen el umbral / integrantes del viaje, 24 h después del regreso.
- **Meta:** 100 % (6 de 6) · **Por qué:** es el criterio de avance del nivel (ninguna deuda fuera del neto, ningún gasto de quien no tiene la app fuera). Línea base T4: 6 de 6; una meta más baja permitiría retroceder.
- **Registros necesarios:** actividad de Splitwise (quién creó cada gasto, "pagado por", monto, número de personas); hoja de captura por integrante (gastos grandes que pagó y si quedaron en la app, cómo conoció su neto, si su deuda se calculó con el neto, si hubo cálculo paralelo y dónde); chat del viaje (cálculos o Excel compartidos).

## Retention
- **Señal:** cada día en que la persona pagó un gasto grande, ese gasto quedó en la app la misma noche, por día de viaje.
- **Definición ampliada:** "la misma noche" = creado en Splitwise antes de las 06:00 del día siguiente, según la fecha de creación de la actividad (no la fecha del gasto, que se puede editar). Es recurrente quien lo cumple todos los días en que pagó algo grande. Cuenta el registro hecho por otro integrante a su nombre que no sea la organizadora. Viene del criterio de la historia 2: "queda registrado en la app el mismo día".
- **Curva de retención:** una cohorte por día del viaje (quienes pagaron algo grande ese día) y el % que lo registró esa misma noche. Con 2 o 3 días y ~6 personas, la lectura es direccional.
- **Cálculo:** integrantes que registraron la misma noche todos los gastos grandes que pagaron / integrantes del viaje, durante el viaje.
- **Meta:** ≥ 67 % (4 de 6) y la curva no baja de la primera noche a la última · **Por qué:** no todos pagan algo grande (quien no paga nada grande no puede contar), así que la meta queda por debajo de la activación. El plan no tiene criterio de mismo día. Sin línea base: en el T4 no se anotó la hora de creación. Riesgo conocido: la versión gratis de Splitwise limita los gastos por día (12 de 32 reseñas públicas, product/data/2026-11-24-resenas-publicas-splitwise.md); si alguien choca con el límite, se anota, porque bajaría esta métrica por una causa externa.
- **Lectura posterior, entre viajes:** de los activados en este viaje, cuántos usan la app en el siguiente. `not computable` hasta que haya otro viaje; si organiza otra persona, se mezcla con la #18.
- **Registros necesarios:** fecha y hora de creación y quién creó cada gasto (historial de actividad de Splitwise; la exportación CSV solo trae la fecha del gasto); día en que se pagó cada gasto grande (hoja de captura); avisos de límite diario de la app, si aparecen.

## Satisfaction
- **Instrumento:** CSAT de 1 a 5 en un formulario corto (Google Forms, solo un link) con nombre y una pregunta abierta opcional; lo manda al chat alguien que no sea Lina · **Pregunta:** "Del 1 al 5, ¿qué tan fácil fue saber cuánto debías o te debían y cerrar las cuentas de este viaje?" + "¿Por qué?" (opcional) · **Cuándo se muestra:** al día siguiente del regreso, después de que todos pagaron su neto · **Corte:** 4 o más.
- **Definición ampliada:** responden todos los integrantes, con o sin la app. Quien no responde cuenta como no satisfecho. Sesgos declarados: cortesía entre amigos y hacia la sponsor (sube la nota) y no respuesta (la baja).
- **Cálculo:** integrantes con nota ≥ 4 / integrantes del viaje (la tasa de respuesta y el % de satisfechos entre quienes respondieron se reportan aparte).
- **Meta:** ≥ 67 % (4 de 6), con respuesta de al menos 5 de 6 · **Por qué:** el plan no tiene criterio de satisfacción; con 4 de 6 sobre la audiencia, la mayoría tiene que estar satisfecha aunque alguien no responda. Una nota baja entre amigos es una señal fuerte y se lee con el "¿por qué?".
- **Registros necesarios:** respuestas del formulario (nombre, nota, comentario, fecha y hora); fecha y hora del envío del link; fecha de pago de cada neto.

## Métricas de negocio
Declaradas en el overview, tal cual:
- **Criterio de continuidad de la sponsor:** Lina sigue si en un viaje el grupo lo usa de principio a fin sin volver al Excel, con cada persona registrando sus gastos y marcando sus pagos. Lo suelta si le toca cargar todo y revisar si los demás actualizaron. Para leerlo hace falta anotar también si cada uno marcó su pago en la app.
- **#14 [viability]:** Lina solo registra lo que ella pagó. Según el plan, en cada viaje se anota si Lina registró algo que pagó otra persona; si pasa dos veces, se rompe su criterio de continuidad.
- **#18 [viability]:** sin Lina armando el grupo, el uso se sostiene. Solo se puede leer cuando organice otra persona.

## Conciliación con el plan de exposición
- **Avanzar si ninguna deuda queda fuera del neto** → `activation` 100 %.
- **Avanzar si no hay Excel ni cálculo en el chat** → `activation` 100 % (excluye a quien cerró por Excel o por el chat).
- **Avanzar si no queda fuera ningún gasto de quien no tiene la app** → `activation` 100 % (lectura de pagadores) y `acquisition` 100 % (nadie sin su neto).
- **Parar si dos o más deudas quedan fuera** → `activation` ≤ 4 de 6 por deudas fuera del neto.
- **Parar si el grupo cierra por Excel o por el chat** → `activation`: mayoría no activada por cálculo paralelo.
- **#14, la organizadora no registra gastos ajenos** → excluido en `activation` y `retention`; se lee en las métricas de negocio.
- **Pantallazo público (posible exposición del que más debe)** → ninguna métrica lo lee; se lee en el "¿por qué?" del formulario y en las quejas del chat.
