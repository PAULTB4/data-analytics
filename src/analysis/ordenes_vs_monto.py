import pandas as pd

from src.config.settings import (
    ANALYTICAL_DATA_FILE,
    TABLES_DIR,
)

def run():
    df = pd.read_parquet(ANALYTICAL_DATA_FILE)

    resumen = (
        df
        .groupby(["ruc", "razon_social"])
        .agg(
            numero_ordenes=("numero_orden", "count"),
            monto_promedio=("monto", "mean"),
            monto_total=("monto", "sum")
        )
        .reset_index()
        .sort_values("monto_promedio", ascending=False)
    )

    resumen.to_csv(TABLES_DIR / "ordenes_vs_monto.csv", index=False)
