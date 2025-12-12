import pandas as pd
from src.config.settings import ANALYTICAL_DATA_FILE, TABLES_DIR


def load_data() -> pd.DataFrame:
    return pd.read_parquet(ANALYTICAL_DATA_FILE)


def analyze_estado(df: pd.DataFrame) -> pd.DataFrame:
    """
    Distribución de órdenes según su estado.
    """
    summary = (
        df
        .groupby("estado", dropna=False)
        .agg(
            numero_ordenes=("numero_orden", "count"),
            monto_total=("monto", "sum")
        )
        .reset_index()
        .sort_values("numero_ordenes", ascending=False)
    )
    return summary


def run() -> None:
    df = load_data()
    result = analyze_estado(df)

    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    result.to_csv(TABLES_DIR / "resumen_estado.csv", index=False)


if __name__ == "__main__":
    run()
