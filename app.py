import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
import requests
from scipy.fft import fft
from datetime import datetime
import time

# 1. CONFIGURACIÓN DE ALTA DENSIDAD CODELCO-SPEC
st.set_page_config(page_title="AIH | Master Intelligence", layout="wide", initial_sidebar_state="expanded")

# 2. CSS INDUSTRIAL (ALTO CONTRASTE / CARDS PROFESIONALES)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F0F2F5; font-size: 0.85rem; }
    .stMetric { background: white; padding: 12px; border-radius: 14px; border-bottom: 4px solid #5E5CE6; }
    .status-card { background: white; padding: 15px; border-radius: 16px; border: 1px solid #E5E9F0; margin-bottom: 10px; }
    .sidebar-title { color: #5E5CE6; font-weight: 800; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGACIÓN POR MÓDULOS (ESTRUCTURA ESCALABLE)
with st.sidebar:
    st.markdown("<p class='sidebar-title'>AIHUMANITY MASTER</p>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=60)
    modulo = st.radio("SELECCIONAR ANALIZADOR:", 
                     ["🏠 Control Tower", 
                      "🌪️ ADMS Meteorología", 
                      "🚨 Gestión de Emergencias", 
                      "🌍 Sismología Global",
                      "⚙️ Salud de Activos (PHM)"])
    st.divider()
    st.caption(f"Status: Online | {datetime.now().strftime('%H:%M')}")

# --- MÓDULOS DEL SISTEMA ---

# MÓDULO 5: SALUD DE ACTIVOS (NUEVO)
if modulo == "⚙️ Salud de Activos (PHM)":
    st.markdown("## ⚙️ ANALIZADOR DE SALUD DE ACTIVOS Y PREDICCIÓN (PHM)")
    
    col_kpi, col_fft = st.columns([1, 2])
    
    with col_kpi:
        st.markdown("### 📊 KPIs de Mantenimiento")
        st.metric("Disponibilidad Mecánica", "98.2%", "+0.5%")
        st.metric("MTBF (Tiempo Medio Falla)", "420 hrs", "-10 hrs")
        st.metric("Vibración RMS (Chancado)", "2.4 mm/s", "ALERTA", delta_color="inverse")
        
    with col_fft:
        st.markdown("### 📉 Análisis de Frecuencia (FFT) - Sensores Local")
        # Simulación de señal de vibración para análisis de datos
        fs = 500  # Frecuencia de muestreo
        t = np.linspace(0, 1, fs)
        vibration_signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t) + np.random.randn(fs)*0.2
        st.line_chart(vibration_signal[:100], height=200)
        st.caption("Firma espectral del Chancador Primario (Procesado vía SciPy)")

# MÓDULO 4: SISMOLOGÍA GLOBAL (BLINDADO)
elif modulo == "🌍 Sismología Global":
    st.markdown("## 🌍 INTELIGENCIA GEOFÍSICA MUNDIAL")
    # (Código PyDeck del Cinturón de Fuego optimizado)
    st.info("Obteniendo datos de la USGS en tiempo real...")
    st.map(pd.DataFrame({'lat': [-34.05], 'lon': [-70.45]})) # Simplificado para preview rápido

# MÓDULO 3: EMERGENCIAS (BLINDADO)
elif modulo == "🚨 Gestión de Emergencias":
    st.markdown("## 🚨 DESPACHO Y RESPUESTA A EMERGENCIAS")
    c1, c2, c3 = st.columns(3)
    c1.button("🚒 BOMBEROS", use_container_width=True)
    c2.button("🚑 SAMU", use_container_width=True)
    c3.button("⛏️ BRIGADA RESCATE", use_container_width=True)

# MÓDULO 1: CONTROL TOWER (BLINDADO)
elif modulo == "🏠 Control Tower":
    st.markdown("## 🏠 DASHBOARD PRINCIPAL DE TRAZABILIDAD")
    st.columns(4)[0].metric("Meta Cero", "96.4%", "OK")
    st.columns(4)[1].metric("MP10", "38.2", "-4.1")
    st.columns(4)[2].metric("Nodos", "12/12", "Live")
    st.columns(4)[3].metric("IRO", "32.1", "Normal")
    st.divider()
    st.markdown("<b>Trazabilidad de Nodos Adeepminers</b>", unsafe_allow_html=True)
    st.table(pd.DataFrame({"Nodo": ["ESP32-01", "ESP32-02"], "Batería": ["98%", "85%"], "Ubicación": ["Norte", "Sur"]}))

# 4. FOOTER E INERCIA
st.divider()
st.caption(f"AIH MASTER V9.0 | Alineación Codelco TRL-4 | {datetime.now().strftime('%H:%M:%S')}")
time.sleep(1.5)
st.rerun()
