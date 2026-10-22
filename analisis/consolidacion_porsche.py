"""Ejercicio de sesgo de consolidación: integración de Porsche AG en el Grupo VW.

Replica en pequeño la lógica de Hess y Wang (2026), sección 3:
  - proxy de markup: x = Q/M (ingresos / costo de materiales). Bajo Cobb-Douglas,
    mu = beta_m * Q/M (ec. 7), así que Δln x = Δln mu sin estimar beta_m;
  - especificación "solo adquirente": VW antes vs grupo consolidado después (ec. 8);
  - especificación "consolidación virtual": (VW + Porsche) antes vs grupo después;
  - agregación: pooled (pesos por costo) vs ponderado por ventas (Proposición 2);
  - descomposición del sesgo de frontera: x_pool - x_A = w_T (x_T - x_A) (sección 3.3.2);
  - ilustración de la Proposición 1 (TFPR) con elasticidades del paper (NACE 29).

A = Grupo VW, T = Porsche AG. Antes = 2011 (último año completo con Porsche fuera
del perímetro de VW). Después = 2013 y 2014 (primeros años completos dentro).
Corre: python3 analisis/consolidacion_porsche.py
"""
import numpy as np
import pandas as pd

from estilo import AZUL, AQUA, DATA, GRIS, NARANJA, RES, TEXTO_2, guardar, plt

PRE, POSTS = 2011, (2013, 2014)
# Elasticidades de producto, NACE 29 (fabricación de vehículos), Hess y Wang (2026),
# Tabla B.1, producción bruta. Estimadas para empresas españolas: solo ilustrativas.
BK, BL, BM = 0.267, 0.229, 0.388


def cargar():
    g = pd.read_csv(DATA / "global_vw_porsche.csv")
    vw = g[g.entidad == "VW_Grupo"].set_index("anio")
    pa = g[g.entidad == "Porsche_AG"].set_index("anio")
    marcas = pd.read_csv(DATA / "vw_marcas_ingresos.csv")
    return vw, pa, marcas


def ln(x):
    return float(np.log(x))


def ejercicio_markup(vw, pa):
    QA, MA = vw.loc[PRE, "ingresos_meur"], vw.loc[PRE, "costo_materiales_meur"]
    QT, MT = pa.loc[PRE, "ingresos_meur"], pa.loc[PRE, "costo_materiales_meur"]
    xA, xT = QA / MA, QT / MT
    x_pool = (QA + QT) / (MA + MT)
    wA, wT = MA / (MA + MT), MT / (MA + MT)          # pesos por costo (materiales)
    piA, piT = QA / (QA + QT), QT / (QA + QT)        # pesos por ventas
    x_sales = piA * xA + piT * xT

    pre = {
        "x_VW_2011": xA, "x_Porsche_2011": xT, "x_pool_2011": x_pool,
        "x_ventas_2011": x_sales, "w_T (peso costo Porsche)": wT,
        "pi_T (peso ventas Porsche)": piT,
        "Termino w_T(x_T - x_A)": wT * (xT - xA),
        "x_pool - x_A (verificación identidad)": x_pool - xA,
        "w_A x_A + w_T x_T (verificación)": wA * xA + wT * xT,
        "Sesgo frontera ln x_pool - ln x_A": ln(x_pool) - ln(xA),
        "Sesgo agregación ln x_pool - ln x_ventas": ln(x_pool) - ln(x_sales),
    }
    assert abs(pre["x_pool - x_A (verificación identidad)"] - pre["Termino w_T(x_T - x_A)"]) < 1e-12
    assert x_sales >= x_pool  # Proposición 2

    filas = []
    for post in POSTS:
        x_post = vw.loc[post, "ingresos_meur"] / vw.loc[post, "costo_materiales_meur"]
        filas.append({
            "post": post,
            "x_post": x_post,
            "solo_adquirente": ln(x_post) - ln(xA),
            "consolidacion_virtual": ln(x_post) - ln(x_pool),
            "virtual_pesos_ventas": ln(x_post) - ln(x_sales),
        })
    return pre, pd.DataFrame(filas)


def sensibilidad_intragrupo(vw, pa, marcas):
    """Antes de 2012, las ventas de Porsche a sociedades de VW (p. ej. Porsche Holding
    Salzburg) figuran como ingreso de Porsche y como compra de VW. Tras consolidar se
    eliminan. Se aproxima su tamaño con la proporción observada en 2013 (VW_AR2014 p.55):
    ventas intragrupo de Porsche / ingresos de Porsche."""
    p13 = marcas[(marcas.marca == "Porsche") & (marcas.anio == 2013)].iloc[0]
    s = 1 - p13.ventas_a_terceros_meur / p13.ingresos_meur
    QA, MA = vw.loc[PRE, "ingresos_meur"], vw.loc[PRE, "costo_materiales_meur"]
    QT, MT = pa.loc[PRE, "ingresos_meur"], pa.loc[PRE, "costo_materiales_meur"]
    E = s * QT  # supuesto: misma proporción en 2011
    x_pool_adj = (QA + QT - E) / (MA + MT - E)
    out = []
    for post in POSTS:
        x_post = vw.loc[post, "ingresos_meur"] / vw.loc[post, "costo_materiales_meur"]
        out.append({"post": post, "proporcion_intragrupo_2013": s, "eliminacion_supuesta_meur": E,
                    "x_pool_ajustado_2011": x_pool_adj,
                    "consolidacion_virtual_ajustada": ln(x_post) - ln(x_pool_adj)})
    return pd.DataFrame(out)


def sensibilidad_man(vw, pa, marcas):
    """MAN entra al perímetro el 9-nov-2011: ~2 meses en 2011 y año completo en 2013-14.
    VW publica los ingresos de la marca MAN, pero no su costo de materiales.
    Si existe data/man.csv (anio,ingresos_meur,costo_materiales_meur, de los reportes de
    MAN SE), se usa el ratio observado. Si no, se muestra un rango HIPOTÉTICO de ratios
    Q/M para MAN, solo para ver si el signo de la conclusión depende de MAN."""
    man_rev = marcas[marcas.marca == "MAN"].set_index("anio").ingresos_meur
    ruta = DATA / "man.csv"
    if ruta.exists():
        m = pd.read_csv(ruta).set_index("anio")
        escenarios = {"observado (reportes MAN SE)": {a: m.loc[a, "ingresos_meur"] / m.loc[a, "costo_materiales_meur"]
                                                      for a in m.index}}
    else:
        escenarios = {f"hipotético x_MAN={v:.2f}": {a: v for a in (PRE,) + POSTS}
                      for v in (1.30, 1.40, 1.50, 1.60, 1.70)}
    QT, MT = pa.loc[PRE, "ingresos_meur"], pa.loc[PRE, "costo_materiales_meur"]
    out = []
    for nombre, xm in escenarios.items():
        def sin_man(anio):
            Q = vw.loc[anio, "ingresos_meur"] - man_rev[anio]
            M = vw.loc[anio, "costo_materiales_meur"] - man_rev[anio] / xm[anio]
            return Q, M
        QA, MA = sin_man(PRE)
        x_pool = (QA + QT) / (MA + MT)
        for post in POSTS:
            Qp, Mp = sin_man(post)
            out.append({"escenario": nombre, "post": post,
                        "solo_adquirente_sin_MAN": ln(Qp / Mp) - ln(QA / MA),
                        "consolidacion_virtual_sin_MAN": ln(Qp / Mp) - ln(x_pool)})
    return pd.DataFrame(out), ruta.exists()


def ilustracion_tfpr(vw, pa):
    """Proposición 1: Z_pool / Z_A = a + r b. K = activos totales (proxy muy imperfecto:
    incluye servicios financieros), L = empleados, M = costo de materiales."""
    A = vw.loc[PRE]; T = pa.loc[PRE]
    K = A.activos_totales_meur + T.activos_totales_meur
    L = A.empleados + T.empleados
    M = A.costo_materiales_meur + T.costo_materiales_meur
    sK, sL, sM = A.activos_totales_meur / K, A.empleados / L, A.costo_materiales_meur / M
    Z = lambda Q, k, l, m: Q / (k ** BK * l ** BL * m ** BM)  # noqa: E731
    ZA = Z(A.ingresos_meur, A.activos_totales_meur, A.empleados, A.costo_materiales_meur)
    ZT = Z(T.ingresos_meur, T.activos_totales_meur, T.empleados, T.costo_materiales_meur)
    Zp = Z(A.ingresos_meur + T.ingresos_meur, K, L, M)
    a = sK ** BK * sL ** BL * sM ** BM
    b = (1 - sK) ** BK * (1 - sL) ** BL * (1 - sM) ** BM
    r = ZT / ZA
    assert abs(Zp / ZA - (a + r * b)) < 1e-9  # identidad de la Proposición 1
    return {"s_K": sK, "s_L": sL, "s_M": sM, "a": a, "b": b, "a+b": a + b,
            "rendimientos (bk+bl+bm)": BK + BL + BM, "r = Z_T/Z_A": r,
            "umbral r* = (1-a)/b": (1 - a) / b, "sesgo TFPR ln(a + r b)": ln(a + r * b)}


def figuras(vw, pa, res, sens_man, man_observado):
    # 1) Nivel del proxy Q/M por año: muestra por qué el sesgo es positivo en este caso
    fig, ax = plt.subplots(figsize=(7, 3.8))
    xv = vw.ingresos_meur / vw.costo_materiales_meur
    xp = pa.ingresos_meur / pa.costo_materiales_meur
    ax.plot(xv.index, xv.values, color=AZUL, marker="o", label="Grupo VW (consolidado)")
    ax.plot(xp.index, xp.values, color=NARANJA, marker="o", label="Porsche AG")
    ax.axvspan(2011.6, 2012.4, color=GRIS, alpha=0.12, lw=0)
    ax.text(2012, xp.max() + 0.005, "Consolidación\n1-ago-2012", ha="center", va="bottom", fontsize=8, color=TEXTO_2)
    for s, c in ((xv, AZUL), (xp, NARANJA)):
        ax.annotate(f"{s.iloc[-1]:.2f}", (s.index[-1], s.iloc[-1]), xytext=(6, 0),
                    textcoords="offset points", va="center", fontsize=9, color=TEXTO_2)
    ax.set_title("Proxy de markup: ingresos / costo de materiales")
    ax.set_ylabel("Q / M")
    ax.set_xticks(range(2009, 2015))
    ax.set_ylim(1.45, 1.80)
    ax.legend(loc="upper left")
    guardar(fig, "fig1_proxy_markup_vw_porsche.png")

    # 2) Cambio estimado del log-markup según especificación
    fig, ax = plt.subplots(figsize=(7, 3.6))
    specs = [("solo_adquirente", "Solo adquirente\n(VW 2011 → grupo)", AZUL),
             ("consolidacion_virtual", "Consolidación virtual\n(VW+Porsche 2011 → grupo)", NARANJA),
             ("virtual_pesos_ventas", "Virtual con pesos\npor ventas (Prop. 2)", AQUA)]
    ancho = 0.26
    for i, (col, etq, c) in enumerate(specs):
        vals = res[col].values * 100
        pos = np.arange(len(res)) + (i - 1) * ancho
        ax.bar(pos, vals, width=ancho - 0.02, color=c, label=etq.replace("\n", " "))
        for p, v in zip(pos, vals):
            ax.text(p, v + (0.08 if v >= 0 else -0.08), f"{v:+.2f}", ha="center",
                    va="bottom" if v >= 0 else "top", fontsize=8, color=TEXTO_2)
    ax.axhline(0, color=TEXTO_2, lw=0.8)
    ax.set_ylim(min(0, res[[c for c, _, _ in specs]].values.min() * 100) - 0.2,
                res[[c for c, _, _ in specs]].values.max() * 100 * 1.18)
    ax.set_xticks(range(len(res)), [f"Después = {p}" for p in res.post])
    ax.set_ylabel("Δ ln(Q/M) × 100 (≈ %)")
    ax.set_title("Cambio estimado del markup de VW tras integrar Porsche (antes = 2011)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=8)
    guardar(fig, "fig2_especificaciones_markup.png")

    # 3) Sensibilidad a MAN (rango hipotético u observado)
    d = sens_man[sens_man.post == 2013]
    fig, ax = plt.subplots(figsize=(7, 3.4))
    etiquetas = [e.replace("hipotético ", "") for e in d.escenario]
    y = np.arange(len(d))
    ax.barh(y + 0.18, d.solo_adquirente_sin_MAN * 100, height=0.34, color=AZUL, label="Solo adquirente, sin MAN")
    ax.barh(y - 0.18, d.consolidacion_virtual_sin_MAN * 100, height=0.34, color=NARANJA, label="Consolidación virtual, sin MAN")
    ax.axvline(0, color=TEXTO_2, lw=0.8)
    ax.set_yticks(y, etiquetas)
    ax.set_xlabel("Δ ln(Q/M) 2011→2013 × 100")
    titulo = "Sensibilidad: quitando MAN del perímetro" + ("" if man_observado else " (ratios de MAN hipotéticos)")
    ax.set_title(titulo)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=8)
    guardar(fig, "fig3_sensibilidad_man.png")


def main():
    vw, pa, marcas = cargar()
    pre, res = ejercicio_markup(vw, pa)
    intra = sensibilidad_intragrupo(vw, pa, marcas)
    sens_man, man_obs = sensibilidad_man(vw, pa, marcas)
    tfpr = ilustracion_tfpr(vw, pa)
    xcs = (vw.ingresos_meur / vw.costo_ventas_meur).rename("Q/costo_ventas VW")

    pd.Series(pre).to_csv(RES / "porsche_pre2011.csv", header=["valor"])
    res.to_csv(RES / "porsche_especificaciones.csv", index=False)
    intra.to_csv(RES / "porsche_sens_intragrupo.csv", index=False)
    sens_man.to_csv(RES / "porsche_sens_man.csv", index=False)
    pd.Series(tfpr).to_csv(RES / "porsche_tfpr_prop1.csv", header=["valor"])

    pd.set_option("display.float_format", lambda v: f"{v:.4f}")
    print("== Antes (2011) ==")
    print(pd.Series(pre).to_string())
    print("\n== Δ ln(Q/M) por especificación ==")
    print(res.to_string(index=False))
    print("\n== Sensibilidad ventas intragrupo ==")
    print(intra.to_string(index=False))
    print(f"\n== Sensibilidad MAN ({'observado' if man_obs else 'HIPOTÉTICO: falta data/man.csv'}) ==")
    print(sens_man.to_string(index=False))
    print("\n== Ilustración Proposición 1 (TFPR, beta NACE 29 del paper) ==")
    print(pd.Series(tfpr).to_string())
    print(f"   beta_m * x_VW_2011 = {BM * pre['x_VW_2011']:.3f}  (nivel no interpretable como markup: solo usamos cambios)")
    print("\n== Contexto: ingresos / costo de ventas VW ==")
    print(xcs.to_string())
    figuras(vw, pa, res, sens_man, man_obs)


if __name__ == "__main__":
    main()
