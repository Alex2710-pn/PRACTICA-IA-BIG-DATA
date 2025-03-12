import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los logs
df = pd.read_csv("logs.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Título del dashboard
st.title("📊 Análisis de Logs de Seguridad")

# Mostrar tabla con datos
st.subheader("🔍 Datos Recientes")
st.write(df.tail(10))

# Contar eventos
st.subheader("📊 Frecuencia de Eventos")
eventos_contados = df["evento"].value_counts()

# Crear gráfico de barras
fig, ax = plt.subplots()
sns.barplot(x=eventos_contados.index, y=eventos_contados.values, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Filtrar por usuario
usuario_seleccionado = st.selectbox("Selecciona un usuario:", df["usuario"].unique())
df_filtrado = df[df["usuario"] == usuario_seleccionado]
st.write(df_filtrado)
