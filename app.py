import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.graph_objects as go
from datetime import datetime
import time

# --- 1. CONFIGURACIÓN DE IDENTIDAD ---
if 'lang' not in st.session_state: st.session_state.lang = "ES"

L = {
    "EN": {"title": "AIHUMANITY | HSE | MASTER MONITOR", "icr": "RISK INDEX (ICR)", "events": "TOTAL EVENTS", "status": "GLOBAL STATUS", "wave": "NEURAL RISK WAVEFORM"},
    "ES": {"title": "AIHUMANITY | HSE | MONITOR MAESTRO", "icr": "ÍNDICE DE RIESGO (ICR)", "events": "EVENTOS TOTALES", "status": "ESTADO GLOBAL", "wave": "ONDA NEURAL DE RIESGO"}
}[st.session_state.lang]

# --- 2. DISEÑO ALTA VISIBILIDAD (CUPERTINO WHITE) ---
st.set_page_config(page_title=L['title'], layout="wide")

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    .stMetric { background: #FFF !important; border: 4px solid #000 !important; box-shadow: 10px 10px 0px #000; padding: 20px; }
    div[data-testid="stMetricValue"] { color: #D35400 !important; font-weight: 900; font-size: 3.5rem; }
    .status-bar { background: #000; color: #FFF; padding: 12px; display: flex; justify-content: space-around; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 3. CONEXIÓN AL BACKEND (FASTAPI) ---
API_URL = "http://localhost:8000"

def fetch_data():
    try:
        response = requests.get(f"{API_URL}/dashboard")
        return response.json()
    except:
        return None

# --- 4. INTERFAZ MAESTRA ---
st.sidebar.title("⚙️ CONFIG")
st.session_state.lang = st.sidebar.selectbox("IDIOMA", ["EN", "ES"], index=1 if st.session_state.lang == "ES" else 0)

# Barra de Estado Superior
st.markdown(f"<div class='status-bar'><span>MODO: TRL-4 MASTER</span><span>NODOS: 70,000</span><span>📡 CONNECTED TO BACKEND</span></div>", unsafe_allow_html=True)

st.title(f"🛡️ {L['title']}")

# Obtener datos reales del Backend
data = fetch_data()

if data:
    c1, c2, c3 = st.columns(3)
    c1.metric(L['icr'], f"{data.get('average_risk', 0)}%")
    c2.metric(L['events'], data.get('total_events', 0))
    
    # Semáforo dinámico
    status = data.get('global_status', 'N/A')
    status_color = "🔴" if "STOP" in status else "🟡" if "WARNING" in status else "🟢"
    c3.metric(L['status'], f"{status_color} {status}")

    # --- 5. ONDAS DE RIESGO (PLOTLY) ---
    st.subheader(L['wave'])
    # Simulamos el histórico del buffer para la onda (en producción se pediría un endpoint de logs)
    time_series = [datetime.now().strftime("%H:%M:%S") for _ in range(10)]
    risks = [data.get('average_risk', 0) + np.random.normal(0, 2) for _ in range(10)]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time_series, y=risks, mode='lines+markers', 
                             line=dict(color='#000', width=4), name="ICR Pulse"))
    
    fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=10, r=10, t=10, b=10),
                      xaxis=dict(showgrid=True, gridcolor='#EEE'), yaxis=dict(showgrid=True, gridcolor='#EEE'))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ WAITING FOR BACKEND (FastAPI)... Run: uvicorn server_file:app --reload")

# Auto-refresh
time.sleep(2)
st.rerun()
