import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE NÚCLEO (OPTIMIZADO PARA MÓVIL) ---
st.set_page_config(page_title="AIH-MASTER GOLD", layout="wide")

# --- 2. BASE DE DATOS MAESTRA (FAENAS & GPS) ---
MINERIA_CHILE = {
    "Antofagasta": {
        "Chuquicamata (Codelco)": [-22.3, -68.9],
        "Radomiro Tomic (Codelco)": [-22.2, -68.8],
        "Escondida (BHP)": [-24.2, -69.0]
    },
    "O'Higgins": {
        "El Teniente (Codelco)": [-34.1, -70.4]
    },
    "Atacama": {
        "Salvador (Codelco)": [-26.2, -69.6]
    }
}

# --- 3. ESTILO CSS INDUSTRIAL (RESPONSIVO Y BLINDADO) ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    /* Estilo de Tarjetas KPI */
    .metric-card { background: white; padding: 15px; border-radius: 10px; border-left: 6px solid #f39c12; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    /* Barra de Riesgo */
    .risk-container { width: 100%; background: #dfe6e9; border-radius: 20px; height: 30px; margin: 10px 0; }
    .risk-fill { height: 100%; border-radius: 20px; text-align: center; color: white; font-weight: bold; line-height: 30px; transition: 1s; }
    /* Estética de Enlaces */
    .report-link { color: #2980b9; text-decoration: none; font-weight: bold; }
    .report-link:hover { color: #e67e22; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANEL LATERAL (INTERACTIVO) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=100)
    st.title("🛡️ AIH-MASTER")
    
    # Módulo de Fecha y Hora en tiempo real (Chile)
    tz = pytz.timezone('America/Santiago')
    now = datetime.now(tz)
    st.write(f"🕒 **Fecha:** {now.strftime('%d/%m/%Y')}")
    st.write(f"⏱️ **Hora:** {now.strftime('%H:%M:%S')}")
    
    st.divider()
    region_sel = st.selectbox("📍 Sector:", list(MINERIA_CHILE.keys()))
    faena_sel = st.selectbox("🏗️ Faena:", list(MINERIA_CHILE[region_sel].keys()))
    coords = MINERIA_CHILE[region_sel][faena_sel]
    
    st.divider()
    st.info("📱 Interfaz Optimizada para Tablets y Smartphones")

# --- 5. LÓGICA DE GOBERNANZA ---
np.random.seed(sum(map(ord, faena_sel)))
polvo = np.random.randint(30, 80)
viento = np.random.randint(10, 60)
riesgo = int((polvo * 0.5) + (viento * 0.5))

# --- 6. PANTALLA PRINCIPAL ---
st.title(f"PORTAL HSE: {faena_sel.upper()}")

# BARRA DE RIESGO CERO INTERACTIVA
color_risk = "#27ae60" if riesgo < 40 else "#f1c40f" if riesgo < 70 else "#c0392b"
st.markdown(f"""
    <div style="margin-bottom:5px;"><strong>Desviación Meta Riesgo Cero:</strong></div>
    <div class="risk-container">
        <div class="risk-fill" style="width: {riesgo}%; background-color: {color_risk};">{riesgo}%</div>
    </div>
""", unsafe_allow_html=True)

# KPIs (ADAPTABLES A MÓVIL)
k1, k2, k3, k4 = st.columns([1,1,1,1])
with k1: st.metric("💨 Polvo", f"{polvo} mg/m³")
with k2: st.metric("🌬️ Viento", f"{viento} km/h")
with k3: st.metric("💓 Biometría", "98%")
with k4: st.metric("📍 Nodos", "70,000")

st.divider()

# PESTAÑAS MAXIMIZADAS
t1, t2, t3 = st.tabs(["📊 DASHBOARD", "🛰️ MAPA GPS", "📄 REPORTES & PKIS"])

with t1:
    c_rad, c_line = st.columns([1, 1])
    with c_rad:
        st.subheader("🎯 Radar de Riesgo")
        fig_rad = go.Figure(go.Scatterpolar(r=[polvo, viento, 95, 30, riesgo], theta=['Polvo', 'Viento', 'Biometría', 'Gases', 'Riesgo'], fill='toself'))
        st.plotly_chart(fig_rad, use_container_width=True)
    with c_line:
        st.subheader("📈 Tendencia 24h")
        df_hist = pd.DataFrame({'T': range(10), 'R': np.random.randint(20, 90, 10)})
        st.plotly_chart(px.line(df_hist, x='T', y='R'), use_container_width=True)

with t2:
    st.subheader(f"🗺️ Coordenadas Nodos: {coords}")
    m = folium.Map(location=coords, zoom_start=14, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Satellite')
    folium.Marker(coords, popup=faena_sel).add_to(m)
    folium_static(m, width=700, height=400) # Tamaño optimizado para pantalla móvil

with t3:
    st.subheader("📂 Centro de Gestión Documental (HSE)")
    
    # Hipervínculos a Reportes (Simulados como Módulos Interactivos)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 🔗 Accesos Directos")
        st.markdown("- [📁 Histórico de Incidentes - Chuqui](https://streamlit.io/gallery)")
        st.markdown("- [📁 PKIs de Seguridad Trimestral](https://streamlit.io/gallery)")
        st.markdown("- [📁 Manual de Riesgo Cero v2026](https://streamlit.io/gallery)")
        
    with col_b:
        st.markdown("### ⚙️ Acciones")
        email_to = st.text_input("Enviar reporte a:", "gerencia@codelco.cl")
        if st.button("📧 Enviar Reporte por Correo"):
            st.success(f"Reporte enviado exitosamente a {email_to}")
            
    st.divider()
    st.subheader("📦 Descargas Disponibles")
    d1, d2, d3 = st.columns(3)
    d1.download_button("PDF: Reporte HSE Diario", data="Datos de ejemplo", file_name="reporte_diario.pdf")
    d2.download_button("CSV: Datos Nodos GPS", data="Datos de ejemplo", file_name="nodos.csv")
    d3.download_button("PDF: Auditoría PKIs", data="Datos de ejemplo", file_name="auditoria.pdf")

st.divider()
st.caption("AIH-MASTER GOLD | Uniting Technology Belgium | Sistema de Trazabilidad Total")
