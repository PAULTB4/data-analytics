import pandas as pd

from src.config.settings import (
    ANALYTICAL_DATA_FILE,
    TABLES_DIR,
)

def run():
    df = pd.read_parquet(ANALYTICAL_DATA_FILE)

    resumen = (
        df
        .groupby("estado")
        .agg(
            numero_ordenes=("numero_orden", "count"),
            monto_total=("monto", "sum"),
            monto_promedio=("monto", "mean")
        )
        .reset_index()
        .sort_values("numero_ordenes", ascending=False)
    )

    resumen.to_csv(TABLES_DIR / "estados_detallado.csv", index=False)
