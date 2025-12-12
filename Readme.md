# Análisis de Datos – Contratación Pública

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Resultados](#resultados)
- [Tecnologías](#tecnologías)
- [Autores](#autores)

## Descripción

Este proyecto implementa un **análisis descriptivo de datos de contratación pública** utilizando Python, replicando un análisis previamente desarrollado en RStudio.

El enfoque del análisis es **estrictamente descriptivo**, orientado a identificar y caracterizar patrones en los datos:

- Distribución del gasto
- Concentración por proveedor
- Estados del proceso
- Evolución temporal

**Nota:** El análisis no incluye inferencia causal ni modelos predictivos.

## Características

- **Modularidad**: Código organizado en módulos independientes y reutilizables
- **Reproducibilidad**: Pipeline completo ejecutable de inicio a fin
- **Trazabilidad**: Separación clara entre datos, lógica y presentación
- **Automatización**: Generación automática de tablas, gráficos e informes
- **Documentación**: Informes en HTML y PDF con índice navegable

## Requisitos Previos

Antes de comenzar, asegúrese de tener instalado:

- **Python 3.10 o superior**
- **Git**
- (Opcional) **VS Code** con la extensión de Python

Para verificar la versión de Python:

```bash
python --version
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd TRABAJO_FINAL
```

### 2. Crear el entorno virtual

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Importante:** Todos los comandos siguientes deben ejecutarse con el entorno activado.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Preparar los datos

Coloque el archivo de datos original en la carpeta `data/raw/`. El archivo debe:

- Provenir directamente de la fuente original
- No haber sido modificado manualmente
- Conservar su estructura original

**Nota:** Los datos en `data/raw/` nunca se modifican directamente. Esta carpeta actúa como fuente inmutable del análisis.

## Estructura del Proyecto

```
TRABAJO_FINAL/
│
├── data/
│   ├── raw/                  # Datos originales (NO modificar)
│   ├── interim/              # Datos intermedios
│   └── processed/            # Datos procesados
│
├── src/                      # Código fuente modular
│   ├── analysis/             # Scripts de análisis
│   ├── config/               # Configuraciones
│   ├── data/                 # Procesamiento de datos
│   ├── features/             # Transformaciones
│   └── visualization/        # Visualizaciones
│
├── outputs/
│   ├── figures/              # Gráficos generados (.png)
│   └── tables/               # Tablas finales (.csv)
│
├── reports/
│   ├── templates/            # Plantillas Jinja (HTML)
│   ├── build/                # Reportes compilados (HTML/PDF)
│   └── generate_report.py    # Generador de informes
│
├── notebooks/                # Exploración y validación
├── docs/                     # Documentación del proyecto
│
├── main.py                   # Punto de entrada del pipeline
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo
```

## Uso

### Ejecutar el Pipeline Completo

Desde la raíz del proyecto, ejecute:

```bash
python main.py
```

Este comando ejecuta el pipeline completo:

1. Carga de datos desde `data/raw/`
2. Limpieza y validación
3. Transformaciones necesarias
4. Análisis descriptivo
5. Generación automática de resultados

### Generar el Informe Final

**Ejecute este paso solo después de `main.py`**

```bash
python reports/generate_report.py
```

Este script:

- Lee las tablas desde `outputs/tables/`
- Carga las figuras desde `outputs/figures/`
- Renderiza el informe con Jinja + HTML
- Genera automáticamente:
  - `reports/build/informe_final.html`
  - `reports/build/informe_final.pdf`

## Resultados

Al completar el flujo completo, el proyecto genera:

- Tablas analíticas reproducibles (CSV)
- Visualizaciones descriptivas (PNG)
- Informe HTML navegable con índice interactivo
- Informe PDF listo para entrega académica

### Archivos de Salida

```
outputs/
├── figures/              # Gráficos en formato PNG
└── tables/               # Tablas en formato CSV

reports/build/
├── informe_final.html    # Informe web navegable
└── informe_final.pdf     # Informe para impresión
```

## Tecnologías

- **Python 3.10+**: Lenguaje principal
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib/Seaborn**: Visualización de datos
- **Jinja2**: Generación de reportes HTML
- **WeasyPrint**: Conversión de HTML a PDF

## Autores

- **Tarazona Benancio Paul Marco**
- **Romero Rengifo Jorge Faris**

**Trabajo Final – Analítica de Datos**  
Universidad

---

## Notas Adicionales

- El análisis es **descriptivo**, no predictivo
- No se realiza inferencia estadística ni modelos causales
- El pipeline es completamente reproducible
- Los datos originales permanecen inmutables
- El proyecto puede ejecutarse completamente desde consola

---

**Fecha:** Diciembre 2025
