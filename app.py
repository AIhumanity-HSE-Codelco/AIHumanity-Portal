import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime, timedelta
import pytz
import json
import base64

# --- 1. CONFIGURACIÓN DE NÚCLEO INDUSTRIAL ---
st.set_page_config(page_title="AIH-MASTER SUPREME COMMAND", layout="wide", initial_sidebar_state="expanded")

# --- 2. MOTOR DE TIEMPO Y AUDITORÍA (CHILE) ---
tz = pytz.timezone('America/Santiago')
def get_now(): return datetime.now(tz)

# --- 3. BASE DE DATOS DE GOBERNANZA (70K NODOS AIDEEPMINER) ---
# Clasificación de Riesgo Codelco: Probabilidad vs Consecuencia
RISK_DRIVERS = ["Fatiga Humana", "Dispersión Polvo", "Falla EPP", "Meteorología Extrema", "Interacción Hombre-Máquina"]

FAENAS_DB = {
    "CODELCO Norte": {"Chuquicamata": [-22.3, -68.9], "RT": [-22.2, -68.8]},
    "CODELCO Centro": {"El Teniente": [-34.1, -70.4], "Andina": [-33.1, -70.2]},
    "BHP / Otros": {"Escondida": [-24.2, -69.0], "Salvador": [-26.2, -69.6]}
}

# --- 4. CSS: INTERFAZ VIBRANTE & AMIGABLE AL RATÓN ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'JetBrains Mono', monospace; background-color: #ffffff; }
    
    .main-clock { font-size: 55px !important; font-weight: 800; color: #1d1d1f; text-align: center; margin-bottom: 0px; letter-spacing: -2px; }
    .date-label { font-size: 18px; color: #636e72; text-align: center; margin-bottom: 20px; }
    
    .status-card { background: #f8f9fa; padding: 25px; border-radius: 20px; border-left: 8px solid #ff00ff; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .metric-vibrant { color: #6c5ce7; font-weight: 800; font-size: 2.5rem; }
    
    /* Risk Progress Bars */
    .bar-container { width: 100%; background: #dfe6e9; border-radius: 10px; height: 18px; margin: 10px 0; }
    .bar-fill { height: 100%; border-radius: 10px; transition: 1s ease-in-out; }
    
    /* Tooltip & Hover effects */
    .stButton>button { width: 100%; border-radius: 12px; height: 50px; font-weight: bold; background: linear-gradient(90deg, #6c5ce7, #ff00ff); color: white; border: none; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(108, 92, 231, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR: OPEN ADMIN CONFIG & GOBERNANZA ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=140)
    st.markdown("### 🛡️ OPEN ADMIN CONFIG")
    
    # RELOJ AGRANDADO
    st.markdown(f"<p class='main-clock'>{get_now().strftime('%H:%M')}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='date-label'>{get_now().strftime('%A, %d de %B %Y')}</p>", unsafe_allow_html=True)
    
    st.divider()
    op_mode = st.selectbox("CONTROL ROOM MODE", ["HSE CONTROL ROOM", "ADMS TACTICAL", "WORKER SAFETY CORE"])
    
    st.subheader("📍 Despliegue Operativo")
    region = st.selectbox("Región Operativa", list(FAENAS_DB.keys()))
    unidad = st.selectbox("Unidad Minera", list(FAENAS_DB[region].keys()))
    coords = FAENAS_DB[region][unidad]
    
    st.divider()
    st.markdown("### 📥 AUDIT-READY EXPORTS")
    if st.button("EXPORT JSON"): st.download_button("Confirme JSON", "{}", "audit.json")
    if st.button("EXPORT CSV"): st.download_button("Confirme CSV", "id,risk,who", "audit.csv")
    if st.button("EXPORT HSE LOG"): st.success("Log General Generado")

# --- 6. MOTOR DE ANÁLISIS DE RIESGO (PAST & NEW DATA) ---
# Simulación de 70k nodos procesando data histórica y actual
np.random.seed(datetime.now().hour)
hist_data = pd.DataFrame({
    'timestamp': [get_now() - timedelta(minutes=i*10) for i in range(24)],
    'pm10': np.random.normal(50, 15, 24),
    'viento': np.random.normal(30, 10, 24),
    'risk_score': np.random.randint(20, 85, 24)
})

current_risk = int(hist_data['risk_score'].iloc[0])
pm10 = int(hist_data['pm10'].iloc[0])
pm25 = int(pm10 * 0.4)
viento_kmh = int(hist_data['viento'].iloc[0])

# --- 7. PANEL PRINCIPAL: CODELCO OBJECTIVE ZERO ---
st.title(f"🚀 {unidad.upper()} | OPERATIONAL RISK CENTER")
st.markdown(f"**AIDeepMiner Governance** | Sensor Fusion: Active | Latency: 4ms")

# TOP RISK PROBABILITY: WHERE / WHO / WHAT
c_zero1, c_zero2, c_zero3 = st.columns(3)
with c_zero1:
    st.markdown(f"<div class='status-card'><strong>TOP RISK DRIVER</strong><br><span style='color:#ff3b30; font-size:1.5rem;'>{RISK_DRIVERS[0]}</span><br>Probability: {current_risk}%</div>", unsafe_allow_html=True)
with c_zero2:
    st.markdown(f"<div class='status-card'><strong>CRITICAL ZONE (WHERE)</strong><br><span style='color:#6c5ce7; font-size:1.5rem;'>Sector Chancado 04</span><br>Nodos Activos: 450</div>", unsafe_allow_html=True)
with c_zero3:
    st.markdown(f"<div class='status-card'><strong>RESPONSIBLE (WHO)</strong><br><span style='color:#f39c12; font-size:1.5rem;'>Turno B - Cuadrilla 12</span><br>Status: Monitoreado</div>", unsafe_allow_html=True)

st.divider()

# --- 8. MÓDULOS ESPECIALIZADOS (TABS) ---
tab_env, tab_safety, tab_adms, tab_map = st.tabs([
    "🍃 ENVIRONMENTAL FUSION", 
    "👷 WORKER SAFETY CORE", 
    "💧 ADMS TACTICAL",
    "🛰️ SAT-SURVEILLANCE"
])

# 8.1 ENVIRONMENTAL FUSION CORE
with tab_env:
    st.subheader("Meteo & Dust Dispersion Analysis")
    col_e1, col_e2, col_e3 = st.columns(3)
    col_e1.metric("PM10 Ground", f"{pm10} µg/m³", "-5%")
    col_e2.metric("PM2.5 Respirable", f"{pm25} µg/m³", "+2%")
    col_e3.metric("Meteorología", f"{viento_kmh} km/h", "NW Direction")
    
    # Gráfico de dispersión histórica
    fig_env = px.area(hist_data, x='timestamp', y=['pm10', 'pm25'], title="Fusión de Material Particulado (24h)", color_discrete_map={"pm10": "#ff00ff", "pm25": "#6c5ce7"})
    st.plotly_chart(fig_env, use_container_width=True)

# 8.2 WORKER SAFETY CORE (EPP & FALL DETECTION)
with tab_safety:
    st.subheader("AI-PPE & Biometric Monitoring")
        col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.info("PPE Status: **WORN ON**")
        st.markdown("**Fall Detection Algorithm:** STANDBY (Active)")
        st.progress(95)
        st.caption("Cumplimiento de Casco/Guantes/Lentes")
    with col_s2:
        st.error("Alert: **WORN OFF** detected in Zone 3")
        st.markdown("**Worker ID:** AIH-99283 (Contratista)")
        st.button("Trigger Immediate Warning")

# 8.3 ADMS TACTICAL RESPONSE
with tab_adms:
    st.subheader("Mitigation & Forecast Response")
    col_a1, col_a2 = st.columns([1, 2])
    with col_a1:
        st.markdown("### Mitigation Strategy")
        st.write("- **Aspersores:** ACTIVOS (70%)")
        st.write("- **Camiones Aljibe:** 2 en ruta")
        st.write("- **Drones ADMS:** Desplegados")
    with col_a2:
        st.warning("FORECAST: High Dust Peak in 20 mins due to wind shift (35km/h NW)")
        st.metric("Fail Detection Rate", "0.02%", "Stable")

# 8.4 SAT-SURVEILLANCE
with tab_map:
    st.subheader(f"70,000 Nodos en {unidad}")
    m = folium.Map(location=coords, zoom_start=15, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium.Circle(coords, radius=400, color='#ff00ff', fill=True, popup="FUSION CORE RADIUS").add_to(m)
    folium_static(m, width=1100, height=500)

# --- 9. FOOTER AUDIT-READY ---
st.divider()
st.caption("AIH-MASTER COMMAND v11.0 | Objective Zero Risk | aeserviseu@gmail.com | Uniting Technology Belgium")
