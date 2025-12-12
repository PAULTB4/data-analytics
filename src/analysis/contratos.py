import pandas as pd
from src.config.settings import ANALYTICAL_DATA_FILE, TABLES_DIR


def load_data() -> pd.DataFrame:
    return pd.read_parquet(ANALYTICAL_DATA_FILE)


def analyze_tipo_contratacion(df: pd.DataFrame) -> pd.DataFrame:
    """
    Distribución de órdenes y montos por tipo de contratación.
    """
    summary = (
        df
        .groupby("tipo_contratacion", dropna=False)
        .agg(
            numero_ordenes=("numero_orden", "count"),
            monto_total=("monto", "sum")
        )
        .reset_index()
        .sort_values("monto_total", ascending=False)
    )
    return summary


def run() -> None:
    df = load_data()
    result = analyze_tipo_contratacion(df)

    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    result.to_csv(TABLES_DIR / "resumen_tipo_contratacion.csv", index=False)


if __name__ == "__main__":
    run()
