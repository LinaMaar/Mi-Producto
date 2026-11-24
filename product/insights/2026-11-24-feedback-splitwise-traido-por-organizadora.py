"""Conteo de temas del feedback: product/data/2026-11-24-resenas-publicas-splitwise.md
Etiquetas asignadas a mano por entrada (una entrada puede tener más de un tema).
L = límite de gastos por día o espera entre registros (versión gratis)
P = presión o cobro para pasar a Pro
V = útil para viajes y gastos en grupo (elogio)
C = saldos o cierre confusos o en disputa
A = alguien no quiere registrarse (adopción)
B = falla técnica
"""
from collections import Counter, defaultdict

# id: (fuente, año, temas, tipo principal)
E = {
    1: ("Trustpilot", 2026, "L", "complaint"),
    2: ("Trustpilot", 2023, "L", "complaint"),
    3: ("Trustpilot", 2023, "V", "praise"),
    4: ("Trustpilot", 2023, "L", "complaint"),
    5: ("Trustpilot", 2026, "C", "request"),
    6: ("Trustpilot", 2026, "L", "request"),
    7: ("Trustpilot", 2026, "LP", "complaint"),
    8: ("Trustpilot", 2026, "LV", "praise"),
    9: ("Trustpilot", 2026, "PV", "praise"),
    10: ("Trustpilot", 2026, "P", "complaint"),
    11: ("Trustpilot", 2025, "LP", "complaint"),
    12: ("Trustpilot", 2025, "P", "complaint"),
    13: ("Trustpilot", 2025, "P", "complaint"),
    14: ("Trustpilot", 2025, "V", "praise"),
    15: ("Trustpilot", 2024, "V", "praise"),
    16: ("Trustpilot", 2024, "L", "complaint"),
    17: ("Trustpilot", 2024, "B", "bug"),
    18: ("Trustpilot", 2024, "C", "usability"),
    19: ("Trustpilot", 2024, "V", "praise"),
    20: ("Trustpilot", 2024, "L", "complaint"),
    21: ("App Store", 2025, "P", "complaint"),
    22: ("App Store", 2023, "V", "praise"),
    23: ("App Store", 2024, "C", "bug"),
    24: ("App Store", 2024, "L", "complaint"),
    25: ("App Store", 2019, "A", "request"),
    26: ("App Store", 2024, "L", "complaint"),
    27: ("App Store", 2023, "L", "complaint"),
    28: ("App Store", 2024, "P", "complaint"),
    32: ("Product Hunt", 2026, "V", "praise"),  # hace 10 meses
    33: ("Product Hunt", 2025, "V", "praise"),  # hace 1 año
    34: ("Product Hunt", 2025, "V", "praise"),  # hace 1 año
    35: ("Product Hunt", 2023, "L", "complaint"),  # hace 3 años
}
N = len(E)
print("Entradas:", N, "| fuera de alcance: 0")
print("Por fuente:", dict(Counter(f for f, _, _, _ in E.values())))
print("Por tipo principal:", dict(Counter(t for *_, t in E.values())))

por_tema = defaultdict(list)
for i, (f, a, temas, t) in E.items():
    for tema in temas:
        por_tema[tema].append((i, f, a))

for tema, filas in sorted(por_tema.items(), key=lambda kv: -len(kv[1])):
    n = len(filas)
    fuentes = dict(Counter(f for _, f, _ in filas))
    anios = dict(sorted(Counter(a for _, _, a in filas).items()))
    print(f"\n{tema}: {n}/{N} = {100 * n / N:.0f} % | fuentes {fuentes} | por año {anios}")
    print("   ids:", [i for i, _, _ in filas])
