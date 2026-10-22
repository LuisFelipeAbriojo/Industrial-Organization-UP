"""Perú: participaciones del Grupo VW y concentración (HHI) en vehículos livianos nuevos.

Datos: inscripciones SUNARP publicadas por la AAP (data/peru_livianos_marca.csv,
data/peru_lujo_marca.csv). HHI = suma de participaciones al cuadrado (en %^2, 0-10 000).

- Livianos (2020-2025): la AAP detalla las 25 primeras marcas y agrupa el resto en
  "Otros". Se reporta un rango: cota inferior (las marcas de "Otros" son atomísticas)
  y cota superior (cada marca de "Otros" tiene a lo sumo la participación de la marca 25,
  así que su aporte es <= s_otros * s_min).
- Lujo (2022-2025): lista completa de marcas, HHI exacto.
- Además, HHI por grupo propietario (data/grupos_propietarios.csv): las marcas de un mismo
  dueño no compiten entre sí en precios, por lo que el HHI relevante es por grupo.
- Lerner implícito en Cournot (semana 11): L = HHI / epsilon, solo ilustrativo
  (no estimamos la elasticidad de la demanda).
Corre: python3 analisis/peru_concentracion.py
"""
import numpy as np
import pandas as pd

from estilo import AZUL, AQUA, DATA, GRIS, NARANJA, RES, TEXTO_2, guardar, plt

VW_GRUPO = ["Volkswagen", "Audi", "Porsche", "Lamborghini", "Bentley"]


def cargar():
    liv = pd.read_csv(DATA / "peru_livianos_marca.csv")
    lujo = pd.read_csv(DATA / "peru_lujo_marca.csv")
    grupos = pd.read_csv(DATA / "grupos_propietarios.csv").set_index("marca").grupo
    return liv, lujo, grupos


def shares(df):
    tot = df.loc[df.marca == "TOTAL", "unidades"].iloc[0]
    d = df[df.marca != "TOTAL"].copy()
    d["s"] = d.unidades / tot * 100
    return d, tot


def hhi_livianos(liv, lujo, grupos):
    filas = []
    for anio, g in liv.groupby("anio"):
        d, tot = shares(g)
        top = d[d.marca != "Otros"]
        s_otros = d.loc[d.marca == "Otros", "s"].iloc[0]
        lo = (top.s ** 2).sum()
        hi = lo + s_otros * top.s.min()

        # Grupo VW: marca VW (top 25) + marcas premium del grupo (tabla de lujo, desde 2022)
        u_vw = top.loc[top.marca == "Volkswagen", "unidades"].sum()
        lj = lujo[(lujo.anio == anio) & (lujo.marca.isin(VW_GRUPO))]
        u_vw_lujo = lj.unidades.sum() if len(lj) else np.nan

        # HHI por grupo: se suman las marcas identificadas de un mismo dueño. Las marcas
        # de lujo (dentro de "Otros") se mueven de "Otros" a su grupo cuando hay dato.
        d2 = top[["marca", "unidades"]].copy()
        otros = d.loc[d.marca == "Otros", "unidades"].iloc[0]
        lj_all = lujo[(lujo.anio == anio) & (lujo.marca != "TOTAL") & (~lujo.marca.isin(d2.marca))]
        if len(lj_all):
            d2 = pd.concat([d2, lj_all[["marca", "unidades"]]])
            otros -= lj_all.unidades.sum()
        d2["grupo"] = d2.marca.map(grupos).fillna(d2.marca)
        sg = d2.groupby("grupo").unidades.sum() / tot * 100
        lo_g = (sg ** 2).sum()
        hi_g = lo_g + (otros / tot * 100) * top.s.min()

        filas.append({
            "anio": anio, "total": tot,
            "share_VW_marca_%": u_vw / tot * 100,
            "share_grupo_VW_%": (u_vw + u_vw_lujo) / tot * 100 if not np.isnan(u_vw_lujo) else np.nan,
            "share_top4_marcas_%": top.s.nlargest(4).sum(),
            "HHI_marca_min": lo, "HHI_marca_max": hi,
            "HHI_grupo_min": lo_g, "HHI_grupo_max": hi_g,
            "share_otros_%": s_otros,
        })
    return pd.DataFrame(filas)


def hhi_lujo(lujo, grupos):
    filas, detalle = [], []
    for anio, g in lujo.groupby("anio"):
        d, tot = shares(g)
        d["grupo"] = d.marca.map(grupos).fillna(d.marca)
        sg = d.groupby("grupo").s.sum()
        vw = d[d.marca.isin(VW_GRUPO)]
        filas.append({"anio": anio, "total": tot, "HHI_marca": (d.s ** 2).sum(),
                      "HHI_grupo": (sg ** 2).sum(),
                      "share_grupo_VW_%": vw.s.sum(),
                      # ΔHHI por propiedad común VW: (suma s)^2 - suma s^2 = 2 * suma de productos cruzados
                      "dHHI_propiedad_comun_VW": vw.s.sum() ** 2 - (vw.s ** 2).sum(),
                      "dHHI_Audi_Porsche": 2 * vw.loc[vw.marca == "Audi", "s"].sum() * vw.loc[vw.marca == "Porsche", "s"].sum(),
                      "share_Audi_%": vw.loc[vw.marca == "Audi", "s"].sum(),
                      "share_Porsche_%": vw.loc[vw.marca == "Porsche", "s"].sum(),
                      "share_BMW_Group_%": sg.get("BMW Group", 0),
                      "share_Mercedes_%": sg.get("Mercedes-Benz", 0)})
        detalle.append(d.assign(anio=anio))
    return pd.DataFrame(filas), pd.concat(detalle)


def lerner_ilustrativo(lujo_hhi, liv_hhi):
    filas = []
    for eps in (1.5, 3.0, 5.0):
        filas.append({"epsilon_supuesta": eps,
                      "L_livianos_2025 (HHI grupo min)": liv_hhi.set_index("anio").loc[2025, "HHI_grupo_min"] / 10000 / eps,
                      "L_lujo_2025 (HHI grupo)": lujo_hhi.set_index("anio").loc[2025, "HHI_grupo"] / 10000 / eps})
    return pd.DataFrame(filas)


def figuras(liv_hhi, lujo_hhi, lujo_det):
    # 5) participación del Grupo VW en livianos
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(liv_hhi.anio, liv_hhi["share_VW_marca_%"], color=AZUL, marker="o", label="Marca Volkswagen")
    g = liv_hhi.dropna(subset=["share_grupo_VW_%"])
    ax.plot(g.anio, g["share_grupo_VW_%"], color=NARANJA, marker="o",
            label="Grupo VW (VW + Audi + Porsche + Lamborghini + Bentley)")
    for _, r in liv_hhi.iterrows():
        ax.annotate(f"{r['share_VW_marca_%']:.1f}%", (r.anio, r["share_VW_marca_%"]), xytext=(0, -14),
                    textcoords="offset points", ha="center", fontsize=8, color=TEXTO_2)
    ax.set_ylim(0, 5)
    ax.set_ylabel("% de inscripciones de livianos nuevos")
    ax.set_title("Perú: participación del Grupo VW en vehículos livianos nuevos")
    ax.legend(loc="upper right", fontsize=8)
    guardar(fig, "fig5_peru_share_vw.png")

    # 6) segmento de lujo 2025: participaciones por marca, marcas VW destacadas
    d = lujo_det[(lujo_det.anio == 2025) & (lujo_det.s >= 0.5)].sort_values("s")
    fig, ax = plt.subplots(figsize=(7, 3.6))
    colores = [NARANJA if m in VW_GRUPO else GRIS for m in d.marca]
    ax.barh(d.marca, d.s, color=colores, height=0.7)
    for y, (m, s) in enumerate(zip(d.marca, d.s)):
        ax.text(s + 0.4, y, f"{s:.1f}%", va="center", fontsize=8, color=TEXTO_2)
    ax.set_xlabel("% del segmento de lujo (2025)")
    r = lujo_hhi.set_index("anio").loc[2025]
    ax.set_title("Perú, segmento de lujo 2025: marcas del Grupo VW en naranja")
    ax.text(0.98, 0.05, f"HHI marcas = {r.HHI_marca:,.0f}\nHHI grupos = {r.HHI_grupo:,.0f}\n"
            f"Grupo VW = {r['share_grupo_VW_%']:.1f}%", transform=ax.transAxes,
            ha="right", va="bottom", fontsize=8, color=TEXTO_2)
    ax.grid(axis="y", visible=False)
    guardar(fig, "fig6_peru_lujo_2025.png")

    # 7) HHI en el tiempo (misma escala, un solo eje)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.fill_between(liv_hhi.anio, liv_hhi.HHI_grupo_min, liv_hhi.HHI_grupo_max, color=AZUL, alpha=0.15, lw=0)
    ax.plot(liv_hhi.anio, liv_hhi.HHI_grupo_min, color=AZUL, marker="o", label="Livianos, por grupo (rango)")
    ax.plot(lujo_hhi.anio, lujo_hhi.HHI_grupo, color=NARANJA, marker="o", label="Lujo, por grupo")
    ax.plot(lujo_hhi.anio, lujo_hhi.HHI_marca, color=AQUA, marker="o", ls="--", label="Lujo, por marca")
    # Umbral de presunción estructural, Merger Guidelines 2023 (EE.UU.), slides semana 11
    ax.axhline(1800, color=GRIS, lw=0.8, ls=":")
    ax.text(2020, 1840, "HHI = 1 800 (Merger Guidelines 2023, con ΔHHI > 100)", fontsize=7, color=TEXTO_2)
    ax.set_ylim(0, 2700)
    ax.set_ylabel("HHI (0-10 000)")
    ax.set_title("Perú: concentración en vehículos livianos nuevos")
    ax.legend(loc="center right", fontsize=8)
    guardar(fig, "fig7_peru_hhi.png")


def main():
    liv, lujo, grupos = cargar()
    liv_hhi = hhi_livianos(liv, lujo, grupos)
    lujo_hhi, lujo_det = hhi_lujo(lujo, grupos)
    lern = lerner_ilustrativo(lujo_hhi, liv_hhi)
    liv_hhi.to_csv(RES / "peru_livianos_hhi.csv", index=False)
    lujo_hhi.to_csv(RES / "peru_lujo_hhi.csv", index=False)
    lujo_det.to_csv(RES / "peru_lujo_shares.csv", index=False)
    lern.to_csv(RES / "peru_lerner_ilustrativo.csv", index=False)
    pd.set_option("display.width", 200)
    pd.set_option("display.float_format", lambda v: f"{v:.2f}")
    print("== Livianos ==")
    print(liv_hhi.to_string(index=False))
    print("\n== Lujo ==")
    print(lujo_hhi.to_string(index=False))
    print("\n== Lerner ilustrativo L = HHI/epsilon (Cournot, semana 11) ==")
    print(lern.to_string(index=False))
    figuras(liv_hhi, lujo_hhi, lujo_det)


if __name__ == "__main__":
    main()
