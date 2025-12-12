import pandas as pd
from src.config.settings import ANALYTICAL_DATA_FILE, TABLES_DIR


def run():
    df = pd.read_parquet(ANALYTICAL_DATA_FILE)

    total_monto = df["monto"].sum()

    resumen = (
        df
        .groupby(["ruc", "razon_social"])
        .agg(
            numero_ordenes=("numero_orden", "count"),
            monto_total=("monto", "sum")
        )
        .reset_index()
        .sort_values("monto_total", ascending=False)
    )

    resumen["participacion_pct"] = resumen["monto_total"] / total_monto * 100
    resumen["participacion_acum_pct"] = resumen["participacion_pct"].cumsum()

    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    resumen.to_csv(TABLES_DIR / "concentracion_proveedores.csv", index=False)
