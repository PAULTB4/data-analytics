import pandas as pd

df = pd.read_parquet("data/processed/dataset_analytical.parquet")

print("Columnas del dataset analítico:")
for col in df.columns:
    print(repr(col))
