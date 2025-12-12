from pathlib import Path

# =========================
# RUTAS BASE DEL PROYECTO
# =========================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
PROCESSED_DATA_FILE = PROCESSED_DATA_DIR / "dataset_processed.parquet"
ANALYTICAL_DATA_DIR = DATA_DIR / "processed"
ANALYTICAL_DATA_FILE = ANALYTICAL_DATA_DIR / "dataset_analytical.parquet"



# =========================
# ARCHIVOS
# =========================

RAW_DATA_FILE = RAW_DATA_DIR / "dataset_unas.xlsx"
INTERIM_DATA_FILE = INTERIM_DATA_DIR / "dataset_interim.parquet"

# =========================
# PARÁMETROS DE CARGA
# =========================

CSV_ENCODING = "latin1"
CSV_SEPARATOR = ";"

# =========================
# FORMATO DE SALIDA
# =========================

PARQUET_ENGINE = "pyarrow"
