import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.express as px

# --- CONFIGURACIÓN PRO ---
st.set_page_config(page_title="HSE MASTER CONTROL", layout="wide", initial_sidebar_state="collapsed")

# --- ESTILO INDUSTRIAL ---
st.markdown("""<style>
    .stMetric { background-color: #11141b; padding: 15px; border-radius: 10px; border-left: 5px solid #f39c12; }
    </style>""", unsafe_allow_html=True)

# --- CABECERA ---
st.title("🛡️ HSE MASTER CONTROL - CODELCO")
st.subheader("Uniting Technology | Gestión de Riesgo Proactivo")
st.divider()

# --- MÓDULO 1: KPIs SOLICITADOS ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Nodos AIDeepMiner", "70,000", "ONLINE", delta_color="normal")
c2.metric("Polvo Promedio (PM10)", "52 mg/m³", "-5%", delta_color="normal")
c3.metric("Gases (CO/NO2)", "12 ppm", "Estable")
c4.metric("Alertas Activas", "0", "Seguro")

st.markdown("---")

# --- MÓDULO 2: NAVEGACIÓN ---
t1, t2, t3 = st.tabs(["📈 Tendencia Riesgo", "🗺️ Mapa Geográfico", "📑 Auditoría PDF"])

with t1:
    st.write("### Análisis de Exposición 24h")
    df = pd.DataFrame({'Hora': range(24), 'Riesgo': np.random.uniform(20, 52, 24)})
    fig = px.area(df, x='Hora', y='Riesgo', color_discrete_sequence=['#f39c12'])
    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with t2:
    st.write("### Ubicación de Faenas y Nodos")
    # Centrado en Chile Minero
    m = folium.Map(location=[-22.3, -68.9], zoom_start=6, tiles="CartoDB dark_matter")
    folium.Marker([-22.3, -68.9], popup="Chuquicamata", icon=folium.Icon(color='orange')).add_to(m)
    folium.Marker([-34.1, -70.4], popup="El Teniente", icon=folium.Icon(color='orange')).add_to(m)
    folium_static(m)

with t3:
    st.write("### Generación de Reportes HSE")
    st.info("Módulo de Auditoría listo para descarga.")
    st.button("Generar PDF para Codelco")

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=100)
st.sidebar.write("**Integrador:** AIH-Master")
st.sidebar.write("**Versión:** v2.0.4-TRL3")
