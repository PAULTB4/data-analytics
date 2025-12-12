import pandas as pd
from src.config.settings import RAW_DATA_FILE

from src.config.settings import (
    RAW_DATA_FILE,
    INTERIM_DATA_FILE,
    CSV_ENCODING,
    CSV_SEPARATOR,
    PARQUET_ENGINE,
)


def load_raw_data() -> pd.DataFrame:
    """
    Carga el dataset original desde Excel.

    """
    df = pd.read_excel(
        RAW_DATA_FILE,
        engine="openpyxl"
    )
    return df


def basic_type_casting(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica tipado básico inicial si es necesario.
    (No limpieza, solo tipos).

    Parameters
    ----------
    df : pd.DataFrame
        Dataset crudo.

    Returns
    -------
    pd.DataFrame
        Dataset con tipos ajustados.
    """
    # EJEMPLO (ajusta según tu dataset real)
    # df["monto"] = pd.to_numeric(df["monto"], errors="coerce")
    # df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    return df


def save_interim_data(df: pd.DataFrame) -> None:
    """
    Guarda el dataset en formato Parquet para uso posterior.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset a persistir.
    """
    INTERIM_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(
        INTERIM_DATA_FILE,
        engine=PARQUET_ENGINE,
        index=False
    )


def run_data_ingestion() -> None:
    """
    Ejecuta el flujo completo de ingesta de datos.
    """
    df = load_raw_data()
    df = basic_type_casting(df)
    save_interim_data(df)


if __name__ == "__main__":
    run_data_ingestion()
