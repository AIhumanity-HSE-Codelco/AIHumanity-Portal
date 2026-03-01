import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. SETUP DE ALTA DENSIDAD
st.set_page_config(page_title="AIH | Control Tower Teniente", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE ALTA DENSIDAD (TEXTO MÁS PEQUEÑO Y TARJETAS COMPACTAS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F4F7F9; font-size: 0.95rem; }
    .stApp { background-color: #F4F7F9; }
    
    /* Tarjetas Compactas */
    .mini-card {
        background: white;
        padding: 12px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        border: 1px solid #E1E4E8;
        margin-bottom: 10px;
    }
    .status-dot { height: 8px; width: 8px; border-radius: 50%; display: inline-block; margin-right: 5px; }
    .bg-green { background-color: #30D158; }
    .bg-orange { background-color: #FF9500; }
    .bg-red { background-color: #FF3B30; }
    
    /* Grid Personalizado */
    .label-micro { color: #8E8E93; font-size: 0.7rem; font-weight: 600; text-transform: uppercase; }
    .value-bold { font-weight: 700; color: #1D1D1F; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER TECNOLÓGICO
h1, h2, h3 = st.columns([2, 1, 1])
with h1:
    st.markdown("<h2 style='margin:0; color:#5E5CE6;'>🛡️ AIHUMANITY MASTER CONTROL</h2>", unsafe_allow_html=True)
with h2:
    st.markdown(f"<p style='margin:0; text-align:right;'><b>OPERADOR:</b> AIH-ADMIN-01</p>", unsafe_allow_html=True)
with h3:
    st.markdown(f"<p style='margin:0; text-align:right;'>{datetime.now().strftime('%d/%m %H:%M:%S')}</p>", unsafe_allow_html=True)

st.write("---")

# 4. FILA 1: KPIs GLOBALES (6 COLUMNAS)
kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
with kpi1: st.metric("Meta Cero", "94.2%", "+0.5")
with kpi2: st.metric("MP10 Prom.", "42.1", "-2.3")
with kpi3: st.metric("Personal Subt.", "142", "Activos")
with kpi4: st.metric("Disponibilidad Nodos", "99.8%", "OK")
with kpi5: st.metric("Viento Max.", "28 km/h", "NE")
with kpi6: st.metric("IRO Global", "32.1", "Normal", delta_color="inverse")

# 5. FILA 2: EL CORAZÓN DE LA INFORMACIÓN (DENSIDAD +35%)
col_left, col_center, col_right = st.columns([1.2, 2.5, 1.3])

# --- COLUMNA IZQUIERDA: TRAZABILIDAD Y FLOTA ---
with col_left:
    st.markdown("### 👥 Trazabilidad Personal")
    # Generamos data densa
    for i in range(4):
        st.markdown(f"""
        <div class="mini-card">
            <span class="label-micro">Operador {i+1}</span><br>
            <span class="value-bold">👷 ID-00{120+i}</span> | <span style="font-size:0.8rem;">G-4 / Nivel 2</span>
            <div style="margin-top:5px;"><span class="status-dot bg-green"></span>Seguro</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🚜 Flota Activa")
    st.markdown("""
    <div class="mini-card" style="border-left: 4px solid #5E5CE6;">
        <b>LHD-412 (Chancado)</b><br><span class="label-micro">Temp Motor: 88°C | Ocupación: 92%</span>
    </div>
    <div class="mini-card" style="border-left: 4px solid #FF9500;">
        <b>Dozing D10 (Fase 4)</b><br><span class="label-micro">Alerta Polución Cercana</span>
    </div>
    """, unsafe_allow_html=True)

# --- COLUMNA CENTRAL: RADAR Y MAPA DE CALOR ---
with col_center:
    st.markdown("<p style='text-align:center; font-weight:bold; margin:0;'>RADAR DE RIESGO OPERATIVO ACUMULADO</p>", unsafe_allow_html=True)
    
    # Radar más complejo con 7 ejes
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[40, 25, 30, 80, 90, 45, 20],
        theta=['Polvo', 'Gases', 'Fatiga', 'EPP', 'Geom.', 'Tránsito', 'Ruido'],
        fill='toself', fillcolor='rgba(94, 92, 230, 0.2)', line=dict(color='#5E5CE6')
    ))
    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), height=350, margin=dict(t=30, b=30))
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Mapa de Geolocalización (Vista de Planta)
    st.markdown("<b>📍 Geolocalización Nodos Adeepminers (Sector Alpha)</b>", unsafe_allow_html=True)
    map_data = pd.DataFrame(np.random.randn(15, 2) / [250, 250] + [-34.05, -70.45], columns=['lat', 'lon'])
    st.map(map_data, height=250)

# --- COLUMNA DERECHA: CHECKLISTS Y ALERTAS CRÍTICAS ---
with col_right:
    st.markdown("### 📝 Checkeo Digital")
    with st.container():
        st.markdown("<div class='mini-card'>", unsafe_allow_html=True)
        st.checkbox("Charla 5 min (Turno B)", value=True)
        st.checkbox("Inspección LHD-412", value=True)
        st.checkbox("Test Gases Galería N-4", value=False)
        st.button("VALIDAR PROTOCOLOS", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 🚨 Log de Eventos")
    st.error("08:42 - Alerta MP10 Sector 2")
    st.warning("08:15 - Cambio turno completado")
    st.info("07:50 - Calibración Nodo ESP-32 OK")
    
    # Matriz de Riesgo 5x5 simplificada
    st.markdown("### 📊 Matriz de Criticidad")
    risk_data = np.random.randint(1, 5, size=(5, 5))
    st.dataframe(pd.DataFrame(risk_data, columns=['C1','C2','C3','C4','C5']), height=150)

# 6. FOOTER INDUSTRIAL
st.divider()
st.markdown("""
<div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: #8E8E93;">
    <span>AIHumanity Master | TRL-3 Prototype | No masivo</span>
    <span>Sincronización Cloud: OK (0.2s latencia)</span>
    <span>Arquitectura antes que escala</span>
</div>
""", unsafe_allow_html=True)

# 7. ANIMACIÓN DE DATOS (Mantiene el entorno vivo)
time.sleep(2)
st.rerun()
