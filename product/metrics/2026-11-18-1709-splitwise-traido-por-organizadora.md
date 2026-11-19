---
spec: product/specs/2026-11-17-1645-splitwise-traido-por-organizadora.md
exposure-plan: product/exposure-plans/2026-11-17-1725-splitwise-traido-por-organizadora.md
level: 2 — + "Anoten lo de hoy"
status: designed
---

# Métricas para: Splitwise traído por la organizadora

> No hay software propio: los "eventos" son registros que se pueden revisar después (actividad del grupo en Splitwise, chat del viaje, bitácora de gastos chicos, formulario de cierre). La audiencia es de ~5 personas por viaje: cada persona pesa 15–20 % y toda lectura es direccional. No hay viajes planeados (decisión de Lina, 2026-11-17); este archivo queda listo para el próximo.

## Audiencia objetivo
Las personas del viaje que pagaron al menos un gasto chico por el grupo (cuota por persona < 20.000; las invitaciones anunciadas en el momento, "van por mí", no cuentan), tengan o no la app. Se identifican con la bitácora de gastos chicos más la pregunta de cierre, como en el T2. Fuente: segmento del overview (grupo de amigos de Lina, 20 a 26 años, varios pagadores) acotado a la audiencia del nivel 2 (todo el grupo del viaje), y dentro de ella a quien paga lo chico, que es de quien trata la #16. El grupo completo se reporta como contexto.
Tamaño esperado: ~5 (en el T2, 5 de 6 pagaron algo chico).
Quién inicia y quién participa: la organizadora y quien manda "anoten lo de hoy" inician; solo entran al denominador si también pagaron algo chico. Lo que hace cada una se lee en la conciliación.

## Frecuencia esperada
- Dentro del viaje: diaria. En el T2 hubo 7 gastos chicos repartidos en los 2 días (product/tests/materials/t2-splitwise-traido-por-organizadora/T2-bitacora-gastos-chicos.md), y el mecanismo del nivel es un mensaje cada noche.
- Entre viajes: `assumption`. No hay medición real; hubo dos viajes en noviembre (T1 y el del 14–15), y "uno o dos al año" sale de una persona sintética (Camilo).
Ventana de retención: por día de viaje.

## Acquisition
- **Señal:** la persona tiene al menos un gasto suyo, de cualquier tamaño, registrado en Splitwise durante el viaje.
- **Definición ampliada:** cuenta si lo registró ella o si lo registró otro integrante con "pagado por" a su nombre (historia 2). No cuenta si lo registró la organizadora por ella (#14). Haber entrado al grupo o haber leído el mensaje de la noche no cuenta.
- **Cálculo:** pagadores de gastos chicos con ≥ 1 gasto propio en la app / pagadores de gastos chicos, del envío del link al cierre.
- **Meta:** 100 % (p. ej. 5 de 5) · **Por qué:** el nivel 2 incluye todo el nivel 1, y la condición para avanzar en el nivel 1 es que ningún gasto quede fuera del neto; un pagador sin nada en la app es justo ese caso (Felipe en el T2).
- **Registros necesarios:** actividad de Splitwise, por cada gasto: quién lo creó, "pagado por", monto, número de personas, fecha del gasto, fecha y hora de creación. Bitácora: quién pagó cada gasto chico.

## Activation
- **Señal:** al cierre, la persona tiene en la app al menos 3 de cada 4 de sus gastos chicos y no dejó ninguno fuera por pena.
- **Definición ampliada:** el corte es el pantallazo de "Saldos"; lo que se registra después no cuenta. Cuenta el gasto chico que registró ella o que registró otro integrante a su nombre que no sea la organizadora. El total de gastos chicos de cada persona sale de la bitácora más su respuesta a la pregunta de cierre. Las invitaciones no entran ni en el numerador ni en el denominador.
- **Umbral de la señal:** ≥ 3/4 de sus gastos chicos en la app y cero dejados por pena · **Por qué:** es la cláusula de refutación del spec y la #16, aplicadas a cada persona; con 1 a 3 gastos chicos equivale a "todos", y desde 4 permite que falte uno por olvido · **Excluye:** a quien registró lo grande pero dejó lo chico fuera (solo cuenta en acquisition), a quien registró lo chico después del cierre y a quien dejó cualquier gasto chico fuera por pena.
- **Cálculo:** pagadores de gastos chicos que cumplen el umbral / pagadores de gastos chicos, al momento del pantallazo de "Saldos".
- **Meta:** ≥ 75 % (p. ej. 4 de 5) y 0 personas no activadas por pena · **Por qué:** es el mismo 3/4 de la hipótesis. Se permite una persona por debajo solo por olvido o por "no valía la pena"; la pena es una condición de parada del plan. Línea base del T2 (nivel 1, sin el mensaje de la noche): 2 de 5 (40 %).
- **Lectura complementaria (no es AARS, la exige el plan):** gastos chicos en la app / gastos chicos totales, por gasto. Línea base del T2: 4/7 (57 %).
- **Registros necesarios:** actividad de Splitwise (quién creó cada gasto, "pagado por", monto, número de personas, fecha y hora de creación); bitácora de gastos chicos (quién, qué, monto, personas, día, si es invitación); pregunta de cierre por privado ("¿Pagaste algo por el grupo que no quedó en la app? ¿Qué fue y por qué no lo metiste?", con la razón codificada como pena, olvido, "no valía la pena" u otra); hora del pantallazo de "Saldos". Sin bitácora, lo que queda fuera solo se conoce por la pregunta de cierre: alguien tiene que llevarla.

## Retention
- **Señal:** cada día en que la persona pagó algo chico, ese gasto quedó en la app la misma noche, por día de viaje.
- **Definición ampliada:** "la misma noche" = creado en Splitwise antes de las 06:00 del día siguiente, según la fecha de creación de la actividad (no la fecha del gasto, que se puede editar). Es recurrente quien lo cumple todos los días en que pagó algo chico, sea uno o varios. Cuenta el registro hecho por otro integrante a su nombre que no sea la organizadora.
- **Curva de retención:** una cohorte por día del viaje (los pagadores de gastos chicos de ese día) y el % que lo registró esa misma noche. Si la curva baja de la primera noche a la última, el efecto del mensaje se gasta; si se mantiene, el hábito se sostiene. Con 2 o 3 días y ~5 personas, la lectura es direccional.
- **Cálculo:** pagadores de gastos chicos que registraron la misma noche todos los días en que pagaron / pagadores de gastos chicos, durante el viaje.
- **Meta:** ≥ 60 % (p. ej. 3 de 5) y la curva no baja de la primera noche a la última · **Por qué:** es más estricta que la activación (exige el mismo día, no solo estar al cierre), por eso va un escalón por debajo. El plan no tiene criterio de mismo día. Sin línea base: en el T2 no se anotó la hora de creación.
- **Lectura posterior, entre viajes:** de los activados en este viaje, cuántos registran lo suyo en el siguiente. `not computable` hasta que haya otro viaje; la frecuencia entre viajes es `assumption`, y si organiza otra persona se mezcla con la #18.
- **Registros necesarios:** fecha y hora de creación y quién creó cada gasto (del historial de actividad de Splitwise; la exportación CSV solo trae la fecha del gasto); día de pago de cada gasto chico (bitácora); hora de cada mensaje "anoten lo de hoy" (chat).

## Satisfaction
- **Instrumento:** CSAT de 1 a 5 en un formulario corto (Google Forms, solo un link) con nombre y una pregunta abierta opcional; lo manda al chat alguien que no sea Lina, de preferencia quien mandó "anoten lo de hoy" · **Pregunta:** "Del 1 al 5, ¿qué tan bien te funcionó cómo se manejaron los gastos chicos en este viaje (anotarlos cada noche y que se sumen a lo que cada uno pone al final)?" + "¿Por qué?" (opcional) · **Cuándo se muestra:** al día siguiente del regreso, después de que todos pagaron su neto y antes de la pregunta de cierre del T2 · **Corte:** 4 o más.
- **Definición ampliada:** solo cuentan las respuestas de la audiencia; las de otros integrantes se reportan aparte como contexto. Quien no responde cuenta como no satisfecho. Sesgos declarados: cortesía entre amigos y hacia la sponsor (sube la nota) y no respuesta (la baja).
- **Cálculo:** pagadores de gastos chicos con nota ≥ 4 / pagadores de gastos chicos (la tasa de respuesta y el % de satisfechos entre quienes respondieron se reportan aparte).
- **Meta:** ≥ 60 % (p. ej. 3 de 5), con tasa de respuesta de al menos 4 de 5 · **Por qué:** el plan no tiene criterio de satisfacción; con 60 % sobre la audiencia, la mayoría tiene que estar satisfecha de verdad aunque alguien no responda. Una nota baja entre amigos es una señal fuerte y se lee con el "¿por qué?".
- **Registros necesarios:** respuestas del formulario (nombre, nota, comentario, fecha y hora); fecha y hora del envío del link; fecha de pago de cada neto.

## Métricas de negocio
Declaradas en el overview, tal cual:
- **Criterio de continuidad de la sponsor:** Lina sigue si en un viaje el grupo lo usa de principio a fin sin volver al Excel, con cada persona registrando sus gastos y marcando sus pagos. Lo suelta si le toca cargar todo y revisar si los demás actualizaron.
- **#14 [viability]:** Lina solo registra lo que ella pagó. Según el plan (validaciones en paralelo), en cada viaje se anota si Lina registró algo que pagó otra persona; si pasa dos veces, se rompe su criterio de continuidad, sin importar el nivel.
- **#18 [viability]:** sin Lina armando el grupo, el uso se sostiene. Solo se puede leer cuando organice otra persona.

## Conciliación con el plan de exposición
- **Avanzar si al menos 3 de cada 4 gastos chicos están en la app** → lectura complementaria por gasto (≥ 3/4), acompañada de `activation` ≥ 75 %. Los dos usan el mismo corte, así que no hay contradicción.
- **Avanzar si ningún pagador dejó uno fuera por pena** → `activation`: 0 personas no activadas por pena (pregunta de cierre).
- **Parar si queda en la app menos de la mitad** (se reconsidera A4) → lectura complementaria por gasto < 1/2.
- **Entre 1/2 y 3/4, se ajusta antes del nivel 3** → lectura complementaria por gasto.
- **Heredado del nivel 1: ningún gasto de quien no tiene la app queda fuera** → `acquisition` 100 % (en parte: solo cubre a quien pagó algo chico).
- **Heredado del nivel 1: ninguna deuda fuera del neto; ni Excel ni cálculo en el chat** → ninguna métrica AARS lo lee; se lee con los registros del T4 (cómo conoció su neto cada persona, si hubo cálculo paralelo).
- **Persona nombrada (no Lina) que manda "anoten lo de hoy" cada noche** → ninguna métrica lo lee; es un chequeo del proceso (hora y autor de cada mensaje en el chat).
- **#14, Lina no registra gastos ajenos** → excluido en `acquisition`, `activation` y `retention`; se lee en las métricas de negocio.
