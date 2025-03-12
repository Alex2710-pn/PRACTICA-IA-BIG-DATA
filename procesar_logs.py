import pandas as pd

# Cargar los logs desde el CSV
df = pd.read_csv("logs.csv")

# Convertir la columna de tiempo a formato datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Mostrar los primeros registros
print(df.head())
