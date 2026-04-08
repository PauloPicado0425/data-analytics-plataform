import pandas as pd
import matplotlib.pyplot as plt
import os
from app.utils.file_utils import save_file
import uuid

async def analyze_data(file):
    # Guardar archivo
    filepath = save_file(file)

    df = pd.read_csv(filepath)

    # Crear carpeta de gráficas
    os.makedirs("charts", exist_ok=True)

    charts = []

    for col in df.select_dtypes(include='number').columns:
        plt.figure()
        df[col].hist()
        plt.title(f"Distribución de {col}")

        filename = f"charts/{uuid.uuid4()}_{col}_hist.png"
        plt.savefig(filename)
        plt.close()

        charts.append(filename)

    columnas_texto = df.select_dtypes(include='object').columns
    columnas_numericas = df.select_dtypes(include='number').columns

    if len(columnas_texto) > 0 and len(columnas_numericas) > 0:
        eje_x = columnas_texto[0]  # ejemplo: nombre

        for col in columnas_numericas:
            plt.figure()
            df.plot(kind="bar", x=eje_x, y=col, legend=False)
            plt.title(f"{col} por {eje_x}")

            filename = f"charts/{uuid.uuid4()}_{col}_bar.png"
            plt.savefig(filename)
            plt.close()

            charts.append(filename)

    return {
        "archivo_guardado": filepath,
        "graficas": charts,
        "filas": len(df),
        "columnas": list(df.columns),
        "tipos": df.dtypes.astype(str).to_dict(),
        "estadisticas": df.describe().to_dict(),
        "preview": df.head(10).to_dict(orient="records")
    }