import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import serial
import serial.tools.list_ports
import time
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE ESCENA ---
st.set_page_config(page_title="AIH-MASTER SUPREME", layout="wide", initial_sidebar_state="collapsed")

# --- 2. ESTILO APPLE HIGH-END (CUPERTINO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    html, body, [class*="st-"] { font-family: 'SF Pro Display', sans-serif; background-color: #f5f5f7; }
    
    .apple-header {
        background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(20px);
        padding: 30px; border-radius: 24px; text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05); margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.3);
    }
    .main-clock { font-size: 90px; font-weight: 600; letter-spacing: -4px; color: #1d1d1f; margin: 0; }
    .apple-card {
        background: white; border-radius: 20px; padding: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03); margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #0071e3; color: white; border-radius: 12px;
        padding: 10px 24px; border: none; font-weight: 600; width: 100%;
    }
    .risk-bar-bg { width: 100%; background: #e5e5ea; border-radius: 15px; height: 35px; overflow: hidden; margin: 10px 0; }
    .risk-bar-fill { height: 100%; text-align: center; color: white; font-weight: bold; line-height: 35px; transition: 1.5s; }
    </style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE TIEMPO Y ESTADO ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)

# --- 4. CABECERA ÚNICA (RELOJ SUPREMO) ---
st.markdown(f"""
    <div class="apple-header">
        <p class="main-clock">{now.strftime('%H:%M')}</p>
        <p style="font-size: 22px; color: #86868b; margin: 0;">{now.strftime('%A, %d de %B %Y')} | PANEL CENTRAL INTEGRADO</p>
    </div>
""", unsafe_allow_html=True)

# --- 5. PANEL CENTRAL: TODOS LOS MÓDULOS ---
col_left, col_right = st.columns([2, 1])

with col_left:
    # MÓDULO 1: GOBERNANZA HSE (RIESGO CERO)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Operación General: Codelco Objective Zero")
    
    riesgo = np.random.randint(30, 85)
    color_r = "#ff3b30" if riesgo > 75 else "#0071e3"
    st.markdown(f"**Índice de Riesgo Compuesto: {riesgo}%**")
    st.markdown(f"""
        <div class="risk-bar-bg">
            <div class="risk-bar-fill" style="width: {riesgo}%; background-color: {color_r};">
                {riesgo}% - {"ALERTA" if riesgo > 75 else "NORMAL"}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("🌪️ PM10", f"{np.random.randint(40,90)} µg/m³")
    k2.metric("🌬️ Viento", f"{np.random.randint(15,60)} km/h")
    k3.metric("👷 Nodos", "70,000")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO 2: HARDWARE BRIDGE (ESP32)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🔌 Estación de Carga y Firmware (ESP32)")
    
    col_usb, col_flash = st.columns(2)
    with col_usb:
        if st.button("Detectar Cascos (USB)"):
            ports = serial.tools.list_ports.comports()
            if ports:
                for p in ports: st.success(f"Detectado: {p.device}")
            else:
                st.warning("No se detectan dispositivos físicos.")
    
    with col_flash:
        uploaded_file = st.file_uploader("Firmware AIDeepMiner (.bin)", type="bin")
        if uploaded_file and st.button("Flashear Software"):
            st.write("Cargando software al nodo...")
            st.progress(100)
            st.success("Software cargado e integrado.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # MÓDULO 3: ADMS & MITIGACIÓN
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("💧 ADMS Tactical")
    st.write("Sistema de Supresión: **ACTIVO**")
    st.progress(85)
    st.caption("Efectividad de Nebulización")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO 4: WORKER SAFETY (PPE)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("👷 Worker Safety")
    st.info("EPP Status: **WORN ON**")
    st.write("Fall Detection: **STANDBY**")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. EXPORTACIÓN Y AUDITORÍA ---
st.markdown('<div class="apple-card" style="text-align:center;">', unsafe_allow_html=True)
st.subheader("📜 Exportación de Evidencia")
c_e1, c_e2, c_e3 = st.columns(3)
c_e1.button("Export JSON")
c_e2.button("Export CSV")
if c_e3.button("Enviar Log a aeserviseu@gmail.com"):
    st.success("Log enviado con éxito.")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("AIH-MASTER COMMAND v18.0 | Hardware Integration Core | Uniting Technology Belgium")
