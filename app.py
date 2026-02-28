import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH-MASTER COMMAND", layout="wide")

# --- 2. MOTOR DE TIEMPO (RESTAURADO Y FIJADO) ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)

# --- 3. CSS: ESTILO VIBRANTE INTEGRADO ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #ffffff; }}
    .header-box {{ 
        background: linear-gradient(90deg, #6c5ce7, #ff00ff); 
        padding: 25px; border-radius: 20px; text-align: center; color: white; 
        box-shadow: 0 10px 25px rgba(108, 92, 231, 0.3); margin-bottom: 20px;
    }}
    .main-clock {{ font-size: 80px !important; font-weight: 900; margin: 0; line-height: 1; }}
    .risk-bar-bg {{ width: 100%; background: #eee; border-radius: 15px; height: 35px; overflow: hidden; margin: 10px 0; }}
    .risk-bar-fill {{ height: 100%; text-align: center; color: white; font-weight: bold; line-height: 35px; transition: 1s; }}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR: LÓGICA DE RUTEO ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("⚙️ CONTROL PANEL")
    st.divider()
    
    # Menú de Portal (Ruteo Principal)
    room_mode = st.selectbox("PORTAL SELECTION:", 
                              ["HSE CONTROL ROOM", "ADMS TACTICAL RESPONSE", "ADMIN CONFIG & EXPORT"])
    
    st.divider()
    
    # Menú de Unidades
    region = st.selectbox("REGION:", ["CODELCO NORTE", "CODELCO CENTRO", "ANTOFAGASTA"])
    unidades = {
        "CODELCO NORTE": {"Chuquicamata": [-22.3, -68.9], "Radomiro Tomic": [-22.2, -68.8]},
        "CODELCO CENTRO": {"El Teniente": [-34.1, -70.4], "Andina": [-33.1, -70.2]},
        "ANTOFAGASTA": {"Escondida": [-24.2, -69.0]}
    }
    faena_sel = st.selectbox("UNIDAD OPERATIVA:", list(unidades[region].keys()))
    coords = unidades[region][faena_sel]

    st.divider()
    st.info(f"Sincronización: 70k Nodos AIDeepMiner\nUser: AIH-Master")

# --- 5. CABECERA DINÁMICA ---
st.markdown(f"""
    <div class="header-box">
        <p class="main-clock">{now.strftime('%H:%M:%S')}</p>
        <p style="font-size: 20px; opacity: 0.9;">{now.strftime('%A, %d de %B %Y')} | PORTAL: {room_mode}</p>
    </div>
""", unsafe_allow_html=True)

# --- 6. LÓGICA DE PORTALES (PANTALLAS INDEPENDIENTES) ---

# --- PORTAL A: HSE CONTROL ROOM ---
if room_mode == "HSE CONTROL ROOM":
    st.header(f"🚀 MONITOR GLOBAL: {faena_sel}")
    
    # Datos Simulados
    viento = np.random.randint(10, 85)
    polvo = np.random.randint(20, 95)
    riesgo = int((viento * 0.4) + (polvo * 0.6))
    
    # Barra de Riesgo Cero
    color_r = "#ff00ff" if riesgo > 75 else "#6c5ce7" if riesgo > 40 else "#00cec9"
    st.markdown(f"**OBJECTIVE ZERO OPERATIONAL RISK: {riesgo}%**")
    st.markdown(f'<div class="risk-bar-bg"><div class="risk-bar-fill" style="width: {riesgo}%; background: {color_r};">{riesgo}%</div></div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🌪️ PM10", f"{polvo} µg/m³")
    c2.metric("🌬️ VIENTO", f"{viento} km/h")
    c3.metric("👷 EPP", "98% OK")
    c4.metric("📍 NODOS", "70,000")

    st.divider()
    col_left, col_right = st.columns([2, 1])
    with col_left:
        st.subheader("🛰️ Teledetección Táctica")
        m = folium.Map(location=coords, zoom_start=15, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
        folium.Circle(coords, radius=500, color='#ff00ff', fill=True).add_to(m)
        folium_static(m, width=700, height=400)
    with col_right:
        st.subheader("🎯 Risk Drivers")
        st.error("Probabilidad: ALTA")
        st.warning("Factor: Polvo en Suspensión")
        

# --- PORTAL B: ADMS TACTICAL RESPONSE ---
elif room_mode == "ADMS TACTICAL RESPONSE":
    st.header(f"💧 ADMS MITIGATION: {faena_sel}")
    st.subheader("Módulo de Mitigación y Supresión de Polvo")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 📊 Status de Supresión")
        st.write("- **Aspersores Sector Norte:** ACTIVOS")
        st.write("- **Nebulizadores Chancado:** 85% Eficiencia")
        st.progress(85)
    with col_b:
        st.markdown("### 📈 Forecast de Dispersión")
        df_adms = pd.DataFrame({'T': range(10), 'P': np.random.randint(20, 90, 10)})
        st.plotly_chart(px.area(df_adms, x='T', y='P', color_discrete_sequence=['#ff00ff']), use_container_width=True)

# --- PORTAL C: ADMIN CONFIG & EXPORT ---
elif room_mode == "ADMIN CONFIG & EXPORT":
    st.header("⚙️ GOBERNANZA Y CONFIGURACIÓN")
    st.subheader("Exportación de Evidencia Audit-Ready")
    
    st.write("Seleccione el tipo de log para despacho desde **aeserviseu@gmail.com**:")
    
    c_e1, c_e2, c_e3 = st.columns(3)
    c_e1.button("📥 EXPORT FULL JSON")
    c_e2.button("📊 EXPORT KPI CSV")
    c_e3.button("📜 EXPORT HSE LOG")
    
    st.divider()
    st.subheader("📜 Auditoría de Sistema")
    log_data = pd.DataFrame([{
        "Timestamp": now.strftime("%H:%M:%S"),
        "Unidad": faena_sel,
        "Acción": "Sync 70k Nodos",
        "Admin": "AIH-Master",
        "Status": "CERTIFIED"
    }])
    st.table(log_data)

# --- FOOTER ---
st.divider()
st.caption("AIH-MASTER COMMAND v16.0 | Open Codelco | Uniting Technology Belgium")
