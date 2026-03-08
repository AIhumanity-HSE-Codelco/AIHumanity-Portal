import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- CONFIGURACIÓN DE SEGURIDAD ---
st.set_page_config(
    page_title="AIHumanity - Master Control",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- BLINDAJE CSS (Tesla/Industrial Dark) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505;
        color: #D1D1D1;
        font-family: 'Roboto Mono', monospace;
    }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; font-size: 32px !important; }
    [data-testid="stMetricLabel"] { color: #888 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIÓN DE DATOS ---
def get_sensor_data():
    sensor_ids = [f"AIDEEPMINER-{i:03d}" for i in range(1, 201)]
    values = np.random.uniform(5, 95, 200)
    states = ["OK" if v < 70 else "WARN" if v < 85 else "CRIT" for v in values]
    return pd.DataFrame({"ID": sensor_ids, "VAL": values, "STATE": states})

# --- HEADER AIHUMANITY ---
st.markdown(f"# 🛡️ AIHUMANITY MASTER CONTROL <span style='font-size:14px; color:#444;'>| IP: 104.236.210.4 | {datetime.utcnow().strftime('%H:%M:%S')} UTC</span>", unsafe_allow_html=True)
st.divider()

# --- MÉTRICAS HSE (CORREGIDAS) ---
data = get_sensor_data()
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("ESTADO HSE", "NOMINAL", delta="PROTEGIDO")
with col2:
    st.metric("MP10 AVG", f"{data['VAL'].mean():.1f} µg/m³", delta="-1.2%")
with col3:
    st.metric("TALUDES", "98.8%", delta="ESTABLE")
with col4:
    st.metric("TRÁNSITO", "FLUIDO", delta="15 km/h")

st.divider()

# --- MATRIZ DE 200 NODOS ---
st.subheader("RED AIDEEPMINER [NODOS 1-200]")
cols_per_row = 20
for i in range(0, 200, cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        idx = i + j
        if idx < 200:
            row = data.iloc[idx]
            color = "#00FF41" if row["STATE"] == "OK" else "#FFCC00" if row["STATE"] == "WARN" else "#FF3B30"
            cols[j].markdown(f'<div style="background-color: {color}; height: 12px; border-radius: 1px; margin-bottom: 2px;" title="{row["ID"]}"></div>', unsafe_allow_html=True)

st.divider()

# --- FOOTER TÉCNICO ---
t1, t2 = st.columns([2, 1])
with t1:
    st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Polvo', 'Viento']), height=150)
with t2:
    st.code("SYSTEM: OPERATIONAL\nNODES: 200/200\nTRL: 4", language="markdown")
