import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base de datos SQL
engine = create_engine("sqlite:///data/ventas_procesadas.db")

def procesar_y_guardar_ventas():  # <--- Mira que el nombre sea igualito
    df = pd.read_csv("data/ventas.csv")
    df['total_venta'] = df['cantidad'] * df['precio_unitario']
    # Guarda en SQL
    df.to_sql("reporte_ventas", engine, if_exists="replace", index=False)
    return df.to_dict(orient="records")