"""Verificación (Fase 4): cada cifra clave del informe se recalcula desde data/ y
analisis/resultados/ y se comprueba que aparezca, con el mismo redondeo, en
informe/informe_TAG.md, informe/slides_outline.md o informe/preguntas_probables.md.
Corre después de correr_todo.sh:  python3 analisis/verificar_informe.py
"""
import sys

import numpy as np
import pandas as pd

from estilo import DATA, RAIZ, RES

INF = (RAIZ / "informe" / "informe_TAG.md").read_text()
SLI = (RAIZ / "informe" / "slides_outline.md").read_text()
PRE = (RAIZ / "informe" / "preguntas_probables.md").read_text()
TEXTO = {"informe": INF, "slides": SLI, "preguntas": PRE}


def es(x, nd=2, signo=False):
    s = f"{x:+.{nd}f}" if signo else f"{x:.{nd}f}"
    return s


def miles(x):
    """Redondeo convencional (mitad hacia arriba), como en el informe."""
    from decimal import ROUND_HALF_UP, Decimal
    n = int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    return f"{n:,}".replace(",", " ")


fallas = []


def chequear(desc, cadena, donde=("informe",)):
    for d in donde:
        if cadena not in TEXTO[d]:
            fallas.append(f"[{d}] {desc}: no se encontró «{cadena}»")
            return
    print(f"OK  {desc}: «{cadena}» en {', '.join(donde)}")


g = pd.read_csv(DATA / "global_vw_porsche.csv")
pre = pd.read_csv(RES / "porsche_pre2011.csv", index_col=0).valor
esp = pd.read_csv(RES / "porsche_especificaciones.csv").set_index("post")
intra = pd.read_csv(RES / "porsche_sens_intragrupo.csv").set_index("post")
comb = pd.read_csv(RES / "porsche_ajustes_combinados.csv").set_index("post")
tfpr = pd.read_csv(RES / "porsche_tfpr_prop1.csv", index_col=0).valor
cour = pd.read_csv(RES / "cournot_resumen.csv")
liv = pd.read_csv(RES / "peru_livianos_hhi.csv").set_index("anio")
lujo = pd.read_csv(RES / "peru_lujo_hhi.csv").set_index("anio")
sh = pd.read_csv(RES / "peru_lujo_shares.csv")
lern = pd.read_csv(RES / "peru_lerner_ilustrativo.csv")
man = pd.read_csv(DATA / "man.csv").set_index("anio")

# --- Tabla A1: datos crudos ---
for _, r in g.iterrows():
    nombre = "VW" if r.entidad == "VW_Grupo" else "Porsche AG"
    fila = f"| {nombre} | {r.anio} | {miles(r.ingresos_meur)} | {miles(r.costo_materiales_meur)} |"
    chequear(f"Tabla A1 {nombre} {r.anio}", fila)
    chequear(f"Tabla A1 Q/M {nombre} {r.anio}", f"| {r.ingresos_meur / r.costo_materiales_meur:.3f} |")

# --- Ejercicio de consolidación ---
chequear("x_VW_2011", es(pre["x_VW_2011"], 4))
chequear("x_Porsche_2011", es(pre["x_Porsche_2011"], 4))
chequear("x_pool_2011", es(pre["x_pool_2011"], 4))
chequear("x_ventas_2011", es(pre["x_ventas_2011"], 4))
chequear("w_T", f"w_T = {pre['w_T (peso costo Porsche)'] * 100:.1f} %")
chequear("pi_T", f"π_T = {pre['pi_T (peso ventas Porsche)'] * 100:.1f} %")
chequear("Porsche vs VW %", f"{(pre['x_Porsche_2011'] / pre['x_VW_2011'] - 1) * 100:.1f} % más alto")
chequear("término w_T(x_T-x_A)", es(pre["Termino w_T(x_T - x_A)"], 4, True))
chequear("sesgo frontera", f"{pre['Sesgo frontera ln x_pool - ln x_A'] * 100:+.2f} puntos log", ("informe", "slides"))
chequear("sesgo agregación", f"{pre['Sesgo agregación ln x_pool - ln x_ventas'] * 100:.2f} puntos log".replace("-", "−"), ("informe",))
for post in (2013, 2014):
    r = esp.loc[post]
    for col in ("solo_adquirente", "consolidacion_virtual", "virtual_pesos_ventas"):
        chequear(f"{col} {post}", f"| {r[col] * 100:+.2f}".replace("+-", "−"))
chequear("intragrupo 2013", f"**{intra.loc[2013, 'consolidacion_virtual_ajustada'] * 100:+.1f} %**")
chequear("intragrupo 2014", f"**{intra.loc[2014, 'consolidacion_virtual_ajustada'] * 100:.2f} %**".replace("-", "−"))
chequear("proporción intragrupo", f"{intra.loc[2013, 'proporcion_intragrupo_2013'] * 100:.0f} %")
chequear("sin MAN 2013", f"**{comb.loc[2013, 'virtual_sin_MAN'] * 100:+.2f} %**")
chequear("sin MAN 2014", f"**{comb.loc[2014, 'virtual_sin_MAN'] * 100:.2f} %**".replace("-", "−"))
chequear("sin MAN ni intragrupo 2013", f"**{comb.loc[2013, 'virtual_sin_MAN_ni_intragrupo'] * 100:+.2f} %**")
chequear("sin MAN ni intragrupo 2014", f"**{comb.loc[2014, 'virtual_sin_MAN_ni_intragrupo'] * 100:.2f} %**".replace("-", "−"))
chequear("MAN Q/M 2011", f"{man.loc[2011, 'ingresos_meur'] / man.loc[2011, 'costo_materiales_meur']:.2f} en 2011")
chequear("MAN Q/M 2013", f"{man.loc[2013, 'ingresos_meur'] / man.loc[2013, 'costo_materiales_meur']:.2f} en 2013")
vw = g[g.entidad == "VW_Grupo"].set_index("anio")
x = vw.ingresos_meur / vw.costo_materiales_meur
chequear("caída VW 2010-2011", f"{np.log(x[2011] / x[2010]) * 100:.1f} %".replace("-", "−"), ("informe", "slides"))
pa = g[g.entidad == "Porsche_AG"].set_index("anio")
xp = pa.ingresos_meur / pa.costo_materiales_meur
chequear("Porsche Q/M 2011→2013", f"de {xp[2011]:.2f} (2011) a {xp[2013]:.2f} (2013)")
chequear("β_m * x_VW", f"{0.388 * pre['x_VW_2011']:.2f} < 1")
chequear("TFPR sesgo", f"{tfpr['sesgo TFPR ln(a + r b)'] * 100:+.2f} puntos log")
chequear("TFPR r", f"r = {tfpr['r = Z_T/Z_A']:.2f}")
chequear("TFPR r*", f"r* = {tfpr['umbral r* = (1-a)/b']:.2f}")
chequear("TFPR a+b", f"| a + b | {tfpr['a+b']:.3f} |")

# --- Cournot ---
A, B = cour.iloc[0], cour.iloc[1]
chequear("Cournot A P_pre", f"{A.P_pre:.2f}")
chequear("Cournot A umbral precio", f"{A.umbral_precio:.2f}".replace("-", "−"))
chequear("Cournot A umbral W", f"c_M ≤ {A.umbral_bienestar:.1f}")
chequear("Cournot A umbral rentabilidad", f"c_M ≤ {A.umbral_rentabilidad:.2f}")
chequear("Cournot B umbral precio", f"c_M ≤ {B.umbral_precio:.0f}")
chequear("Cournot B reducción", f"{B['reduccion_necesaria_precio_%']:.0f} %")
chequear("Cournot A reducción W", f"{(1 - A.umbral_bienestar / 30) * 100:.0f} %")

# --- Perú ---
for anio, r in liv.iterrows():
    chequear(f"livianos total {anio}", miles(r.total))
    chequear(f"share VW marca {anio}", f"{r['share_VW_marca_%']:.2f} %")
    chequear(f"HHI marca {anio}", f"{miles(r.HHI_marca_min)}–{miles(r.HHI_marca_max)}")
    chequear(f"HHI grupo {anio}", f"{miles(r.HHI_grupo_min)}–{miles(r.HHI_grupo_max)}")
chequear("grupo VW livianos 2025", f"{liv.loc[2025, 'share_grupo_VW_%']:.1f} %", ("informe", "slides"))
chequear("grupo VW livianos 2022", f"{liv.loc[2022, 'share_grupo_VW_%']:.1f} %")
chequear("top 4 marcas", f"{liv.loc[2025, 'share_top4_marcas_%']:.0f} %")
for anio, r in lujo.iterrows():
    chequear(f"lujo HHI marca {anio}", f"| {miles(r.HHI_marca)} |")
    chequear(f"lujo HHI grupo {anio}", f"| {miles(r.HHI_grupo)} |")
    chequear(f"lujo ΔHHI {anio}", f"| {r.dHHI_propiedad_comun_VW:.0f} |")
chequear("lujo grupo VW 2025", f"{lujo.loc[2025, 'share_grupo_VW_%']:.1f} %", ("informe", "slides", "preguntas"))
chequear("lujo BMW Group 2025", f"{lujo.loc[2025, 'share_BMW_Group_%']:.1f} %")
chequear("ΔHHI Audi-Porsche 2025", f"{lujo.loc[2025, 'dHHI_Audi_Porsche']:.0f}", ("informe", "slides", "preguntas"))
s25 = sh[sh.anio == 2025].set_index("marca").s
for m in ("BMW", "Mercedes-Benz", "Audi", "Volvo", "Lexus", "Mini", "Porsche"):
    chequear(f"lujo 2025 {m}", f"{s25[m]:.1f} %")
chequear("Lerner lujo rango", f"entre {lern.iloc[-1, 2]:.2f} y {lern.iloc[0, 2]:.2f}")
chequear("Lerner livianos rango", f"entre {lern.iloc[-1, 1]:.2f} y {lern.iloc[0, 1]:.2f}")

print()
if fallas:
    print(f"{len(fallas)} FALLAS:")
    print("\n".join(fallas))
    sys.exit(1)
print("Todas las cifras verificadas coinciden.")
