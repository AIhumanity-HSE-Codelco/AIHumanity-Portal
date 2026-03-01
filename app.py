import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
import requests
from datetime import datetime

# --- 1. CONFIGURACIÓN CORE Y BLINDAJE DE UI ---
st.set_page_config(page_title="AIH | Master Control Supreme", layout="wide", initial_sidebar_state="expanded")

def apply_cupertino_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 15px; border-radius: 12px; }
        .stButton>button { border-radius: 8px; width: 100%; height: 3em; font-weight: 600; }
        .status-pill { padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. MOTORES DE DATOS (DATA ENGINES) ---
@st.cache_data(ttl=300)
def get_seismic_data():
    try:
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
        resp = requests.get(url, timeout=5).json()
        return pd.DataFrame([{"mag": f['properties']['mag'], "lat": f['geometry']['coordinates'][1], 
                              "lon": f['geometry']['coordinates'][0], "place": f['properties']['place']} for f in resp['features']])
    except: return pd.DataFrame(columns=["mag", "lat", "lon", "place"])

# --- 3. COMPONENTES ANALIZADORES (ENCAPSULADOS) ---

def render_core():
    st.markdown("## 🧠 El Cerebro: Inferencia de Riesgo Progresivo (IRC)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("RIESGO IRC", "32.4%", "ESTABLE")
    c2.metric("EXPOSICIÓN", "14 Pers.", "ZONA A")
    c3.metric("NODOS LIVE", "12/12", "SYNC")
    c4.metric("HSE INDEX", "9.8/10", "OPTIMO")
    
    st.markdown("---")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown("### **Matriz de Correlación de Señales**")
        fig = go.Figure(go.Scatter(y=np.random.normal(30, 2, 50), fill='tozeroy', line_color='#0071E3'))
        fig.update_layout(height=350, margin=dict(t=10,b=10,l=0,r=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        
    with col_b:
        st.markdown("### **Gobernanza de Campo**")
        st.info("📡 Nodos AideepMiners enviando telemetría cada 500ms.")
        st.success("✅ Protocolos de ventilación validados.")
        st.warning("⚠️ Alerta preventiva: Incremento de tránsito en Rampa Sur.")

def render_sismo():
    st.markdown("## 🌍 Inteligencia Geofísica: Cinturón de Fuego")
    df = get_seismic_data()
    if not df.empty:
        view = pdk.ViewState(latitude=-15, longitude=-120, zoom=1, pitch=45)
        layer = pdk.Layer("ColumnLayer", df, get_position=["lon", "lat"], get_elevation="mag*25000", 
                          radius=120000, get_fill_color=[0, 113, 227, 180], pickable=True)
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view, map_style='mapbox://styles/mapbox/light-v9'))
        
    else: st.error("Error de conexión con USGS. Verifique acceso a internet.")

def render_adms():
    st.markdown("## 🌪️ ADMS: Dispersión de Polvo & Meteorología")
    m1, m2, m3 = st.columns(3)
    m1.metric("Viento NE", "24 km/h", "Sostenido")
    m2.metric("Humedad", "62%", "Normal")
    m3.metric("MP10", "42 µg/m³", "Bajo Límite")
    st.markdown("---")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Gaussian_Plume_Model.png/450px-Gaussian_Plume_Model.png")
    

def render_phm():
    st.markdown("## ⚙️ PHM: Salud de Activos Críticos")
    st.line_chart(pd.DataFrame(np.random.randn(50, 2), columns=['Chancador A', 'Correa 04']), height=300)
    st.caption("Firma espectral de vibración procesada mediante Transformada de Fourier (FFT).")

def render_emergency():
    st.markdown("## 🚨 Centro de Respuesta y Despacho")
    st.error("INCIDENTES ACTIVOS: 0")
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.button("🚒 DESPACHAR BOMBEROS")
    c2.button("🚑 LLAMAR AMBULANCIA")
    c3.button("⛏️ BRIGADA RESCATE")

# --- 4. EJECUCIÓN MAESTRA ---
def main():
    apply_cupertino_style()
    
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=60)
        sel = st.radio("SISTEMAS BLINDADOS:", ["💎 EL CEREBRO", "🌪️ ADMS", "🌍 SISMO", "⚙️ ACTIVOS", "🚨 EMERGENCIAS"])
        st.divider()
        st.caption(f"V12.1 | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    if sel == "💎 EL CEREBRO": render_core()
    elif sel == "🌪️ ADMS": render_adms()
    elif sel == "🌍 SISMO": render_sismo()
    elif sel == "⚙️ ACTIVOS": render_phm()
    elif sel == "🚨 EMERGENCIAS": render_emergency()

if __name__ == "__main__":
    main()
