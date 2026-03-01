import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
import requests
from datetime import datetime

# 1. CONFIGURACIÓN VISUAL CUPERTINO (ESTILO APPLE INDUSTRIAL)
st.set_page_config(page_title="AIH | Master Control", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
    
    /* Entorno Claro Cupertino */
    .stApp { background-color: #F5F5f7; color: #1d1d1f; font-family: 'SF Pro Display', sans-serif; }
    
    /* Tarjetas Blancas con Sombra Suave */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border: 1px solid #d2d2d7;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    /* Botones y Radio Selectors */
    .stButton>button { border-radius: 8px; background-color: #0071e3; color: white; border: none; }
    .stRadio>div { background: white; padding: 10px; border-radius: 12px; border: 1px solid #d2d2d7; }
    </style>
    """, unsafe_allow_html=True)

# 2. MOTORES DE DATOS (RECUPERACIÓN)
@st.cache_data(ttl=600)
def fetch_sismo_real():
    try:
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
        data = requests.get(url).json()['features']
        return pd.DataFrame([{"mag": f['properties']['mag'], "lat": f['geometry']['coordinates'][1], "lon": f['geometry']['coordinates'][0]} for f in data])
    except: return pd.DataFrame(columns=["mag", "lat", "lon"])

# 3. NAVEGACIÓN LATERAL (BLINDADA)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=60)
    st.markdown("### **AIH COMMAND**")
    modulo = st.radio("ANALIZADOR:", [
        "💎 EL CEREBRO (IRC)", 
        "🌪️ ADMS (METEOROLOGÍA)", 
        "🌍 SISMO (CINTURÓN FUEGO)", 
        "⚙️ PHM (SALUD ACTIVOS)",
        "🚨 EMERGENCIAS"
    ])
    st.divider()
    if st.button("ACTUALIZAR SISTEMA"): st.rerun()

# --- INTERFAZ DE ANALIZADORES ---

if modulo == "💎 EL CEREBRO (IRC)":
    st.markdown("## 🧠 El Cerebro: Correlación de Riesgo")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("RIESGO IRC", "32.4%", "ESTABLE")
    c2.metric("EXPOSICIÓN HUMANA", "14 Pers.", "NORMAL")
    c3.metric("CONECTIVIDAD NODOS", "100%", "OPTIMO")
    c4.metric("ÍNDICE HSE", "9.8/10", "OK")
    
    st.write("---")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown("### **Matriz de Correlación Progresiva**")
        fig = go.Figure(go.Scatter(y=np.random.randn(20).cumsum(), fill='tozeroy', line_color='#0071e3'))
        fig.update_layout(height=300, margin=dict(t=0,b=0,l=0,r=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    with col_b:
        st.markdown("### **Estado de Gobernanza**")
        st.success("SISTEMA AUTÓNOMO: ON")
        st.info("Protocolo ADMS: Stand-by")

elif modulo == "🌍 SISMO (CINTURÓN FUEGO)":
    st.markdown("## 🌍 Inteligencia Geofísica Global")
    df_s = fetch_sismo_real()
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(latitude=-15, longitude=-120, zoom=1, pitch=45),
        layers=[pdk.Layer("ColumnLayer", df_s, get_position=["lon", "lat"], get_elevation="mag*20000", radius=100000, get_fill_color=[0, 113, 227, 200])]
    ))

elif modulo == "🌪️ ADMS (METEOROLOGÍA)":
    st.markdown("## 🌪️ Dispersión de Polvo (ADMS)")
    m1, m2 = st.columns(2)
    m1.metric("Viento", "24 km/h", "NE")
    m2.metric("Humedad", "62%", "Normal")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Gaussian_Plume_Model.png/400px-Gaussian_Plume_Model.png", caption="Modelo Gaussiano de Dispersión Local")

elif modulo == "⚙️ PHM (SALUD ACTIVOS)":
    st.markdown("## ⚙️ Salud Estructural y de Activos")
    st.line_chart(np.random.randn(50, 2), height=250)
    st.caption("Frecuencia de Vibración Chancador (FFT)")

elif modulo == "🚨 EMERGENCIAS":
    st.markdown("## 🚨 Despacho de Respuesta Crítica")
    st.columns(3)[0].button("🚒 BOMBEROS", use_container_width=True)
    st.columns(3)[1].button("🚑 AMBULANCIA", use_container_width=True)
    st.columns(3)[2].button("⛏️ RESCATE", use_container_width=True)

# 4. FOOTER
st.divider()
st.caption(f"AIH MASTER V12.0 | TRL-4 Cupertino Base | {datetime.now().strftime('%H:%M:%S')}")
