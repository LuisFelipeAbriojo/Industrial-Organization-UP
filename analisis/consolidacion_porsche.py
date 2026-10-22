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
    VW no publica el costo de materiales de MAN. Con data/man.csv (reportes de MAN SE):
      - 2013 y 2014: se restan de VW los ingresos y el costo de materiales propios de MAN;
      - 2011: se restan los ingresos de MAN dentro de VW (2 652, VW_AR2012 p.109) y un costo
        de materiales aproximado con la razón Q/M de MAN en 2011 (aproximación documentada).
    Además se muestra un rango HIPOTÉTICO de razones Q/M para MAN como sensibilidad."""
    man_rev = marcas[marcas.marca == "MAN"].set_index("anio").ingresos_meur
    escenarios = {}
    ruta = DATA / "man.csv"
    if ruta.exists():
        m = pd.read_csv(ruta).set_index("anio")
        x11 = m.loc[PRE, "ingresos_meur"] / m.loc[PRE, "costo_materiales_meur"]
        escenarios["observado (MAN SE)"] = {
            PRE: (man_rev[PRE], man_rev[PRE] / x11),
            **{a: (m.loc[a, "ingresos_meur"], m.loc[a, "costo_materiales_meur"]) for a in POSTS}}
    for v in (1.30, 1.50, 1.70, 1.90):
        escenarios[f"hipotético x_MAN={v:.2f}"] = {a: (man_rev[a], man_rev[a] / v) for a in (PRE,) + POSTS}
    QT, MT = pa.loc[PRE, "ingresos_meur"], pa.loc[PRE, "costo_materiales_meur"]
    out = []
    for nombre, man in escenarios.items():
        def sin_man(anio):
            return (vw.loc[anio, "ingresos_meur"] - man[anio][0],
                    vw.loc[anio, "costo_materiales_meur"] - man[anio][1])
        QA, MA = sin_man(PRE)
        x_pool = (QA + QT) / (MA + MT)
        for post in POSTS:
            Qp, Mp = sin_man(post)
            out.append({"escenario": nombre, "post": post,
                        "x_MAN_post": man[post][0] / man[post][1],
                        "solo_adquirente_sin_MAN": ln(Qp / Mp) - ln(QA / MA),
                        "consolidacion_virtual_sin_MAN": ln(Qp / Mp) - ln(x_pool)})
    return pd.DataFrame(out), ruta.exists()


def ajustes_combinados(vw, pa, marcas, intra):
    """Consolidación virtual con ajustes acumulados (solo datos observados):
    (1) tal cual, (2) sin MAN, (3) sin MAN y sin ventas intragrupo de Porsche en 2011."""
    m = pd.read_csv(DATA / "man.csv").set_index("anio")
    man_rev = marcas[marcas.marca == "MAN"].set_index("anio").ingresos_meur
    x11 = m.loc[PRE, "ingresos_meur"] / m.loc[PRE, "costo_materiales_meur"]
    man = {PRE: (man_rev[PRE], man_rev[PRE] / x11),
           **{a: (m.loc[a, "ingresos_meur"], m.loc[a, "costo_materiales_meur"]) for a in POSTS}}
    E = intra.eliminacion_supuesta_meur.iloc[0]
    QA, MA = vw.loc[PRE, "ingresos_meur"], vw.loc[PRE, "costo_materiales_meur"]
    QT, MT = pa.loc[PRE, "ingresos_meur"], pa.loc[PRE, "costo_materiales_meur"]
    pre = {"virtual": (QA + QT) / (MA + MT),
           "virtual_sin_MAN": (QA - man[PRE][0] + QT) / (MA - man[PRE][1] + MT),
           "virtual_sin_MAN_ni_intragrupo": (QA - man[PRE][0] + QT - E) / (MA - man[PRE][1] + MT - E)}
    out = []
    for post in POSTS:
        Q, M = vw.loc[post, "ingresos_meur"], vw.loc[post, "costo_materiales_meur"]
        x_con, x_sin = Q / M, (Q - man[post][0]) / (M - man[post][1])
        out.append({"post": post,
                    "virtual": ln(x_con) - ln(pre["virtual"]),
                    "virtual_sin_MAN": ln(x_sin) - ln(pre["virtual_sin_MAN"]),
                    "virtual_sin_MAN_ni_intragrupo": ln(x_sin) - ln(pre["virtual_sin_MAN_ni_intragrupo"])})
    return pd.DataFrame(out)


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


def figuras(vw, pa, res, comb):
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

    # 3) Ajustes de perímetro acumulados (datos observados)
    if comb is not None:
        fig, ax = plt.subplots(figsize=(7, 3.6))
        specs = [("virtual", "Consolidación virtual (tal cual)", NARANJA),
                 ("virtual_sin_MAN", "… sin MAN", AZUL),
                 ("virtual_sin_MAN_ni_intragrupo", "… sin MAN ni ventas intragrupo", AQUA)]
        ancho = 0.26
        for i, (col, etq, c) in enumerate(specs):
            vals = comb[col].values * 100
            pos = np.arange(len(comb)) + (i - 1) * ancho
            ax.bar(pos, vals, width=ancho - 0.02, color=c, label=etq)
            for p_, v in zip(pos, vals):
                ax.text(p_, v + (0.06 if v >= 0 else -0.06), f"{v:+.2f}", ha="center",
                        va="bottom" if v >= 0 else "top", fontsize=8, color=TEXTO_2)
        ax.axhline(0, color=TEXTO_2, lw=0.8)
        lo, hi = comb[[c for c, _, _ in specs]].values.min() * 100, comb[[c for c, _, _ in specs]].values.max() * 100
        ax.set_ylim(min(0, lo) - 0.4, hi + 0.4)
        ax.set_xticks(range(len(comb)), [f"2011 → {p_}" for p_ in comb.post])
        ax.set_ylabel("Δ ln(Q/M) × 100 (≈ %)")
        ax.set_title("Al limpiar el perímetro, el aumento del markup desaparece")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=8)
        guardar(fig, "fig3_ajustes_perimetro.png")


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
    comb = ajustes_combinados(vw, pa, marcas, intra) if man_obs else None
    if comb is not None:
        comb.to_csv(RES / "porsche_ajustes_combinados.csv", index=False)
        print("\n== Consolidación virtual con ajustes acumulados ==")
        print(comb.to_string(index=False))
    figuras(vw, pa, res, comb)


if __name__ == "__main__":
    main()
