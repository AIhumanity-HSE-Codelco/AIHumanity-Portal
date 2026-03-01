import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- 1. MULTI-LANGUAGE ENGINE ---
if 'lang' not in st.session_state:
    st.session_state.lang = "EN"

translations = {
    "EN": {
        "title": "AIHumanity | HSE | CONTROL CENTER",
        "welcome": "SYSTEM GATEWAY",
        "sub": "Secure Mining Operations - TRL 4 High-Visibility Mode",
        "op_access": "OPERATOR ACCESS",
        "ad_access": "ADMINISTRATOR ACCESS",
        "pass_prompt": "Authorization Key",
        "btn_unlock": "UNLOCK SYSTEM",
        "status": "CONNECTIVITY: GLOBAL-NET",
        "traffic": "DATA TRAFFIC",
        "wind": "WIND SPEED",
        "temp": "ENV. TEMP",
        "hse_status": "HSE RISK LEVEL",
        "secure": "SECURE / NOMINAL",
        "logout": "TERMINATE SESSION",
        "diag": "Neural Diagnostic Center",
        "nodes": "ACTIVE NODES (70k)",
        "wave": "Real-Time Risk Waveform (ICR)",
        "pm10": "PM 10 (Dust)",
        "pm25": "PM 2.5 (Dust)"
    },
    "ES": {
        "title": "AIHumanity | HSE | CENTRO DE CONTROL",
        "welcome": "PORTAL DEL SISTEMA",
        "sub": "Operaciones Mineras Seguras - Modo Alta Visibilidad",
        "op_access": "ACCESO OPERADOR",
        "ad_access": "ACCESO ADMINISTRADOR",
        "pass_prompt": "Clave de Autorización",
        "btn_unlock": "DESBLOQUEAR SISTEMA",
        "status": "CONECTIVIDAD: RED-GLOBAL",
        "traffic": "TRÁFICO DE DATOS",
        "wind": "VEL. VIENTO",
        "temp": "TEMP. AMB.",
        "hse_status": "NIVEL RIESGO HSE",
        "secure": "SEGURO / NOMINAL",
        "logout": "CERRAR SESIÓN",
        "diag": "Centro de Diagnóstico Neuronal",
        "nodes": "NODOS ACTIVOS (70k)",
        "wave": "Ondas de Riesgo en Tiempo Real (ICR)",
        "pm10": "MP 10 (Polvo)",
        "pm25": "MP 2.5 (Polvo)"
    }
}

L = translations[st.session_state.lang]

# --- 2. HIGH-CONTRAST LIGHT UI CONFIG ---
st.set_page_config(page_title=L['title'], layout="wide")

def inject_light_high_contrast():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
    
    /* White Background & Black Text */
    html, body, [class*="css"], [data-testid="stAppViewContainer"] {{ 
        font-family: 'SF Pro Display', sans-serif; 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
    }}

    /* Sidebar - Light Gray */
    [data-testid="stSidebar"] {{
        background-color: #F8F9FA !important;
        border-right: 2px solid #EEEEEE;
    }}

    /* Metrics - High Contrast Light */
    div[data-testid="stMetricValue"] {{ color: #D35400 !important; font-weight: 700; font-size: 2.8rem; }}
    div[data-testid="stMetricLabel"] {{ color: #444444 !important; text-transform: uppercase; font-weight: 600; letter-spacing: 1px; }}
    
    .stMetric {{
        background: #FFFFFF;
        border: 2px solid #000000;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 4px 4px 0px #000000;
    }}

    /* Industrial Status Bar - Light Mode */
    .status-bar {{
        background: #000000;
        padding: 10px 30px;
        display: flex;
        justify-content: space-between;
        margin-bottom: 30px;
        color: #FFFFFF;
        font-weight: 600;
        font-size: 0.9rem;
    }}

    /* Form Inputs */
    input {{
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

inject_light_high_contrast()

# --- 3. SESSION & LANGUAGE ---
st.sidebar.title("🛠️ SETTINGS")
st.session_state.lang = st.sidebar.selectbox("UI LANGUAGE", ["EN", "ES"], 
                                             index=0 if st.session_state.lang == "EN" else 1)

# --- 4. SECURE GATEWAY ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
    st.session_state.role = None

if not st.session_state.auth:
    st.markdown(f"<div style='border:3px solid #000; padding:40px; text-align:center;'><h1>{L['welcome']}</h1><h3>{L['sub']}</h3></div>", unsafe_allow_html=True)
    
    t1, t2 = st.tabs([L['op_access'], L['ad_access']])
    with t1:
        p1 = st.text_input(f"{L['pass_prompt']} (Operator)", type="password", key="k1")
        if st.button(L['btn_unlock'], key="b1"):
            if p1 == "1234": st.session_state.role="Operator"; st.session_state.auth=True; st.rerun()
    with t2:
        p2 = st.text_input(f"{L['pass_prompt']} (Admin)", type="password", key="k2")
        if st.button(L['btn_unlock'], key="b2"):
            if p2 == "Admin": st.session_state.role="Admin"; st.session_state.auth=True; st.rerun()
    st.stop()

# --- 5. MAIN INTERFACE ---
st.markdown(f"""
<div class='status-bar'>
    <span>{L['status']}</span>
    <span>{L['traffic']}: 14.2 GB/s</span>
    <span>{L['wind']}: 10 KM/H</span>
    <span>🕒 {datetime.now().strftime('%H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

st.title(f"📊 {L['title']}")

c1, c2, c3 = st.columns(3)
c1.metric(L['hse_status'], L['secure'])
c2.metric(L['pm10'], "10.8 µg/m³", "-2.1")
c3.metric(L['pm25'], "3.9 µg/m³", "0.1", delta_color="inverse")

# ICR Waveform with high-contrast lines
st.subheader(L['wave'])
chart_data = pd.DataFrame(np.random.randn(50, 2), columns=['Dust', 'Vibration'])
st.line_chart(chart_data, color=["#000000", "#D35400"])

if st.sidebar.button(L['logout']):
    st.session_state.auth = False; st.rerun()
