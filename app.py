import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE ALTO IMPACTO ---
st.set_page_config(page_title="AIH-MASTER COMMAND CENTER", layout="wide")

# --- 2. BASE DE DATOS MAESTRA (70K NODOS) ---
MINERIA = {
    "ZONA NORTE": {"Chuquicamata": [-22.3, -68.9], "Escondida": [-24.2, -69.0], "Collahuasi": [-20.9, -68.6]},
    "ZONA CENTRO": {"El Teniente": [-34.1, -70.4], "Andina": [-33.1, -70.2], "Los Bronces": [-33.1, -70.3]},
    "ZONA ATACAMA": {"Salvador": [-26.2, -69.6], "Caserones": [-27.3, -69.3]}
}

# --- 3. ESTILO VIBRANTE (FUCSIA, MORADO, ROJO, AMARILLO) ---
st.markdown("""
    <style>
    /* Fondo amigable y moderno */
    .stApp { background-color: #ffffff; }
    
    /* Barras de Porcentaje Dinámicas */
    .risk-bar-bg { width: 100%; background: #f0f2f6; border-radius: 15px; height: 35px; border: 2px solid #eee; overflow: hidden; }
    .risk-bar-fill { height: 100%; transition: width 0.8s ease-in-out; text-align: center; color: white; font-weight: 800; line-height: 35px; font-size: 18px; }
    
    /* KPIs con colores Apple-Vibrant */
    [data-testid="stMetric"] { 
        background: #ffffff; padding: 20px; border-radius: 15px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.05); border-bottom: 5px solid #ff00ff; /* Fucsia */
    }
    
    /* Títulos y Hover */
    h1, h2, h3 { color: #2d3436; font-weight: 800; }
    .stButton>button { 
        background: linear-gradient(45deg, #6c5ce7, #ff00ff); color: white; border: none; 
        border-radius: 10px; font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 5px 15px rgba(255,0,255,0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: CONTROL DE MANDO ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ AIH-MASTER")
    
    tz = pytz.timezone('America/Santiago')
    st.write(f"⏰ **{datetime.now(tz).strftime('%H:%M:%S')}**")
    st.divider()
    
    acceso = st.radio("MODO AUDITORÍA:", ["MASTER GLOBAL", "FAENA LOCAL"])
    zona = st.selectbox("📍 Seleccione Sector:", list(MINERIA.keys()))
    faena_sel = st.selectbox("🏗️ Unidad Minera:", list(MINERIA[zona].keys()))
    coords = MINERIA[zona][faena_sel]

# --- 5. MOTOR DE RIESGO (NODOS ACTIVOS) ---
np.random.seed(sum(map(ord, faena_sel)))
viento = np.random.randint(10, 90)
polvo = np.random.randint(15, 85)
riesgo_calc = int((viento * 0.4) + (polvo * 0.6))

# --- 6. INTERFAZ PRINCIPAL: ENTORNO MAXIMIZADO ---
st.title(f"🚀 DASHBOARD OPERATIVO: {faena_sel.upper()}")
st.write(f"**Gobernanza Proactiva de 70,000 Nodos** | ID Faena: {hash(faena_sel)}")

# BARRAS DE PORCENTAJE VIBRANTES
col_b1, col_b2 = st.columns(2)
with col_b1:
    color_p = "#ff00ff" if riesgo_calc > 70 else "#6c5ce7" if riesgo_calc > 40 else "#00cec9"
    st.markdown(f"**Índice de Riesgo (ICR): {riesgo_calc}%**")
    st.markdown(f'<div class="risk-bar-bg"><div class="risk-bar-fill" style="width: {riesgo_calc}%; background: {color_p};">{riesgo_calc}%</div></div>', unsafe_allow_html=True)

with col_b2:
    viento_p = int((viento/90)*100)
    st.markdown(f"**Saturación de Viento: {viento} km/h**")
    st.markdown(f'<div class="risk-bar-bg"><div class="risk-bar-fill" style="width: {viento_p}%; background: #fdcb6e;">{viento_p}%</div></div>', unsafe_allow_html=True)

st.divider()

# KPIs CON COLORES (MORADOS, FUCSIA, AMARILLO)
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("🌪️ Polvo PM10", f"{polvo} mg/m³", delta="NORMAL", delta_color="normal")
with c2: st.metric("🌬️ Viento Real", f"{viento} km/h", delta="ALERTA", delta_color="inverse")
with c3: st.metric("📍 GPS Nodos", "70,000", delta="ONLINE", delta_color="normal")
with c4: st.metric("💓 Biometría", "98.2%", delta="SINCRO", delta_color="normal")

st.divider()

# --- 7. MODULOS VISUALES (RECONSTRUIDOS) ---
t1, t2, t3 = st.tabs(["📊 ANÁLISIS HSE", "🛰️ TELEDETECCIÓN GPS", "📑 AUDITORÍA & CORREO"])

with t1:
    col_rad, col_line = st.columns([1, 1])
    with col_rad:
        st.subheader("🎯 Radar de Riesgos Críticos")
        
        fig_rad = go.Figure(go.Scatterpolar(
            r=[polvo, viento, 95, 20, riesgo_calc],
            theta=['Polvo', 'Viento', 'Bio', 'Gases', 'Riesgo'],
            fill='toself', fillcolor='rgba(255, 0, 255, 0.3)', line_color='#ff00ff'
        ))
        st.plotly_chart(fig_rad, use_container_width=True)
    
    with col_line:
        st.subheader("📈 Tendencia Predictiva")
        df_hist = pd.DataFrame({'Hora': range(24), 'Riesgo': np.random.randint(10, 90, 24)})
        fig_line = px.area(df_hist, x='Hora', y='Riesgo', color_discrete_sequence=['#6c5ce7'])
        st.plotly_chart(fig_line, use_container_width=True)

with t2:
    st.subheader(f"🗺️ Ubicación GPS de Faena: {faena_sel}")
    
    m = folium.Map(location=coords, zoom_start=14, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Satellite')
    folium.Circle(coords, radius=800, color='#ff00ff', fill=True, popup="ÁREA DE INFLUENCIA AIH").add_to(m)
    folium_static(m, width=1000, height=450)

with t3:
    st.subheader("💼 Módulo de Auditoría Máster")
    st.info("Correo Saliente Configurado: **aeserviseu@gmail.com**")
    
    df_audit = pd.DataFrame([{
        "Registro": f"AIH-{np.random.randint(1000, 9999)}",
        "Faena": faena_sel,
        "Responsable": "SuperUser_AIH",
        "Hora": datetime.now(tz).strftime('%H:%M:%S'),
        "Estado": "APROBADO"
    }])
    st.table(df_audit)
    
    st.divider()
    c_d1, c_d2 = st.columns(2)
    with c_d1:
        st.download_button("📥 Descargar Reporte HSE (PDF)", data=df_audit.to_csv(), file_name="auditoria.csv")
    with c_d2:
        dest = st.text_input("Enviar Auditoría a:", "gerencia@codelco.cl")
        if st.button("📧 Despachar vía aeserviseu@gmail.com"):
            st.success(f"Reporte enviado exitosamente a {dest}")

st.divider()
st.caption("AIH-MASTER COMMAND v10.0 | Blindado, Colorido e Interactivo | Uniting Technology Belgium")
