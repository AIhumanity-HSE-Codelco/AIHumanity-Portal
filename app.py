import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime

# --- 1. CONFIGURACIÓN DE GRADO MILITAR ---
st.set_page_config(page_title="AIH-MASTER MAXIMIZED CORE", layout="wide")

# --- 2. BASE DE DATOS MAESTRA (REGIONES, FAENAS Y GPS) ---
MINERIA_CHILE = {
    "Antofagasta": {
        "Chuquicamata (Codelco)": [-22.3, -68.9],
        "Radomiro Tomic (Codelco)": [-22.2, -68.8],
        "Escondida (BHP)": [-24.2, -69.0],
        "Gabriela Mistral (Codelco)": [-24.3, -69.1]
    },
    "O'Higgins": {
        "El Teniente (Codelco)": [-34.1, -70.4],
        "Minera Florida": [-34.0, -71.0]
    },
    "Atacama": {
        "Salvador (Codelco)": [-26.2, -69.6],
        "Caserones": [-27.3, -69.3]
    },
    "Valparaíso/RM": {
        "Andina (Codelco)": [-33.1, -70.2],
        "Los Bronces": [-33.1, -70.3]
    }
}

METAS_HSE = {"Polvo": 45, "Viento": 50, "Biometria": 95}

# --- 3. ESTILO CSS (RECUPERANDO EL CONTRASTE) ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .status-bar-container { width: 100%; background-color: #d1d8e0; border-radius: 15px; margin: 15px 0; }
    .status-bar-fill { height: 30px; border-radius: 15px; text-align: center; color: white; font-weight: bold; line-height: 30px; }
    [data-testid="stMetric"] { background-color: white; border-left: 8px solid #f39c12; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANEL LATERAL (EL MENÚ QUE VOLVIÓ) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ CONTROL MAESTRO")
    st.divider()
    region_sel = st.selectbox("📍 Región:", list(MINERIA_CHILE.keys()))
    faena_sel = st.selectbox("🏗️ Faena:", list(MINERIA_CHILE[region_sel].keys()))
    coords = MINERIA_CHILE[region_sel][faena_sel]
    
    st.divider()
    st.success(f"GPS FAENA: {coords}")
    st.info(f"Nodos AIDeepMiner: 70,000 en Red")

# --- 5. LÓGICA DE CÁLCULO DE RIESGO ---
np.random.seed(sum(map(ord, faena_sel)))
polvo_r = np.random.randint(20, 80)
viento_r = np.random.randint(10, 70)
bio_r = np.random.randint(85, 100)
riesgo_calc = int((polvo_r * 0.4) + (viento_r * 0.4) + ((100-bio_r)*2))
riesgo_calc = min(riesgo_calc, 100)

# --- 6. INTERFAZ PRINCIPAL MAXIMIZADA ---
st.title(f"PORTAL DE GOBERNANZA: {faena_sel.upper()}")
st.write(f"**Integrador Jefe:** AIH-Master | **Estatus de Red:** 🟢 Sincronizado | {datetime.now().strftime('%H:%M:%S')}")

# BARRA DE PORCENTAJE INTERACTIVA (RIESGO CERO)
color_bar = "#2ecc71" if riesgo_calc < 40 else "#f1c40f" if riesgo_calc < 75 else "#e74c3c"
st.markdown(f"""
    <div style="margin-top: 20px;"><strong>Desviación de Riesgo Cero: {riesgo_calc}%</strong></div>
    <div class="status-bar-container">
        <div class="status-bar-fill" style="width: {riesgo_calc}%; background-color: {color_bar};">
            {riesgo_calc}%
        </div>
    </div>
""", unsafe_allow_html=True)

# KPIs RECUPERADOS
c1, c2, c3, c4 = st.columns(4)
c1.metric("💨 Polvo (PM10)", f"{polvo_r} mg/m³", f"{polvo_r - METAS_HSE['Polvo']} delta", delta_color="inverse")
c2.metric("🌬️ Viento", f"{viento_r} km/h", f"{viento_r - METAS_HSE['Viento']} delta", delta_color="inverse")
c3.metric("💓 Biometría", f"{bio_r}%", f"{bio_r - METAS_HSE['Biometria']}% meta")
c4.metric("📊 Nodos GPS", "70,000", "ONLINE")

st.divider()

# DASHBOARD DE ANÁLISIS
tab_data, tab_map = st.tabs(["📊 ANÁLISIS DE RIESGO Y METAS", "🛰️ TELEDETECCIÓN GPS"])

with tab_data:
    col_rad, col_top = st.columns([1, 1])
    with col_rad:
        st.subheader("🎯 Radar de Correlación")
        
        fig_radar = go.Figure(go.Scatterpolar(
            r=[polvo_r, viento_r, bio_r, 40, riesgo_calc],
            theta=['Polvo', 'Viento', 'Biometría', 'Gases', 'Riesgo'],
            fill='toself', line_color='#e67e22'
        ))
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with col_top:
        st.subheader("🏆 Contribución al Riesgo Global")
        # Gráfico comparativo de aporte
        mineras_data = pd.DataFrame({
            'Minera': ["Chuquicamata", "El Teniente", "Escondida", "Salvador"],
            'Riesgo': [85, 42, 65, 30]
        }).sort_values('Riesgo', ascending=False)
        fig_bar = px.bar(mineras_data, x='Minera', y='Riesgo', color='Riesgo', color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig_bar, use_container_width=True)

with tab_map:
    st.subheader(f"🗺️ Despliegue de Nodos GPS en {faena_sel}")
    
    m = folium.Map(location=coords, zoom_start=14, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Satellite')
    
    # Simular puntos GPS de nodos
    for i in range(15):
        folium.CircleMarker(
            location=[coords[0] + np.random.normal(0, 0.005), coords[1] + np.random.normal(0, 0.005)],
            radius=4, color='red' if riesgo_calc > 70 else 'blue', fill=True
        ).add_to(m)
    
    folium_static(m, width=1100, height=450)

st.divider()
st.caption("AIH-MASTER CORE | Sistema de Gobernanza Blindada | Uniting Technology Belgium")
