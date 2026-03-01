import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. CONFIGURACIÓN CUPERTINO
st.set_page_config(page_title="AIH Master | El Teniente", layout="wide", initial_sidebar_state="collapsed")

# 2. MOTOR DE ESTILOS CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'SF Pro Display', sans-serif; background-color: #F5F5F7; color: #1D1D1F; }
    .stApp { background-color: #F5F5F7; }
    .mod-card { background: rgba(255, 255, 255, 0.9); border-radius: 24px; padding: 22px; box-shadow: 0 10px 40px rgba(0,0,0,0.03); border: 1px solid rgba(255,255,255,0.6); margin-bottom: 20px; transition: all 0.3s; }
    .progress-bg { width: 100%; background-color: #E5E5EA; border-radius: 10px; height: 14px; margin: 10px 0; }
    .progress-fill { height: 14px; border-radius: 10px; transition: width 0.5s ease-in-out; }
    </style>
    """, unsafe_allow_html=True)

# 3. MEMORIA DE SENSORES (SESSION STATE PARA FLUIDEZ)
# Esto evita que los datos salten a lo loco y crea un efecto de "respiración" natural
if 'mp10' not in st.session_state:
    st.session_state.mp10 = 38.0
    st.session_state.wind = 22.0
    st.session_state.stab = 98.0
    st.session_state.gas = 15.0

def update_sensors():
    # Caminata aleatoria (Random Walk) simulando telemetría real
    st.session_state.mp10 = max(0, st.session_state.mp10 + np.random.uniform(-1.5, 1.8))
    st.session_state.wind = max(0, st.session_state.wind + np.random.uniform(-1.0, 1.2))
    st.session_state.stab = min(100, max(0, st.session_state.stab + np.random.uniform(-0.1, 0.1)))
    st.session_state.gas = max(0, st.session_state.gas + np.random.uniform(-0.5, 0.6))
    
    # Motor de Riesgo
    risk = (st.session_state.mp10*0.3) + ((100-st.session_state.stab)*2.5) + (st.session_state.gas*0.2) + (st.session_state.wind*0.1)
    return min(100, risk)

# 4. STATUS BAR & CONTROL DE TELEMETRÍA
col_top1, col_top2 = st.columns([3, 1])
with col_top1:
    st.markdown(f"""
        <div style="padding: 10px 20px; background: white; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.02);">
            <span style="font-weight:600; color:#5E5CE6;">📍 EL TENIENTE SUBTERRÁNEA</span> | 
            <span style="color:#8E8E93;">{datetime.now().strftime('%H:%M:%S')} CLT</span>
        </div>
        """, unsafe_allow_html=True)
with col_top2:
    # EL BOTÓN MÁGICO QUE DA VIDA AL DASHBOARD
    live_feed = st.toggle("📡 Telemetría en Vivo (Auto-Sync)", value=True)

# Actualizar variables si el feed está activo
if live_feed:
    risk_index = update_sensors()
else:
    risk_index = (st.session_state.mp10*0.3) + ((100-st.session_state.stab)*2.5) + (st.session_state.gas*0.2) + (st.session_state.wind*0.1)

meta_zero_val = max(0, 100 - (risk_index * 0.4))

# 5. DASHBOARD LAYOUT
col_stats, col_radar, col_alerts = st.columns([1, 2, 1])

# --- MÓDULO: META CERO & SENSORES ---
with col_stats:
    # Color dinámico para la barra
    bar_color = "#30D158" if meta_zero_val > 80 else "#FF9500" if meta_zero_val > 50 else "#FF3B30"
    st.markdown(f"""
        <div class="mod-card">
            <p style="color:#8E8E93; font-size:0.8rem; margin:0; font-weight:600;">OBJETIVO META CERO</p>
            <h2 style="color:{bar_color}; margin:0;">{round(meta_zero_val,1)}%</h2>
            <div class="progress-bg"><div class="progress-fill" style="width: {meta_zero_val}%; background: {bar_color};"></div></div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="mod-card">
            <p style="color:#8E8E93; font-size:0.8rem; margin:0; font-weight:600;">SENSOR MP10 (POLVO)</p>
            <h3 style="margin:0; color:#1D1D1F;">{round(st.session_state.mp10, 1)} <small>µg/m³</small></h3>
        </div>
        """, unsafe_allow_html=True)

# --- MÓDULO CENTRAL: RADAR DINÁMICO ---
with col_radar:
    st.markdown('<div class="mod-card" style="text-align:center;">', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:600; color:#8E8E93;'>ÍNDICE DE RIESGO GLOBAL (HSE-STOP-WORK)</p>", unsafe_allow_html=True)
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[st.session_state.mp10, 100-st.session_state.stab, st.session_state.gas, st.session_state.wind, 25],
        theta=['Polvo MP10', 'Geomecánica (Raveling)', 'Gases CO/NOx', 'Viento/Disp.', 'Tránsito'],
        fill='toself',
        fillcolor='rgba(94, 92, 230, 0.3)',
        line=dict(color='#5E5CE6', width=3)
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        margin=dict(t=20, b=20, l=40, r=40),
        paper_bgcolor='rgba(0,0,0,0)',
        height=350
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Alerta visual central
    status_color = "#30D158" if risk_index < 40 else "#FF9500" if risk_index < 70 else "#FF3B30"
    st.markdown(f"<h2 style='color:{status_color}; margin:0;'>IRG: {round(risk_index, 1)}</h2>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- MÓDULO: MAPA Y GEOLOCALIZACIÓN ---
with col_alerts:
    st.markdown('<div class="mod-card">', unsafe_allow_html=True)
    st.markdown("<p style='font-weight:600; color:#8E8E93;'>ADEEPMINERS TRACKING</p>", unsafe_allow_html=True)
    # Mapa que cambia ligeramente simulando movimiento
    lat_jitter = np.random.uniform(-0.002, 0.002, 5)
    lon_jitter = np.random.uniform(-0.002, 0.002, 5)
    map_df = pd.DataFrame({
        'lat': [-34.08] * 5 + lat_jitter,
        'lon': [-70.46] * 5 + lon_jitter
    })
    st.map(map_df, zoom=12, height=200)
    st.button("🆘 STOP-WORK ALERT", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. BUCLE DE ACTUALIZACIÓN (EL MOTOR DE VIDA)
# Si el toggle está activo, la app espera 1.5 segundos y se recarga sola.
if live_feed:
    time.sleep(1.5)
    st.rerun()
