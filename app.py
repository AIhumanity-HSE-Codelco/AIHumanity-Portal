import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH-GLOBAL CORE", layout="wide")

# --- CSS DE ALTA DENSIDAD ---
st.markdown("""
    <style>
    .reportview-container { background: #fdfdfd; }
    .stMetric { border: 1px solid #2d3436; background: white; padding: 10px; border-radius: 5px; }
    .sidebar .sidebar-content { background: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# --- COMANDO CENTRAL ---
st.sidebar.header("🛡️ AIH-MASTER CORE")
st.sidebar.subheader("Global Security & Defense")

menu = st.sidebar.radio("NIVELES DE ACCESO:", [
    "🛰️ Teledetección (Satelital)", 
    "🛡️ HSE Master (Minería)", 
    "🌋 Red Sismológica Nacional", 
    "⚡ Red Eléctrica & SCADA", 
    "🔬 Laboratorio IA & Biometría"
])

# --- HEADER UNIVERSAL ---
st.title(f"CENTRO DE MANDO: {menu}")
st.write(f"Sincronizando con Copernicus & USGS | **Nodos Activos:** 70,000")

# --- LÓGICA DE VISUALIZACIÓN ---

if menu == "🛰️ Teledetección (Satelital)":
    st.subheader("Análisis de Firmas Espectrales (Sentinel-2)")
    # 
    col1, col2 = st.columns([3, 1])
    with col1:
        # Mapa Satelital con Capas
        m = folium.Map(location=[-22.3, -68.9], zoom_start=12, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
        folium_static(m, width=900)
    with col2:
        st.write("**Análisis Espectral:**")
        st.info("Detectando concentraciones de Silicio y Cobre desde órbita.")
        st.progress(85)
        st.write("NDVI: 0.12 (Zona Árida)")

elif menu == "🛡️ HSE Master (Minería)":
    # 
    st.subheader("Gestión de Riesgo Proactivo (ICR)")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Polvo", "52 mg/m³", "-2%")
    k2.metric("Viento", "45 km/h", "Alerta")
    k3.metric("Nodos OK", "69,998", "2 Offline")
    k4.metric("Turno", "A", "Activo")
    
    # Gráfico de Radar de Riesgos
    categories = ['Polvo', 'Gases', 'Fatiga', 'Clima', 'Sismo']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[52, 12, 15, 45, 5], theta=categories, fill='toself', name='Riesgo Actual'))
    st.plotly_chart(fig)

elif menu == "🌋 Red Sismológica Nacional":
    # 
    st.subheader("Monitoreo Sísmico en Tiempo Real (Cinturón de Fuego)")
    data_sismo = pd.DataFrame({
        'lat': [-22.3, -33.4, -36.8],
        'lon': [-68.9, -70.6, -73.0],
        'mag': [4.2, 3.1, 5.5]
    })
    st.map(data_sismo)

elif menu == "⚡ Red Eléctrica & SCADA":
    # 
    st.subheader("Flujo Eléctrico y Control de Subestaciones")
    st.line_chart(np.random.randn(50, 3))
    st.success("Subestación El Teniente: Operando en 220kV nominales.")

st.divider()
st.caption("AIH-MASTER SYSTEM | Propiedad de Uniting Technology | Basado en Bélgica para el Mundo.")
