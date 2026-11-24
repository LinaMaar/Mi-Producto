---
source: real
corpus: product/data/2026-11-24-resenas-publicas-splitwise.md
metrics-analysis: none
period: 2019-02 to 2026-11
script: product/insights/2026-11-24-feedback-splitwise-traido-por-organizadora.py
---

# Análisis de feedback: Splitwise (alternativa que usa el grupo), para el nivel 1

## Corpus
32 reseñas públicas de Splitwise: Trustpilot 20, App Store 8, Product Hunt 4. Van de 2019 a nov 2026; 25 son de 2024 en adelante. 0 fuera de alcance. Tipo principal: 16 `complaint`, 10 `praise`, 3 `request`, 2 `bug`, 1 `usability`.
- **Trustpilot es más de la mitad del corpus (20 de 32)**: los temas se inclinan a su sesgo, que es el de quien entra a quejarse (1 estrella) y el del muy contento (5).
- Las reseñas de tiendas y Product Hunt sobrerrepresentan a los muy contentos y los muy molestos, y a usuarios de habla inglesa de otros países. No es el grupo de Lina.
- Son fragmentos de hasta 125 caracteres, no la reseña completa.
- `real` porque son usuarios reales de la alternativa, pero no del segmento: no anota creencias del overview.
- Quien deja de usar Splitwise en silencio no aparece aquí.

## Temas
Una reseña puede tener más de un tema, así que los porcentajes suman más de 100 %.

### F1. La versión gratis limita cuántos gastos se registran por día
- **Entradas:** 13 (41 %) · **Fuentes:** Trustpilot 9, App Store 3, Product Hunt 1 · **Segmentos:** usuarios de la versión gratis, varios en viajes de grupo
- **Parte de la feature:** registrar gastos (historias 2 y 3; señal de activation y retention)
- **Tipo:** `complaint` (12) y `request` (1)
- **Severidad:** alta. Es el tema más frecuente y bloquea la acción central: varios dicen "unusable". 12 hablan de un tope de 2 a 4 gastos por día; 2 (ids 20 y 27) de una espera de 10 segundos entre registros.
- **Tendencia:** `stable` (2023: 4, 2024: 4, 2025: 1, 2026: 4)
- > "Can't add more than 2 expenses a day. What if I paid like 6-7 bills a day?" (Trustpilot, ago 2026)
- > "Tried to use it for a group vacation. After putting in a few exoenses it asked for a pro subscription" (Trustpilot, jul 2026)

### F2. Útil para viajes y gastos en grupo
- **Entradas:** 10 (31 %) · **Fuentes:** Trustpilot 6, Product Hunt 3, App Store 1
- **Parte de la feature:** la app como un todo, en viajes
- **Tipo:** `praise`
- **Severidad:** n/a (elogio)
- **Tendencia:** `stable` (2023: 2, 2024: 2, 2025: 3, 2026: 3). Varios lo dicen en pasado ("used to be").
- > "Great for splitting expenses with a travel group!" (Trustpilot, mar 2023)
- > "This app stopped any tricky conversations and also allowed us to just buy stuff for other kids and adults" (App Store GB, feb 2023)

### F3. Presión o cobro para pasar a Pro
- **Entradas:** 8 (25 %) · **Fuentes:** Trustpilot 6, App Store 2
- **Parte de la feature:** el uso gratis de la app (la feature supone que la app es gratis)
- **Tipo:** `complaint`
- **Severidad:** media. Molesta y empuja a abandonar, pero solo bloquea cuando coincide con F1.
- **Tendencia:** `growing` (2024: 1, 2025: 4, 2026: 3)
- > "This year Splitwise was completely useless. It kept prompting us to go pro ( ie to pay for the app )" (Trustpilot, abr 2026)

### F4. Saldos o cierre confusos o en disputa
- **Entradas:** 3 (9 %) · **Fuentes:** Trustpilot 2, App Store 1
- **Parte de la feature:** el neto y el cierre (historia 4; señal de activation)
- **Tipo:** `request`, `usability`, `bug`
- **Severidad:** media. Es poco frecuente, pero toca la plata y la confianza en el neto.
- **Tendencia:** n/a (muy pocas entradas)
- > "one of my group members settled up without actually paying." (App Store GB, nov 2024)
- > "It attempts to record each transaction, and then each person see a different owing and owed.." (Trustpilot, sep 2024)

## Frente a las hipótesis de métricas
No hay análisis de métricas real del nivel 1 (`metrics-analysis: none`). El ensayo sintético del nivel 2 no se guardó y no se usa aquí.
Lo que el feedback anticipa para las métricas del nivel 1 (product/metrics/2026-11-18-1709-splitwise-traido-por-organizadora.md):
- F1 puede bajar `retention` (registrar la misma noche) y `activation` (gastos grandes fuera) por una causa externa: el tope diario de la versión gratis. Está previsto en el archivo de métricas: se anota si alguien choca con el límite.
- F4 toca `activation` (cerrar con el neto): un "settle up" marcado sin pagar o un saldo que cada uno ve distinto daría deudas que no cierran con el neto.

## Señales débiles
- **Alguien que debe no quiere registrarse** (id 25, App Store NZ, 2019): "but I can't add bills if somebody who owes me doesn't want to sign up." Es el caso de Esteban en el T1 y el T4. El grupo lo resolvió con el pantallazo.
- **La app evita conversaciones incómodas** (id 22, dentro de F2): "stopped any tricky conversations". Toca la pena de cobrar del T2.
- **Falla al compartir en iPhone SE** (id 17, Trustpilot, 2024).
