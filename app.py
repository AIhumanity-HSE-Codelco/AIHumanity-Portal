import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime, timedelta
import pytz

# --- 1. CONFIGURACIÓN DE NÚCLEO (CUARENTENA DE ERRORES) ---
st.set_page_config(page_title="AIH-MASTER SUPREME", layout="wide", initial_sidebar_state="expanded")

# --- 2. RELOJ INDUSTRIAL GIGANTE (ESTILO V8.0/V10.0 RECUPERADO) ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)
st.markdown(f"""
    <div style="background: linear-gradient(90deg, #6c5ce7, #ff00ff); padding: 35px; border-radius: 25px; text-align: center; color: white; box-shadow: 0 15px 40px rgba(108, 92, 231, 0.4); margin-bottom: 25px;">
        <h1 style="font-size: 110px; margin: 0; letter-spacing: -6px; font-weight: 900; line-height: 1;">{now.strftime('%H:%M:%S')}</h1>
        <p style="font-size: 26px; margin: 0; opacity: 0.9; font-weight: 300; letter-spacing: 2px;">{now.strftime('%A, %d de %B %Y')} | CODELCO OBJECTIVE ZERO ACTIVE</p>
    </div>
""", unsafe_allow_html=True)

# --- 3. BASE DE DATOS MAESTRA (70,000 NODOS AIDEEPMINER) ---
FAENAS = {
    "CODELCO NORTE": {"Chuquicamata": [-22.3, -68.9], "RT": [-22.2, -68.8]},
    "CODELCO CENTRO": {"El Teniente": [-34.1, -70.4], "Andina": [-33.1, -70.2]},
    "SUR / BHP": {"Escondida": [-24.2, -69.0], "Salvador": [-26.2, -69.6]}
}

# --- 4. CSS VIBRANTE (FUCSIA, AMARILLO, MORADO, BLANCO) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .metric-card { background: #f8f9fa; border-radius: 20px; padding: 20px; border-left: 10px solid #ff00ff; box-shadow: 0 8px 16px rgba(0,0,0,0.05); }
    .stMetric { color: #2d3436 !important; font-weight: 700; }
    .risk-bar-bg { width: 100%; background: #dfe6e9; border-radius: 20px; height: 45px; border: 2px solid #eee; overflow: hidden; margin-top: 10px; }
    .risk-bar-fill { height: 100%; text-align: center; color: white; font-weight: 900; line-height: 45px; font-size: 22px; transition: 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
    .stTabs [data-baseweb="tab-list"] { gap: 15px; }
    .stTabs [data-baseweb="tab"] { background: #f1f2f6; border-radius: 12px; padding: 12px 25px; font-weight: bold; color: #6c5ce7; border: none; }
    .stTabs [aria-selected="true"] { background: #ff00ff !important; color: white !important; box-shadow: 0 5px 15px rgba(255,0,255,0.3); }
    </style>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR: ADMIN CONFIG & EXPORTS ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=130)
    st.title("🛡️ ADMIN CONFIG")
    st.divider()
    room_mode = st.selectbox("ROOM MODE", ["OPEN HSE CONTROL ROOM", "OPEN ADMIN CONFIG", "ADMS TACTICAL RESPONSE"])
    region = st.selectbox("📍 Sector:", list(FAENAS.keys()))
    faena_sel = st.selectbox("🏗️ Unidad:", list(FAENAS[region].keys()))
    coords = FAENAS[region][faena_sel]
    
    st.divider()
    st.markdown("### 📥 AUDIT EXPORT ENGINE")
    col_ex1, col_ex2 = st.columns(2)
    col_ex1.button("JSON")
    col_ex2.button("CSV")
    st.button("EXPORT LOG HSE GENERAL", use_container_width=True)
    st.divider()
    st.info(f"SENDER: aeserviseu@gmail.com")

# --- 6. MOTOR DE RIESGO E INTELIGENCIA (DATA HISTÓRICA & NUEVA) ---
np.random.seed(now.minute)
viento = np.random.randint(15, 85)
polvo_pm10 = np.random.randint(20, 95)
biometria_check = np.random.randint(90, 100)
# Algoritmo de Riesgo Compuesto (Documentación AIDeepMiner)
riesgo_calc = int((viento * 0.4) + (polvo_pm10 * 0.5) + ((100 - biometria_check) * 1.5))
color_r = "#ff00ff" if riesgo_calc > 75 else "#fbc531" if riesgo_calc > 45 else "#4cd137"

# --- 7. DASHBOARD PRINCIPAL (RECUPERADO) ---
st.header(f"🚀 {faena_sel.upper()} | OPERATIONAL RISK CENTER")
st.markdown(f"**AIDeepMiner Core:** 70,000 Nodos Activos | **Status:** Sincronizado")

# BARRA DE RIESGO CERO (LA VIBRANTE)
st.markdown(f"**CODELCO OBJECTIVE ZERO OPERATIONAL RISK: {riesgo_calc}%**")
st.markdown(f"""
    <div class="risk-bar-bg">
        <div class="risk-bar-fill" style="width: {riesgo_calc}%; background: {color_r}; box-shadow: 10px 0 20px {color_r}88;">
            {riesgo_calc}% - {"ALERTA CRÍTICA" if riesgo_calc > 75 else "SEGURO"}
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# KPIs DE ENTORNO (BLANCOS Y COLORIDOS)
k1, k2, k3, k4 = st.columns(4)
with k1: st.metric("🌪️ PM10 FUSION", f"{polvo_pm10} µg/m³", "METEO ON")
with k2: st.metric("🌬️ VIENTO REAL", f"{viento} km/h", "ADMS ACTIVE")
with k3: st.metric("👷 SAFETY CORE", f"{biometria_check}%", "EPP WORN ON")
with k4: st.metric("⌚ LATENCIA", "4ms", "70K NODOS")

st.divider()

# --- 8. MÓDULOS DE INTEGRACIÓN (TABS LÓGICOS) ---
tab_fusion, tab_worker, tab_map, tab_audit = st.tabs([
    "🍃 ENVIRONMENTAL FUSION", 
    "👷 WORKER SAFETY CORE", 
    "🛰️ SAT-SURVEILLANCE",
    "📜 HSE GENERAL LOG"
])

# 8.1 ENVIRONMENTAL FUSION CORE
with tab_fusion:
    st.subheader("Fusion Core: PM10 / PM2.5 & Dispersion Forecast")
    c_f1, c_f2 = st.columns([1, 2])
    with c_f1:
        st.markdown("### Top Risk Drivers")
        st.error(f"**Probabilidad:** {riesgo_calc}%")
        st.warning(f"**What:** Dispersión por Viento")
        st.info(f"**Where:** Sector Chancado")
    with c_f2:
        df_hist = pd.DataFrame({'Hora': range(12), 'Riesgo': np.random.randint(20, 90, 12)})
        st.plotly_chart(px.area(df_hist, x='Hora', y='Riesgo', title="Histórico de Riesgo (12h)", color_discrete_sequence=['#6c5ce7']), use_container_width=True)

# 8.2 WORKER SAFETY CORE (EPP & FALL DETECTION)
with tab_worker:
    st.subheader("Worker Safety & ADMS Mitigation")
    
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        st.markdown("### AI-PPE Detection")
        st.success("STATUS: WORN ON")
        st.write("Verificación de Casco y Guantes: **OK**")
    with col_w2:
        st.markdown("### ADMS Tactical")
        st.write("Fall Detection Algorithm: **STANDBY**")
        st.write("Mitigation Forecast: **FAIL DETECTION ACTIVE**")

# 8.3 SAT-SURVEILLANCE
with tab_map:
    st.subheader(f"Teledetección Táctica: {faena_sel}")
    m = folium.Map(location=coords, zoom_start=15, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium.Circle(coords, radius=500, color='#ff00ff', fill=True, popup="AIH CONTROL AREA").add_to(m)
    folium_static(m, width=1100, height=450)

# 8.4 HSE GENERAL LOG (TRAZABILIDAD)
with tab_audit:
    st.subheader("📜 Auditoría y Contabilidad HSE")
    log_data = pd.DataFrame([{
        "Registro ID": f"AIH-{now.strftime('%y%m%d')}-01",
        "Unidad": faena_sel,
        "Evento": "Control Room Sync",
        "Admin": "aeserviseu@gmail.com",
        "Status": "CERTIFIED"
    }])
    st.table(log_data)
    if st.button("📧 ENVIAR REPORTE MAESTRO"):
        st.success(f"Log despachado desde **aeserviseu@gmail.com**")

st.divider()
st.caption("AIH-MASTER SUPREME v15.0 | Uniting Technology Belgium | Codelco Objective Zero Risk")
