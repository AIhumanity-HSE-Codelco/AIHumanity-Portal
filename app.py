import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts
from datetime import datetime
import time

# 1. SETUP DE DIMENSIONES (WIDE MODE FORZADO)
st.set_page_config(page_title="AIH | Command Center", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE PRECISIÓN QUIRÚRGICA (CUPERTINO INDUSTRIAL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    /* Configuración de Escala */
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F2F4F7; font-size: 0.85rem; }
    
    /* Tarjetas de Alta Densidad */
    .module-box {
        background: white;
        padding: 10px 15px;
        border-radius: 16px;
        border: 1px solid #E5E9F0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        margin-bottom: 8px;
        height: 100%;
    }
    
    /* Indicadores de Trazabilidad */
    .person-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 6px 0;
        border-bottom: 1px solid #F0F2F5;
    }
    
    .status-pill {
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    
    /* Animación de Latido para Nodos Activos */
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    .live-dot { height: 8px; width: 8px; background-color: #30D158; border-radius: 50%; display: inline-block; animation: pulse 2s infinite; }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE DATOS DINÁMICOS
if 'init' not in st.session_state: st.session_state.init = True

# --- HEADER COMPACTO ---
h1, h2, h3 = st.columns([2, 1, 1])
with h1:
    st.markdown("<h3 style='margin:0; color:#5E5CE6;'>🛰️ AIHUMANITY MASTER: TENIENTE SUBT.</h3>", unsafe_allow_html=True)
with h2:
    st.markdown(f"<div style='text-align:right;'><b>OPERATIVIDAD:</b> <span class='live-dot'></span> 99.8%</div>", unsafe_allow_html=True)
with h3:
    st.markdown(f"<div style='text-align:right;'>{datetime.now().strftime('%H:%M:%S')} | TURNO B</div>", unsafe_allow_html=True)

# 4. GRID PRINCIPAL (REORGANIZADO POR DIMENSIONES)
row1_col1, row1_col2, row1_col3, row1_col4, row1_col5 = st.columns([1,1,1,1,1])
with row1_col1: st.metric("META CERO", "96.4%", "+0.2")
with row1_col2: st.metric("MP10 (µg/m³)", "38.2", "-4.1")
with row1_col3: st.metric("MP2.5 (µg/m³)", "12.5", "-0.8")
with row1_col4: st.metric("VIENTO NE", "22 km/h", "ESTABLE")
with row1_col5: st.metric("HUMEDAD", "45%", "OK")

st.markdown("---")

# ZONA DE OPERACIONES (DISTRIBUCIÓN 25% | 50% | 25%)
left_op, center_op, right_op = st.columns([1, 2, 1])

# --- MÓDULO: TRAZABILIDAD DE PERSONAL Y ADEEPMINERS ---
with left_op:
    st.markdown("<div class='module-box'>", unsafe_allow_html=True)
    st.markdown("<b>👥 TRAZABILIDAD PERSONAL (HSE)</b>", unsafe_allow_html=True)
    personal_data = [
        ("J. Pérez", "G-4", "SEGURO", "#30D158"),
        ("M. Soto", "CH-1", "ALERTA", "#FF9500"),
        ("A. León", "STK-2", "SEGURO", "#30D158"),
        ("R. Díaz", "G-4", "SEGURO", "#30D158"),
        ("C. Vega", "N-1", "DANGER", "#FF3B30")
    ]
    for nombre, zona, status, color in personal_data:
        st.markdown(f"""
        <div class='person-row'>
            <span>{nombre} <small style='color:grey;'>({zona})</small></span>
            <span class='status-pill' style='background:{color}; color:white;'>{status}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><b>📡 STATUS ADEEPMINERS</b>", unsafe_allow_html=True)
    st.caption("Nodo 01-ESP32: 🟢 Activo | RSSI: -65dBm")
    st.caption("Nodo 02-ESP32: 🟢 Activo | RSSI: -72dBm")
    st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO: RADAR HSE INTERACTIVO (ECHART) ---
with center_op:
    st.markdown("<div class='module-box'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:bold; margin:0;'>RADAR DE RIESGO OPERATIVO ACUMULATIVO (IRO)</p>", unsafe_allow_html=True)
    
    options = {
        "radar": {
            "indicator": [
                {"name": "POLVO (MP)", "max": 100},
                {"name": "VIENTO", "max": 100},
                {"name": "GASES", "max": 100},
                {"name": "TRAZABILIDAD", "max": 100},
                {"name": "GEOMECÁNICA", "max": 100},
                {"name": "CHECKLIST", "max": 100},
            ],
            "splitNumber": 4,
            "axisLine": {"lineStyle": {"color": "#E5E9F0"}},
            "splitLine": {"lineStyle": {"color": "#E5E9F0"}},
        },
        "series": [{
            "type": "radar",
            "data": [{
                "value": [42, 35, 20, 95, 15, 88],
                "name": "Riesgo Actual",
                "areaStyle": {"color": "rgba(94, 92, 230, 0.3)"},
                "lineStyle": {"color": "#5E5CE6", "width": 3},
                "itemStyle": {"color": "#5E5CE6"}
            }]
        }]
    }
    st_echarts(options=options, height="300px")
    
    # Mapa compacto integrado
    st.markdown("<b>📍 MAPA DE CALOR SECTORIAL</b>", unsafe_allow_html=True)
    map_data = pd.DataFrame(np.random.randn(8, 2) / [300, 300] + [-34.05, -70.45], columns=['lat', 'lon'])
    st.map(map_data, height=180)
    st.markdown("</div>", unsafe_allow_html=True)

# --- MÓDULO: CHECKEO Y REPORTES ---
with right_op:
    st.markdown("<div class='module-box'>", unsafe_allow_html=True)
    st.markdown("<b>📝 CHECKEO DIGITAL HSE</b>", unsafe_allow_html=True)
    st.checkbox("EPP Completo (Turno)", value=True)
    st.checkbox("Test de Alcohol/Fatiga", value=True)
    st.checkbox("Ventilación Verificada", value=False)
    st.button("ENVIAR REPORTE KPI", use_container_width=True)
    
    st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)
    st.markdown("<b>⚠️ ALERTAS ACTIVAS</b>", unsafe_allow_html=True)
    st.error("G-4: Saturación de Polvo")
    st.warning("P-1: Mantenimiento Dozer")
    
    st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)
    st.markdown("<b>📊 KPI SEMANAL</b>", unsafe_allow_html=True)
    st.line_chart(np.random.randn(10, 1), height=100)
    st.markdown("</div>", unsafe_allow_html=True)

# 5. BARRA DE ACCIÓN INFERIOR
st.markdown("---")
f1, f2, f3 = st.columns([2,1,1])
with f1: st.button("🚨 STOP-WORK AUTHORITY (DETENCIÓN TOTAL)", type="secondary", use_container_width=True)
with f2: st.button("📡 RESET NODOS", use_container_width=True)
with f3: st.button("🛠️ ADMIN DIAGNÓSTICO", use_container_width=True)

# REFRESH PARA INTERACTIVIDAD
time.sleep(1.5)
st.rerun()
import streamlit as st
import pandas as pd
import numpy as np
import requests
from streamlit_echarts import st_echarts
import plotly.graph_objects as go
from scipy.stats import multivariate_normal
from datetime import datetime
import time

# 1. SETUP DE PÁGINA (ESTILO BLINDADO)
st.set_page_config(page_title="AIH | ADMS & MET-SISMIC", layout="wide", initial_sidebar_state="expanded")

# 2. MOTOR DE DATOS REAL-TIME (API METEOROLÓGICA)
# Nota: Aquí se usaría una API Key de OpenWeatherMap. Por ahora simulamos la estructura real.
def get_real_weather():
    # Simulación de llamada a API: https://api.openweathermap.org/data/2.5/weather?lat=-34.05&lon=-70.45
    weather_data = {
        "temp": 22.5,
        "wind_speed": 18.4 + np.random.uniform(-2, 2),
        "wind_deg": 225, # Suroeste
        "hum": 58,
        "press": 1012
    }
    return weather_data

# 3. LÓGICA DE NAVEGACIÓN
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1684/1684375.png", width=60)
    st.title("SISTEMA ADMS")
    page = st.selectbox("MÓDULO SELECCIONADO:", ["🏠 Dashboard Principal", "🌪️ Analizador ADMS", "📉 Monitor Sismográfico"])
    st.divider()
    st.info("📡 STATUS: Conectado a Estación Rancagua / El Teniente")

# 4. PÁGINA: ANALIZADOR ADMS (DISPERSIÓN DE POLVO)
if page == "🌪️ Analizador ADMS":
    st.markdown("<h2 style='color:#5E5CE6;'>🌪️ MODELAMIENTO DE DISPERSIÓN ATMOSFÉRICA (ADMS)</h2>", unsafe_allow_html=True)
    
    weather = get_real_weather()
    
    # FILA 1: TELEMETRÍA REAL
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("VIENTO ACTUAL", f"{round(weather['wind_speed'],1)} km/h", f"{weather['wind_deg']}°")
    with c2: st.metric("ESTABILIDAD PASQUILL", "Clase B", "Inestable")
    with c3: st.metric("PUNTO ROCÍO", "12.4°C", "Normal")
    with c4: st.metric("FACTOR DISPERSIÓN", "Alta", "Protocolo 2")

    st.divider()

    # FILA 2: EL RADAR ADMS (MODELO GAUSSIANO)
    col_map, col_controls = st.columns([2, 1])

    with col_map:
        st.markdown("### 🗺️ Proyección de Pluma de Polvo (Real-Time)")
        
        # Simulación de Pluma Gaussiana
        x, y = np.mgrid[-50:50:1, -50:50:1]
        pos = np.dstack((x, y))
        # La pluma se estira según la velocidad del viento y gira según la dirección
        rv = multivariate_normal([0, 0], [[weather['wind_speed']*2, 0], [0, 5]])
        z = rv.pdf(pos)
        
        fig = go.Figure(data=[go.Contour(z=z, colorscale='Viridis', showscale=False)])
        fig.update_layout(title="Concentración MP10 Proyectada (Suelo)", height=450, 
                          xaxis_visible=False, yaxis_visible=False, paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        

    with col_controls:
        st.markdown("<div style='background:white; padding:20px; border-radius:15px;'>", unsafe_allow_html=True)
        st.write("### ⚙️ Parámetros ADMS")
        source_type = st.selectbox("Fuente de Polvo", ["Chancado Primario", "Tránsito Camiones", "Stockpiles"])
        stack_height = st.slider("Altura de Emisión (m)", 0, 50, 15)
        st.divider()
        st.write("### 🛡️ Acción Sugerida")
        if weather['wind_speed'] > 15:
            st.error("⚠️ CRÍTICO: Dispersión hacia Zona de Dormitorios")
            st.button("ACTIVAR NEBULIZADORES SECTOR 4")
        st.markdown("</div>", unsafe_allow_html=True)

# 5. PÁGINA: MONITOR SISMOGRÁFICO (VIBRACIÓN TRL-4)
elif page == "📉 Monitor Sismográfico":
    st.markdown("<h2 style='color:#30D158;'>📉 MONITOR SISMOGRÁFICO DE TALUDES</h2>", unsafe_allow_html=True)
    
    col_sismo, col_data = st.columns([2, 1])
    
    with col_sismo:
        # Gráfico dinámico de aceleración (g)
        sismo_data = pd.DataFrame(np.random.randn(100, 1) * 0.01, columns=['Aceleración (g)'])
        st.line_chart(sismo_data, height=400)
        
        
    with col_data:
        st.write("### 📏 Análisis de Vibración")
        st.metric("VPP (Vel. Pico Partícula)", "1.2 mm/s", "Bajo")
        st.metric("Frecuencia Dominante", "15 Hz", "Normal")
        st.info("Estatus: Sin riesgo de desprendimiento (Raveling) en Sector Alpha.")

# 6. FOOTER Y REFRESH
time.sleep(1)
st.rerun()
