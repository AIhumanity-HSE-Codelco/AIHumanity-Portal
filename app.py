import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. CONFIGURACIÓN DE INTERFAZ CUPERTINO (WHITE/SOFT)
st.set_page_config(
    page_title="AIH Master | El Teniente HSE",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. MOTOR DE ESTILOS CSS (CUSTOM UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'SF Pro Display', sans-serif; background-color: #F5F5F7; color: #1D1D1F; }
    .stApp { background-color: #F5F5F7; }
    
    /* Tarjetas Modulares */
    .mod-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 24px;
        padding: 22px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.03);
        border: 1px solid rgba(255,255,255,0.6);
        margin-bottom: 20px;
    }
    
    /* Barra de Progreso Meta Cero */
    .progress-bg { width: 100%; background-color: #E5E5EA; border-radius: 10px; height: 14px; margin: 10px 0; }
    .progress-fill { height: 14px; border-radius: 10px; background: linear-gradient(90deg, #30D158, #34C759); transition: width 1s ease-in-out; }
    
    /* Botonera Digital */
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        background: #F2F2F7;
        color: #5E5CE6;
        border: 1px solid #D1D1D6;
        padding: 12px;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton>button:hover { background: #5E5CE6; color: white; border: none; transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# 3. MOTOR CENTRAL DE ÍNDICE DE RIESGO (AIH-CORE ENGINE)
def get_live_metrics():
    # Simulación de sensores Adeepminers
    mp10 = 38.5 + np.random.uniform(-4, 6)
    viento = 22 + np.random.uniform(-5, 5)
    estabilidad = 98.4 - (mp10 * 0.04)
    gases = 15 + np.random.uniform(0, 10)
    
    # Cálculo de Riesgo Acumulado (Pesos: Geo 40%, Polvo 30%, Gases 20%, Viento 10%)
    risk_index = (mp10*0.3) + ((100-estabilidad)*2.5) + (gases*0.2) + (viento*0.1)
    return round(mp10, 1), round(viento, 1), round(estabilidad, 1), round(gases, 1), round(risk_index, 1)

mp10, wind, stab, gas, risk = get_live_metrics()
meta_zero_val = 100 - (risk * 0.4)

# 4. MODULO 1 & 2: STATUS BAR & REGIONAL TIME
st.markdown(f"""
    <div style="display: flex; justify-content: space-between; padding: 10px 20px; background: white; border-radius: 15px; margin-bottom: 25px; box-shadow: 0 2px 10px rgba(0,0,0,0.02);">
        <span style="font-weight:600; color:#5E5CE6;">📍 EL TENIENTE SUBTERRÁNEA</span>
        <span style="color:#8E8E93;">{datetime.now().strftime('%d/%m/%Y | %H:%M:%S')} CLT</span>
        <span style="color:#30D158; font-weight:600;">● SISTEMA SINCRONIZADO</span>
    </div>
    """, unsafe_allow_html=True)

# 5. DASHBOARD LAYOUT
col_stats, col_radar, col_alerts = st.columns([1, 2, 1])

# --- COLUMNA IZQUIERDA: META CERO & VIENTO ---
with col_stats:
    st.markdown(f"""
        <div class="mod-card">
            <p style="color:#8E8E93; font-size:0.8rem; margin:0;">META CERO OBJETIVO</p>
            <h2 style="color:#30D158; margin:0;">{round(meta_zero_val,1)}%</h2>
            <div class="progress-bg"><div class="progress-fill" style="width: {meta_zero_val}%;"></div></div>
            <p style="font-size:0.75rem; color:#1D1D1F;">Días sin incidentes: <b>442</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="mod-card">
            <p style="color:#8E8E93; font-size:0.8rem; margin:0;">VIENTO Y DISPERSIÓN</p>
            <h3 style="margin:0; color:#1D1D1F;">{wind} <small>km/h</small></h3>
            <p style="color:#5E5CE6; font-size:0.8rem;">Vector: NE | Dispersión Baja</p>
        </div>
        """, unsafe_allow_html=True)

# --- COLUMNA CENTRAL: RADAR HSE-STOP-WORK ---
with col_radar:
    st.markdown('<div class="mod-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:600;'>ÍNDICE DE RIESGO GLOBAL ACUMULATIVO</p>", unsafe_allow_html=True)
    
    # Plotly Radar Chart
    categories = ['Polvo MP10', 'Geomecánica', 'Gases CO/NOx', 'Viento/Disp.', 'Tránsito']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[mp10, 100-stab, gas, wind, 25],
        theta=categories,
        fill='toself',
        fillcolor='rgba(94, 92, 230, 0.2)',
        line=dict(color='#5E5CE6', width=3)
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        margin=dict(t=30, b=30, l=40, r=40),
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Dinámica de Color de Riesgo
    status_color = "#30D158" if risk < 40 else "#FF9500" if risk < 70 else "#FF3B30"
    st.markdown(f"<h1 style='color:{status_color}; margin:0;'>{risk} IRG</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLUMNA DERECHA: ALERTAS & REPORTES ---
with col_alerts:
    st.markdown('<div class="mod-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:600;'>REPORTES HSE DIGITALES</p>", unsafe_allow_html=True)
    st.button("📥 Descargar Reporte Turno")
    st.button("📉 Ver KPIs Históricos")
    st.divider()
    st.error("⚠️ ALERTA: Ventilación G-4")
    st.warning("☁️ CLIMA: Rachas 40km/h")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. MODULOS INFERIORES: GEOLOCALIZACIÓN & BOTONERA
st.markdown("### 📍 Geolocalización Adeepminers (Red Intra-Mina)")
m_map, m_btns = st.columns([3, 1])

with m_map:
    # Simulación de puntos Adeepminers en El Teniente
    map_df = pd.DataFrame(
        np.random.randn(8, 2) / [180, 180] + [-34.05, -70.45],
        columns=['lat', 'lon']
    )
    st.map(map_df, zoom=13)

with m_btns:
    st.write("### Panel Digital")
    st.button("🔄 Sync Nodos")
    st.button("📡 Calibrar GPS")
    st.button("🆘 STOP-WORK", type="primary")

st.markdown("---")
st.caption("AIHumanity Core v4.0 | El Teniente Subterránea | Software Robustness: High Availability")
