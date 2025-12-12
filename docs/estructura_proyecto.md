# Proyecto de Análisis de Datos – Contratación Pública

## 📁 Estructura del proyecto

data_analysis_project/
│
├── data/
│   ├── raw/                    # Datos originales (NO se modifican)
│   │   └── dataset_original.csv
│   │
│   ├── interim/                # Datos parcialmente procesados
│   │   └── dataset_limpio.parquet
│   │
│   └── processed/              # Datos listos para análisis
│       └── dataset_analitico.parquet
│
├── scripts/
│   └── debug_columns.py
├── src/
│   ├── config/
│   │   └── settings.py         # Rutas, constantes, parámetros globales
│   │
│   ├── data/
│   │   ├── load_data.py        # Carga eficiente de datos
│   │   ├── clean_data.py       # Limpieza y normalización
│   │   └── validate_data.py    # Chequeos básicos de calidad
│   │
│   ├── features/
│   │   └── transformations.py # Variables derivadas y recodificaciones
│   │
│   ├── analysis/
│   │   ├── contratos.py        # Análisis por tipo de contrato
│   │   ├── entidades.py        # Análisis por entidad
│   │   ├── proveedores.py     # Análisis por proveedor
│   │   └── estados.py          # Análisis por estado del proceso
│   │
│   ├── visualization/
│   │   ├── plots.py            # Funciones de gráficos reutilizables
│   │   └── styles.py           # Estilos visuales consistentes
│   │
│   └── utils/
│       └── helpers.py          # Funciones auxiliares comunes
│
├── notebooks/
│   ├── 01_exploracion.ipynb    # EDA inicial (ligero)
│   ├── 02_analisis.ipynb       # Ejecución del análisis modular
│   └── 03_resultados.ipynb     # Visualización y narrativa final
│
├── outputs/
│   ├── figures/               # Gráficos exportados
│   └── tables/                # Tablas finales
│
reports/
├── templates/
│   └── informe.html.jinja
├── build/
│   └── informe_final.html
└── generate_report.py
│
├── requirements.txt
├── README.md
└── main.py                     # Punto de entrada opcional
