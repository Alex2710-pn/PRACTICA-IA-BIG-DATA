import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los logs
df = pd.read_csv("logs.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Contar eventos
eventos_contados = df["evento"].value_counts()

# Crear gráfico de barras
plt.figure(figsize=(8,5))
sns.barplot(x=eventos_contados.index, y=eventos_contados.values)
plt.xticks(rotation=45)
plt.title("Frecuencia de Eventos en Logs")
plt.ylabel("Cantidad")
plt.xlabel("Evento")
plt.show()
