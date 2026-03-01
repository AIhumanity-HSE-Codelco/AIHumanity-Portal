import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- 1. MOTOR DE LENGUAJE INTEGRADO ---
if 'lang' not in st.session_state:
    st.session_state.lang = "EN"

translations = {
    "EN": {
        "title": "AIHumanity | HSE | CONTROL CENTER",
        "welcome": "SYSTEM GATEWAY",
        "sub": "Secure Mining Operations - TRL 4 Protocol",
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
        "audit": "AI AUDIT LOG",
        "pm10": "PM 10 (Dust)",
        "pm25": "PM 2.5 (Dust)"
    },
    "ES": {
        "title": "AIHumanity | HSE | CENTRO DE CONTROL",
        "welcome": "PORTAL DEL SISTEMA",
        "sub": "Operaciones Mineras Seguras - Protocolo TRL 4",
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
        "audit": "REGISTRO DE AUDITORÍA IA",
        "pm10": "MP 10 (Polvo)",
        "pm25": "MP 2.5 (Polvo)"
    }
}

L = translations[st.session_state.lang]

# --- 2. CONFIGURACIÓN DE INTERFAZ CUPERTINO OLED ---
st.set_page_config(page_title=L['title'], layout="wide", initial_sidebar_state="expanded")

def inject_high_end_css():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    
    /* OLED Black Theme */
    html, body, [class*="css"], [data-testid="stAppViewContainer"] {{ 
        font-family: 'SF Pro Display', sans-serif; 
        background-color: #000000 !important; 
        color: #FFFFFF !important; 
    }}

    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {{
        background-color: #050505 !important;
        border-right: 1px solid #1a1a1a;
    }}

    /* Metrics High Contrast */
    div[data-testid="stMetricValue"] {{ color: #FF6B00 !important; font-weight: 600; font-size: 2.8rem; }}
    div[data-testid="stMetricLabel"] {{ color: #999999 !important; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.8rem; }}
    
    .stMetric {{
        background: rgba(15, 15, 15, 0.9);
        border: 1px solid #222;
        border-radius: 16px;
        padding: 25px;
        transition: 0.3s;
    }}
    .stMetric:hover {{ border-color: #FF6B00; }}

    /* Status Bar Industrial */
    .status-bar {{
        background: #000;
        padding: 12px 30px;
        border-bottom: 2px solid #FF6B00;
        display: flex;
        justify-content: space-between;
        margin-bottom: 30px;
        color: #FF6B00;
        font-weight: 600;
        font-size: 0.9rem;
        letter-spacing: 1px;
    }}

    /* Login Box */
    .gateway-box {{
        border: 1px solid #333;
        border-radius: 20px;
        padding: 50px;
        background: #050505;
        text-align: center;
        margin: auto;
        max-width: 600px;
    }}
    </style>
    """, unsafe_allow_html=True)

inject_high_end_css()

# --- 3. GESTIÓN DE IDIOMAS ---
st.sidebar.title("🛠️ SYSTEM SETTINGS")
st.session_state.lang = st.sidebar.selectbox("UI LANGUAGE", ["EN", "ES"], 
                                             index=0 if st.session_state.lang == "EN" else 1)

# --- 4. PORTAL DE ACCESO SEGURO ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
    st.session_state.role = None

if not st.session_state.auth:
    st.markdown(f"<div class='gateway-box'><h1 style='color:#FF6B00;'>{L['welcome']}</h1><p style='color:#888;'>{L['sub']}</p></div>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs([L['op_access'], L['ad_access']])
    
    with tab1:
        op_pass = st.text_input(f"{L['pass_prompt']} (Operator)", type="password", key="op_key")
        if st.button(L['btn_unlock'], key="b1"):
            if op_pass == "1234":
                st.session_state.role = "Operator"; st.session_state.auth = True; st.rerun()
            else: st.error("Access Denied")

    with tab2:
        ad_pass = st.text_input(f"{L['pass_prompt']} (Admin)", type="password", key="ad_key")
        if st.button(L['btn_unlock'], key="b2"):
            if ad_pass == "Admin":
                st.session_state.role = "Admin"; st.session_state.auth = True; st.rerun()
            else: st.error("Access Denied")
    st.stop()

# --- 5. INTERFAZ MAESTRA DE CONTROL ---
st.markdown(f"""
<div class='status-bar'>
    <span>{L['status']}</span>
    <span>{L['traffic']}: 12.8 GB/s</span>
    <span>{L['wind']}: 14 KM/H NE</span>
    <span>{L['temp']}: 26.4°C</span>
    <span>🕒 {datetime.now().strftime('%H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

if st.session_state.role == "Operator":
    st.title(f"🛡️ {L['title']}")
    
    c1, c2, c3 = st.columns(3)
    c1.metric(L['hse_status'], L['secure'])
    c2.metric(L['pm10'], "11.5 µg/m³", "-1.8")
    c3.metric(L['pm25'], "4.2 µg/m³", "0.3", delta_color="inverse")
    
    st.subheader(L['wave'])
    # Simulación de onda ICR dinámica
    chart_data = pd.DataFrame(np.random.randn(50, 2), columns=['Dust', 'Stability'])
    st.line_chart(chart_data, color=["#FF6B00", "#333333"])

else:
    st.title(f"🛠️ {L['diag']}")
    st.sidebar.warning("ADMIN PRIVILEGES: GRANTED")
    
    c_left, c_right = st.columns([1, 2])
    with c_left:
        st.write(f"### {L['audit']}")
        st.code(f"AI Engine: OpenAI-4o\nNode Sync: 69,842/70,000\nLatency: 12ms\nBuffer: 0% loss")
        st.success("Predictive Model: STABLE")
    with c_right:
        st.write(f"### {L['nodes']} Pulse")
        st.area_chart(np.random.randn(30, 1), color=["#FF6B00"])
        st.progress(99)

if st.sidebar.button(L['logout']):
    st.session_state.auth = False; st.rerun()
