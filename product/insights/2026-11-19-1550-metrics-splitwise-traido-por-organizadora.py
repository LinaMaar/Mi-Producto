"""AARS del nivel 2 de splitwise-traido-por-organizadora.

Definiciones: product/metrics/2026-11-18-1709-splitwise-traido-por-organizadora.md
Uso: python 2026-11-19-1550-metrics-splitwise-traido-por-organizadora.py <carpeta de datos> <organizadora>
Ej.:  python ... ../data/2026-11-19-synthetic-nivel2 Laura
Solo lee la carpeta de datos; no la modifica.
"""
import csv
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA = Path(sys.argv[1])
ORG = sys.argv[2]
FMT = "%Y-%m-%d %H:%M"


def leer(nombre):
    with open(DATA / nombre, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def dt(s):
    return datetime.strptime(s, FMT)


def pct(n, d):
    return f"{n}/{d} = {100 * n / d:.0f} %" if d else f"{n}/0 = n/a"


actividad = {r["id_app"]: r for r in leer("actividad_splitwise.csv")}
bitacora = leer("bitacora_gastos_chicos.csv")
cierre = leer("pregunta_cierre.csv")
chat = leer("chat.csv")
satis = leer("satisfaccion.csv")
pagos = leer("pagos.csv")

saldos = min(dt(m["fecha_hora"]) for m in chat if m["tipo"] == "saldos")
chicos = [g for g in bitacora if g["invitacion"] != "si"]
for g in chicos:  # verificación de la definición de gasto chico
    assert int(g["monto"]) / int(g["n_personas"]) < 20000, g["id"]

audiencia = sorted({g["pagado_por"] for g in chicos})
A = len(audiencia)
pena = {r["persona"] for r in cierre if r["razon"] == "pena"}


def valido(reg, pagador):
    """Registro que cuenta: no lo creó la organizadora por otra persona."""
    return reg["creado_por"] != ORG or pagador == ORG


def en_app_al_cierre(g):
    reg = actividad.get(g["id_app"])
    return bool(reg) and valido(reg, g["pagado_por"]) and dt(reg["creado_en"]) <= saldos


def misma_noche(g):
    reg = actividad.get(g["id_app"])
    if not reg or not valido(reg, g["pagado_por"]):
        return False
    limite = datetime.strptime(g["dia"], "%Y-%m-%d") + timedelta(days=1, hours=6)
    return dt(reg["creado_en"]) < limite


print(f"Audiencia (pagadores de gastos chicos): {A} -> {', '.join(audiencia)}")
print(f"Corte de cierre (pantallazo de Saldos): {saldos:%Y-%m-%d %H:%M}\n")

# ---- acquisition
adq = [p for p in audiencia
       if any(r["pagado_por"] == p and valido(r, p) and dt(r["creado_en"]) <= saldos
              for r in actividad.values())]
print("ACQUISITION:", pct(len(adq), A), "| meta 100 %")

# ---- activation
act = []
print("\nACTIVATION, por persona:")
for p in audiencia:
    suyos = [g for g in chicos if g["pagado_por"] == p]
    dentro = sum(en_app_al_cierre(g) for g in suyos)
    ok = dentro / len(suyos) >= 0.75 and p not in pena
    if ok:
        act.append(p)
    print(f"  {p}: {dentro}/{len(suyos)} en la app; pena={'sí' if p in pena else 'no'} -> {'activado' if ok else 'no'}")
no_act_pena = [p for p in audiencia if p not in act and p in pena]
print("ACTIVATION:", pct(len(act), A), f"| no activados por pena: {len(no_act_pena)} {no_act_pena} | meta ≥ 75 % y 0 por pena")
dentro_total = sum(en_app_al_cierre(g) for g in chicos)
print("Lectura por gasto (plan):", pct(dentro_total, len(chicos)), "| avanzar ≥ 3/4, parar < 1/2")

# ---- retention
ret = []
for p in audiencia:
    suyos = [g for g in chicos if g["pagado_por"] == p]
    if all(misma_noche(g) for g in suyos):
        ret.append(p)
print("\nRETENTION:", pct(len(ret), A), "| meta ≥ 60 % y la curva no baja")
print("Curva por día (pagadores de ese día que registraron todo lo de ese día la misma noche):")
curva = []
for dia in sorted({g["dia"] for g in chicos}):
    del_dia = [g for g in chicos if g["dia"] == dia]
    personas = sorted({g["pagado_por"] for g in del_dia})
    ok = [p for p in personas if all(misma_noche(g) for g in del_dia if g["pagado_por"] == p)]
    curva.append(len(ok) / len(personas))
    anoten = [m for m in chat if m["tipo"] == "anoten" and m["fecha_hora"].startswith(dia)]
    hora = anoten[0]["fecha_hora"][11:] + " por " + anoten[0]["autor"] if anoten else "sin mensaje"
    print(f"  {dia}: {pct(len(ok), len(personas))} ({', '.join(personas)}) | anoten: {hora}")
print("  ¿La curva baja de la primera noche a la última?", "sí" if curva[-1] < curva[0] else "no")

# ---- satisfaction
form = min(dt(m["fecha_hora"]) for m in chat if m["tipo"] == "formulario")
ultimo_pago = max(dt(r["pagado_en"]) for r in pagos)
resp = [r for r in satis if r["nombre"] in audiencia]
sat = [r["nombre"] for r in resp if int(r["nota"]) >= 4]
print("\nSATISFACTION:", pct(len(sat), A), "| meta ≥ 60 %")
print("  Tasa de respuesta:", pct(len(resp), A), "| meta ≥ 80 %")
print("  Satisfechos entre quienes respondieron:", pct(len(sat), len(resp)))
print("  No respondieron:", [p for p in audiencia if p not in {r['nombre'] for r in resp}])
print(f"  Formulario {form:%Y-%m-%d %H:%M} después del último pago {ultimo_pago:%Y-%m-%d %H:%M}:", form > ultimo_pago)

# ---- embudo
print("\nEMBUDO:")
print("  llegó -> obtuvo valor:", pct(len(set(act) & set(adq)), len(adq)))
print("  obtuvo valor -> volvió (misma noche):", pct(len(set(ret) & set(act)), len(act)))
print("  retenidos no activados:", sorted(set(ret) - set(act)))

# ---- proceso y negocio
ajenos = [r["id_app"] for r in actividad.values() if r["creado_por"] == ORG and r["pagado_por"] != ORG]
print("\nPROCESO Y NEGOCIO:")
print("  Gastos ajenos registrados por la organizadora (#14):", len(ajenos), ajenos)
autores = {m["autor"] for m in chat if m["tipo"] == "anoten"}
print("  'Anoten lo de hoy' enviados:", sum(m["tipo"] == "anoten" for m in chat), "| autores:", autores, "| ¿la organizadora?", ORG in autores)
print("  Mensajes con la línea de que lo chico se suma al total:", sum(m.get("incluye_linea_total") == "si" for m in chat if m["tipo"] == "anoten"))
