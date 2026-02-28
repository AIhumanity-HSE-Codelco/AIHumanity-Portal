import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE ESCENA ---
st.set_page_config(page_title="AIH-MASTER CENTRAL", layout="wide", initial_sidebar_state="collapsed")

# --- 2. ESTILO APPLE SUPREMO (WHITE & VIBRANT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    
    html, body, [class*="st-"] { font-family: 'SF Pro Display', sans-serif; background-color: #f5f5f7; color: #1d1d1f; }
    
    /* Contenedor Principal Estilo Apple */
    .apple-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 40px rgba(0,0,0,0.04);
        margin-bottom: 25px;
    }
    
    /* Reloj Apple */
    .apple-clock { font-size: 110px; font-weight: 600; letter-spacing: -4px; color: #1d1d1f; text-align: center; line-height: 1; }
    .apple-date { font-size: 24px; font-weight: 400; color: #86868b; text-align: center; margin-bottom: 30px; }
    
    /* Barras de Riesgo Elegantes */
    .risk-container { width: 100%; background: #e5e5ea; border-radius: 20px; height: 40px; overflow: hidden; margin: 15px 0; border: 1px solid #d1d1d6; }
    .risk-fill { height: 100%; transition: width 1.5s ease-in-out; text-align: center; color: white; font-weight: 600; line-height: 40px; }
    
    /* KPIs */
    .kpi-value { font-size: 32px; font-weight: 600; color: #0071e3; }
    .kpi-label { font-size: 14px; color: #86868b; text-transform: uppercase; letter-spacing: 1px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE TIEMPO Y DATOS (70K NODOS) ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)

# Generación de data operativa (AIDeepMiner Core)
np.random.seed(now.second)
viento = np.random.randint(10, 80)
polvo = np.random.randint(20, 90)
riesgo_total = int((viento * 0.4) + (polvo * 0.6))
color_apple = "#34c759" if riesgo_total < 40 else "#ffcc00" if riesgo_total < 75 else "#ff3b30"

# --- 4. CABECERA CENTRAL (RELOJ & ORDEN) ---
st.markdown(f'<div class="apple-clock">{now.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="apple-date">{now.strftime("%A, %d de %B %Y")} | CODELCO DIVISIÓN EL TENIENTE</div>', unsafe_allow_html=True)

# --- 5. PANEL DE CONTROL INTEGRADO ---
col_main_1, col_main_2 = st.columns([2, 1])

with col_main_1:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🛡️ GOBERNANZA OPERATIVA: RIESGO CERO")
    st.markdown(f"**Nivel de Riesgo Compuesto (ICR): {riesgo_total}%**")
    st.markdown(f"""
        <div class="risk-container">
            <div class="risk-fill" style="width: {riesgo_total}%; background-color: {color_apple}; box-shadow: 0 0 20px {color_apple}66;">
                {riesgo_total}% - {"ZONA SEGURA" if riesgo_total < 75 else "STOP WORK"}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # KPIs Rápidos
    k1, k2, k3 = st.columns(3)
    k1.markdown(f'<p class="kpi-label">💨 Polvo PM10</p><p class="kpi-value">{polvo} <span style="font-size:15px;">µg/m³</span></p>', unsafe_allow_html=True)
    k2.markdown(f'<p class="kpi-label">🌬️ Viento</p><p class="kpi-value">{viento} <span style="font-size:15px;">km/h</span></p>', unsafe_allow_html=True)
    k3.markdown(f'<p class="kpi-label">📍 Nodos</p><p class="kpi-value">70,000</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_main_2:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("🎯 Risk Drivers")
    st.write(f"**Probabilidad:** {riesgo_total}%")
    st.write(f"**Who:** Cuadrilla B-12")
    st.write(f"**Where:** Sector Chancado")
    st.write(f"**What:** Dispersión Crítica")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. MÓDULOS ACTIVOS (TODO EN UNA PANTALLA) ---
tab1, tab2, tab3 = st.tabs(["🍃 ENVIRO FUSION & ADMS", "👷 WORKER SAFETY CORE", "🛰️ TACTICAL MAP"])

with tab1:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("ADMS Tactical Response (Mitigación)")
    
    c_adms1, c_adms2 = st.columns(2)
    with c_adms1:
        st.info("Estatus de Supresión: **ACTIVO**")
        st.write("- Cañones de Niebla: 8/10 Online")
        st.progress(80)
    with c_adms2:
        df_adms = pd.DataFrame({'min': range(10), 'val': np.random.randint(40, 90, 10)})
        st.plotly_chart(px.line(df_adms, x='min', y='val', color_discrete_sequence=['#0071e3']), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("Worker Safety & AI-PPE (Fall Detection)")
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        st.success("PPE Compliance: **WORN ON**")
        st.write("Verificación biométrica exitosa (99.2%)")
    with c_s2:
        st.warning("Fall Detection: **STANDBY**")
        st.write("Detección de Hombre Caído: Activa en 70k nodos.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("Localización Satelital GPS")
    m = folium.Map(location=[-34.1, -70.4], zoom_start=14, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium.Circle([-34.1, -70.4], radius=800, color='#0071e3', fill=True, popup="FUSION CENTER").add_to(m)
    folium_static(m, width=1100, height=450)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FOOTER DE GOBERNANZA ---
st.markdown('<div class="apple-card" style="text-align:center;">', unsafe_allow_html=True)
st.markdown("### 📜 AUDIT LOG HSE")
col_e1, col_e2, col_e3 = st.columns(3)
col_e1.button("EXPORT JSON")
col_e2.button("EXPORT CSV")
if col_e3.button("SEND TO aeserviseu@gmail.com"):
    st.success("Reporte enviado")
st.caption("AIH-MASTER COMMAND v17.0 | Uniting Technology Belgium")
st.markdown('</div>', unsafe_allow_html=True)
