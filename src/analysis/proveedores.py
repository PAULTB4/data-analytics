import pandas as pd
from src.config.settings import ANALYTICAL_DATA_FILE, TABLES_DIR


def load_data() -> pd.DataFrame:
    return pd.read_parquet(ANALYTICAL_DATA_FILE)


def analyze_proveedores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Concentración de montos por proveedor.
    """
    summary = (
        df
        .groupby(["ruc", "razon_social"], dropna=False)
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
    result = analyze_proveedores(df)

    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    result.to_csv(TABLES_DIR / "resumen_proveedores.csv", index=False)


if __name__ == "__main__":
    run()
