import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- CONFIGURACIÓN DE IDENTIDAD AIH-MASTER ---
st.set_page_config(
    page_title="AIHumanity | HSE Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estética Industrial (CSS Personalizado)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #f0883e !important; font-family: 'Courier New', monospace; }
    .stAlert { background-color: #1b1f23; border: 1px solid #f0883e; color: #e6edf3; }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO DE MISIÓN ---
st.title("🛡️ AIHUMANITY MASTER - SERVIDOR DE OPERACIONES")
st.markdown(f"**Arquitecto Jefe:** Identidad AIH-Master | **Estado:** Monitoreo Activo | **Región:** Atacama/BHP")

# --- SIMULACIÓN DE FLUJO DE DATOS (NÚCLEO DE LA IA) ---
if 'data_buffer' not in st.session_state:
    st.session_state.data_buffer = pd.DataFrame(columns=['Hora', 'Flujo', 'Temperatura', 'Estabilidad'])

def generar_pulso_onda():
    now = datetime.now().strftime("%H:%M:%S")
    # Simulación de telemetría de 70k nodos (ruido gaussiano)
    flujo = 400 + np.random.normal(0, 15)
    temp = 25.5 + np.random.normal(0, 0.5)
    estabilidad = 98.2 + np.random.normal(0, 0.1)
    return {'Hora': now, 'Flujo': flujo, 'Temperatura': temp, 'Estabilidad': estabilidad}

# --- INTERFAZ DE MONITOREO ---
col1, col2, col3, col4 = st.columns(4)

# Actualizar datos del búfer
nuevo_dato = generar_pulso_onda()
st.session_state.data_buffer = pd.concat([st.session_state.data_buffer, pd.DataFrame([nuevo_dato])]).tail(30)

with col1:
    st.metric("NODOS ACTIVOS", "70,000", delta="Sync OK")
with col2:
    st.metric("FLUJO PROMEDIO", f"{nuevo_dato['Flujo']:.1f} lx", delta="-2.1%")
with col3:
    st.metric("TEMP. NÚCLEO", f"{nuevo_dato['Temperatura']:.1f} °C", delta="Estable")
with col4:
    st.metric("ESTABILIDAD RED", f"{nuevo_dato['Estabilidad']:.2f}%", delta="Normal")

# --- GRÁFICO DE ONDAS HSE (EL CORAZÓN DEL SERVIDOR) ---
st.subheader("📈 Análisis de Ondas de Riesgo Preventivo (ICR)")
st.line_chart(st.session_state.data_buffer.set_index('Hora')[['Flujo', 'Temperatura']])

# --- PANEL DE ALERTAS IA ---
st.sidebar.title("LOG DE AUDITORÍA")
if nuevo_dato['Flujo'] > 410:
    st.error("🚨 ALERTA: Pico de radiación detectado en Nivel 4.")
else:
    st.success("✅ Sistema operando bajo parámetros nominales.")

st.sidebar.info(f"Última inyección de datos: {nuevo_dato['Hora']}")

# --- AUTO-REFRESCO (LOOP DEL SERVIDOR) ---
time.sleep(1)
st.rerun()
