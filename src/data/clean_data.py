import pandas as pd
from src.config.settings import INTERIM_DATA_FILE, PROCESSED_DATA_FILE


def load_interim_data() -> pd.DataFrame:
    """
    Carga el dataset intermedio desde data/interim.
    """
    return pd.read_parquet(INTERIM_DATA_FILE)


def normalize_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza columnas tipo string:
    - strip
    - lower
    - reemplazo de valores vacíos por NaN
    """
    string_cols = df.select_dtypes(include="object").columns

    for col in string_cols:
        df[col] = (
            df[col]
            .str.strip()
            .str.lower()
            .replace("", pd.NA)
        )

    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Manejo explícito de valores nulos.
    Ajustar reglas según el dataset.
    """
    # EJEMPLOS (personalizar según tu análisis en R)
    # df = df.dropna(subset=["monto"])
    # df["estado"] = df["estado"].fillna("no especificado")

    return df


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Orquesta la limpieza completa del dataset.
    """
    df = normalize_strings(df)
    df = handle_missing_values(df)
    return df


def save_processed_data(df: pd.DataFrame) -> None:
    """
    Guarda el dataset limpio en data/processed.
    """
    PROCESSED_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(PROCESSED_DATA_FILE, index=False)


def run_data_cleaning() -> None:
    """
    Ejecuta el flujo completo de limpieza.
    """
    df = load_interim_data()
    df = clean_dataset(df)
    save_processed_data(df)


if __name__ == "__main__":
    run_data_cleaning()
