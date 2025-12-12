import pandas as pd
from src.config.settings import (
    PROCESSED_DATA_FILE,
    ANALYTICAL_DATA_FILE,
)


def load_processed_data() -> pd.DataFrame:
    """
    Carga el dataset limpio desde data/processed.
    """
    return pd.read_parquet(PROCESSED_DATA_FILE)


def create_monetary_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea variables relacionadas a montos.
    Ajustar nombres según el dataset real.
    """
    # EJEMPLO
    # df["monto_total"] = df["monto"].fillna(0)
    return df


def recode_contract_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recodifica tipos de contrato si aplica.
    """
    # EJEMPLO
    # mapping = {
    #     "licitacion publica": "licitación",
    #     "contratacion directa": "directa",
    # }
    # df["tipo_contrato"] = df["tipo_contrato"].replace(mapping)
    return df


def create_auxiliary_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Variables auxiliares para análisis descriptivo.
    """
    # EJEMPLO
    # df["n_contratos"] = 1
    return df

def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza nombres de columnas para análisis.
    """
    df = df.rename(columns={
        "N°": "id",
        "Tipo de Orden": "tipo_orden",
        "Número de orden": "numero_orden",
        "Tipo de Contratación": "tipo_contratacion",
        "Descripción y Finalidad de la contratación": "descripcion",
        "Nro. Exp. SIAF": "exp_siaf",
        "Fecha de Emisión": "fecha_emision",
        "Fecha de Compromiso": "fecha_compromiso",
        "Estado": "estado",
        "Monto": "monto",
        "RUC": "ruc",
        "Denominación o razón Social": "razon_social",
    })
    return df



def transform_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Orquesta todas las transformaciones analíticas.
    """
    df = create_monetary_features(df)
    df = recode_contract_types(df)
    df = create_auxiliary_features(df)
    df = normalize_column_names(df)
    return df


def save_analytical_data(df: pd.DataFrame) -> None:
    """
    Guarda el dataset analítico.
    """
    ANALYTICAL_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(ANALYTICAL_DATA_FILE, index=False)


def run_feature_engineering() -> None:
    """
    Ejecuta el flujo completo de transformaciones analíticas.
    """
    df = load_processed_data()
    df = transform_dataset(df)
    save_analytical_data(df)


if __name__ == "__main__":
    run_feature_engineering()
