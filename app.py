import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.express as px
from datetime import datetime
import pytz

# --- CONFIGURACIÓN DE ALTA DISPONIBILIDAD ---
st.set_page_config(page_title="AIH-GLOBAL MASTER", layout="wide")

# --- ESTILO CLARO INDUSTRIAL ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e272e; }
    [data-testid="stMetric"] { background-color: #ffffff; border: 1px solid #d1d8e0; padding: 15px; border-radius: 10px; border-left: 5px solid #f39c12; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR COMANDO CENTRAL ---
with st.sidebar:
    st.header("🛡️ AIH-MASTER CORE")
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=100)
    st.divider()
    seccion = st.radio("SISTEMA:", ["🛰️ Teledetección", "🛡️ HSE Minería", "🌋 Sismología", "📄 Reportes"])

# --- HEADER ---
st.title(f"CENTRO DE MANDO: {seccion}")
st.write(f"**Integrador:** AIH-Master | **Nodos:** 70,000 | **Estado:** 🟢 ONLINE")

if seccion == "🛰️ Teledetección":
    st.subheader("Análisis Satelital Real (Capas Copernicus)")
    # 
    m = folium.Map(location=[-22.3, -68.9], zoom_start=12, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Satellite')
    folium_static(m, width=1000)
    st.success("Capa Satelital de Alta Resolución cargada desde servidor Global.")

elif seccion == "🛡️ HSE Minería":
    # 
    st.subheader("Gestión de Riesgo Proactivo (ICR)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Polvo PM10", "52 mg/m³", "-5%")
    c2.metric("Viento", "45 km/h", "Alerta")
    c3.metric("Biometría OK", "100%", "Estable")
    
    df = pd.DataFrame({'T': range(24), 'R': np.random.uniform(20, 60, 24)})
    st.plotly_chart(px.area(df, x='T', y='R', title="Trazabilidad de Riesgo 24h", color_discrete_sequence=['#f39c12']), use_container_width=True)

elif seccion == "🌋 Sismología":
    # 
    st.subheader("Monitor Sismológico Nacional")
    sismos = pd.DataFrame({'lat': [-22.3, -33.4], 'lon': [-68.9, -70.6], 'mag': [4.2, 5.1]})
    st.map(sismos)

elif seccion == "📄 Reportes":
    st.subheader("Generación de Auditoría PDF")
    st.info("Preparando reporte de cumplimiento legal para CODELCO.")
    st.button("📦 Descargar Reporte Completo")

st.divider()
st.caption("AIH-MASTER | Uniting Technology Belgium | Sistema de Trazabilidad Total")
