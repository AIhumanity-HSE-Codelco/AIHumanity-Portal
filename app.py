import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- 1. CONFIGURACIÓN DE IDENTIDAD Y LENGUAJE ---
if 'lang' not in st.session_state: st.session_state.lang = "EN"
if 'auth' not in st.session_state: st.session_state.auth = False

translations = {
    "EN": {
        "title": "AIHumanity | HSE | CONTROL CENTER",
        "status": "SYSTEM STATUS: ACTIVE",
        "nodes": "70k NODES SYNCED",
        "traffic": "DATA TRAFFIC",
        "op_access": "OPERATOR ACCESS",
        "ad_access": "ADMIN ACCESS",
        "icr": "RISK INDEX (ICR)",
        "pm10": "DUST MP10",
        "pm25": "DUST MP2.5",
        "wave": "REAL-TIME WAVE ANALYSIS",
        "logout": "TERMINATE SESSION"
    },
    "ES": {
        "title": "AIHumanity | HSE | CENTRO DE CONTROL",
        "status": "ESTADO DEL SISTEMA: ACTIVO",
        "nodes": "70k NODOS SINCRONIZADOS",
        "traffic": "TRÁFICO DE DATOS",
        "op_access": "ACCESO OPERADOR",
        "ad_access": "ACCESO ADMIN",
        "icr": "ÍNDICE DE RIESGO (ICR)",
        "pm10": "POLVO MP10",
        "pm25": "POLVO MP2.5",
        "wave": "ANÁLISIS DE ONDAS T-REAL",
        "logout": "CERRAR SESIÓN"
    }
}

L = translations[st.session_state.lang]

# --- 2. DISEÑO INDUSTRIAL HIGH-CONTRAST (WHITE MODE) ---
st.set_page_config(page_title=L['title'], layout="wide", initial_sidebar_state="expanded")

st.markdown(f"""
<style>
    /* Estética Cupertino High-Contrast */
    html, body, [class*="css"], [data-testid="stAppViewContainer"] {{
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{ background-color: #F0F2F6 !important; border-right: 2px solid #000; }}

    /* Cards Brutalistas */
    .stMetric {{
        background: #FFFFFF !important;
        border: 3px solid #000000 !important;
        border-radius: 0px !important;
        padding: 20px !important;
        box-shadow: 8px 8px 0px #000000;
    }}
    
    div[data-testid="stMetricValue"] {{ color: #D35400 !important; font-weight: 800; }}
    
    /* Botones Industriales */
    .stButton>button {{
        width: 100%;
        border-radius: 0px;
        border: 2px solid #000;
        background-color: #FFFFFF;
        color: #000;
        font-weight: bold;
        transition: 0.2s;
    }}
    .stButton>button:hover {{ background-color: #000; color: #FFF; }}

    /* Status Bar Negra */
    .status-bar {{
        background: #000;
        color: #FFF;
        padding: 10px 25px;
        display: flex;
        justify-content: space-between;
        font-weight: bold;
        margin-bottom: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE ACCESO (GATEWAY) ---
if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center; border-bottom: 5px solid #000;'>AIHumanity | SYSTEM GATEWAY</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(L['op_access'])
        if st.text_input("Operator PIN", type="password") == "1234":
            if st.button("UNLOCK OPERATOR"): st.session_state.auth = True; st.session_state.role = "OP"; st.rerun()
            
    with col2:
        st.subheader(L['ad_access'])
        if st.text_input("Admin Password", type="password") == "Admin":
            if st.button("UNLOCK ADMIN"): st.session_state.auth = True; st.session_state.role = "AD"; st.rerun()
    st.stop()

# --- 4. INTERFAZ DE CONTROL ACTIVA ---
st.sidebar.radio("🌐 Language", ["EN", "ES"], key="lang_choice", on_change=lambda: setattr(st.session_state, 'lang', st.session_state.lang_choice))

st.markdown(f"""
<div class='status-bar'>
    <span>{L['status']}</span>
    <span>{L['traffic']}: 14.2 GB/s</span>
    <span>{L['nodes']}</span>
    <span>🕒 {datetime.now().strftime('%H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

st.title(f"📊 {L['title']}")

# Métricas Críticas (HSE Priority)
c1, c2, c3 = st.columns(3)
c1.metric(L['icr'], "94.2%", "Normal")
c2.metric(L['pm10'], "12.5 µg/m³", "-1.2")
c3.metric(L['pm25'], "5.8 µg/m³", "0.4", delta_color="inverse")

# Gráfico de Ondas de Riesgo
st.subheader(L['wave'])
chart_data = pd.DataFrame(np.random.randn(40, 2), columns=['Seismic', 'Dust_Pulse'])
st.line_chart(chart_data, color=["#000000", "#D35400"])

if st.sidebar.button(L['logout']):
    st.session_state.auth = False; st.rerun()
