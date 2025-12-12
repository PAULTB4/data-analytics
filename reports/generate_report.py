import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime
import subprocess

# =====================
# DIRECTORIOS
# =====================

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "reports" / "templates"
OUTPUT_DIR = BASE_DIR / "reports" / "build"
TABLES_DIR = BASE_DIR / "outputs" / "tables"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# =====================
# CARGA DE DATOS (TOP 10)
# =====================

concentracion = (
    pd.read_csv(TABLES_DIR / "concentracion_proveedores.csv")
      .dropna(subset=["razon_social"])
      .sort_values("participacion_pct", ascending=False)
      .head(10)
)

estados = (
    pd.read_csv(TABLES_DIR / "resumen_estado.csv")
      .dropna(subset=["estado"])
      .sort_values("numero_ordenes", ascending=False)
      .head(10)
)

ordenes_monto = (
    pd.read_csv(TABLES_DIR / "ordenes_vs_monto.csv")
      .sort_values("monto_total", ascending=False)
      .head(10)
)

temporal = (
    pd.read_csv(TABLES_DIR / "temporal_ordenes.csv")
      .sort_values("anio_mes", ascending=False)
      .head(10)
)

tipo_contratacion = (
    pd.read_csv(TABLES_DIR / "resumen_tipo_contratacion.csv")
      .dropna(subset=["tipo_contratacion"])
      .sort_values("monto_total", ascending=False)
      .head(10)
)

# =====================
# MÉTRICAS
# =====================

top_proveedor_pct = round(concentracion.iloc[0]["participacion_pct"], 2)
fecha_generacion = datetime.today().strftime("%d/%m/%Y")

# =====================
# RENDER HTML
# =====================

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
template = env.get_template("informe.html.jinja")

html = template.render(
    fecha_generacion=fecha_generacion,
    top_proveedor_pct=top_proveedor_pct,
    concentracion=concentracion.to_dict(orient="records"),
    estados=estados.to_dict(orient="records"),
    ordenes_monto=ordenes_monto.to_dict(orient="records"),
    temporal=temporal.to_dict(orient="records"),
    tipo_contratacion=tipo_contratacion.to_dict(orient="records"),
)

html_path = OUTPUT_DIR / "informe_final.html"
pdf_path = OUTPUT_DIR / "informe_final.pdf"

html_path.write_text(html, encoding="utf-8")
print(f"✔ HTML generado: {html_path}")

# =====================
# HTML → PDF (wkhtmltopdf)
# =====================

WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

subprocess.run([
    WKHTMLTOPDF_PATH,
    "--enable-local-file-access",
    str(html_path),
    str(pdf_path)
], check=True)


print(f"✔ PDF generado:  {pdf_path}")
