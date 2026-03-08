import streamlit as st
import pandas as pd
import numpy as np
import time

# Configuración de página - Alto Contraste / Modo Oscuro
st.set_page_config(page_title="AIHumanity HSE Master Control", layout="wide")

# Estilo CSS para forzar fondo oscuro y colores industriales
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    .stMetric { background-color: #1E1E1E; padding: 15px; border-radius: 10px; border: 1px solid #333; }
    .status-nominal { color: #00FF00; font-weight: bold; }
    .status-alert { color: #FF0000; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: ESTADO DE CONECTIVIDAD ---
with st.sidebar:
    st.header("🌐 DIAGNÓSTICO")
    st.info("IP Servidor: 104.236.210.4")
    st.success("CONECTIVIDAD: ESTABLE")
    st.divider()
    view_mode = st.radio("VISTA", ["Operador Simple", "Admin Diagnóstico"])

# --- HEADER PRINCIPAL ---
st.title("🛡️ AIHUMANITY MASTER CONTROL")
col_hse, col_mp10, col_mp25 = st.columns(3)

with col_hse:
    st.metric(label="ESTADO HSE", value="NOMINAL", delta="ESTABLE")
with col_mp10:
    st.metric(label="MP10 PROM.", value="42 µg/m³", delta="-2.1")
with col_mp25:
    st.metric(label="MP2.5 PROM.", value="18 µg/m³", delta="+0.5")

st.divider()

# --- VIEWPORT CENTRAL: ANALIZADORES 1-200 ---
st.subheader("📊 MATRIZ DE ANALIZADORES (TRL 4)")

# Simulación de datos para los 200 nodos
data = pd.DataFrame({
    'ID': [f"AN-{i:03d}" for i in range(1, 201)],
    'MP10': np.random.uniform(20, 60, 200).round(2),
    'Estado': np.random.choice(['Verde', 'Amarillo', 'Rojo'], 200, p=[0.85, 0.10, 0.05])
})

# Grid de visualización
rows = 10
cols = 20
for r in range(rows):
    cols_grid = st.columns(cols)
    for c in range(cols):
        idx = r * cols + c
        if idx < 200:
            sensor = data.iloc[idx]
            color = "#00FF00" if sensor['Estado'] == 'Verde' else "#FFFF00" if sensor['Estado'] == 'Amarillo' else "#FF0000"
            cols_grid[c].markdown(f"""
                <div style="background-color: {color}; height: 10px; border-radius: 2px; margin-bottom: 2px;" title="{sensor['ID']}: {sensor['MP10']} µg/m³"></div>
            """, unsafe_allow_html=True)

# --- DETALLE TÉCNICO ---
if view_mode == "Admin Diagnóstico":
    st.divider()
    st.subheader("⚙️ VARIABLES CRÍTICAS & TALUDES")
    c1, c2, c3 = st.columns(3)
    c1.write("**Erosión/Raveling:** Detectado en Sector Sur")
    c2.write("**Viento:** 12 km/h - Dir: NE")
    c3.write("**Buffer DB:** 98% Libre")
