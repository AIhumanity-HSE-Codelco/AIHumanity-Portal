import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURACIÓN ESTRUCTURAL ---
st.set_page_config(page_title="AIH-MASTER CONTROL", layout="wide", initial_sidebar_state="expanded")

# --- 2. ESTILO CSS (RECUPERANDO EL ORDEN VISUAL) ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 2px solid #d1d8e0;
        padding: 15px;
        border-radius: 12px;
        border-left: 8px solid #f39c12; /* Color Naranja Minero */
    }
    .map-container { border: 2px solid #2d3436; border-radius: 15px; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANEL LATERAL (CONTROL DE MANDO) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("AIH-MASTER CORE")
    st.divider()
    modo = st.radio("VISUALIZACIÓN:", ["📊 Dashboard de Riesgo", "🛰️ Teledetección Satelital", "🌋 Monitor Sísmico"])

# --- 4. CABECERA ---
st.title("🛡️ HSE MASTER CONTROL - INTEGRACIÓN GLOBAL")
st.write(f"**Estatus:** 🟢 ONLINE | **Nodos:** 70,000 | **Sector:** Chile-Bélgica")
st.divider()

# --- 5. LÓGICA DE PANTALLAS ---

if modo == "📊 Dashboard de Riesgo":
    # FILA 1: INDICADORES (KPIs) - Recuperamos el Polvo y Nodos
    st.subheader("⚠️ Indicadores Críticos de Seguridad")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Nodos AIDeepMiner", "70,000", "Sincro OK")
    with col2: st.metric("Polvo PM10", "52 mg/m³", "-5%", delta_color="normal")
    with col3: st.metric("Viento Real", "45 km/h", "Alerta Ráfagas")
    with col4: st.metric("Riesgo ICR", "12.4%", "Bajo Control")

    st.markdown("---")

    # FILA 2: GRÁFICOS Y ANÁLISIS
    c_left, c_right = st.columns([2, 1])
    
    with c_left:
        st.subheader("📈 Tendencia Predictiva de Riesgo")
        df = pd.DataFrame({'Hora': range(24), 'Riesgo': np.random.uniform(20, 55, 24)})
        fig = px.area(df, x='Hora', y='Riesgo', color_discrete_sequence=['#f39c12'])
        fig.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=30, b=20), height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with c_right:
        st.subheader("📋 Estado de Faenas")
        resumen = pd.DataFrame({
            'Faena': ['Chuqui', 'Teniente', 'Salvador'],
            'Estado': ['🟢', '🟢', '🟡']
        })
        st.table(resumen)

elif modo == "🛰️ Teledetección Satelital":
    st.subheader("🌍 Teledetección Copernicus (Visión Satelital)")
    # 
    # Mapa con tamaño controlado
    m = folium.Map(location=[-22.3, -68.9], zoom_start=12, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Satellite')
    folium_static(m, width=1100, height=500)
    st.info("Capa Activa: Relieve Satelital de Alta Resolución.")

elif modo == "🌋 Monitor Sísmico":
    st.subheader("🌋 Trazabilidad Sismológica (Alertas Tempranas)")
    # 
    sismos = pd.DataFrame({'lat': [-22.31, -34.08], 'lon': [-68.91, -70.45], 'mag': [4.5, 3.2]})
    st.map(sismos)

# --- 6. PIE DE PÁGINA ---
st.divider()
st.caption("AIHumanity Core v3.0 | Uniting Technology Belgium | Sistema de Auditoría Legal")
