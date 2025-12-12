from src.data.load_data import run_data_ingestion
from src.data.clean_data import run_data_cleaning
from src.data.validate_data import run_data_validation
from src.features.transformations import run_feature_engineering
from src.analysis.contratos import run as run_contratos
from src.analysis.estados import run as run_estados
from src.analysis.proveedores import run as run_proveedores
from src.analysis.concentracion_proveedores import run as run_concentracion
from src.analysis.ordenes_vs_monto import run as run_ordenes_monto
from src.analysis.tipo_contratacion_estado import run as run_cruce
from src.analysis.temporal import run as run_temporal
from src.analysis.estados_profundizado import run as run_estados_det
from src.analysis.duplicados import run as run_duplicados


def main() -> None:
    """
    Punto de entrada principal del proyecto.
    Orquesta el flujo completo de procesamiento de datos.
    """
    print("Iniciando FASE 1: Ingesta de datos...")
    run_data_ingestion()

    print("Iniciando FASE 2: Limpieza de datos...")
    run_data_cleaning()

    print("Iniciando FASE 2: Validación de datos...")
    run_data_validation()

    print("Iniciando FASE 3: Transformaciones analíticas...")
    run_feature_engineering()

    print("Iniciando FASE 4: Análisis descriptivo...")
    run_contratos()
    run_estados()
    run_proveedores()
    run_concentracion()
    run_ordenes_monto()
    run_cruce()
    run_temporal()
    run_estados_det()
    run_duplicados()

    print("Pipeline ejecutado correctamente.")


if __name__ == "__main__":
    main()
