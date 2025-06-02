import streamlit as st
import pandas as pd
import os

st.title("Dashboard Dinámico - Análisis Comercial")

# Cargar Excel desde la raíz del proyecto
def cargar_excel(nombre_archivo, hoja):
    if os.path.exists(nombre_archivo):
        return pd.read_excel(nombre_archivo, sheet_name=hoja)
    else:
        st.error(f"❌ No se encontró el archivo '{nombre_archivo}' en el mismo directorio que App.py")
        return pd.DataFrame()

# Cargar los archivos directamente
df_competencia = cargar_excel("Competencia.xlsx", "Competencia ")
df_cadenas = cargar_excel("cadenas comerciales.xlsx", "Hoja1")
df_crecimiento = cargar_excel("Crecimiento.xlsx", "Crecimiento")
df_proyecciones = cargar_excel("proyecciones.xlsx", "Hoja1")
df_participacion = cargar_excel("participación.xlsx", "participación")

# Sección 1: Competencia
if not df_competencia.empty:
    st.subheader("1. Competencia")
    columnas_relevantes = ["Empresa", "Año Fundación", "Ubicación", "Producto Principal"]
    if all(col in df_competencia.columns for col in columnas_relevantes):
        st.dataframe(df_competencia[columnas_relevantes])
    else:
        st.warning("⚠ Las columnas esperadas no están disponibles.")
        st.dataframe(df_competencia)

# Sección 2: Cadenas Comerciales
if not df_cadenas.empty:
    st.subheader("2. Cadenas Comerciales")
    if "Cadena Comercial" in df_cadenas.columns:
        st.dataframe(df_cadenas[["Cadena Comercial"]])
    else:
        st.dataframe(df_cadenas)

# Sección 3: Crecimiento
if not df_crecimiento.empty:
    st.subheader("3. Crecimiento por Periodo")
    if {"Periodo", "Tipo de Crecimiento", "Porcentaje"} <= set(df_crecimiento.columns):
        st.line_chart(df_crecimiento.set_index("Periodo")["Porcentaje"])
        st.dataframe(df_crecimiento[["Periodo", "Tipo de Crecimiento", "Porcentaje"]])
    else:
        st.dataframe(df_crecimiento)

# Sección 4: Proyecciones
if not df_proyecciones.empty:
    st.subheader("4. Proyecciones en Millones de USD")
    if {"Año", "Valor (Millones USD)", "Mercado"} <= set(df_proyecciones.columns):
        st.bar_chart(df_proyecciones.set_index("Año")["Valor (Millones USD)"])
        st.dataframe(df_proyecciones[["Año", "Valor (Millones USD)", "Mercado"]])
    else:
        st.dataframe(df_proyecciones)

# Sección 5: Participación
if not df_participacion.empty:
    st.subheader("5. Participación de Mercado")
    if {"Año", "Participación (%)", "Región"} <= set(df_participacion.columns):
        st.line_chart(df_participacion.set_index("Año")["Participación (%)"])
        st.dataframe(df_participacion[["Año", "Participación (%)", "Región"]])
    else:
        st.dataframe(df_participacion)
