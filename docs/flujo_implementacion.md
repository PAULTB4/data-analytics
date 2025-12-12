# Flujo de Implementación del Análisis de Datos en Python

Este documento describe el flujo de trabajo completo para implementar un análisis de datos
descriptivo en Python, replicando el enfoque desarrollado previamente en RStudio, y aplicando
principios de arquitectura y diseño de software para asegurar modularidad, eficiencia y
reproducibilidad.

---

## FASE 0 — Preparación del proyecto

**Objetivo:** establecer una base sólida antes de manipular datos.

- Crear la estructura de carpetas y archivos del proyecto.
- Inicializar un entorno virtual de Python.
- Definir las dependencias mínimas del proyecto.
- Centralizar rutas, constantes y parámetros globales en `config/settings.py`.

**Resultado esperado:**  
Proyecto inicializado, reproducible y listo para desarrollo.

---

## FASE 1 — Ingesta de datos

**Objetivo:** cargar el dataset original de forma eficiente y controlada.

- Implementar el módulo `src/data/load_data.py`.
- Leer el archivo original desde `data/raw/`.
- Realizar tipado inicial de columnas si es necesario.
- Persistir el dataset en un formato eficiente (`parquet` o `feather`) en `data/interim/`.

**Buenas prácticas:**
- El dataset original no debe modificarse.
- La carga del archivo original debe realizarse una sola vez.

**Resultado esperado:**  
Dataset disponible en formato optimizado para procesamiento posterior.

---

## FASE 2 — Limpieza y validación de datos

**Objetivo:** asegurar la calidad y consistencia del dataset.

- Implementar `src/data/clean_data.py`:
  - Normalización de strings.
  - Manejo explícito de valores nulos.
  - Homogeneización de categorías.
- Implementar `src/data/validate_data.py`:
  - Chequeos básicos de integridad (nulos, duplicados, rangos).
- Guardar el dataset limpio en `data/processed/`.

**Buenas prácticas:**
- Toda transformación debe ser explícita y reproducible.
- Evitar supuestos implícitos sobre la calidad del dato.

**Resultado esperado:**  
Dataset limpio, validado y confiable para análisis.

---

## FASE 3 — Transformaciones analíticas

**Objetivo:** preparar el dataset para responder preguntas analíticas.

- Implementar `src/features/transformations.py`.
- Crear variables derivadas necesarias para el análisis descriptivo.
- Definir recodificaciones o clasificaciones analíticas.
- Generar un dataset analítico final.

**Buenas prácticas:**
- Separar limpieza de transformación analítica.
- Mantener funciones puras y reutilizables.

**Resultado esperado:**  
Dataset analítico listo para agregaciones y comparaciones.

---

## FASE 4 — Análisis descriptivo modular

**Objetivo:** responder cada pregunta analítica de forma independiente.

- Implementar módulos en `src/analysis/`, por ejemplo:
  - `contratos.py`
  - `entidades.py`
  - `proveedores.py`
  - `estados.py`
- Cada módulo debe:
  - recibir el dataset analítico,
  - realizar agregaciones específicas,
  - retornar tablas o estructuras de resultados.

**Buenas prácticas:**
- No incluir visualización en esta fase.
- No modificar el dataset original.

**Resultado esperado:**  
Resultados analíticos claros, reutilizables y consistentes.

---

## FASE 5 — Visualización de resultados

**Objetivo:** representar los resultados de manera clara y consistente.

- Implementar `src/visualization/plots.py` con funciones reutilizables.
- Definir estilos comunes en `src/visualization/styles.py`.
- Exportar gráficos a `outputs/figures/`.

**Buenas prácticas:**
- Cada gráfico debe responder a una pregunta analítica concreta.
- Mantener coherencia visual entre gráficos.

**Resultado esperado:**  
Visualizaciones limpias y alineadas con el análisis descriptivo.

---

## FASE 6 — Orquestación del flujo

**Objetivo:** controlar la ejecución completa del análisis.

- Implementar `main.py` como punto de entrada del proyecto.
- Orquestar las fases:
  - carga,
  - limpieza,
  - transformación,
  - análisis,
  - visualización.
- Evitar duplicación de lógica entre scripts y notebooks.

**Resultado esperado:**  
Análisis ejecutable de principio a fin con un único flujo controlado.

---

## FASE 7 — Exploración y narrativa

**Objetivo:** comunicar los resultados del análisis.

- Utilizar notebooks exclusivamente para:
  - exploración inicial ligera,
  - interpretación de resultados,
  - redacción de conclusiones.
- Importar funciones desde `src/`, sin lógica pesada en notebooks.

**Buenas prácticas:**
- Priorizar claridad sobre complejidad técnica.
- Evitar recomputar resultados ya procesados.

**Resultado esperado:**  
Narrativa analítica clara y alineada con el enfoque del curso.

---

## FASE 8 — Revisión y optimización

**Objetivo:** mejorar eficiencia y calidad del proyecto.

- Verificar tiempos de carga y procesamiento.
- Identificar y eliminar cálculos redundantes.
- Validar consistencia de resultados con el análisis en R.
- Documentar decisiones técnicas relevantes.

**Resultado esperado:**  
Proyecto optimizado, mantenible y académicamente sólido.

---

## Principio rector del flujo

> La lógica del análisis reside en los módulos del proyecto (`src/`).
>  
> Los notebooks y documentos finales únicamente consumen y comunican resultados.
