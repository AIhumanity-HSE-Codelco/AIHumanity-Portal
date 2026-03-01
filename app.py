import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import time

# --- 1. CONFIGURACIÓN DE PÁGINA (MODO DIRECTO) ---
st.set_page_config(page_title="AIHumanity | HSE | DIRECT CONTROL", layout="wide")

# Diseño High-Contrast White (Brutalismo Industrial)
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    .stMetric { background: #FFF !important; border: 4px solid #000 !important; box-shadow: 10px 10px 0px #000; padding: 20px; }
    div[data-testid="stMetricValue"] { color: #D35400 !important; font-weight: 900; font-size: 3.5rem; }
    .status-bar { background: #000; color: #FFF; padding: 12px; display: flex; justify-content: space-around; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 2. BARRA DE ESTADO GLOBAL ---
st.markdown(f"<div class='status-bar'><span>MODO: ACCESO DIRECTO</span><span>RED: 70,000 NODOS</span><span>TRÁFICO: 22.4 GB/s</span><span>🕒 {datetime.now().strftime('%H:%M:%S')}</span></div>", unsafe_allow_html=True)

# --- 3. PROCESAMIENTO DE IA (ISOLATION FOREST) ---
if 'buffer' not in st.session_state:
    st.session_state.buffer = pd.DataFrame(columns=['temp', 'dust', 'Time'])

# Simulación de Ingesta Continua
new_data = {'temp': 22.0 + np.random.normal(0, 1), 'dust': 145 + np.random.normal(0, 10), 'Time': datetime.now().strftime('%H:%M:%S')}
st.session_state.buffer = pd.concat([st.session_state.buffer, pd.DataFrame([new_data])]).tail(50)

# Motor de Riesgo (ICR)
scaler = StandardScaler()
model = IsolationForest(contamination=0.05)
if len(st.session_state.buffer) > 10:
    X = scaler.fit_transform(st.session_state.buffer[['temp', 'dust']])
    model.fit(X)
    score = model.decision_function(X[-1:])
    icr = max(0, min(100, 100 + (score[0] * 100)))
else:
    icr = 100.0

# --- 4. PANEL DE MÉTRICAS CRÍTICAS ---
st.title("🛡️ AIHUMANITY | HSE | MASTER MONITOR")

c1, c2, c3 = st.columns(3)
c1.metric("ÍNDICE ICR", f"{icr:.1f}%")
c2.metric("POLVO PM10", f"{new_data['dust']:.1f} µg/m³")
c3.metric("TEMPERATURA", f"{new_data['temp']:.2f} °C")

# --- 5. ONDAS NEURALES DE ALTA DEFINICIÓN ---
fig = go.Figure()
fig.add_trace(go.Scatter(x=st.session_state.buffer['Time'], y=st.session_state.buffer['dust'],
                         mode='lines+markers', line=dict(color='#000000', width=4), name="Pulso MP10"))
fig.add_trace(go.Scatter(x=st.session_state.buffer['Time'], y=st.session_state.buffer['temp']*5,
                         mode='lines', line=dict(color='#D35400', width=3, dash='dot'), name="Tendencia Térmica"))

fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=10, r=10, t=10, b=10),
                  xaxis=dict(showgrid=True, gridcolor='#DDD'), yaxis=dict(showgrid=True, gridcolor='#DDD'))
st.plotly_chart(fig, use_container_width=True)

time.sleep(1)
st.rerun()
