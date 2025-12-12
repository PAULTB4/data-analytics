import pandas as pd

from src.config.settings import (
    ANALYTICAL_DATA_FILE,
    TABLES_DIR,
)

def run():
    df = pd.read_parquet(ANALYTICAL_DATA_FILE)

    df["anio_mes"] = df["fecha_emision"].dt.to_period("M").astype(str)

    resumen = (
        df
        .groupby("anio_mes")
        .agg(
            numero_ordenes=("numero_orden", "count"),
            monto_total=("monto", "sum")
        )
        .reset_index()
        .sort_values("anio_mes")
    )

    resumen.to_csv(TABLES_DIR / "temporal_ordenes.csv", index=False)
