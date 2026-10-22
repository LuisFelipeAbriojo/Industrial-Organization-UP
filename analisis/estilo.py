"""Estilo común de las figuras (PNG estáticos para el informe y las slides)."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
DATA = RAIZ / "data"
FIG = RAIZ / "analisis" / "figuras"
RES = RAIZ / "analisis" / "resultados"
FIG.mkdir(parents=True, exist_ok=True)
RES.mkdir(parents=True, exist_ok=True)

# Paleta categórica validada (orden fijo; ver skill dataviz, references/palette.md)
AZUL, NARANJA, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
GRIS = "#8a8984"
TEXTO, TEXTO_2 = "#0b0b0b", "#52514e"
SUPERFICIE = "#fcfcfb"

plt.rcParams.update({
    "figure.facecolor": SUPERFICIE,
    "axes.facecolor": SUPERFICIE,
    "axes.edgecolor": "#d6d5d0",
    "axes.labelcolor": TEXTO_2,
    "axes.titlecolor": TEXTO,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.axisbelow": True,
    "grid.color": "#e8e7e2",
    "grid.linewidth": 0.8,
    "xtick.color": TEXTO_2,
    "ytick.color": TEXTO_2,
    "font.size": 10,
    "legend.frameon": False,
    "lines.linewidth": 2,
    "lines.markersize": 6,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
})


def guardar(fig, nombre):
    ruta = FIG / nombre
    fig.savefig(ruta)
    plt.close(fig)
    print(f"  figura -> {ruta.relative_to(RAIZ)}")
