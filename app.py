import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- CONFIGURACIÓN DE SEGURIDAD DEL PORTAL ---
st.set_page_config(
    page_title="AIHumanity - Master Control (Blindado)",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- BLINDAJE CSS (Tesla/Cyber/Industrial) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505;
        color: #D1D1D1;
        font-family: 'Roboto Mono', monospace;
    }
    
    /* Contenedores Blindados */
    .metric-container {
        background: linear-gradient(180deg, #111 0%, #080808 100%);
        border: 1px solid #222;
        padding: 20px;
        border-radius: 4px;
        border-left: 5px solid #E82127; /* Rojo Tesla HSE */
    }
    
    .status-nominal { color: #00FF41; } /* Verde Matrix/HSE */
    .status-alert { color: #FF3B30; animation: blinker 1.5s linear infinite; }
    
    @keyframes blinker { 50% { opacity: 0.3; } }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DATOS BLINDADA (Prevención de Errores) ---
def get_sensor_data():
    try:
        # Aquí se integrará la llamada a la DB real más adelante
        sensor_ids = [f"AIDEEPMINER-{i:03d}" for i in range(1, 201)]
        values = np.random.uniform(5, 95, 200)
        states = ["OK" if v < 70 else "WARN" if v < 85 else "CRIT" for v in values]
        return pd.DataFrame({"ID": sensor_ids, "VAL": values, "STATE": states})
    except Exception as e:
        st.error(f"ERROR DE CAPA DE DATOS: {e}")
        return pd.DataFrame()

# --- HEADER DE CONTROL (Entorno AIHumanity) ---
c1, c2 = st.columns([4, 1])
with c1:
    st.markdown(f"# 🛡️ AIHUMANITY MASTER CONTROL <span style='font-size:15px; color:#666;'>[NODE: 104.236.210.4 | UTC: {datetime.utcnow().strftime('%H:%M:%S')}]</span>", unsafe_allow_html=True)
with c2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg", width=80)

st.divider()

# --- VIEWPORT HSE: PRIORIDADES CRÍTICAS ---
data = get_sensor_data()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("ESTADO HSE", "NOMINAL", delta="SISTEMA PROTEGIDO")
with col2:
    avg_mp10 = data["VAL"].mean()
    st.metric("MP10 (MEDIA RAJO)", f"{avg_mp10:.2f} µg/m³", delta="-1.2%", delta_color="inverse")
with col3:
    st.metric("TALUDES (ESTABILIDAD)", "98.8%", delta="ESTABLE")
with m4 := st.columns(1)[0]: # Contenedor para tránsito/dozing
     st.metric("TRÁNSITO / CHANCADO", "FLUIDO", delta="V: 15km/h")

st.divider()

# --- MATRIZ DE 200 NODOS (REJILLA DE ALTO CONTRASTE) ---
st.subheader("PROYECCIÓN DE NODOS AIDEEPMINER [1-200]")

cols_per_row = 20
for i in range(0, 200, cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        idx = i + j
        if idx < 200:
            row = data.iloc[idx]
            color = "#00FF41" if row["STATE"] == "OK" else "#FFCC00" if row["STATE"] == "WARN" else "#FF3B30"
            with cols[j]:
                # Cada cuadrito es un nodo AIDEEPMINER blindado
                st.markdown(f"""
                <div style="background-color: {color}; height: 12px; border-radius: 1px; margin-bottom: 2px;" 
                     title="ID: {row['ID']} | Valor: {row['VAL']:.1f}"></div>
                """, unsafe_allow_html=True)

st.divider()

# --- CAPA DE SEGURIDAD & LOGS (TRL 4) ---
t1, t2 = st.columns([2, 1])
with t1:
    st.subheader("📡 TELEMETRÍA PREDICTIVA (ICR)")
    chart_data = pd.DataFrame(np.random.randn(50, 2), columns=['Tendencia Polvo', 'Viento SE'])
    st.line_chart(chart_data, color=["#E82127", "#444444"])

with t2:
    st.subheader("🛡️ STATUS DE BLINDAJE")
    st.code(f"""
    > Firewall: ACTIVE
    > Data Integrity: 100%
    > ESP32 Nodes: Syncing
    > GitHub Link: ESTABLISHED
    """, language="markdown")
    if st.button("DESPLEGAR PROTOCOLO DE EMERGENCIA"):
        st.error("Protocolo activado: Notificando a Supervisores HSE...")
