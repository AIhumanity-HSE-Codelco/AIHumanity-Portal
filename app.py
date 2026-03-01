import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. SETUP PROFESIONAL (RESPONSIVO Y ESTABLE)
st.set_page_config(page_title="AIH | THE CORE V10.1", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS REFINADO (ESTILO DARK-INDUSTRIAL SIN PALPITACIONES)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    /* Fondo Gris Carbón Industrial */
    .stApp { background-color: #1A1C21; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    
    /* Tarjetas de Datos Blindadas */
    .metric-card {
        background: #25282F;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #3A3F47;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        text-align: center;
    }
    
    /* Tipografía para Laptops y PC */
    .value-main { font-size: 2.2rem; font-weight: 800; margin: 0; }
    .label-sub { font-size: 0.8rem; color: #8E949E; text-transform: uppercase; letter-spacing: 1px; }
    
    /* Estatus de Riesgo Sin Parpadeo */
    .status-safe { border-left: 5px solid #30D158; }
    .status-warn { border-left: 5px solid #FF9500; }
    .status-crit { border-left: 5px solid #FF3B30; }
    </style>
    """, unsafe_allow_html=True)

# 3. MOTOR DE GOBERNANZA (DATOS SUAVIZADOS)
if 'buffer_irc' not in st.session_state: st.session_state.buffer_irc = [50.0]

def get_smoothed_irc():
    # Simulamos entrada de sensores
    raw_val = 40 + np.sin(time.time() * 0.1) * 20 + np.random.normal(0, 2)
    st.session_state.buffer_irc.append(raw_val)
    if len(st.session_state.buffer_irc) > 10: st.session_state.buffer_irc.pop(0)
    return np.mean(st.session_state.buffer_irc)

# 4. INTERFAZ DE ALTA DENSIDAD
with st.sidebar:
    st.title("🧠 AIH CORE")
    modulo = st.radio("SELECCIONAR VISTA:", ["💎 MOTOR DE DECISIONES", "🏠 DASHBOARD", "🌍 GEOFÍSICA"])

# --- VISTA: MOTOR DE DECISIONES ---
if modulo == "💎 MOTOR DE DECISIONES":
    current_irc = get_smoothed_irc()
    
    h1, h2 = st.columns([3, 1])
    with h1:
        st.markdown("<h2 style='margin:0;'>🧠 GOBERNANZA DE RIESGO PROGRESIVO</h2>", unsafe_allow_html=True)
        st.caption(f"Nodo Maestro: ESP32-GATEWAY-01 | Sincronización: {datetime.now().strftime('%H:%M:%S')}")
    with h2:
        status_label = "SEGURO" if current_irc < 40 else "PRECAUCIÓN" if current_irc < 70 else "CRÍTICO"
        status_class = "status-safe" if current_irc < 40 else "status-warn" if current_irc < 70 else "status-crit"
        st.markdown(f"<div class='metric-card {status_class}'><p class='label-sub'>ESTADO HSE</p><p class='value-main'>{status_label}</p></div>", unsafe_allow_html=True)

    st.write("")

    # FILA 1: INDICADORES COMPUESTOS
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='metric-card'><p class='label-sub'>Índice IRC</p><p class='value-main' style='color:#5E5CE6;'>{round(current_irc,1)}%</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-card'><p class='label-sub'>MP10 Activo</p><p class='value-main'>42.1</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-card'><p class='label-sub'>Nodos Online</p><p class='value-main'>12/12</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown(f"<div class='metric-card'><p class='label-sub'>Personal</p><p class='value-main'>14</p></div>", unsafe_allow_html=True)

    st.write("")

    # FILA 2: ANÁLISIS DE CORRELACIÓN Y RED DE NODOS
    col_chart, col_net = st.columns([2, 1])
    
    with col_chart:
        st.markdown("### 📈 Correlación Cruzada de Señales")
        # Gráfico de Riesgo Progresivo
        chart_data = pd.DataFrame(np.random.normal(current_irc, 2, size=(20, 1)), columns=['Probabilidad de Incidente'])
        st.area_chart(chart_data, height=250)
        

    with col_net:
        st.markdown("### 🕸️ Red de Trazabilidad")
        # Visualización de la red de nodos AideepMiners
        fig_net = go.Figure(go.Scatter(
            x=[1, 2, 3, 2, 1], y=[1, 2, 1, 0, 0],
            mode='markers+lines+text',
            text=['N1', 'N2', 'N3', 'P1', 'P2'],
            marker=dict(size=[40, 40, 40, 60, 60], color=['#5E5CE6', '#5E5CE6', '#5E5CE6', '#30D158', '#30D158']),
            textposition="bottom center"
        ))
        fig_net.update_layout(showlegend=False, height=250, margin=dict(t=0,b=0,l=0,r=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_visible=False, yaxis_visible=False)
        st.plotly_chart(fig_net, use_container_width=True)
        

    # FILA 3: PROTOCOLOS DE ACCIÓN (INTERACTIVO)
    st.markdown("### 🛡️ Acciones de Gobernanza")
    if current_irc > 65:
        st.warning(f"⚠️ El sistema ha detectado una correlación crítica entre Polvo y Personal. Activando protocolo de mitigación.")
        if st.button("AUTORIZAR EVACUACIÓN"):
            st.error("EVACUACIÓN INICIADA")
    else:
        st.success("Sincronización de campo estable. No se requieren intervenciones.")

# 5. FOOTER Y REFRESH (MÁS LENTO PARA EVITAR ESTRÉS)
st.divider()
st.caption(f"AIH MASTER V10.1 | Sistema de Gobernanza Estabilizado | {datetime.now().strftime('%H:%M:%S')}")
time.sleep(3) # Refresco cada 3 segundos para estabilidad visual
st.rerun()
