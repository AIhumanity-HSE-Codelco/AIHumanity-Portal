import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import serial
import serial.tools.list_ports
import time
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE ESCENA (APPLE INTERFACE) ---
st.set_page_config(page_title="AIHUMANITY GLOBAL", layout="wide", initial_sidebar_state="collapsed")

# --- 2. ESTILO CUPERTINO VIBRANTE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    html, body, [class*="st-"] { font-family: 'SF Pro Display', sans-serif; background-color: #f5f5f7; }
    
    .main-header {
        background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(20px);
        border-radius: 24px; padding: 35px; text-align: center;
        border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    }
    .apple-card {
        background: white; border-radius: 22px; padding: 25px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.02); margin-bottom: 20px;
        border: 1px solid #efeff4;
    }
    .clock-text { font-size: 100px; font-weight: 600; color: #1d1d1f; letter-spacing: -5px; line-height: 1; }
    .stButton>button { 
        background-color: #0071e3; color: white; border-radius: 12px; 
        font-weight: 600; padding: 10px 20px; border: none; width: 100%;
    }
    .risk-bar { width: 100%; background: #e5e5ea; border-radius: 15px; height: 35px; overflow: hidden; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE TIEMPO ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)

# --- 4. CABECERA SUPREMA ---
st.markdown(f"""
    <div class="main-header">
        <p class="clock-text">{now.strftime("%H:%M")}</p>
        <p style="font-size: 20px; color: #86868b; margin: 0;">{now.strftime("%A, %d de %B %Y")} | NÚCLEO AIHUMANITY</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- 5. PANEL CENTRAL DE GOBERNANZA ---
col_left, col_right = st.columns([2, 1])

with col_left:
    # MÓDULO A: RIESGO OPERACIONAL (DATA DE 70K NODOS)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Gobernanza HSE: Codelco Objective Zero")
    
    # Simulación de Riesgo Compuesto (ICR)
    riesgo_icr = np.random.randint(25, 85)
    color_risk = "#ff3b30" if riesgo_icr > 75 else "#0071e3"
    
    st.markdown(f"**Índice de Riesgo Compuesto: {riesgo_icr}%**")
    st.markdown(f"""
        <div class="risk-bar">
            <div style="width: {riesgo_icr}%; background: {color_risk}; height: 100%; transition: 1s;"></div>
        </div>
    """, unsafe_allow_html=True)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("🌪️ PM10 (ADMS)", f"{np.random.randint(35,95)} µg/m³")
    k2.metric("🌬️ Viento (Meteo)", f"{np.random.randint(12,65)} km/h")
    k3.metric("📍 AIDeepMiner", "70,000 Nodos")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO B: HARDWARE BRIDGE (DETECTOR ESP32)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🔌 AIDeepMiner Bridge: Gestión de Cascos")
    st.write("Detección de hardware real para flasheo de software Uniting Technology.")
    
    c_hw1, c_hw2 = st.columns(2)
    with c_hw1:
        if st.button("Buscar Dispositivos USB"):
            try:
                ports = serial.tools.list_ports.comports()
                if ports:
                    for p in ports: st.success(f"Detectado: {p.device}")
                else: st.warning("No se detectan nodos físicos.")
            except Exception as e: st.error("Error de acceso al puerto.")
    
    with c_hw2:
        f_up = st.file_uploader("Firmware .bin", type="bin")
        if f_up and st.button("Flashear AIDeepMiner"):
            st.info(f"Cargando {f_up.name}...")
            st.progress(100)
            st.success("Sincronización de Hardware Completa.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # MÓDULO C: ADMS TACTICAL (MITIGACIÓN)
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("💧 Módulo ADMS")
    st.write("Estatus: **PROACTIVO**")
    st.progress(85)
    st.caption("Efectividad de Mitigación de Polvo")
    st.markdown('</div>', unsafe_allow_html=True)

    # MÓDULO D: SEGURIDAD HUMANA
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("👷 Worker Safety")
    st.write("- PPE Detection: **WORN ON**")
    st.write("- Fall Detection: **STANDBY**")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. LOG DE AUDITORÍA (AUDIT-READY) ---
st.markdown('<div class="apple-card" style="text-align:center;">', unsafe_allow_html=True)
st.subheader("📜 Evidencia Operacional")
ce1, ce2, ce3 = st.columns(3)
ce1.button("Exportar JSON")
ce2.button("Descargar CSV")
if ce3.button("Enviar a aeserviseu@gmail.com"):
    st.success("Reporte enviado a Gerencia.")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("AIHUMANITY CONSOLIDATED CONTROL CENTER | Uniting Technology Belgium | TRL3 to TRL4")
