import pandas as pd

from src.config.settings import (
    ANALYTICAL_DATA_FILE,
    TABLES_DIR,
)


def run():
    df = pd.read_parquet(ANALYTICAL_DATA_FILE)

    duplicados = df[df.duplicated(subset=["numero_orden"], keep=False)]

    duplicados.to_csv(TABLES_DIR / "ordenes_duplicadas.csv", index=False)
