import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime, timedelta
import pytz

# --- 1. CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH-MASTER SUPREME", layout="wide")

# --- 2. RELOJ INDUSTRIAL AGRANDADO (OPEN HSE CONTROL ROOM) ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)
st.markdown(f"""
    <div style="background: linear-gradient(90deg, #6c5ce7, #ff00ff); padding: 40px; border-radius: 25px; text-align: center; color: white; box-shadow: 0 15px 35px rgba(255,0,255,0.2);">
        <h1 style="font-size: 100px; margin: 0; letter-spacing: -5px;">{now.strftime('%H:%M:%S')}</h1>
        <p style="font-size: 24px; font-weight: 300; margin: 0; opacity: 0.9;">{now.strftime('%A, %d de %B %Y')} | MASTER CONTROL ROOM ACTIVE</p>
    </div>
""", unsafe_allow_html=True)

# --- 3. GOBERNANZA DE DATOS (70K NODOS) ---
FAENAS = {
    "CODELCO NORTE": {"Chuquicamata": [-22.3, -68.9], "RT": [-22.2, -68.8]},
    "CODELCO CENTRO": {"El Teniente": [-34.1, -70.4], "Andina": [-33.1, -70.2]},
    "ANTOFAGASTA": {"Escondida (BHP)": [-24.2, -69.0]}
}

# --- 4. CSS VIBRANTE Y AMIGABLE ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #f0f2f6; border-radius: 10px; padding: 10px 20px; font-weight: bold; color: #6c5ce7;
    }
    .stTabs [aria-selected="true"] { background-color: #ff00ff !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR: OPEN ADMIN CONFIG & EXPORTS ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=140)
    st.title("🛡️ ADMIN CONFIG")
    st.divider()
    
    op_mode = st.selectbox("ROOM MODE", ["OPEN HSE CONTROL ROOM", "ADMS TACTICAL", "WORKER SAFETY CORE"])
    region = st.selectbox("📍 Región:", list(FAENAS.keys()))
    faena_sel = st.selectbox("🏗️ Faena:", list(FAENAS[region].keys()))
    coords = FAENAS[region][faena_sel]
    
    st.divider()
    st.markdown("### 📥 EXPORT ENGINE")
    st.button("EXPORT JSON")
    st.button("EXPORT CSV")
    st.button("EXPORT LOG HSE GENERAL")
    st.divider()
    st.info("Correo Saliente: aeserviseu@gmail.com")

# --- 6. MOTOR DE ANÁLISIS DE RIESGO (DATA PASADA Y NUEVA) ---
# Simulamos data de 70,000 sensores procesando 24 horas
np.random.seed(now.minute)
time_axis = [now - timedelta(hours=i) for i in range(24)]
risk_trend = np.random.randint(20, 90, 24)
pm10_trend = np.random.normal(50, 15, 24)

curr_risk = risk_trend[0]
pm10 = int(pm10_trend[0])
pm25 = int(pm10 * 0.4)
viento = np.random.randint(10, 85)

# --- 7. PANEL CENTRAL: CODELCO OBJECTIVE ZERO ---
st.header(f"🚀 {faena_sel.upper()} | OPERATIONAL RISK CENTER")

# BARRAS DE PORCENTAJE ACTIVAS (STILO VIBRANTE)
color_p = "#ff00ff" if curr_risk > 75 else "#6c5ce7" if curr_risk > 45 else "#00cec9"
st.markdown(f"**OBJECTIVE ZERO OPERATIONAL RISK: {curr_risk}%**")
st.markdown(f"""
    <div style="width:100%; background:#f0f2f6; border-radius:20px; height:40px; border: 2px solid #eee; overflow:hidden;">
        <div style="width:{curr_risk}%; background:{color_p}; height:100%; text-align:center; color:white; font-weight:bold; line-height:40px; font-size:20px;">
            {curr_risk}% - {"CRÍTICO" if curr_risk > 75 else "CONTROLADO"}
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- 8. MÓDULOS DE SENSORES Y TÁCTICA ---
t1, t2, t3, t4 = st.tabs(["🍃 ENVIRO FUSION", "👷 WORKER SAFETY", "🎯 TOP RISK PROBABILITY", "🛰️ TACTICAL MAP"])

with t1:
    st.subheader("Environmental Fusion Core (PM10 / PM2.5 / Meteo)")
    c1, c2, c3 = st.columns(3)
    c1.metric("PM10 (Dust)", f"{pm10} µg/m³", "Dispersion Active")
    c2.metric("PM2.5 (Resp)", f"{pm25} µg/m³", "Meteo Fusion")
    c3.metric("Wind Speed", f"{viento} km/h", "NW Direction")
    
    fig_env = px.area(x=time_axis, y=pm10_trend, title="Histórico de Dispersión (24h)", color_discrete_sequence=['#ff00ff'])
    st.plotly_chart(fig_env, use_container_width=True)

with t2:
    st.subheader("Worker Safety Core: PPE & Fall Detection")
    
    s1, s2 = st.columns(2)
    s1.success("PPE Status: **WORN ON** (98% Compliance)")
    s2.warning("Fall Detection Algorithm: **ACTIVE**")
    st.info("Monitoreando 70k nodos AIDeepMiner en tiempo real.")

with t3:
    st.subheader("Top Risk Probability: Who / Where / What")
    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown("**WHERE (Zone)**")
        st.error("Sector Chancado 04")
    with r2:
        st.markdown("**WHO (Driver)**")
        st.error("Cuadrilla B - Turno 2")
    with r3:
        st.markdown("**WHAT (Event)**")
        st.error("High Wind Dispersion")

with t4:
    st.subheader("ADMS Tactical Response Map")
    m = folium.Map(location=coords, zoom_start=15, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium.Circle(coords, radius=500, color='#ff00ff', fill=True, popup="FUSION RADIUS").add_to(m)
    folium_static(m, width=1100, height=450)

# --- 9. LOG HSE GENERAL ---
st.divider()
st.subheader("📜 HSE GENERAL LOG / AUDIT TRAIL")
log_data = pd.DataFrame([{
    "Timestamp": now.strftime("%H:%M:%S"),
    "Unit": faena_sel,
    "Event": "Tactical Mitigation Fail Detection",
    "Status": "CERTIFIED",
    "Admin": "aeserviseu@gmail.com"
}])
st.table(log_data)

if st.button("📧 ENVIAR LOG A GERENCIA"):
    st.success("Reporte despachado exitosamente desde aeserviseu@gmail.com")

st.divider()
st.caption("AIH-MASTER SUPREME v13.0 | Uniting Technology Belgium | Codelco Objective Zero Operational Risk")
