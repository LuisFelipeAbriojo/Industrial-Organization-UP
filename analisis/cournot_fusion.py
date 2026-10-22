"""Mini-modelo: fusión horizontal en Cournot con reducción del costo marginal.

Trade-off de Williamson / condición de Farrell y Shapiro (1990) con demanda lineal
P = a - Q y costos marginales constantes (al estilo de los ejercicios de la semana 9).
Para cada costo marginal post-fusión c_M se calculan precio, excedentes y beneficios, y
se obtienen tres umbrales:
  1. precio (y excedente del consumidor) no sube:  c_M <= c_1 + c_2 - P_pre  (Farrell-Shapiro)
  2. bienestar total no cae (criterio de Williamson)
  3. la fusión es rentable para las partes:  pi_M >= pi_1 + pi_2
Corre: python3 analisis/cournot_fusion.py
"""
import numpy as np
import pandas as pd
from scipy.optimize import brentq

from estilo import AZUL, GRIS, NARANJA, RES, TEXTO_2, guardar, plt


def cournot(a, c):
    """Equilibrio de Cournot con P = a - Q y costos c (elimina empresas con q <= 0)."""
    c = np.asarray(c, float)
    activos = np.ones(len(c), bool)
    while True:
        n, S = activos.sum(), c[activos].sum()
        q = np.where(activos, (a + S - (n + 1) * c) / (n + 1), 0.0)
        if (q[activos] > 0).all():
            break
        activos &= q > 0
    Q = q.sum()
    P = a - Q
    pi = (P - c) * q
    return {"q": q, "Q": Q, "P": P, "pi": pi, "EC": Q ** 2 / 2, "W": Q ** 2 / 2 + pi.sum()}


def analizar(nombre, a, c, fusionan=(0, 1)):
    pre = cournot(a, c)
    resto = [ci for i, ci in enumerate(c) if i not in fusionan]
    post = lambda cM: cournot(a, [cM] + resto)  # noqa: E731
    i, j = fusionan
    c_fs = c[i] + c[j] - pre["P"]  # Farrell-Shapiro (lineal): precio igual
    pi_partes = pre["pi"][i] + pre["pi"][j]
    lo, hi = 0.0, min(c[i], c[j])
    f_w = lambda cM: post(cM)["W"] - pre["W"]  # noqa: E731
    f_pi = lambda cM: post(cM)["pi"][0] - pi_partes  # noqa: E731
    c_w = brentq(f_w, lo, hi) if f_w(lo) * f_w(hi) < 0 else (hi if f_w(hi) >= 0 else np.nan)
    c_pi = brentq(f_pi, lo, hi) if f_pi(lo) * f_pi(hi) < 0 else (hi if f_pi(hi) >= 0 else np.nan)
    if c_fs >= 0:
        assert abs(post(c_fs)["P"] - pre["P"]) < 1e-9
    sin_sinergia = post(min(c[i], c[j]))

    print(f"\n=== {nombre}: P = {a} - Q, costos {c}, se fusionan {i + 1} y {j + 1} ===")
    print(f"Pre-fusión:  q = {np.round(pre['q'], 2)}, Q = {pre['Q']:.2f}, P = {pre['P']:.2f}, "
          f"pi = {np.round(pre['pi'], 2)}, EC = {pre['EC']:.2f}, W = {pre['W']:.2f}")
    print(f"Post sin sinergias (c_M = {min(c[i], c[j])}): P = {sin_sinergia['P']:.2f}, "
          f"pi_M = {sin_sinergia['pi'][0]:.2f} vs pi_1+pi_2 = {pi_partes:.2f}, W = {sin_sinergia['W']:.2f}")
    print(f"Umbral precio/EC (Farrell-Shapiro): c_M <= {c_fs:.2f}"
          + ("  -> INALCANZABLE (costo negativo)" if c_fs < 0 else ""))
    print(f"Umbral bienestar total (Williamson): c_M <= {c_w:.2f}")
    print(f"Umbral rentabilidad para las partes: c_M <= {c_pi:.2f}")

    grid = np.linspace(0, min(c[i], c[j]), 121)
    tabla = pd.DataFrame([{"c_M": g, "P_post": post(g)["P"], "EC_post": post(g)["EC"],
                           "W_post": post(g)["W"], "pi_M": post(g)["pi"][0]} for g in grid])
    tabla["P_pre"], tabla["EC_pre"], tabla["W_pre"], tabla["pi_partes_pre"] = pre["P"], pre["EC"], pre["W"], pi_partes
    resumen = {"escenario": nombre, "a": a, "costos": str(c), "P_pre": pre["P"],
               "P_post_sin_sinergias": sin_sinergia["P"], "umbral_precio": c_fs,
               "umbral_bienestar": c_w, "umbral_rentabilidad": c_pi,
               "reduccion_necesaria_precio_%": (1 - c_fs / min(c[i], c[j])) * 100}
    return tabla, resumen


def figura(tablas, resumenes):
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    for ax, tabla, r in zip(axes, tablas, resumenes):
        ax.plot(tabla.c_M, tabla.P_post, color=AZUL, label="Precio post-fusión")
        ax.axhline(r["P_pre"], color=NARANJA, lw=2, ls="--", label=f"Precio pre-fusión = {r['P_pre']:.2f}")
        if r["umbral_precio"] >= 0:
            ax.axvspan(0, r["umbral_precio"], color=AZUL, alpha=0.10, lw=0)
            ax.annotate(f"c_M ≤ {r['umbral_precio']:.1f}:\nel precio no sube",
                        (r["umbral_precio"] * 0.62, r["P_pre"]), xytext=(0, 10),
                        textcoords="offset points", ha="center", fontsize=8, color=TEXTO_2)
        else:
            ax.text(0.5, 0.08, f"Umbral c_M ≤ {r['umbral_precio']:.2f} < 0:\nel precio siempre sube",
                    transform=ax.transAxes, ha="center", fontsize=8, color=TEXTO_2)
        if not np.isnan(r["umbral_bienestar"]):
            ax.axvline(r["umbral_bienestar"], color=GRIS, lw=1, ls=":")
            sin_sin = r["umbral_bienestar"] >= tabla.c_M.max()
            etq = " W total no cae\n aun sin sinergias" if sin_sin else " W total no cae\n si c_M ≤ %.1f" % r["umbral_bienestar"]
            ax.text(r["umbral_bienestar"], ax.get_ylim()[1], etq, fontsize=7, color=TEXTO_2,
                    va="top", ha="right" if sin_sin else "left")
        ax.set_title(r["escenario"], fontsize=10)
        ax.set_xlabel("Costo marginal de la empresa fusionada (c_M)")
        ax.set_ylabel("Precio")
        ax.legend(loc="upper left", fontsize=7.5, bbox_to_anchor=(0, -0.2), ncol=1)
    fig.suptitle("Cournot: ¿cuánta eficiencia necesita una fusión para que el precio no suba?",
                 x=0.01, ha="left", fontsize=12, fontweight="bold")
    fig.tight_layout()
    guardar(fig, "fig4_cournot_umbral.png")


def main():
    escenarios = [
        ("A. Datos semana 9: socios simétricos", 150, [30, 30, 45]),
        ("B. Socio grande eficiente + socio pequeño", 150, [30, 50, 30, 30]),
    ]
    tablas, resumenes = [], []
    for nombre, a, c in escenarios:
        t, r = analizar(nombre, a, c)
        tablas.append(t)
        resumenes.append(r)
        t.to_csv(RES / f"cournot_{nombre[0]}.csv", index=False)
    pd.DataFrame(resumenes).to_csv(RES / "cournot_resumen.csv", index=False)
    figura(tablas, resumenes)


if __name__ == "__main__":
    main()
