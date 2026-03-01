import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA Y LENGUAJE ---
if 'lang' not in st.session_state:
    st.session_state.lang = "EN"

# Diccionario de Idiomas
content = {
    "EN": {
        "welcome": "AIHumanity HSE System",
        "sub": "Mining Operations Control Center",
        "op_btn": "OPERATOR ACCESS",
        "ad_btn": "ADMINISTRATOR ACCESS",
        "pass_label": "Enter Password",
        "status": "CONNECTIVITY: GLOBAL-NET",
        "traffic": "TRAFFIC",
        "wind": "WIND",
        "hse_status": "HSE STATUS",
        "secure": "SECURE",
        "logout": "LOGOUT",
        "role_label": "Role",
        "diag": "Admin Diagnostic Center"
    },
    "ES": {
        "welcome": "Sistema HSE AIHumanity",
        "sub": "Centro de Control de Operaciones Mineras",
        "op_btn": "ACCESO OPERADOR",
        "ad_btn": "ACCESO ADMINISTRADOR",
        "pass_label": "Ingrese Contraseña",
        "status": "CONECTIVIDAD: RED-GLOBAL",
        "traffic": "TRÁFICO",
        "wind": "VIENTO",
        "hse_status": "ESTADO HSE",
        "secure": "SEGURO",
        "logout": "CERRAR SESIÓN",
        "role_label": "Rol",
        "diag": "Centro de Diagnóstico Admin"
    }
}

L = content[st.session_state.lang]

st.set_page_config(page_title="AIH Master HSE", layout="wide", initial_sidebar_state="collapsed")

# --- CUPERTINO HIGH-CONTRAST UI ---
def apply_style():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
    
    html, body, [class*="css"] {{ font-family: 'SF Pro Display', sans-serif; background-color: #000000; color: #FFFFFF; }}
    
    /* Fondo Naranja Minero con Alto Contraste */
    .welcome-card {{
        background: linear-gradient(135deg, #FF6B00 0%, #E65C00 100%);
        padding: 60px;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 40px;
        border: 2px solid #FFFFFF;
    }}

    /* Tarjetas Cupertino Glass con Contraste Reforzado */
    .stMetric {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 18px;
        padding: 25px;
    }}

    .status-bar {{
        background: #111111;
        padding: 12px 25px;
        border-radius: 50px;
        border: 1px solid #FF6B00;
        display: flex;
        justify-content: space-between;
        margin-bottom: 25px;
        font-weight: 600;
        color: #FF6B00;
    }}
    
    /* Inputs y Botones */
    .stButton>button {{
        border-radius: 12px;
        background-color: #FF6B00;
        color: white;
        font-weight: bold;
        border: none;
    }}
    </style>
    """, unsafe_allow_html=True)

apply_style()

# --- SELECTOR DE IDIOMA (FLOTANTE) ---
st.session_state.lang = st.sidebar.selectbox("🌐 Language / Idioma", ["EN", "ES"], index=0 if st.session_state.lang == "EN" else 1)

# --- GATEWAY DE SEGURIDAD ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
    st.session_state.role = None

if not st.session_state.auth:
    st.markdown(f"<div class='welcome-card'><h1>{L['welcome']}</h1><p>{L['sub']}</p></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(L['op_btn'])
        op_pass = st.text_input(f"{L['pass_label']} (OP)", type="password", key="op_p")
        if st.button("LOGIN OPERATOR"):
            if op_pass == "1234":
                st.session_state.role = "Operator"
                st.session_state.auth = True
                st.rerun()
            else: st.error("Invalid Code")

    with col2:
        st.subheader(L['ad_btn'])
        ad_pass = st.text_input(f"{L['pass_label']} (ADMIN)", type="password", key="ad_p")
        if st.button("LOGIN ADMIN"):
            if ad_pass == "Admin":
                st.session_state.role = "Admin"
                st.session_state.auth = True
                st.rerun()
            else: st.error("Access Denied")
    st.stop()

# --- DASHBOARD PRINCIPAL ---
st.markdown(f"""
<div class='status-bar'>
    <span>{L['status']}</span>
    <span>{L['traffic']}: 5.1 GB/s</span>
    <span>{L['wind']}: 12 KM/H NE</span>
    <span>🕒 {datetime.now().strftime('%H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

if st.session_state.role == "Operator":
    st.title(f"Operator Dashboard - {st.session_state.role}")
    c1, c2, c3 = st.columns(3)
    c1.metric(L['hse_status'], L['secure'])
    c2.metric("PM 10", "14.2 µg/m³", "-1.2")
    c3.metric("PM 2.5", "5.1 µg/m³", "0.2")
    
    st.subheader("Real-Time Risk Wave")
    st.line_chart(np.random.randn(20, 2))

else:
    st.title(L['diag'])
    st.sidebar.warning("ADMIN PRIVILEGES ACTIVE")
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.write("### Neural Audit")
        st.code("OpenAI Instance: ACTIVE\nICR Analysis: NOMINAL\nLatency: 9ms")
    with col_b:
        st.write("### Node Distribution (70k)")
        st.progress(98)
        st.area_chart(np.random.randn(20, 1))

if st.sidebar.button(L['logout']):
    st.session_state.auth = False
    st.rerun()
