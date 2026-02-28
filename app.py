import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.express as px

# --- CONFIGURACIÓN DE ALTA VISIBILIDAD ---
st.set_page_config(page_title="HSE MASTER CONTROL", layout="wide")

# --- ESTILO INDUSTRIAL CLARO (FONDO BLANCO/GRIS, TEXTO NEGRO) ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; color: #1a1a1a; }
    h1, h2, h3, p { color: #1a1a1a !important; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 10px; 
        border: 2px solid #d1d8e0; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .stMetric [data-testid="stMetricValue"] { color: #2d3436 !important; }
    .stTabs [data-baseweb="tab-list"] { background-color: #ffffff; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("🛡️ HSE MASTER CONTROL - CODELCO")
st.markdown("### **Uniting Technology | Portal de Gestión de Riesgo Real-Time**")
st.divider()

# --- MÓDULO 1: KPIs CON ALTA VISIBILIDAD ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Nodos AIDeepMiner", "70,000", "Sincronizado", delta_color="normal")
with c2:
    st.metric("Polvo Promedio (PM10)", "52 mg/m³", "-5% (Baja)", delta_color="normal")
with c3:
    st.metric("Gases (Global)", "12 ppm", "Normal")
with c4:
    st.metric("Alertas Clima", "DESPEJADO", "Chile-Bélgica")

st.markdown("---")

# --- MÓDULO 2: NAVEGACIÓN ---
t1, t2, t3 = st.tabs(["📈 Análisis de Riesgo", "🗺️ Mapa Satelital & Clima", "📄 Reportes PDF"])

with t1:
    st.subheader("Análisis de Exposición Proactiva")
    df = pd.DataFrame({'Hora': range(24), 'Riesgo %': np.random.uniform(15, 45, 24)})
    # Gráfico con colores vivos sobre fondo claro
    fig = px.area(df, x='Hora', y='Riesgo %', color_discrete_sequence=['#e67e22'])
    fig.update_layout(
        template="plotly_white", 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="black")
    )
    st.plotly_chart(fig, use_container_width=True)

with t2:
    st.subheader("Red Geográfica de Nodos (Mapa de Relieve Real)")
    # MAPA SATELITAL (OpenStreetMap con Relieve o Google-style)
    # Usamos "OpenStreetMap" que tiene colores naturales de tierra y verde
    m = folium.Map(location=[-22.3, -68.9], zoom_start=6, tiles="OpenStreetMap")
    
    # Añadimos capas de relieve
    folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', name='Topográfico', attr='Map data: &copy; OpenTopoMap').add_to(m)
    
    # Marcadores con colores Mineros
    folium.Marker([-22.3, -68.9], popup="Chuquicamata", icon=folium.Icon(color='red', icon='fire')).add_to(m)
    folium.Marker([-34.1, -70.4], popup="El Teniente", icon=folium.Icon(color='blue', icon='info-sign')).add_to(m)
    
    folium_static(m, width=1100, height=600)
    st.caption("Mapa en colores reales con topografía de la zona minera.")

with t3:
    st.subheader("Generación de Documentación Auditoría")
    st.write("Configurando generador de informes A4 con fuentes de alta lectura...")
    st.button("Descargar Reporte HSE (PDF)")

st.sidebar.markdown("## Configuración")
st.sidebar.write("**Estado Sistema:** 🟢 ONLINE")
st.sidebar.write("**Ubicación:** Antofagasta, Chile")
