import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
import requests
from datetime import datetime
from scipy.signal import find_peaks

# --- 1. CONFIGURACIÓN Y ESTILO CUPERTINO ---
st.set_page_config(page_title="AIH | Master Control V15", layout="wide", initial_sidebar_state="expanded")

def apply_global_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 15px; border-radius: 12px; }
        .stButton>button { border-radius: 10px; background-color: #0071E3; color: white; border: none; font-weight: 600; width: 100%; }
        .card { background: white; padding: 20px; border-radius: 14px; border: 1px solid #D2D2D7; margin-bottom: 15px; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. MOTORES DE DATOS (DATA ENGINES) ---
@st.cache_data(ttl=300)
def get_sismo_api():
    try:
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
        resp = requests.get(url, timeout=5).json()
        return pd.DataFrame([{"mag": f['properties']['mag'], "lat": f['geometry']['coordinates'][1], "lon": f['geometry']['coordinates'][0]} for f in resp['features']])
    except: return pd.DataFrame(columns=["mag", "lat", "lon"])

# --- 3. FUNCIONES DE RENDERIZADO (MODULOS REINTEGRADOS) ---

def render_core():
    st.markdown("## 🧠 El Cerebro: Inferencia de Riesgo (IRC)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC GLOBAL", "42.5%", "+5.2%")
    c2.metric("NIVEL DE FATIGA", "ALERTA", "Op: J. Pérez")
    c3.metric("GASES (CO)", "18 ppm", "Estable")
    c4.metric("NODOS", "12/12", "Sync")
    st.divider()
    # Radar de Riesgo Unificado
    fig = go.Figure(go.Scatterpolar(r=[42, 30, 25, 60, 20], theta=['Gases','Sismo','PHM','Humano','Clima'], fill='toself', line_color='#0071E3'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)

def render_biometria():
    st.markdown("## 🧬 M07: Biometría y Fatiga Humana")
    col_l, col_r = st.columns([1, 2])
    with col_l:
        st.markdown("### **Estado Operador 01**")
        st.metric("Pulso (BPM)", "92", "Taquicardia Leve")
        st.metric("Temp. Corporal", "37.4°C", "Alerta Térmica")
        st.error("Sugerencia: Pausa Activa de 15 min.")
    with col_r:
        st.markdown("### **Variabilidad Cardíaca (HRV)**")
        st.line_chart(np.random.normal(65, 4, 30), color="#FF3B30")
        

def render_gases():
    st.markdown("## 💨 M06: Analizador de Gases Críticos")
    g1, g2, g3 = st.columns(3)
    g1.metric("Oxígeno (O2)", "20.8%", "Normal")
    g2.metric("Monóxido (CO)", "12 ppm", "Bajo Límite")
    g3.metric("Nitrosos (NOx)", "1.5 ppm", "Ok")
    st.write("---")
    st.markdown("### **Mapa de Concentración en Galería**")
    st.area_chart(np.random.randint(5, 20, 24), color="#34C759")
    

def render_adms():
    st.markdown("## 🌪️ ADMS: Dispersión de Polvo")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Gaussian_Plume_Model.png/400px-Gaussian_Plume_Model.png")
    st.metric("Viento NE", "22 km/h", "Hacia Stockpile")

def render_sismo():
    st.markdown("## 🌍 Sismo: Cinturón de Fuego")
    df = get_sismo_api()
    view = pdk.ViewState(latitude=-15, longitude=-120, zoom=1, pitch=45)
    layer = pdk.Layer("ColumnLayer", df, get_position=["lon", "lat"], get_elevation="mag*20000", radius=100000, get_fill_color=[0, 113, 227, 200])
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view, map_style='mapbox://styles/mapbox/light-v9'))

def render_phm():
    st.markdown("## ⚙️ PHM: Salud de Activos")
    st.line_chart(np.random.randn(50, 1), height=250)
    st.caption("Firma Vibracional Chancador Primario")

def render_emergency():
    st.markdown("## 🚨 Gestión de Emergencias")
    e1, e2, e3 = st.columns(3)
    e1.button("🚒 BOMBEROS")
    e2.button("🚑 AMBULANCIA")
    e3.button("⛏️ RESCATE")

# --- 4. EJECUCIÓN MAESTRA (NAVEGACIÓN) ---
def main():
    apply_global_style()
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=60)
        sel = st.radio("SISTEMAS REINTEGRADOS:", [
            "💎 EL CEREBRO", 
            "🧬 BIOMETRÍA (M07)", 
            "💨 GASES (M06)", 
            "🌪️ ADMS", 
            "🌍 SISMO", 
            "⚙️ ACTIVOS", 
            "🚨 EMERGENCIAS"
        ])
        st.divider()
        st.caption(f"V15.0 | Todos los módulos activos | {datetime.now().strftime('%H:%M')}")

    # Switch de Navegación (Blindado)
    if sel == "💎 EL CEREBRO": render_core()
    elif sel == "🧬 BIOMETRÍA (M07)": render_biometria()
    elif sel == "💨 GASES (M06)": render_gases()
    elif sel == "🌪️ ADMS": render_adms()
    elif sel == "🌍 SISMO": render_sismo()
    elif sel == "⚙️ ACTIVOS": render_phm()
    elif sel == "🚨 EMERGENCIAS": render_emergency()

if __name__ == "__main__":
    main()
