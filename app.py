import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. SETUP DE ALTA DENSIDAD - DARK MODE INDUSTRIAL
st.set_page_config(page_title="AIH | THE CORE", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS PERSONALIZADO (ALTO CONTRASTE - FONDO OSCURO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'JetBrains Mono', monospace; background-color: #0E1117; color: #E0E0E0; }
    .stApp { background-color: #0E1117; }
    .metric-container { background: #161B22; border: 1px solid #30363D; padding: 15px; border-radius: 12px; }
    .risk-high { color: #FF3B30; font-weight: 800; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    """, unsafe_allow_html=True)

# 3. MOTOR DE CORRELACIÓN (EL CEREBRO)
def calcular_riesgo_compuesto(mp10, viento, personal_count):
    # Lógica de Inferencia: Correlaciona ambiente + exposición humana
    base_risk = (mp10 * 0.4) + (viento * 0.2) + (personal_count * 5)
    return min(base_risk, 100)

# 4. NAVEGACIÓN
with st.sidebar:
    st.title("🧠 AIH CORE")
    modulo = st.radio("SISTEMA:", ["💎 CEREBRO DE DECISIONES", "🏠 Control Tower", "🌍 Geofísica", "🌪️ ADMS"])

# --- MÓDULO MAESTRO: CEREBRO DE DECISIONES ---
if modulo == "💎 CEREBRO DE DECISIONES":
    st.markdown("<h2 style='text-align: center; color:#5E5CE6;'>🧠 MOTOR DE INFERENCIA DE RIESGO PROGRESIVO</h2>", unsafe_allow_html=True)
    
    # DATOS DE CAMPO EN TIEMPO REAL (SIMULACIÓN DE NODOS)
    mp10_val = 45 + np.random.uniform(-5, 5)
    viento_val = 22 + np.random.uniform(-2, 2)
    personal_val = 14
    
    irc = calcular_riesgo_compuesto(mp10_val, viento_val, personal_val)

    # FILA 1: INDICADORES COMPUESTOS (GAUGES)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fig_irc = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = irc,
            title = {'text': "IRC (Índice Riesgo Combinado)"},
            gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#5E5CE6"},
                     'steps': [{'range': [0, 40], 'color': "green"}, {'range': [40, 70], 'color': "yellow"}, {'range': [70, 100], 'color': "red"}]}
        ))
        fig_irc.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white", 'family': "Arial"}, height=300)
        st.plotly_chart(fig_irc, use_container_width=True)

    with col2:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.markdown("<p class='label-micro'>CORRELACIÓN NODO-HUMANO</p>", unsafe_allow_html=True)
        st.write(f"Nodos Activos: 8/8")
        st.write(f"Personal en Zona Crítica: {personal_val}")
        st.write(f"Probabilidad Incidente: {round(irc/1.2, 1)}%")
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
        st.markdown("<p class='label-micro'>ESTADO DE GOBERNANZA</p>", unsafe_allow_html=True)
        status_color = "#30D158" if irc < 50 else "#FF3B30"
        st.markdown(f"<h1 style='color:{status_color}; text-align:center;'>{'ESTABLE' if irc < 50 else 'CRÍTICO'}</h1>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # FILA 2: ANÁLISIS DE CORRELACIÓN ESPACIAL
    st.markdown("### 📊 Correlación de Señales de Campo")
    chart_data = pd.DataFrame({
        'Tiempo': pd.date_range(start='now', periods=20, freq='min'),
        'Polvo (Señal A)': np.random.normal(40, 5, 20),
        'Vibración (Señal B)': np.random.normal(20, 2, 20),
        'Riesgo Humano (Señal C)': np.random.normal(60, 10, 20)
    })
    st.line_chart(chart_data.set_index('Tiempo'))
    

    # FILA 3: LOG DE DECISIONES AUTOMÁTICAS
    st.markdown("### 📜 Log de Decisiones del Cerebro")
    if irc > 60:
        st.error(f"⚠️ {datetime.now().strftime('%H:%M:%S')} - ALERTA AUTOMÁTICA: Riesgo Compuesto excede el 60%. Sugerida evacuación Sector Alpha.")
    else:
        st.success(f"✅ {datetime.now().strftime('%H:%M:%S')} - Sistema operando bajo parámetros de seguridad nominales.")

# --- MÓDULOS BLINDADOS (Llamada simple para no saturar) ---
else:
    st.info(f"Módulo {modulo} activo. Cargando base de datos blindada...")
    st.button("VOLVER AL CEREBRO")

# 5. REFRESH & FOOTER
st.divider()
st.caption(f"AIH MASTER V10.0 | MOTOR DE GOBERNANZA TRL-4 | {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
time.sleep(2)
st.rerun()
