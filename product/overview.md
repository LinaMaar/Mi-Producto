# Cuentas Claras

mode: new · internal

Una herramienta para que un grupo de amigos sepa quién le debe a quién después
de salidas y viajes. Cada persona registra lo que compró para el grupo, ve
cuánto le toca y marca cuando ya pagó, en un solo lugar en vez de repartido
entre un Excel y WhatsApp. Es un proyecto personal, pensado por ahora solo
para el grupo de amigos de Lina.

## Para quién

El grupo de amigos de Lina (20 a 26 años) que viaja y sale junto. En sus viajes
no hay un pagador único: distintas personas pagan distintas cosas (uno la
comida, otro la bebida) y cada gasto se reparte por separado. Antes del viaje
arman un presupuesto estimado en Excel o por WhatsApp y lo van llenando con lo
real; el Excel lo arma quien se anime y cada persona cobra lo que le deben.
A veces el grupo es mixto, con familia y amigos de todas las edades; ese grupo
queda fuera del foco por ahora.

Observado por Lina en sus propios viajes: las cuentas se resuelven sin mayor
drama, pero se cobra días después del viaje, los montos pequeños (dulces y
similares) quedan sin cobrar y es difícil encontrar la información para pagar.

## Sponsor

Lina, con su propio tiempo. Sigue si en un viaje el grupo lo usa de principio a
fin sin volver al Excel, con cada persona registrando sus gastos y marcando sus
pagos. Lo suelta si le toca a ella cargar todo y revisar si los demás
actualizaron.

## Creencias no verificadas

Ordenadas por impacto × incertidumbre: la primera es la siguiente a atacar.

1. [product] [value] Durante un viaje, cada amigo registrará por su cuenta lo
   que compró para el grupo y marcará sus pagos, sin que Lina tenga que
   cargarlo ni perseguirlos. — weakened by [product/personas/camilo-restrepo.md], [product/personas/santiago-mejia.md] (2026-10-19, synthetic)
   — weakened by [product/insights/2026-11-09-0836-entrevistas-deudor-sinteticas.md] (2026-11-09, synthetic): 0 de 4 registraron lo suyo; 3 de 4 no cobraron gastos propios
   — weakened by [product/insights/2026-11-09-0847-entrevistas-deudor-reales.md] (2026-11-09, real): en 5 de 6 viajes nadie registró lo suyo; solo pasó cuando el organizador trajo Splitwise; los gastos chicos se pierden por pena
2. [product] [value] El grupo dejará el Excel y WhatsApp por una herramienta
   nueva aunque hoy las cuentas se resuelven sin mayor drama; el fastidio
   actual alcanza para cambiar de hábito. — weakened by [product/personas/santiago-mejia.md] (2026-10-19, synthetic)
   — weakened by [product/insights/2026-11-09-0847-entrevistas-deudor-reales.md] (2026-11-09, real): 2 de 6 lo describen como "normal" y sin arreglos propios; en los demás la molestia fue plata, efectivo u olvido más que las cuentas
3. [product] [viability] Construir y mantener una herramienta propia le rinde
   más a Lina que adoptar una app gratuita que ya exista para dividir gastos.
   — weakened by [product/insights/2026-11-09-0836-entrevistas-deudor-sinteticas.md] (2026-11-09, synthetic): Splitwise abandonado porque solo 2 lo instalaron; link de app que nadie abrió
   — contradicted by [product/insights/2026-11-09-0847-entrevistas-deudor-reales.md] (2026-11-09, real): Splitwise resolvió cuánto y a quién y se sigue usando cuando lo trajo el organizador; falló 2 veces por adopción ("otra app no, por favor"), algo que también le pasaría a una herramienta propia
4. [opportunity: deudor-no-sabe-cuanto-ni-a-quien] [value] En un viaje típico
   del grupo, al menos 1 de cada 3 deudores pregunta en el chat cuánto o a
   quién pagar, o paga un monto distinto al que debe (de menos, de más o doble).
5. [opportunity: deudor-no-sabe-cuanto-ni-a-quien] [viability] El retraso en
   los pagos se explica sobre todo por no saber cuánto y a quién, y no por
   otras causas (falta de plata hasta la quincena, tener solo efectivo, simple
   olvido); si esas otras causas pesan más, aclarar el monto no hará que se
   pague a tiempo. — weakened by [product/research/2026-04-07-chat-viaje-cuanto-enviar.md] (2026-10-19)
   — weakened by [product/insights/2026-10-28-0845-encuesta-deudor-sintetica.md] (2026-10-28, synthetic): solo 3 de 18 retrasos se deben a no saber cuánto; 7 de 18 dependen del acreedor (monto corregido o cobro que no llegó)
   — weakened by [product/insights/2026-11-09-0807-encuesta-deudor-real.md] (2026-11-09, survey): es la causa principal más común (7 de 17) pero sin mayoría; de quienes no tenían cuánto o a quién, 14 de 15 pagaron tarde
   — weakened by [product/insights/2026-11-09-0836-entrevistas-deudor-sinteticas.md] (2026-11-09, synthetic): los retrasos fueron por cobros incompletos (sin monto claro, sin llave, sin neto, cobro que no llegó), ninguno por plata u olvido
   — contradicted by [product/insights/2026-11-09-0847-entrevistas-deudor-reales.md] (2026-11-09, real): solo 2 de 6 retrasos por cuánto o a quién; 4 por olvido, falta de plata o solo efectivo (0 de 3 entre los referidos)
6. [product] [value] Lo que más le pesa al grupo es no encontrar fácil cuánto
   debe cada uno y a quién, no hacer el cálculo; con verlo en un solo lugar
   se cobraría durante el viaje o al terminar, no días después. — weakened by [product/research/2026-04-07-chat-viaje-cuanto-enviar.md] (2026-10-19): quien cobraba se equivocó en el monto, así que el cálculo también falla
   — weakened by [product/insights/2026-10-28-0845-encuesta-deudor-sintetica.md] (2026-10-28, synthetic): en lo más difícil, 22 de 30 menciones son reconstruir, acordar o cuadrar gastos; 6 son encontrar el cobro o la cuenta
   — weakened by [product/insights/2026-11-09-0807-encuesta-deudor-real.md] (2026-11-09, survey): lo más molesto es reconstruir o cuadrar (8 menciones) más que encontrar la cuenta (4), aunque 12 de 23 no tenían el número al pagar
7. [product] [value] El grupo quiere el presupuesto estimado previo y los
   gastos reales en la misma herramienta, no solo el reparto final.
8. [opportunity: quien-paga-pierde-plata-y-persigue] [value] En un viaje
   típico, al menos 1 de cada 2 personas que pagan por el grupo deja algún
   gasto sin cobrar o tiene que cobrarle más de una vez a algún deudor.
9. [opportunity: quien-paga-pierde-plata-y-persigue] [viability] Quien pagó
   por el grupo sí registrará lo que puso, porque es quien quiere recuperarlo,
   sin que Lina tenga que cargarlo; el deudor no tiene ese motivo.
   Nota: por impacto × incertidumbre va antes que la #1, a la que acota; se
   agregó al final para no romper las referencias por número.
