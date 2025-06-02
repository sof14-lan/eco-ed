import streamlit as st
import pandas as pd
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

# --- Proyecciones de ventas ---
st.subheader("Proyecciones de Ventas")
st.line_chart(df_proyecciones.set_index(df_proyecciones.columns[0]))

# --- Participación de mercado ---
st.subheader("Participación de Mercado")
st.bar_chart(df_participacion.set_index(df_participacion.columns[0]))

# --- Crecimiento anual ---
st.subheader("Crecimiento Anual")
st.line_chart(df_crecimiento.set_index(df_crecimiento.columns[0]))

# --- Competencia ---
st.subheader("Resumen de Competencia")
st.dataframe(df_competencia)

# --- Cadenas comerciales ---
st.subheader("Información Cualitativa de Cadenas")
st.dataframe(df_cadenas.iloc[1:, [1, 2, 3]].rename(columns={
    df_cadenas.columns[1]: "Cadena Comercial",
    df_cadenas.columns[2]: "Descripción",
    df_cadenas.columns[3]: "Ventajas Clave"
}))
