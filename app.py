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
st.set_page_config(page_title="AIH-MASTER INTEGRATED", layout="wide")

# --- 2. RELOJ INDUSTRIAL SUPREMO (RECUPERADO Y AGRANDADO) ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)
st.markdown(f"""
    <div style="background: linear-gradient(90deg, #6c5ce7, #ff00ff); padding: 30px; border-radius: 20px; text-align: center; color: white; box-shadow: 0 10px 30px rgba(108, 92, 231, 0.3);">
        <h1 style="font-size: 85px; margin: 0; letter-spacing: -3px; font-weight: 800;">{now.strftime('%H:%M:%S')}</h1>
        <p style="font-size: 22px; margin: 0; opacity: 0.9; font-weight: 400;">{now.strftime('%A, %d de %B %Y')} | CENTRAL CONTROL ROOM</p>
    </div>
""", unsafe_allow_html=True)

# --- 3. GOBERNANZA DE DATOS (70,000 NODOS) ---
FAENAS = {
    "CODELCO NORTE": {"Chuquicamata": [-22.3, -68.9], "RT": [-22.2, -68.8]},
    "CODELCO CENTRO": {"El Teniente": [-34.1, -70.4], "Andina": [-33.1, -70.2]},
    "ANTOFAGASTA": {"Escondida (BHP)": [-24.2, -69.0], "Salvador": [-26.2, -69.6]}
}

# --- 4. CSS VIBRANTE (BLANCO, FUCSIA, MORADO, AMARILLO) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stMetric { background: #f8f9fa; border-left: 8px solid #ff00ff; border-radius: 15px; padding: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .risk-bar-bg { width: 100%; background: #eee; border-radius: 15px; height: 35px; border: 1px solid #ddd; overflow: hidden; margin: 10px 0; }
    .risk-bar-fill { height: 100%; text-align: center; color: white; font-weight: bold; line-height: 35px; font-size: 18px; transition: 1s; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background: #f1f2f6; border-radius: 10px 10px 0 0; font-weight: bold; color: #6c5ce7; }
    .stTabs [aria-selected="true"] { background: #ff00ff !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR: ADMIN CONFIG & EXPORTS ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("⚙️ ADMIN CONFIG")
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
    st.info("SENDER: aeserviseu@gmail.com")

# --- 6. MOTOR DE ANÁLISIS (DATA INTEGRADA) ---
np.random.seed(now.minute)
viento = np.random.randint(10, 90)
polvo = np.random.randint(20, 100)
riesgo_calc = int((viento * 0.45) + (polvo * 0.55))
color_p = "#ff00ff" if riesgo_calc > 70 else "#6c5ce7" if riesgo_calc > 40 else "#00cec9"

# --- 7. DASHBOARD PRINCIPAL (CODELCO OBJECTIVE ZERO) ---
st.header(f"🚀 {faena_sel.upper()} | GOBERNANZA OPERATIVA")

# BARRA DE RIESGO CERO (RECUPERADA)
st.markdown(f"**CODELCO OBJECTIVE ZERO RISK: {riesgo_calc}%**")
st.markdown(f'<div class="risk-bar-bg"><div class="risk-bar-fill" style="width: {riesgo_calc}%; background: {color_p};">{riesgo_calc}%</div></div>', unsafe_allow_html=True)

# KPIs VIBRANTES (RECUPERADOS)
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("🌪️ Polvo PM10", f"{polvo} µg/m³", "FUSION CORE")
with c2: st.metric("🌬️ Viento Meteo", f"{viento} km/h", "ADMS ACTIVE")
with c3: st.metric("📍 Nodos GPS", "70,000", "ONLINE")
with c4: st.metric("💓 Biometría", "98%", "EPP WORN ON")

st.divider()

# --- 8. MÓDULOS TÁCTICOS (ORDENADOS POR PESTAÑAS) ---
t1, t2, t3, t4 = st.tabs(["🍃 ENVIRO FUSION", "👷 WORKER SAFETY", "🎯 TOP RISK PROBABILITY", "🛰️ SAT-SURVEILLANCE"])

with t1:
    st.subheader("Environmental Fusion Core (PM10 / PM2.5 / Meteo)")
    col_e1, col_e2 = st.columns([1, 2])
    with col_e1:
        st.write("**Mitigation Forecast:**")
        st.info("Intervención sugerida en 15 min")
        st.write("**Dispersion Level:**")
        st.warning("High (Sector Norte)")
    with col_e2:
        df_env = pd.DataFrame({'Hora': range(10), 'Nivel': np.random.randint(30, 90, 10)})
        st.plotly_chart(px.line(df_env, x='Hora', y='Nivel', title="Tendencia Particulado", color_discrete_sequence=['#ff00ff']), use_container_width=True)

with t2:
    st.subheader("Worker Safety: PPE & Fall Detection")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("### Status EPP")
        st.success("98% Compliance")
        st.write("- **Helmet:** Worn On")
        st.write("- **Gloves:** Worn On")
    with col_s2:
        st.markdown("### ADMS Response")
        st.write("- **Fall Detection:** Standby")
        st.write("- **Mitigation:** Active")

with t3:
    st.subheader("Top Risk Probability: Where / Who / What")
    r1, r2, r3 = st.columns(3)
    r1.error(f"**WHERE:** Sector Chancado")
    r2.error(f"**WHO:** Cuadrilla {np.random.randint(1,10)}")
    r3.error(f"**WHAT:** Dispersion Peak")

with t4:
    st.subheader("Tactical Sat-Response")
    m = folium.Map(location=coords, zoom_start=15, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium.Circle(coords, radius=500, color='#ff00ff', fill=True, popup="AIH CONTROL RADIUS").add_to(m)
    folium_static(m, width=1050, height=450)

# --- 9. LOG DE AUDITORÍA (AUDIT-READY) ---
st.divider()
st.subheader("📜 HSE GENERAL AUDIT LOG")
log_data = pd.DataFrame([{
    "Timestamp": now.strftime("%H:%M:%S"),
    "Faena": faena_sel,
    "Status": "CERTIFIED",
    "Admin": "aeserviseu@gmail.com"
}])
st.table(log_data)
if st.button("📧 ENVIAR AUDITORÍA A GERENCIA"):
    st.success("Reporte enviado desde aeserviseu@gmail.com")

st.divider()
st.caption("AIH-MASTER COMMAND v14.0 | Uniting Technology Belgium | Codelco Objective Zero Risk")
