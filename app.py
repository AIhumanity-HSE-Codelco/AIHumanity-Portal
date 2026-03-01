import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. CONFIGURACIÓN DE ESCENARIO
st.set_page_config(page_title="AIH | El Teniente HSE", layout="wide", initial_sidebar_state="collapsed")

# 2. INYECCIÓN DE ESTILO PROFESIONAL (CSS PREMIUM)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F0F2F5; }
    
    /* Contenedores Tipo Apple */
    .metric-card {
        background: white;
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid rgba(0,0,0,0.02);
        text-align: center;
    }
    
    /* Header Flotante */
    .main-header {
        background: linear-gradient(90deg, #5E5CE6, #30D158);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 0px;
    }
    
    /* Botón de Emergencia */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 50px;
        background: #FF3B30;
        color: white;
        border: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE TELEMETRÍA (SIMULACIÓN FLUIDA)
if 'step' not in st.session_state: st.session_state.step = 0
st.session_state.step += 1

# Generación de datos con "Inercia" (No saltan feo)
val_mp10 = 35 + (np.sin(st.session_state.step * 0.2) * 8)
val_risk = 40 + (np.cos(st.session_state.step * 0.2) * 12)

# 4. CUERPO DEL DASHBOARD
st.markdown("<h1 class='main-header'>AIHUMANITY CORE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8E8E93;'>CENTRO DE INTELIGENCIA PREVENTIVA - EL TENIENTE</p>", unsafe_allow_html=True)

# Fila 1: Indicadores Críticos
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"<div class='metric-card'><p style='color:#8E8E93; font-weight:600;'>META CERO</p><h2 style='color:#30D158;'>{round(100-val_risk,1)}%</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><p style='color:#8E8E93; font-weight:600;'>MP10 (POLVO)</p><h2 style='color:#5E5CE6;'>{round(val_mp10,1)}</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='metric-card'><p style='color:#8E8E93; font-weight:600;'>VIENTO</p><h2 style='color:#1D1D1F;'>14 <small>km/h</small></h2></div>", unsafe_allow_html=True)
with c4:
    st.markdown(f"<div class='metric-card'><p style='color:#8E8E93; font-weight:600;'>ESTATUS</p><h2 style='color:#30D158;'>OK</h2></div>", unsafe_allow_html=True)

st.write("") # Espaciador

# Fila 2: Radar y Alertas
col_radar, col_side = st.columns([2, 1])

with col_radar:
    # RADAR CHART PROFESIONAL
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[val_mp10, val_risk, 20, 15, 25],
        theta=['Polvo', 'Geomecánica', 'Gases', 'Viento', 'Tránsito'],
        fill='toself',
        fillcolor='rgba(94, 92, 230, 0.2)',
        line=dict(color='#5E5CE6', width=4)
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100], gridcolor="#EEE")),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=40, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)

with col_side:
    st.markdown("### 🚨 Panel de Control")
    st.info("**ADEEPMINERS:** 8 Nodos en línea")
    st.warning("**CLIMA:** Dispersión sector Sur estable")
    st.write("---")
    if st.button("STOP-WORK AUTHORITY"):
        st.error("PROCEDIMIENTO INICIADO")
    
    # Reloj Regional
    st.markdown(f"**Hora Local:** {datetime.now().strftime('%H:%M:%S')}")

# 5. REFRESCO AUTOMÁTICO (ANIMACIÓN)
time.sleep(1.2)
st.rerun()
