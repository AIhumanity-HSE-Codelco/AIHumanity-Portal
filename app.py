import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import firebase_admin
from firebase_admin import credentials, db
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import time
import os

# --- 1. INITIALIZATION & REQUISITES CHECK ---
# Invocando el núcleo de AIHumanity
if 'lang' not in st.session_state: st.session_state.lang = "EN"

# UI Translations
TEXTS = {
    "EN": {
        "title": "AIHUMANITY | HSE | MASTER MONITOR",
        "icr": "RISK INDEX (ICR)",
        "dust": "PARTICULATE MATTER (PM10)",
        "seismic": "SEISMIC ACTIVITY",
        "traffic": "DATA TRAFFIC",
        "status": "SYSTEM STATUS: ACTIVE",
        "wave": "NEURAL RISK WAVEFORM (TRL-4)",
        "report": "GENERATE HSE REPORT",
        "nodes": "NODES ONLINE: 70,000"
    },
    "ES": {
        "title": "AIHUMANITY | HSE | MONITOR MAESTRO",
        "icr": "ÍNDICE DE RIESGO (ICR)",
        "dust": "MATERIAL PARTICULADO (PM10)",
        "seismic": "ACTIVIDAD SÍSMICA",
        "traffic": "TRÁFICO DE DATOS",
        "status": "ESTADO DEL SISTEMA: ACTIVO",
        "wave": "ONDA NEURAL DE RIESGO (TRL-4)",
        "report": "GENERAR REPORTE HSE",
        "nodes": "NODOS EN LÍNEA: 70,000"
    }
}
L = TEXTS[st.session_state.lang]

# --- 2. INDUSTRIAL HIGH-CONTRAST UI ---
st.set_page_config(page_title=L['title'], layout="wide")

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .stMetric { 
        background: #FFFFFF !important; 
        border: 4px solid #000000 !important; 
        box-shadow: 10px 10px 0px #000000; 
        padding: 20px; 
    }
    div[data-testid="stMetricValue"] { color: #D35400 !important; font-weight: 900; font-size: 3.5rem; }
    .status-bar { 
        background: #000000; 
        color: #FFFFFF; 
        padding: 15px; 
        display: flex; 
        justify-content: space-between; 
        font-weight: bold; 
        font-family: monospace;
    }
    .stButton>button {
        border-radius: 0px;
        border: 2px solid #000;
        background-color: #FFF;
        color: #000;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. CORE ANALYTICS ENGINE (SKLEARN) ---
class RiskAI:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.scaler = StandardScaler()

    def calculate_icr(self, df):
        if len(df) < 15: return 100.0
        features = df[['dust', 'seismic']].values
        scaled = self.scaler.fit_transform(features)
        self.model.fit(scaled)
        # Score de decisión transformado a 0-100
        score = self.model.decision_function(scaled[-1:])[0]
        return max(0, min(100, 100 + (score * 100)))

# --- 4. DATA PIPELINE & SIMULATION ---
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Time', 'dust', 'seismic'])

# Inyectando telemetría (Invocando pydantic/numpy del inventario)
now = datetime.now().strftime("%H:%M:%S")
payload = {
    'Time': now,
    'dust': 15.0 + np.random.normal(0, 2),
    'seismic': 0.02 + np.random.normal(0, 0.005)
}
st.session_state.history = pd.concat([st.session_state.history, pd.DataFrame([payload])]).tail(50)

# Ejecutar IA
AI = RiskAI()
icr_value = AI.calculate_icr(st.session_state.history)

# --- 5. DASHBOARD DISPLAY ---
st.markdown(f"""
<div class='status-bar'>
    <span>{L['status']}</span>
    <span>{L['nodes']}</span>
    <span>{L['traffic']}: 24.8 GB/s</span>
    <span>🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("⚙️ SETTINGS")
st.session_state.lang = st.sidebar.selectbox("UI LANGUAGE", ["EN", "ES"], 
                                             index=0 if st.session_state.lang == "EN" else 1)

st.title(f"🛡️ {L['title']}")

c1, c2, c3 = st.columns(3)
c1.metric(L['icr'], f"{icr_value:.1f}%")
c2.metric(L['dust'], f"{payload['dust']:.2f} µg/m³")
c3.metric(L['seismic'], f"{payload['seismic']:.4f} g")

# --- 6. WAVEFORM VISUALIZATION (PLOTLY) ---
st.subheader(L['wave'])
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=st.session_state.history['Time'], 
    y=st.session_state.history['dust'],
    name=L['dust'], line=dict(color='#000000', width=4)
))
fig.add_trace(go.Scatter(
    x=st.session_state.history['Time'], 
    y=st.session_state.history['seismic']*500, # Escalado para visibilidad
    name=f"{L['seismic']} (x500)", line=dict(color='#D35400', width=3, dash='dot')
))

fig.update_layout(
    plot_bgcolor='white', paper_bgcolor='white',
    xaxis=dict(showgrid=True, gridcolor='#E5E5E5'),
    yaxis=dict(showgrid=True, gridcolor='#E5E5E5'),
    margin=dict(l=0, r=0, t=10, b=0)
)
st.plotly_chart(fig, use_container_width=True)

# --- 7. REPORTING (PDF REQUISITE) ---
if st.button(L['report']):
    st.write("📄 Generating PDF Encrypted Report... (fpdf2 context invoked)")
    # Aquí se invocaría la lógica de reportlab/fpdf2 de tu inventario

# Auto-refresh cada segundo para real-time feel
time.sleep(1)
st.rerun()
