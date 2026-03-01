import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. SETUP RESPONSIVO (AJUSTADO PARA LAPTOPS Y MÓVILES)
st.set_page_config(page_title="AIH | Emergency Control", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE ALTA PRECISIÓN (ESTILO CUPERTINO INDUSTRIAL DARK-MODAL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F8F9FA; color: #1D1D1F; }
    
    /* Optimización de texto para pantallas pequeñas */
    .metric-value { font-size: 1.8rem !important; font-weight: 800; color: #1D1D1F; }
    .label-micro { font-size: 0.7rem; color: #8E8E93; font-weight: 600; text-transform: uppercase; }
    
    /* Módulos de Despacho */
    .dispatch-card {
        background: white;
        padding: 15px;
        border-radius: 16px;
        border-left: 6px solid #FF3B30;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 10px;
    }
    .btn-emergency {
        background-color: #FF3B30 !important;
        color: white !important;
        font-weight: bold !important;
        height: 60px !important;
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVEGADOR ESTRATÉGICO
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1022/1022331.png", width=70)
    st.title("AIH MASTER")
    modulo = st.radio("MÓDULO:", ["🏠 Dashboard Operativo", "🌪️ Analizador ADMS", "🚨 Despacho Emergencias"])
    st.divider()
    st.caption("v7.0 | TRL-4 Rescue Ready")

# --- LÓGICA DE PÁGINAS ---

# MÓDULO 1: DASHBOARD OPERATIVO (REDISEÑADO SIN LATENCIA)
if modulo == "🏠 Dashboard Operativo":
    st.markdown("<h3 style='margin:0;'>📊 ESTADO OPERATIVO INTEGRADO</h3>", unsafe_allow_html=True)
    
    # KPIs Rápidos y Legibles
    c1, c2, c3, c4 = st.columns([1,1,1,1])
    c1.metric("META CERO", "96%", "OK")
    c2.metric("MP10", "34.2", "-2.1")
    c3.metric("NODOS", "12/12", "LIVE")
    c4.metric("RIESGO", "BAJO", "12%")

    st.write("---")
    
    # REEMPLAZO DEL RADAR (MENOS LATENCIA)
    col_traz, col_stats = st.columns([1, 1])
    
    with col_traz:
        st.markdown("<b>👥 TRAZABILIDAD DE PERSONAL</b>", unsafe_allow_html=True)
        t_data = pd.DataFrame({
            "Operador": ["J. Pérez", "M. Soto", "L. Mora", "A. Ruiz"],
            "Zona": ["Nivel 4", "Chancado", "Rampa", "Stock"],
            "Status": ["Seguro", "Seguro", "Alerta", "Seguro"]
        })
        st.table(t_data)

    with col_stats:
        st.markdown("<b>📈 TENDENCIA AMBIENTAL (24H)</b>", unsafe_allow_html=True)
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['MP10', 'Humedad'])
        st.line_chart(chart_data, height=200)

# MÓDULO 3: DESPACHO DE EMERGENCIAS (EL NUEVO ANALIZADOR)
elif modulo == "🚨 Despacho Emergencias":
    st.markdown("<h2 style='color:#FF3B30;'>🚨 CENTRO DE DESPACHO Y RESCATE</h2>", unsafe_allow_html=True)
    
    # FILA DE BOTONES DE ACTIVACIÓN INMEDIATA (PROTOCOLO)
    st.write("### ⚡ ACTIVACIÓN DE PROTOCOLO")
    b1, b2, b3, b4 = st.columns(4)
    with b1: 
        if st.button("🚒 BOMBEROS", use_container_width=True): st.toast("Despachando Bomberos...")
    with b2: 
        if st.button("🚑 AMBULANCIA", use_container_width=True): st.toast("Despachando SAMU...")
    with b3: 
        if st.button("👮 POLICÍA", use_container_width=True): st.toast("Avisando a Carabineros...")
    with b4: 
        if st.button("⛏️ RESCATE MINERO", use_container_width=True): st.toast("Activando Brigada...")

    st.divider()

    # TRAZABILIDAD DE INCIDENTES ACTIVOS
    col_active, col_log = st.columns([2, 1])

    with col_active:
        st.markdown("### 📋 Incidentes en Curso")
        st.markdown("""
        <div class="dispatch-card">
            <div style="display:flex; justify-content:space-between;">
                <b>ID: INC-092 - AMAGO DE INCENDIO</b>
                <span style="color:#FF3B30; font-weight:bold;">EN CURSO</span>
            </div>
            <p class="label-micro">UBICACIÓN: NIVEL 4 SECTOR ALPHA | DESPACHO: 18:05:12</p>
            <progress value="75" max="100" style="width:100%;"></progress>
        </div>
        """, unsafe_allow_html=True)
        
        # Mapa de ubicación del incidente
        st.markdown("<b>📍 UBICACIÓN DEL RESCATE (GEOPOSICIÓN)</b>", unsafe_allow_html=True)
        st.map(pd.DataFrame({'lat': [-34.05], 'lon': [-70.45]}), zoom=14, height=250)
        

    with col_log:
        st.markdown("### 📜 Log de Trazabilidad")
        st.caption("18:10 - Brigada de Rescate ingresa a Nivel 4")
        st.caption("18:06 - Bomberos confirmados en ruta")
        st.caption("18:05 - Alarma activada por Nodo ESP32-04")
        st.divider()
        st.write("<b>Protocolo sugerido:</b> Evacuación Sector Alpha por rampa de emergencia.")

# MÓDULO 2 (EL QUE YA TENÍAMOS BLINDADO)
else:
    st.markdown("<h2 style='color:#5E5CE6;'>🌪️ METEOROLOGÍA & ADMS</h2>", unsafe_allow_html=True)
    st.info("Visualizando Modelo de Dispersión Atmosférica...")
    # (Aquí va la lógica de ADMS que ya probamos)

# 4. FOOTER DINÁMICO
st.divider()
st.caption(f"AIHumanity Master | Login: Admin | {datetime.now().strftime('%H:%M:%S')} | No Masivo")
time.sleep(1.5)
st.rerun()
