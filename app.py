import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- 1. CONFIGURACIÓN DE SISTEMA ---
st.set_page_config(page_title="AIH-MASTER REAL-TIME", layout="wide", initial_sidebar_state="collapsed")

# --- 2. LÓGICA DE ESTADO (PERSISTENCIA) ---
if 'session_active' not in st.session_state:
    st.session_state.session_active = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# --- 3. ESTILO APPLE CUPERTINO (DYNAMIC DARK/LIGHT) ---
st.markdown("""
    <style>
    .metric-card {
        background: white; border-radius: 20px; padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center;
        border: 1px solid #efeff4;
    }
    .conn-bar { width: 100%; background: #e5e5ea; border-radius: 10px; height: 12px; margin-top: 10px; }
    .conn-fill { height: 100%; border-radius: 10px; transition: width 0.5s ease; }
    .status-live { color: #34c759; font-weight: 600; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
""", unsafe_allow_html=True)

# --- 4. CABECERA OPERATIVA ---
t1, t2 = st.columns([3, 1])
with t1:
    st.title("🛰️ AIHumanity: Operación en Tiempo Real")
with t2:
    if st.session_state.session_active:
        st.markdown("<p class='status-live'>● LIVE STREAMING</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#ff3b30;'>● OFFLINE / STANDBY</p>", unsafe_allow_html=True)

# --- 5. MONITOR DE CONECTIVIDAD TOTAL (100%) ---
# Cada módulo (D32, D26, D25) = 33.3%
modulos_ok = sum([1 if st.session_state.get('luz_sync', True) else 0, 
                  1 if st.session_state.get('temp_sync', True) else 0, 
                  1 if st.session_state.session_active else 0])
conectividad = int((modulos_ok / 3) * 100)
color_conn = "#34c759" if conectividad > 90 else "#ffcc00" if conectividad > 30 else "#ff3b30"

st.markdown(f"**Conectividad de Sensores: {conectividad}%**")
st.markdown(f'<div class="conn-bar"><div class="conn-fill" style="width:{conectividad}%; background:{color_apple if "color_apple" in locals() else color_conn};"></div></div>', unsafe_allow_html=True)

st.divider()

# --- 6. PANELES DE SENSORES (33.3% c/u) ---
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.caption("MÓDULO LUZ (D32)")
    luz_val = np.random.randint(600, 900) if st.session_state.session_active else 0
    st.subheader(f"🔆 {luz_val} lx")
    st.progress(luz_val/1024)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.caption("MÓDULO TEMP (D26)")
    temp_val = round(24.0 + np.random.uniform(0, 2), 1) if st.session_state.session_active else 0.0
    st.subheader(f"🌡️ {temp_val} °C")
    st.write("Variación: ±0.2s")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.caption("INFRARROJO (D25)")
    if st.button("SIMULAR CONTACTO IR (D25)"):
        st.session_state.session_active = not st.session_state.session_active
        st.session_state.start_time = datetime.now().strftime("%H:%M:%S") if st.session_state.session_active else None
        st.rerun()
    
    if st.session_state.session_active:
        st.success("CASCO PUESTO")
        st.write(f"Sesión iniciada: {st.session_state.start_time}")
    else:
        st.error("D25: SIN CONTACTO")
        st.write("Modo: Offline")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. GRÁFICA EN TIEMPO REAL ---
if st.session_state.session_active:
    st.subheader("📈 Flujo de Datos AIDeepMiner")
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Luz (D32)', 'Temp (D26)'])
    st.line_chart(chart_data)



st.caption("AIH-MASTER v27.0 | Sincronización Telenet 5E4ED | Uniting Technology Belgium")
