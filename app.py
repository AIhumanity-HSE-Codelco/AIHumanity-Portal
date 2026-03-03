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
