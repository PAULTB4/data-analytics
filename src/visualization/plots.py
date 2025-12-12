import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FuncFormatter


from src.visualization.styles import format_millions, set_style

FIGURES_DIR = Path("outputs/figures")


def plot_tipo_contratacion():
    set_style()
    df = pd.read_csv("outputs/tables/resumen_tipo_contratacion.csv")

    df = (
        df.dropna(subset=["tipo_contratacion"])
          .sort_values("monto_total")
    )

    plt.barh(df["tipo_contratacion"], df["monto_total"])
    plt.xlabel("Monto total")
    plt.title("Monto total según tipo de contratación")

    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_millions))

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "tipo_contratacion.png")
    plt.close()




def plot_estados():
    set_style()
    df = pd.read_csv("outputs/tables/estados_detallado.csv")

    df = (
        df.dropna(subset=["estado"])
          .sort_values("numero_ordenes")
    )

    plt.barh(df["estado"], df["numero_ordenes"])
    plt.xlabel("Número de órdenes")
    plt.title("Distribución de órdenes según estado del proceso")

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "estados.png")
    plt.close()



def plot_concentracion_proveedores():
    set_style()
    df = pd.read_csv("outputs/tables/concentracion_proveedores.csv")

    df = (
        df.dropna(subset=["razon_social"])
          .head(10)
          .sort_values("participacion_pct")
    )

    plt.barh(df["razon_social"], df["participacion_pct"])
    plt.xlabel("Participación (%)")
    plt.title("Concentración del gasto en los principales proveedores")

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "concentracion_proveedores.png")
    plt.close()



def plot_ordenes_vs_monto():
    set_style()
    df = pd.read_csv("outputs/tables/ordenes_vs_monto.csv")

    plt.scatter(
        df["numero_ordenes"],
        df["monto_total"],
        alpha=0.7
    )

    plt.xlabel("Número de órdenes")
    plt.ylabel("Monto total")
    plt.title("Relación entre volumen de órdenes y monto total")

    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "ordenes_vs_monto.png")
    plt.close()



def plot_temporal():
    set_style()
    df = pd.read_csv("outputs/tables/temporal_ordenes.csv")

    plt.plot(df["anio_mes"], df["monto_total"], marker="o")

    # 🔧 Mostrar solo algunos ticks (cada 3 meses)
    step = max(1, len(df) // 10)
    plt.xticks(
        ticks=range(0, len(df), step),
        labels=df["anio_mes"].iloc[::step],
        rotation=45
    )

    plt.xlabel("Periodo")
    plt.ylabel("Monto total")
    plt.title("Evolución temporal del monto total comprometido")

    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "temporal.png")
    plt.close()


