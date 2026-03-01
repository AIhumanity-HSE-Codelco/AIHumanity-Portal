import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- 1. GLOBAL LANGUAGE ENGINE ---
if 'lang' not in st.session_state:
    st.session_state.lang = "EN"

translations = {
    "EN": {
        "title": "AIHumanity | HSE | CONTROL CENTER",
        "welcome": "SYSTEM GATEWAY",
        "sub": "Secure Mining Operations - TRL 4 Protocol",
        "op_btn": "OPERATOR ACCESS",
        "ad_btn": "ADMINISTRATOR ACCESS",
        "pass_label": "Authorization Key",
        "status": "CONNECTIVITY: GLOBAL-NET",
        "traffic": "DATA TRAFFIC",
        "wind": "WIND SPEED",
        "temp": "ENV. TEMP",
        "hse_status": "HSE RISK LEVEL",
        "secure": "SECURE / NOMINAL",
        "logout": "TERMINATE SESSION",
        "diag": "Neural Diagnostic Center",
        "nodes": "ACTIVE NODES (70k)",
        "wave": "Real-Time Risk Waveform",
        "audit": "AI AUDIT LOG"
    },
    "ES": {
        "title": "AIHumanity | HSE | CENTRO DE CONTROL",
        "welcome": "PORTAL DEL SISTEMA",
        "sub": "Operaciones Mineras Seguras - Protocolo TRL 4",
        "op_btn": "ACCESO OPERADOR",
        "ad_btn": "ACCESO ADMINISTRADOR",
        "pass_label": "Clave de Autorización",
        "status": "CONECTIVIDAD: RED-GLOBAL",
        "traffic": "TRÁFICO DE DATOS",
        "wind": "VEL. VIENTO",
        "temp": "TEMP. AMB.",
        "hse_status": "NIVEL RIESGO HSE",
        "secure": "SEGURO / NOMINAL",
        "logout": "CERRAR SESIÓN",
        "diag": "Centro de Diagnóstico Neuronal",
        "nodes": "NODOS ACTIVOS (70k)",
        "wave": "Ondas de Riesgo en Tiempo Real",
        "audit": "REGISTRO DE AUDITORÍA IA"
    }
}

L = translations[st.session_state.lang]

# --- 2. PAGE CONFIG & CUPERTINO BLACK THEME ---
st.set_page_config(page_title=L['title'], layout="wide", initial_sidebar_state="expanded")

def apply_industrial_design():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
    
    /* Pure Black Background */
    html, body, [class*="css"], [data-testid="stAppViewContainer"] {{ 
        font-family: 'SF Pro Display', sans-serif; 
        background-color: #000000 !important; 
        color: #FFFFFF !important; 
    }}

    /* Sidebar - Cupertino Dark */
    [data-testid="stSidebar"] {{
        background-color: #050505 !important;
        border-right: 1px solid #222;
    }}

    /* Metrics - Glassmorphism */
    div[data-testid="stMetricValue"] {{ color: #FF6B00 !important; font-weight: bold; font-size: 2.5rem; }}
    div[data-testid="stMetricLabel"] {{ color: #888888 !important; text-transform: uppercase; letter-spacing: 1px; }}
    
    .stMetric {{
        background: rgba(20, 20, 20, 0.8);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 20px;
    }}

    /* Gateway Container */
    .gateway-container {{
        border: 2px solid #FF6B00;
        border-radius: 20px;
        padding: 40px;
        background: #080808;
        text-align: center;
        margin-top: 10%;
    }}

    /* Status Bar */
    .status-bar {{
        background: #000;
        padding: 10px 25px;
        border-radius: 8px;
        border-bottom: 2px solid #FF6B00;
        display: flex;
        justify-content: space-between;
        margin-bottom: 25px;
        color: #FF6B00;
        font-weight: 600;
        font-size: 0.85rem;
    }}
    </style>
    """, unsafe_allow_html=True)

apply_industrial_design()

# --- 3. LANGUAGE SELECTOR (Reactive Sidebar) ---
st.sidebar.title("⚙️ CONFIG")
st.session_state.lang = st.sidebar.radio("LANGUAGE / IDIOMA", ["EN", "ES"], 
                                         index=0 if st.session_state.lang == "EN" else 1)

# --- 4. SECURITY GATEWAY ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
    st.session_state.role = None

if not st.session_state.auth:
    st.markdown(f"""
    <div class='gateway-container'>
        <h1 style='color:#FF6B00;'>{L['welcome']}</h1>
        <p style='color:#666;'>{L['sub']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_op, col_ad = st.columns(2)
    
    with col_op:
        st.subheader(L['op_btn'])
        op_pass = st.text_input(L['pass_label'], type="password", key="op_p")
        if st.button("UNLOCK OPERATOR"):
            if op_pass == "1234":
                st.session_state.role = "Operator"; st.session_state.auth = True; st.rerun()
            else: st.error("Access Denied")

    with col_ad:
        st.subheader(L['ad_btn'])
        ad_pass = st.text_input(L['pass_label'], type="password", key="ad_p")
        if st.button("UNLOCK ADMINISTRATOR"):
            if ad_pass == "Admin":
                st.session_state.role = "Admin"; st.session_state.auth = True; st.rerun()
            else: st.error("Access Denied")
    st.stop()

# --- 5. DASHBOARD MAIN INTERFACE ---
st.markdown(f"""
<div class='status-bar'>
    <span>{L['status']}</span>
    <span>{L['traffic']}: 8.4 GB/s</span>
    <span>{L['wind']}: 18 KM/H NE</span>
    <span>{L['temp']}: 24°C</span>
    <span>🕒 {datetime.now().strftime('%H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

if st.session_state.role == "Operator":
    st.title(f"🛡️ {L['title']}")
    st.subheader(f"ROLE: {st.session_state.role}")
    
    c1, c2, c3 = st.columns(3)
    c1.metric(L['hse_status'], L['secure'])
    c2.metric("PM 10 (Dust)", "12.8 µg/m³", "-1.4")
    c3.metric("PM 2.5 (Dust)", "4.9 µg/m³", "0.1")
    
    st.subheader(L['wave'])
    st.line_chart(np.random.randn(30, 2), color=["#FF6B00", "#444444"])

else:
    st.title(f"🛠️ {L['diag']}")
    st.sidebar.warning("ADMIN PRIVILEGES: GRANTED")
    
    c_diag, c_nodes = st.columns([1, 2])
    with c_diag:
        st.write(f"### {L['audit']}")
        st.code(f"OpenAI Core: Connected\nESP32 Sync: 100%\nLatency: 8ms\nProtocol: ICR-Predictive")
    with c_nodes:
        st.write(f"### {L['nodes']}")
        st.progress(98)
        st.area_chart(np.random.randn(20, 1), color=["#FF6B00"])

if st.sidebar.button(L['logout']):
    st.session_state.auth = False; st.rerun()
