import pandas as pd
from src.config.settings import PROCESSED_DATA_FILE


def load_processed_data() -> pd.DataFrame:
    """
    Carga el dataset limpio para validación.
    """
    return pd.read_parquet(PROCESSED_DATA_FILE)


def check_missing_values(df: pd.DataFrame) -> None:
    """
    Reporta columnas con valores nulos.
    """
    missing = df.isna().sum()
    missing = missing[missing > 0]

    if not missing.empty:
        print("Columnas con valores nulos:")
        print(missing)
    else:
        print("No se detectaron valores nulos.")


def check_duplicates(df: pd.DataFrame) -> None:
    """
    Reporta filas duplicadas.
    """
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        print(f"Filas duplicadas detectadas: {duplicates}")
    else:
        print("No se detectaron filas duplicadas.")


def run_data_validation() -> None:
    """
    Ejecuta validaciones básicas de calidad.
    """
    df = load_processed_data()
    check_missing_values(df)
    check_duplicates(df)


if __name__ == "__main__":
    run_data_validation()
