import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import time

# --- 1. CONFIGURACIÓN DE IDENTIDAD AIH-MASTER ---
if 'lang' not in st.session_state: st.session_state.lang = "EN"
if 'auth' not in st.session_state: st.session_state.auth = False

# Traducciones Reactivas
L = {
    "EN": {"title": "AIHumanity | PRO-POWER CONTROL", "icr": "RISK INDEX (ICR)", "dust": "DUST PM10", "wind": "WIND SPEED", "wave": "NEURAL RISK WAVEFORM"},
    "ES": {"title": "AIHumanity | CONTROL PRO-POWER", "icr": "ÍNDICE DE RIESGO (ICR)", "dust": "POLVO PM10", "wind": "VEL. VIENTO", "wave": "ONDA NEURAL DE RIESGO"}
}[st.session_state.lang]

st.set_page_config(page_title=L['title'], layout="wide")

# --- 2. DISEÑO HIGH-CONTRAST (CUPERTINO WHITE) ---
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFFFF !important; color: #000000 !important; }
    [data-testid="stSidebar"] { background-color: #F8F9FA !important; border-right: 2px solid #000; }
    .stMetric { background: #FFF !important; border: 3px solid #000 !important; box-shadow: 8px 8px 0px #000; padding: 15px; }
    div[data-testid="stMetricValue"] { color: #D35400 !important; font-weight: 800; font-size: 3rem; }
    .status-bar { background: #000; color: #FFF; padding: 10px; display: flex; justify-content: space-around; font-weight: bold; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE INTELIGENCIA (SCIKIT-LEARN) ---
# Explotamos Isolation Forest para detectar anomalías en los 70k nodos
class AIH_Predictor:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.scaler = StandardScaler()

    def get_risk_score(self, data):
        if len(data) < 10: return 100.0
        scaled_data = self.scaler.fit_transform(data[['val1', 'val2']])
        self.model.fit(scaled_data)
        scores = self.model.decision_function(scaled_data[-1:])
        return max(0, min(100, 100 + (scores[0] * 100)))

# --- 4. PORTAL DE ACCESO (GATEWAY) ---
if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center; border: 4px solid #000; padding: 20px;'>GATEWAY UNLOCKED | AIH-MASTER</h1>", unsafe_allow_html=True)
    role = st.selectbox("SELECT ROLE", ["Operator", "Administrator"])
    pwd = st.text_input("AUTHORIZATION KEY", type="password")
    if st.button("EXECUTE ACCESS"):
        if (role == "Operator" and pwd == "1234") or (role == "Administrator" and pwd == "Admin"):
            st.session_state.auth = True; st.session_state.role = role; st.rerun()
    st.stop()

# --- 5. DASHBOARD DINÁMICO (PLOTLY EXPLOTATION) ---
st.sidebar.radio("🌐 LANGUAGE", ["EN", "ES"], key="lang", index=0 if st.session_state.lang == "EN" else 1)

st.markdown(f"<div class='status-bar'><span>CONNECTIVITY: 100%</span><span>TRAFFIC: 18.5 GB/s</span><span>NODES: 70,000 ACTIVE</span></div>", unsafe_allow_html=True)
st.title(f"📊 {L['title']}")

# Generación de Datos Sintéticos para Simular los 70k Nodos
if 'buffer' not in st.session_state:
    st.session_state.buffer = pd.DataFrame(columns=['val1', 'val2', 'Time'])

new_data = {'val1': np.random.normal(20, 2), 'val2': np.random.normal(150, 15), 'Time': datetime.now().strftime('%H:%M:%S')}
st.session_state.buffer = pd.concat([st.session_state.buffer, pd.DataFrame([new_data])]).tail(40)

# Cálculo ICR vía Machine Learning
engine = AIH_Predictor()
icr_val = engine.get_risk_score(st.session_state.buffer)

# Métricas de Alta Visibilidad
c1, c2, c3 = st.columns(3)
c1.metric(L['icr'], f"{icr_val:.1f}%")
c2.metric(L['dust'], f"{new_data['val2']:.1f} µg/m³")
c3.metric(L['wind'], "14.2 KM/H")

# --- ONDAS DE RIESGO (PLOTLY ENGINE) ---
st.subheader(L['wave'])
fig = go.Figure()
fig.add_trace(go.Scatter(x=st.session_state.buffer['Time'], y=st.session_state.buffer['val2'],
                         mode='lines+markers', line=dict(color='#000000', width=3), name="PM10 Pulse"))
fig.add_trace(go.Scatter(x=st.session_state.buffer['Time'], y=st.session_state.buffer['val1']*5,
                         mode='lines', line=dict(color='#D35400', width=4, dash='dot'), name="Stability Index"))

fig.update_layout(plot_bgcolor='white', paper_bgcolor='white', margin=dict(l=20, r=20, t=20, b=20),
                  xaxis=dict(showgrid=True, gridcolor='#EEE'), yaxis=dict(showgrid=True, gridcolor='#EEE'))
st.plotly_chart(fig, use_container_width=True)



# Auto-refresh cada 2 segundos
time.sleep(2)
st.rerun()
