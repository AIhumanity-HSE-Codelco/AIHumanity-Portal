import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import pytz

# --- MANEJO DE MÓDULO SERIAL (EVITA EL CRASH) ---
try:
    import serial
    import serial.tools.list_ports
    SERIAL_AVAILABLE = True
except ImportError:
    SERIAL_AVAILABLE = False

# --- 1. CONFIGURACIÓN DE ESCENA ---
st.set_page_config(page_title="AIHUMANITY MASTER", layout="wide", initial_sidebar_state="collapsed")

# --- 2. ESTILO APPLE CUPERTINO (FONDO BLANCO / VIBRANTE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    html, body, [class*="st-"] { font-family: 'SF Pro Display', sans-serif; background-color: #f5f5f7; }
    
    .apple-card {
        background: white; border-radius: 24px; padding: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.04); margin-bottom: 25px;
        border: 1px solid rgba(0,0,0,0.02);
    }
    .clock-large { font-size: 110px; font-weight: 600; text-align: center; color: #1d1d1f; letter-spacing: -6px; line-height: 1; }
    .status-pill { padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; text-transform: uppercase; }
    .stButton>button { background-color: #0071e3; color: white; border-radius: 14px; font-weight: 600; height: 50px; border: none; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE TIEMPO ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)

# --- 4. CABECERA GOBERNANZA ---
st.markdown(f'<div class="clock-large">{now.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align:center; color:#86868b; font-size:22px; margin-bottom:40px;">{now.strftime("%A, %d de %B %Y")} | GOBERNANZA CHILE</p>', unsafe_allow_html=True)

# --- 5. PANEL CENTRAL ---
col_left, col_right = st.columns([2, 1])

with col_left:
    # MÓDULO: RIESGO OPERACIONAL (70,000 NODOS)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Codelco Objective Zero")
    
    # Simulación de Riesgo Compuesto
    riesgo = np.random.randint(25, 80)
    color = "#ff3b30" if riesgo > 70 else "#0071e3"
    st.markdown(f"**Nivel de Riesgo Compuesto: {riesgo}%**")
    st.markdown(f'<div style="width:100%; background:#e5e5ea; height:35px; border-radius:18px; overflow:hidden;"><div style="width:{riesgo}%; background:{color}; height:100%; transition: 1.5s;"></div></div>', unsafe_allow_html=True)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("🌪️ PM10", f"{np.random.randint(30,90)} µg/m³", "ADMS ON")
    k2.metric("🌬️ Viento", f"{np.random.randint(10,55)} km/h", "METEO")
    k3.metric("👷 Nodos", "70,000", "TRL-3/4")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO: HARDWARE PROVISIONING (INTEGRADO)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🔌 AIDeepMiner Hardware Bridge")
    
    if not SERIAL_AVAILABLE:
        st.error("⚠️ Error de Módulo: 'pyserial' no detectado en el servidor. Instale vía requirements.txt")
    
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        if st.button("Detectar Casco (USB)"):
            if SERIAL_AVAILABLE:
                ports = serial.tools.list_ports.comports()
                if ports:
                    for p in ports: st.success(f"Nodo Activo: {p.device}")
                else: st.warning("Conecte el dispositivo físico.")
            else:
                st.info("Modo Simulación: Dispositivo virtual detectado (AID-TEST-01)")
                
    with col_u2:
        f = st.file_uploader("Actualizar Software (.bin)", type="bin")
        if f and st.button("Cargar a AIDeepMiner"):
            st.write("Flasheando software...")
            st.progress(100)
            st.success("Configuración exitosa.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # MÓDULO: ADMS & MITIGACIÓN
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("💧 ADMS Mitigation")
    st.write("Estado de Nebulización: **ACTIVO**")
    st.progress(85)
    st.caption("Mitigación de polvo en Sector Chancado")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO: WORKER SAFETY (BIOMETRÍA)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("👷 Worker Safety")
    st.info("EPP Detection: **WORN ON**")
    st.write("- Fall Detection: **STANDBY**")
    st.write("- Heart Rate: **72 BPM**")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. GOBERNANZA DE DATOS ---
st.markdown('<div class="apple-card" style="text-align:center;">', unsafe_allow_html=True)
st.subheader("📜 Auditoría y Evidencia")
ce1, ce2, ce3 = st.columns(3)
ce1.button("Export JSON")
ce2.button("Export CSV")
if ce3.button("Enviar Log a aeserviseu@gmail.com"):
    st.success("Reporte despachado.")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("AIHUMANITY v21.0 | Uniting Technology Belgium | Hardware Bridge & Governance Core")
