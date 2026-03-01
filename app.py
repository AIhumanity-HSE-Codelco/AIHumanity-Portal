import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# CONFIGURACIÓN BÁSICA (PARA EVITAR PANTALLA BLANCA)
st.set_page_config(page_title="AIH Teniente", layout="wide")

# ESTILO CUPERTINO INYECTADO
st.markdown("""
    <style>
    .stApp { background-color: #F5F5F7; color: #1D1D1F; }
    .card { background: white; border-radius: 20px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; border: 1px solid #E5E5E5; }
    h1, h2, h3 { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #1D1D1F; }
    </style>
    """, unsafe_allow_html=True)

# LÓGICA DE DATOS (SIMULACIÓN AUTOMÁTICA)
if 'count' not in st.session_state: st.session_state.count = 0
st.session_state.count += 1

# VALORES SIMULADOS
mp10 = 40 + (np.sin(st.session_state.count * 0.1) * 5)
riesgo = 30 + (np.cos(st.session_state.count * 0.1) * 10)

# INTERFAZ VISUAL
st.markdown(f"<h1 style='text-align: center; color: #5E5CE6;'>🛡️ AIHUMANITY | EL TENIENTE</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{datetime.now().strftime('%H:%M:%S')} | STATUS: ONLINE</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown(f"""<div class='card'>
        <p style='color: grey;'>META CERO</p>
        <h2 style='color: #30D158;'>{round(100 - riesgo, 1)}%</h2>
    </div>""", unsafe_allow_html=True)
    st.metric("MP10 Actual", f"{round(mp10, 1)} µg/m³")

with col2:
    # RADAR DE RIESGO HSE
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[mp10, riesgo, 20, 15, 25],
        theta=['Polvo', 'Geomecánica', 'Gases', 'Viento', 'Tránsito'],
        fill='toself', fillcolor='rgba(94, 92, 230, 0.2)', line=dict(color='#5E5CE6')
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=400, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.markdown("<div class='card'><h3>Alertas</h3><p style='color: red;'>● Galería N-4: Bloqueada</p></div>", unsafe_allow_html=True)
    if st.button("🚨 STOP-WORK"):
        st.error("Protocolo Activado")

# MOTOR DE MOVIMIENTO (EVITA QUE SE QUEDE ESTÁTICO)
time.sleep(2)
st.rerun()
