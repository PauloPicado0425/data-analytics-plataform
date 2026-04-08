from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os
from datetime import datetime

def generar_pdf(data):
    filename = "reporte.pdf"
    filepath = os.path.join("app", filename)

    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # TÍTULO
    elements.append(Paragraph("<b>Reporte de Análisis de Datos</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Fecha
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    elements.append(Paragraph(f"Fecha: {fecha}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Información general
    elements.append(Paragraph("<b>Información General</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Filas: {data['filas']}", styles["Normal"]))
    elements.append(Paragraph(f"Columnas: {', '.join(data['columnas'])}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Estadísticas formateadas
    elements.append(Paragraph("<b>Estadísticas</b>", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    for col, stats in data["estadisticas"].items():
        elements.append(Paragraph(f"<b>{col.upper()}</b>", styles["Heading3"]))
        
        elements.append(Paragraph(f"Promedio: {round(stats['mean'], 2)}", styles["Normal"]))
        elements.append(Paragraph(f"Mínimo: {stats['min']}", styles["Normal"]))
        elements.append(Paragraph(f"Máximo: {stats['max']}", styles["Normal"]))
        elements.append(Paragraph(f"Desviación estándar: {round(stats['std'], 2)}", styles["Normal"]))
        
        elements.append(Spacer(1, 10))

    # Gráficas
    elements.append(Paragraph("<b>Gráficas</b>", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    for chart in data["graficas"]:
        if os.path.exists(chart):
            elements.append(Image(chart, width=400, height=300))
            elements.append(Spacer(1, 12))

    # Generar PDF
    doc.build(elements)

    return filepath