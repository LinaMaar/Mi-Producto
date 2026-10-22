---
opportunity: product/opportunities/2026-10-19-1613-deudor-no-sabe-cuanto-ni-a-quien.md
beliefs: overview #4, overview #5
status: draft
---

# Encuesta: cómo se saldan las cuentas después de un viaje entre amigos

- **Objetivos de aprendizaje:**
  1. **Frecuencia del problema (creencia #4).** En su último viaje, ¿qué proporción de deudores no supo cuánto o a quién pagar, preguntó, pagó "a ojo" o pagó un monto equivocado? → Si es menos de 1 de cada 3, el problema del deudor es débil y se reabre la variante del acreedor antes de `/explore-solutions`.
  2. **Causas del pago tardío (creencia #5).** Según los deudores, ¿el retraso se debe a no saber cuánto o a quién, o a otras causas (efectivo, falta de plata, olvido, cobro que no llegó)? → Si dominan efectivo o liquidez, se priorizan alternativas como el fondo común por encima de las que solo aclaran montos.
- **Encuestados:** personas de 20 a 26 años que en los últimos 12 meses viajaron con un grupo de solo amigos en el que varias personas pagaron cosas distintas. Se excluyen los viajes con familia (persona negative: Patricia Gómez), los viajes con un solo pagador o con fondo común y los viajes donde cada quien pagó lo suyo.
- **Duración estimada:** 4 de screening + 1 de rol + hasta 6 de deudor o 2 de acreedor + 1 abierta + 3 de opt-in. Con las ramas, cada persona ve unas 11–14 preguntas, casi todas de un clic: ~4 min.
- **Complementa, no reemplaza,** la revisión de chats (31 oct) y la observación del viaje (14 nov): la encuesta mide lo que la gente *reporta*, y la revisión de chats mide lo que *pasó*. La encuesta sí cubre las causas que nadie escribe en el chat (olvido, falta de plata).
- **Datos sensibles:** no se piden montos, números de cuenta ni teléfonos, salvo el contacto voluntario de R3.

## Texto de introducción (va en la herramienta)

> Encuesta de 4 minutos sobre cómo se pagan las cuentas entre amigos después de un viaje. Es anónima, salvo que al final decidas dejar tu contacto. No hay respuestas correctas: nos sirve más un "no recuerdo" honesto que una respuesta a medias.

(No se menciona que se está construyendo una herramienta: eso sesgaría las respuestas hacia el problema.)

## Screening

S1. ¿Qué edad tienes? [opción única]
   - Menos de 20 · 20–23 · 24–26 · 27–30 · Más de 30
   → descalificar si no está entre 20 y 26
   > Objetivo: perfil del segmento

S2. ¿Hace cuánto fue tu último viaje de al menos una noche con un grupo de personas? [opción única]
   - Menos de 1 mes · 1 a 3 meses · 3 a 6 meses · 6 a 12 meses · Más de 12 meses · Nunca he viajado en grupo
   → descalificar si fue hace más de 12 meses o nunca
   > Objetivo: perfil del segmento. También sirve para cortar por recencia: los recuerdos de hace más de 6 meses valen menos.

S3. En ese último viaje, ¿quiénes iban? [opción única]
   - Solo amigos (con o sin parejas de amigos) · Amigos y familia · Solo familia · Compañeros de trabajo o de estudio en un plan organizado · Otro
   → descalificar si no es "Solo amigos"
   > Objetivo: excluir grupos mixtos con familia (decisión del overview)

S4. ¿Cómo se pagaron los gastos compartidos de ese viaje? [opción única]
   - Varias personas pagaron cosas distintas y después se repartió
   - Una sola persona pagó casi todo y después cobró
   - Antes del viaje todos pusieron plata en un fondo común
   - Cada quien pagó lo suyo; nadie le quedó debiendo a nadie
   - Otro
   → descalificar si no es "Varias personas pagaron cosas distintas"
   > Objetivo: definición del segmento de la oportunidad. Se registra cuántos quedan fuera por cada opción: la proporción de grupos que ya usan fondo común es un dato útil para el objetivo 2.

## Preguntas

Q1. Al terminar ese viaje, ¿cómo quedaste con las cuentas? [opción única]
   - Le debía plata a una o más personas del grupo → Q2
   - Otros me debían plata a mí → Q8
   - Las dos cosas: debía y me debían → Q2 y después Q8
   - Quedé a paz y salvo, no debía ni me debían → Q10
   > Objetivo: 1 y 2. Separa deudores de acreedores; el n que cuenta es el de deudores.

### Rama deudor

Q2. ¿Cuándo terminaste de pagar todo lo que debías de ese viaje? [opción única]
   - Durante el viaje · El mismo día del regreso · 1 a 3 días después · 4 a 7 días después · Más de una semana después · Todavía no he terminado de pagar · No recuerdo
   > Objetivo: 2. Define quién pagó tarde (de 1 a 3 días después en adelante).

Q3. Cuando fuiste a pagar, ¿qué tenías claro? [opción única]
   - Cuánto debía y a quién (con sus datos para pagar)
   - Cuánto debía, pero no a quién o a qué número/cuenta
   - A quién, pero no cuánto
   - Ni cuánto ni a quién
   - No recuerdo
   > Objetivo: 1

Q4. Para pagar lo de ese viaje, ¿hiciste alguna de estas cosas? [opción múltiple]
   - Pregunté en el chat o por mensaje cuánto debía
   - Pregunté a qué número o cuenta pagar
   - Busqué en el chat, el Excel o fotos para encontrar mi monto
   - Pagué un monto aproximado, sin estar seguro de que fuera el exacto
   - Ninguna de estas
   - No recuerdo
   > Objetivo: 1. Son comportamientos concretos y no opiniones; las tres primeras opciones son las de la señal real del chat.

Q5. Después de pagar, ¿resultó que el monto no era el correcto? [opción única]
   - No, pagué el monto exacto
   - Sí, pagué de menos
   - Sí, pagué de más
   - Sí, pagué dos veces lo mismo
   - No sé si fue el monto exacto
   > Objetivo: 1. "No sé" también cuenta como evidencia de que el deudor no tenía claro el monto.

Q6. *(Solo si en Q2 respondió de "1 a 3 días después" en adelante.)* ¿Qué hizo que no pagaras antes? Marca todas las que apliquen. [opción múltiple, opciones en orden aleatorio salvo "Otra"]
   - No sabía cuánto debía
   - No tenía el número o la cuenta para pagar
   - Nadie había mandado el cobro todavía
   - Me corrigieron el monto o estaba esperando que lo confirmaran
   - Solo tenía efectivo
   - No tenía la plata en ese momento
   - Se me olvidó
   - Estaba esperando cruzar cuentas con lo que me debían a mí
   - Otra: ____
   > Objetivo: 2. Separa "no sé cuánto/a quién" (la creencia) de "el cobro no llegó" (problema del acreedor) y de efectivo, liquidez y olvido.

Q7. *(Mismo filtro que Q6.)* De esas, ¿cuál fue la razón principal? [opción única; se muestran solo las marcadas en Q6]
   > Objetivo: 2. Es la medición central de la creencia #5: qué causa domina.

### Rama acreedor

Q8. ¿Cuántas personas del grupo te debían plata de ese viaje? [opción única]
   - 1 · 2–3 · 4–6 · Más de 6 · No recuerdo
   > Objetivo: 1. Es el denominador de Q9.

Q9. De esas personas, ¿cuántas te preguntaron cuánto te debían o a dónde pagarte? [opción única]
   - Ninguna · 1 · 2–3 · 4–6 · Más de 6 · No recuerdo
   > Objetivo: 1. Contrasta desde el lado de Valentina lo que los deudores dicen de sí mismos.

### Para todos

Q10. Piensa en la última vez que tuviste que saldar cuentas con amigos después de un viaje. ¿Qué fue lo más molesto o difícil, si hubo algo? [abierta, opcional]
   > Objetivo: 1 y 2. Puede sacar causas que no estaban en la lista y "porqués" para llevar a las entrevistas.

## Screening + opt-in (reclutamiento de entrevistas)

R1. En los últimos 6 meses, ¿le has quedado debiendo plata a algún amigo después de un viaje o una salida? [sí / no]
   → no es candidato si responde "no". La entrevista busca deudores recientes.
R2. ¿Aceptarías una conversación de 30 minutos (por videollamada o en persona) sobre cómo se saldan las cuentas en tus viajes? [sí / no, opcional]
R3. Si respondiste que sí, ¿cómo te contactamos? (WhatsApp o correo) [abierta, opcional, solo visible si R2 = sí]

Campo oculto: `canal` (lo llena el enlace de cada canal; ver Distribución).

## Distribución

| Canal | A quién llega | Alcance aprox. | Enlace |
|---|---|---|---|
| Chat de WhatsApp del grupo de viaje de Lina | El segmento exacto: Valentina, Camilo y Santiago. **Sesgo:** responden por amistad con Lina, los más activos en el chat responden más, y son las mismas personas de los chats que se van a revisar, así que no es una muestra independiente. | 10–20 | Enlace A (`canal=grupo-lina`) |
| Reenvío por 3–5 amigos del grupo a otro chat de viaje en el que estén (universidad, trabajo, colegio) | Deudores y acreedores de grupos parecidos que no le deben nada a Lina. **Sesgo:** mismo círculo social, edad y ciudad; quien reenvía elige el grupo; responden menos porque no conocen a Lina. | ~30–50 (estimado: 3–5 grupos de ~10 personas) | Enlace B (`canal=reenvio`); si se quiere más detalle, un enlace por cada amigo que reenvía |

- **n objetivo:** 30 **deudores** (Q1 = "le debía" o "las dos cosas"), con al menos 10 de cada canal para poder compararlos.
- **Advertencia antes de publicar:** con el alcance de la tabla, el n objetivo no se alcanza. Suponiendo ~60% de respuesta en el canal 1, ~25% en el canal 2 y que ~70% de quienes pasan el screening sean deudores (todas cifras supuestas, no medidas), salen unos 4–8 deudores del canal 1 y unos 5–9 del canal 2: **~10–17 deudores en total**. Los resultados se van a leer como **direccionales**: se pueden comparar los patrones contra el umbral de "1 de cada 3" y ver qué causa domina, pero no se reportan porcentajes con confianza. Para acercarse a 30 hace falta un tercer canal o más reenvíos.
- **Primera revisión:** 31 oct 2026 (junto con la revisión de chats de la agenda).
- **Cierre:** abierta hasta llegar al n objetivo.
