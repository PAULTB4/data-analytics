import pandas as pd

df = pd.read_parquet("data/processed/dataset_processed.parquet")

print("Columnas del dataset PROCESSED:")
for col in df.columns:
    print(repr(col))
