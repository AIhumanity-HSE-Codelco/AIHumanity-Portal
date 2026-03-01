import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. CONFIGURACIÓN DE ESCENARIO INDUSTRIAL
st.set_page_config(
    page_title="AIH MASTER | CONTROL HSE",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. INYECCIÓN DE ADN VISUAL (CSS SEGURO)
st.markdown("""
    <style>
    /* Fondo Negro Profundo */
    .stApp { background-color: #050505; color: #e0e0e0; }
    
    /* Header con Estilo Minero */
    .header-aih {
        border-bottom: 3px solid #ffcc00;
        padding: 15px;
        background-color: #111;
        margin-bottom: 25px;
        text-align: center;
    }
    
    /* Métricas Neón (Alto Contraste) */
    div[data-testid="stMetricValue"] { color: #66fcf1 !important; font-size: 3.2rem !important; font-weight: bold; }
    div[data-testid="stMetricLabel"] { color: #aaaaaa !important; text-transform: uppercase; letter-spacing: 1.5px; }
    
    /* Estilo de Alerta */
    .alerta-box { 
        padding: 20px; 
        border: 2px solid #00ff00; 
        border-radius: 10px; 
        background-color: #002200; 
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    
    <div class="header-aih">
        <h1 style="color: #ffcc00; margin: 0;">🛡️ AIHUMANITY | PORTAL HSE MINERO</h1>
        <p style="color: #66fcf1; margin: 0; font-size: 1.1rem;">CENTRO DE MONITOREO DE RIESGO PREVENTIVO - TRL-3</p>
    </div>
    """, unsafe_allow_html=True)

# 3. PRIORIDAD 1: ESTADO CRÍTICO HSE
st.markdown('<div class="alerta-box"><h2 style="color: #00ff00; margin:0;">✅ OPERACIÓN SEGURA</h2></div>', unsafe_allow_html=True)

# 4. PRIORIDAD 2 Y 3: MATERIAL PARTICULADO (METRICAS)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="MP10 (Polvo)", value="43.2", delta="-1.5 µg/m³", delta_color="inverse")
with col2:
    st.metric(label="MP2.5 (Fino)", value="14.8", delta="0.3 µg/m³", delta_color="inverse")
with col3:
    st.metric(label="Viento", value="16 km/h", delta="Dirección: NE")
with col4:
    st.metric(label="Talud", value="OK", delta="Estabilidad: 98%")

# 5. VISTA OPERADOR: TENDENCIA TEMPORAL (GRÁFICA)
st.divider()
st.subheader("📊 Tendencia de Estabilidad y Vibración (Stockpiles/Taludes)")

# Generamos datos de simulación "vivos"
chart_data = pd.DataFrame(
    np.random.randn(20, 1),
    columns=['Vibración (mm/s)']
)
st.area_chart(chart_data, color="#ffcc00")

# 6. MODO ADMIN: DIAGNÓSTICO DE RED (VISTA SIMPLE)
with st.sidebar:
    st.title("⚙️ PANEL ADMIN")
    st.write("---")
    st.write("ID Nodo: **AIH-ESP32-MASTER**")
    st.write("Conectividad: **ONLINE (100%)**")
    st.progress(85, text="Carga Batería Nodo")
    st.write("---")
    if st.button("🔴 REINICIAR ALERTA"):
        st.toast("Reiniciando sistema...")
