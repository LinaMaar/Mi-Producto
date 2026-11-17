---
spec: product/specs/2026-11-17-1645-splitwise-traido-por-organizadora.md
kit: product/specs/2026-11-17-1645-splitwise-traido-por-organizadora-kit.md
---

# Plan de exposición: Splitwise traído por la organizadora

> Nota: Lina decidió el 2026-11-17 que no habrá más salidas de prueba. Este plan es el orden en que conviene sumar cada parte del kit si vuelve a organizar un viaje, aunque no sea como prueba. El nivel 1 ya quedó validado con el T4.

**Hipótesis (del spec):** Creemos que, en un viaje del grupo, quienes pagan (Luisa) registrarán lo suyo, incluido lo chico, y recuperarán todo con un solo cobro por deudor, aunque no todos instalen la app. La razón: la organizadora trae la app, un integrante recuerda cada noche anotar lo del día, y el neto y el cobro privado le llegan completos a cada deudor.
Estamos equivocados si, en un viaje del grupo, pasa cualquiera de estas cosas: menos de 3 de cada 4 gastos chicos quedan en la app; algún pagador deja uno fuera por pena; más de 1 de cada 4 pares acreedor–deudor necesita un segundo cobro; alguna deuda se calcula fuera del neto de la app; o la organizadora termina registrando gastos ajenos.

## Nivel 1 — La app y el neto en el chat
- **Qué se muestra:** la invitación con el link (mensaje 1 del kit), un solo recordatorio, la regla para quien no tiene la app (mensaje 2) y el pantallazo de "Saldos" al cerrar. Todavía no hay "anoten lo de hoy" ni cobro privado.
- **Creencia:** quienes pagan registran lo suyo, lo que pagó quien no tiene la app entra igual, y todas las deudas cierran con el neto, sin Excel. (overview #15)
- **Audiencia:** todo el grupo de un viaje que organiza Lina.
- **Duración:** un viaje, más 24 h de cierre.
- **Validación:** **Avanzar si** ninguna deuda queda fuera del neto, no hay Excel ni cálculo en el chat y no queda fuera ningún gasto de quien no tiene la app. **Parar si** dos o más deudas quedan fuera o el grupo cierra por Excel o por el chat.
- **Estado:** validado por el T4 (real, 6 personas, un caso sin app y un gasto grande). Lo chico de quien no tiene la app no se ha probado.

## Nivel 2 — + "Anoten lo de hoy"
- **Qué se muestra:** todo lo del nivel 1, más una persona nombrada antes del viaje (que no es Lina) que manda cada noche el mensaje 3. El cobro privado sigue sin usarse.
- **Creencia:** con el recordatorio de cada noche, quienes pagan meten lo chico y nadie lo deja fuera por pena. (overview #16)
- **Audiencia:** todo el grupo del viaje.
- **Duración:** un viaje.
- **Validación:** **Avanzar si** al menos 3 de cada 4 gastos chicos están en la app y ningún pagador dejó uno fuera por pena. **Parar si** queda en la app menos de la mitad: el recordatorio no basta y se reconsidera A4 (bolsa de gastos chicos). Si queda entre 1/2 y 3/4, se ajusta antes de pasar al nivel 3.

## Nivel 3 — + Cobro privado para copiar y pegar
- **Qué se muestra:** todo lo anterior, más el mensaje 4 del kit: al cerrar, cada acreedor le manda a cada deudor un solo cobro por privado, copiado de la plantilla.
- **Creencia:** con un cobro privado y completo, ningún acreedor tiene que escribirle dos veces al mismo deudor. (overview #17)
- **Audiencia:** los acreedores del neto final y sus deudores.
- **Duración:** del cierre a 48 h después.
- **Validación:** **Avanzar si** ningún par necesita un segundo mensaje y todos pagan antes de 48 h. **Parar si** más de 1 de cada 4 pares necesita un segundo mensaje: la persecución sigue y se reconsidera A5.

## Forma de mostrarlo
No hay software ni flags: cada nivel es una parte del kit que se suma en un viaje, y siempre la ve el grupo completo. Por eso se ajusta al modelo **incremental**, con una condición: entre un viaje y otro, la memoria del proceso es este archivo, no una persona.

## Validaciones en paralelo
- **#18, sin Lina armando el grupo:** solo se sabe cuando otra persona organice. Es de viabilidad y no va como nivel.
- **#14 y criterio de la sponsor:** en cada viaje se anota si Lina registró algo que pagó otra persona. Si pasa dos veces, se rompe su criterio de continuidad, sin importar en qué nivel vaya.
- **Pantallazo público:** Camilo (sintético) dijo que puede exponer al que más debe. Conviene anotar si alguien se queja; no hay evidencia real.

## Preguntas abiertas
- **No hay viajes planeados.** El plan solo avanza si hay otro viaje.
- **¿Un viaje por nivel, o los niveles 2 y 3 juntos en el mismo viaje?** Juntos es más rápido, pero se pierde el punto de parada entre los dos: si falla el cobro, no se sabrá si el problema venía de lo chico.
- **¿Quién manda el "anoten lo de hoy"?** Hay que nombrarlo antes del viaje.
