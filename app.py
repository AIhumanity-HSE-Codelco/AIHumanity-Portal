import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from streamlit_echarts import st_echarts
from scipy.stats import multivariate_normal
from datetime import datetime
import time

# 1. SETUP DE ALTA DENSIDAD Y NAVEGACIÓN
st.set_page_config(page_title="AIH | El Teniente Master", layout="wide", initial_sidebar_state="expanded")

# 2. CSS UNIFICADO (CUPERTINO + ALTO CONTRASTE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F4F7F9; }
    .module-box { background: white; padding: 15px; border-radius: 18px; border: 1px solid #E5E9F0; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-bottom: 10px; }
    .stMetric { background: white; padding: 10px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (EL NAVEGADOR)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=80)
    st.title("AIH COMMAND")
    # Este es el switch que separa las dos páginas
    opcion = st.radio("SELECCIONAR MÓDULO:", 
                     ["🏠 Dashboard Principal (Blindado)", 
                      "🌪️ Analizador ADMS & Sismo"])
    st.divider()
    st.info("📡 STATUS: Nodos Adeepminers Sincronizados")
    st.caption("v6.5 | TRL-4 Industrial")

# --- PÁGINA 1: DASHBOARD PRINCIPAL (TU PÁGINA ANTERIOR) ---
if opcion == "🏠 Dashboard Principal (Blindado)":
    st.markdown("<h2 style='color:#5E5CE6;'>🛰️ CONTROL TOWER: TRAZABILIDAD Y SENSORES</h2>", unsafe_allow_html=True)
    
    # KPIs Rápidos
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("META CERO", "96.4%", "+0.2")
    k2.metric("MP10", "38.2", "-4.1")
    k3.metric("PERSONAS", "142", "ACTIVOS")
    k4.metric("IRO", "32.1", "ESTABLE")

    col_izq, col_der = st.columns([1, 1])
    
    with col_izq:
        st.markdown("<div class='module-box'><b>👥 Trazabilidad Personal (HSE)</b>", unsafe_allow_html=True)
        # Reutilizamos la lógica de trazabilidad
        st.write("J. Pérez (G-4) - 🟢 SEGURO")
        st.write("M. Soto (CH-1) - 🟠 ALERTA MP10")
        st.write("A. León (STK-2) - 🟢 SEGURO")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Mapa de Calor
        st.map(pd.DataFrame(np.random.randn(5, 2) / [300, 300] + [-34.05, -70.45], columns=['lat', 'lon']), height=250)

    with col_der:
        st.markdown("<div class='module-box'><b>📊 Radar de Riesgo Acumulado</b>", unsafe_allow_html=True)
        # Radar ECharts para fluidez
        options = {
            "radar": {"indicator": [{"name": "Polvo", "max": 100}, {"name": "Viento", "max": 100}, {"name": "Gases", "max": 100}, {"name": "Trazabilidad", "max": 100}, {"name": "Geom.", "max": 100}, {"name": "Check", "max": 100}]},
            "series": [{"type": "radar", "data": [{"value": [42, 35, 20, 95, 15, 88], "areaStyle": {"color": "rgba(94, 92, 230, 0.3)"}, "lineStyle": {"color": "#5E5CE6"}}]}]
        }
        st_echarts(options=options, height="300px")
        st.markdown("</div>", unsafe_allow_html=True)

# --- PÁGINA 2: ANALIZADOR ADMS & SISMO (LA NUEVA PÁGINA) ---
else:
    st.markdown("<h2 style='color:#30D158;'>🌪️ INTELIGENCIA METEOROLÓGICA & ADMS</h2>", unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns([1, 2, 1])
    
    with m1:
        st.markdown("<div class='module-box'><b>📡 Datos Reales Estación</b>", unsafe_allow_html=True)
        st.metric("Viento", "24 km/h", "NE")
        st.metric("Humedad", "62%", "Alta")
        st.metric("Sismo VPP", "1.2 mm/s", "Bajo")
        st.markdown("</div>", unsafe_allow_html=True)

    with m2:
        st.markdown("<div class='module-box'><b>🗺️ Modelo Dispersión Gaussiana (ADMS)</b>", unsafe_allow_html=True)
        # Generamos la pluma matemática
        x, y = np.mgrid[-30:30:1, -30:30:1]
        pos = np.dstack((x, y))
        rv = multivariate_normal([0, 0], [[15, 0], [0, 3]]) # Pluma estirada
        z = rv.pdf(pos)
        fig_adms = go.Figure(data=[go.Contour(z=z, colorscale='Viridis', showscale=False)])
        fig_adms.update_layout(height=350, margin=dict(t=0, b=0, l=0, r=0), xaxis_visible=False, yaxis_visible=False)
        st.plotly_chart(fig_adms, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    with m3:
        st.markdown("<div class='module-box'><b>📉 Monitor Sismográfico</b>", unsafe_allow_html=True)
        sismo_data = pd.DataFrame(np.random.randn(40, 1) * 0.02, columns=['Aceleración (g)'])
        st.line_chart(sismo_data, height=200)
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Acción ADMS
    if st.button("🚨 ACTIVAR PROTOCOLO SUPRESIÓN DE POLVO (SECTOR ALPHA)", use_container_width=True):
        st.warning("Nebulizadores activados. Tiempo estimado de mitigación: 15 min.")

# 4. FOOTER E INERCIA
time.sleep(1.5)
st.rerun()
