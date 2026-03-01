import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# 1. SETUP DE ALTA PRECISIÓN (ESTÁTICO)
st.set_page_config(page_title="AIH MASTER | STABLE", layout="wide", initial_sidebar_state="expanded")

# 2. CSS DE ALTO CONTRASTE (FONDO OSCURO - SIN ANIMACIÓN)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap');
    
    /* Entorno Negro Industrial */
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Roboto Mono', monospace; }
    
    /* Bloques de Datos Sólidos */
    .st-emotion-cache-1r6slb0 { background-color: #111111 !important; border: 1px solid #333333 !important; border-radius: 10px !important; }
    
    /* Títulos y Métricas */
    h1, h2, h3 { color: #5E5CE6; font-weight: 700; }
    .big-font { font-size: 3rem !important; font-weight: 800; color: #FFFFFF; }
    .label-font { font-size: 0.9rem; color: #888888; text-transform: uppercase; }
    
    /* Colores de Estado HSE (Sólidos) */
    .status-box { padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 20px; border: 2px solid #333; }
    .bg-green { background-color: #1A3D21; border-color: #30D158; }
    .bg-yellow { background-color: #3D361A; border-color: #FF9500; }
    .bg-red { background-color: #3D1A1A; border-color: #FF3B30; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGACIÓN LATERAL
with st.sidebar:
    st.markdown("### 🛰️ AIH NAV")
    modulo = st.radio("SELECCIONAR:", ["🧠 CEREBRO (IRC)", "🌪️ ADMS", "🌍 SISMO", "⚙️ ACTIVOS"])
    st.divider()
    if st.button("🔄 ACTUALIZAR DATOS"):
        st.rerun()

# --- LÓGICA DE CORRELACIÓN ---
irc_val = 32.5 # Valor base estable
status_color = "bg-green"
status_text = "NOMINAL"

if irc_val > 70:
    status_color = "bg-red"
    status_text = "CRÍTICO"
elif irc_val > 40:
    status_color = "bg-yellow"
    status_text = "PRECAUCIÓN"

# --- MÓDULO: CEREBRO DE RIESGO (IRC) ---
if modulo == "🧠 CEREBRO (IRC)":
    
    # HEADER DE ESTADO
    st.markdown(f"""
    <div class="status-box {status_color}">
        <p class="label-font">ESTADO DE RIESGO COMPUESTO (IRC)</p>
        <p class="big-font">{status_text}</p>
        <p style="margin:0;">Sincronización: {datetime.now().strftime('%H:%M:%S')}</p>
    </div>
    """, unsafe_allow_html=True)

    # GRID DE VARIABLES CRÍTICAS (4 COLUMNAS)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("MP10", "42.1 µg/m³", "-2%")
    with c2:
        st.metric("VIENTO", "22 km/h", "NE")
    with c3:
        st.metric("NODOS", "12/12", "OK")
    with c4:
        st.metric("IRC FINAL", f"{irc_val}%", "ESTABLE")

    st.write("---")

    # CUERPO DE ANÁLISIS
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("### 📊 TENDENCIA DE RIESGO (CORRELACIÓN)")
        # Gráfico estático limpio
        data = pd.DataFrame({'Riesgo': [30, 32, 31, 35, 32, 33, 32]})
        st.area_chart(data, color="#5E5CE6")
        

    with col_right:
        st.markdown("### 👥 TRAZABILIDAD")
        # Tabla simple de alta legibilidad
        t_data = pd.DataFrame({
            "NODO": ["ESP-01", "ESP-04", "ESP-09"],
            "ZONA": ["Chancado", "Nivel 4", "Rampa"],
            "ESTADO": ["OK", "OK", "OK"]
        })
        st.dataframe(t_data, hide_index=True, use_container_width=True)

# 4. FOOTER
st.divider()
st.caption(f"AIH MASTER V11.0 | ENTORNO ESTABILIZADO | TRL-4")
