
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Título
st.title("Dashboard de Cadenas Comerciales")

# Ruta de los datos
DATA_DIR = "data"

# Cargar archivos
df_cadenas = pd.read_excel(os.path.join(DATA_DIR, "cadenas comerciales.xlsx"), sheet_name="Hoja1")
df_competencia = pd.read_excel(os.path.join(DATA_DIR, "Competencia.xlsx"), sheet_name="Competencia ")
df_crecimiento = pd.read_excel(os.path.join(DATA_DIR, "Crecimiento.xlsx"), sheet_name="Crecimiento")
df_participacion = pd.read_excel(os.path.join(DATA_DIR, "participación.xlsx"), sheet_name="participación")
df_proyecciones = pd.read_excel(os.path.join(DATA_DIR, "proyecciones.xlsx"), sheet_name="Hoja1")

# --- Visualización de Proyecciones ---
st.subheader("Proyecciones de Ventas")
fig_proy = px.line(df_proyecciones, x=df_proyecciones.columns[0], y=df_proyecciones.columns[1:], markers=True)
st.plotly_chart(fig_proy)

# --- Visualización de Participación ---
st.subheader("Participación de Mercado")
fig_part = px.bar(df_participacion, x=df_participacion.columns[0], y=df_participacion.columns[1:], barmode="group")
st.plotly_chart(fig_part)

# --- Visualización de Crecimiento ---
st.subheader("Crecimiento Anual")
fig_crec = px.line(df_crecimiento, x=df_crecimiento.columns[0], y=df_crecimiento.columns[1:], markers=True)
st.plotly_chart(fig_crec)

# --- Visualización de Competencia ---
st.subheader("Resumen de Competencia")
st.dataframe(df_competencia)

# --- Información cualitativa de cadenas ---
st.subheader("Información Cualitativa de Cadenas")
st.dataframe(df_cadenas.iloc[1:, [1, 2, 3]].rename(columns={
    df_cadenas.columns[1]: "Cadena Comercial",
    df_cadenas.columns[2]: "Descripción",
    df_cadenas.columns[3]: "Ventajas Clave"
}))
