import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium

# --- 1. CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="AIH-MASTER CONTROL GLOBAL", layout="wide")

# --- 2. BASE DE DATOS MAESTRA DE MINERÍA CHILE ---
MINERIA_CHILE = {
    "Antofagasta": ["Chuquicamata (Codelco)", "Radomiro Tomic (Codelco)", "Escondida (BHP)", "Spence (BHP)", "Sierra Gorda", "Centinela", "Gabriela Mistral (Codelco)"],
    "O'Higgins": ["El Teniente (Codelco)", "Minera Florida"],
    "Atacama": ["Salvador (Codelco)", "Caserones", "Candelaria", "La Coipa"],
    "Coquimbo": ["Los Pelambres", "Carmen de Andacollo"],
    "Tarapacá": ["Cerro Colorado (BHP)", "Quebrada Blanca (Teck)", "Collahuasi"],
    "Valparaíso/RM": ["Andina (Codelco)", "Los Bronces", "El Soldado"],
    "No Metálica/Litio": ["SQM Salar de Atacama", "Nueva Victoria", "Surire (Quiborax)"]
}

# --- 3. ESTILO CSS INDUSTRIAL (ALTA VISIBILIDAD) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e272e; }
    [data-testid="stMetric"] { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 8px solid #f39c12; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #ffffff; border-radius: 10px; padding: 5px; }
    h1, h2, h3 { color: #2c3e50 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANEL LATERAL (CONTROL DE MANDO) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ CONTROL MAESTRO")
    region = st.selectbox("📍 Seleccione Región:", list(MINERIA_CHILE.keys()))
    faena = st.selectbox("🏗️ Seleccione Faena:", MINERIA_CHILE[region])
    st.divider()
    st.success(f"Nodo Activo: {faena}")
    st.info("AIH-Master Core v3.0\nTRL3 Operational")

# --- 5. LÓGICA DE DATOS POR FAENA ---
np.random.seed(sum(map(ord, faena)))
riesgo_val = np.random.randint(15, 90)
polvo = np.random.randint(30, 70)
viento = np.random.randint(10, 65)

# --- 6. INTERFAZ PRINCIPAL ---
st.title(f"HSE MASTER CONTROL: {faena.upper()}")
st.markdown(f"**Gobernanza de 70,000 Nodos AIDeepMiner** | Sector: {region} | 🟢 Sincronizado")
st.divider()

# KPIs CON ICONOS
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("💨 Polvo PM10", f"{polvo} mg/m³", "AIDeepMiner")
with c2: st.metric("🌬️ Viento Real", f"{viento} km/h", "Sismología")
with c3: st.metric("💓 Biometría", "98.5% OK", "IA Humana")
with c4: st.metric("📉 Índice Riesgo", f"{riesgo_val}%", delta_color="inverse")

st.divider()

# PESTAÑAS DE ANÁLISIS
tab_risk, tab_map, tab_docs = st.tabs(["📊 DASHBOARD DE RIESGOS", "🛰️ TELEDETECCIÓN", "📂 GESTIÓN Y REPORTES"])

with tab_risk:
    col_a, col_b = st.columns([1, 2])
    
    with col_a:
        st.subheader("🎯 Factores Críticos")
        # Gráfico de Radar profesional
        fig_radar = go.Figure(go.Scatterpolar(
            r=[polvo, viento, 95, riesgo_val, 20],
            theta=['Polvo', 'Viento', 'Biometría', 'Riesgo', 'Gases'],
            fill='toself', line_color='#e67e22'
        ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=400)
        st.plotly_chart(fig_radar, use_container_width=True)
        
        if riesgo_val > 75:
            st.error("🛑 ALERTA: STOP WORK AUTHORITY RECOMENDADO")

    with col_b:
        st.subheader("📈 Trazabilidad Predictiva (24h)")
        df_tendencia = pd.DataFrame({'Hora': range(24), 'Riesgo': np.random.uniform(20, riesgo_val+5, 24)})
        fig_line = px.area(df_tendencia, x='Hora', y='Riesgo', color_discrete_sequence=['#f39c12'])
        fig_line.update_layout(template="plotly_white", height=400)
        st.plotly_chart(fig_line, use_container_width=True)

with tab_map:
    st.subheader(f"🌍 Vista Satelital: {faena}")
    # Mapa centrado (Chuqui por defecto si no hay coordenadas exactas)
    m = folium.Map(location=[-22.3, -68.9], zoom_start=13, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Satellite')
    folium.Marker([-22.3, -68.9], popup=faena, icon=folium.Icon(color='red', icon='warning')).add_to(m)
    folium_static(m, width=1100, height=500)

with tab_docs:
    st.subheader("📄 Centro de Documentación HSE")
    st.write(f"Gestión de auditoría legal para la unidad: **{faena}**")
    c_rep1, c_rep2 = st.columns(2)
    c_rep1.button(f"📥 Exportar Reporte Diario (PDF)")
    c_rep2.button(f"📊 Descargar Datos AIDeepMiner (CSV)")
    st.table(pd.DataFrame({
        "Modulo": ["Sensorica", "Clima", "Biometría"],
        "Estado": ["Conectado", "Conectado", "Sincronizado"],
        "Nodos": ["23,000", "12,000", "35,000"]
    }))

st.divider()
st.caption("AIH-MASTER CONTROL | Uniting Technology Belgium | Sistema de Auditoría y Proactividad")
