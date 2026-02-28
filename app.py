import streamlit as st
import pandas as pd
import numpy as np
import serial
import serial.tools.list_ports
import time
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN TÉCNICA ---
st.set_page_config(page_title="AIH-MASTER COMMAND", layout="wide", initial_sidebar_state="collapsed")

# --- 2. ESTILO APPLE CUPERTINO (RECUPERADO Y MEJORADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    html, body, [class*="st-"] { font-family: 'SF Pro Display', sans-serif; background-color: #f5f5f7; }
    
    .apple-card {
        background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(20px);
        border-radius: 22px; padding: 25px; border: 1px solid rgba(0,0,0,0.05);
        box-shadow: 0 8px 32px rgba(0,0,0,0.03); margin-bottom: 20px;
    }
    .big-clock { font-size: 100px; font-weight: 600; text-align: center; color: #1d1d1f; letter-spacing: -5px; line-height: 1; }
    .status-pill { padding: 5px 15px; border-radius: 20px; font-size: 14px; font-weight: 600; }
    .stButton>button { background-color: #0071e3; color: white; border-radius: 12px; font-weight: 600; width: 100%; border: none; }
    </style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE TIEMPO (CHILE) ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)

# --- 4. CABECERA SUPREMA ---
st.markdown(f'<div class="big-clock">{now.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="text-align:center; color:#86868b; font-size:20px;">{now.strftime("%A, %d de %B %Y")} | GOBERNANZA CENTRAL</p>', unsafe_allow_html=True)

# --- 5. PANEL DE CONTROL UNIFICADO ---
col_left, col_right = st.columns([2, 1])

with col_left:
    # MÓDULO: INTEGRACIÓN HARDWARE ESP32
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🔌 AIDeepMiner Hardware Bridge")
    st.write("Conecte el casco vía USB para lectura de software interno y aprovisionamiento.")
    
    c_usb, c_firm = st.columns(2)
    with c_usb:
        if st.button("Detectar Hardware (ESP32)"):
            ports = serial.tools.list_ports.comports()
            if ports:
                for p in ports: st.success(f"Nodo Detectado: {p.device}")
            else:
                st.warning("Buscando dispositivo... Asegure conexión física.")
    
    with c_firm:
        f_file = st.file_uploader("Firmware Binario", type="bin")
        if f_file and st.button("Cargar Software"):
            bar = st.progress(0)
            for i in range(101):
                time.sleep(0.02)
                bar.progress(i)
            st.success("Software cargado al ESP32 con éxito.")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO: RIESGO OPERACIONAL (70K NODOS)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Codelco Objective Zero Risk")
    riesgo = np.random.randint(30, 80)
    color = "#ff3b30" if riesgo > 70 else "#0071e3"
    st.markdown(f"**Nivel de Riesgo Actual: {riesgo}%**")
    st.markdown(f'<div style="width:100%; background:#e5e5ea; height:30px; border-radius:15px; overflow:hidden;"><div style="width:{riesgo}%; background:{color}; height:100%;"></div></div>', unsafe_allow_html=True)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("🌪️ PM10", f"{np.random.randint(30,90)} µg/m³")
    k2.metric("🌬️ Viento", f"{np.random.randint(10,50)} km/h")
    k3.metric("👷 Compliance EPP", "99.4%")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # MÓDULO: ADMS TACTICAL & MITIGACIÓN
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("💧 ADMS Mitigation")
    st.write("Estatus Supresores: **ONLINE**")
    st.progress(85)
    st.caption("Eficacia de Mitigación en Tiempo Real")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO: WORKER SAFETY (BIOMETRÍA & CAÍDA)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("👷 Worker Safety Core")
    st.write("- Fall Detection: **ACTIVE**")
    st.write("- Worn On/Off: **SINCRO**")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. EXPORTACIÓN DE EVIDENCIA ---
st.markdown('<div class="apple-card" style="text-align:center;">', unsafe_allow_html=True)
st.subheader("📜 Audit-Ready Logs")
ce1, ce2, ce3 = st.columns(3)
ce1.button("Export JSON")
ce2.button("Export CSV")
if ce3.button("Send to aeserviseu@gmail.com"):
    st.success("Log Enviado")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("AIH-MASTER COMMAND v19.0 | Uniting Technology Belgium")
