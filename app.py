import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
from datetime import datetime

# --- 1. CONFIGURACIÓN Y BLINDAJE ---
st.set_page_config(page_title="AIH | Master Control V17", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 15px; border-radius: 12px; }
        .gis-card { background: white; padding: 15px; border-radius: 12px; border: 1px solid #D2D2D7; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. COMPONENTES ANALIZADORES ---

def render_gis_taludes():
    st.markdown("## 🗺️ Módulo 09: GIS de Taludes y Estabilidad")
    
    # KPIs Geotécnicos
    g1, g2, g3, g4 = st.columns(4)
    g1.metric("Desplazamiento Max", "1.2 mm", "Bajo Control")
    g2.metric("Factor Seguridad (FoS)", "1.45", "Estable")
    g3.metric("Nodos Geotécnicos", "8/8", "Online")
    g4.metric("Alerta Raveling", "Nula", "Safe")

    st.write("---")
    
    col_map, col_info = st.columns([2, 1])
    
    with col_map:
        st.markdown("### **Visualización 3D de Estabilidad de Bancos**")
        # Simulación de puntos de control en el tajo (Lat/Lon locales)
        df_talud = pd.DataFrame({
            'lat': [-34.050, -34.051, -34.052, -34.051],
            'lon': [-70.450, -70.451, -70.452, -70.453],
            'riesgo': [10, 50, 20, 80] # Nivel de movimiento
        })
        
        view = pdk.ViewState(latitude=-34.051, longitude=-70.451, zoom=15, pitch=45)
        layer = pdk.Layer(
            "ColumnLayer", df_talud, get_position=["lon", "lat"], get_elevation="riesgo*2",
            radius=20, get_fill_color=["riesgo * 3", 100, 150, 200], pickable=True
        )
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view, map_style='mapbox://styles/mapbox/satellite-v9'))
        

    with col_info:
        st.markdown("### **Análisis de Perfil Geotécnico**")
        st.info("📌 **Sector Alpha-4:** Detectada vibración anómala por tronadura adyacente. Nodos en recalibración.")
        st.warning("⚠️ **Zona de Erosión:** Pendiente Norte presenta acumulación de humedad (Correlación M04).")
        st.markdown("""
        <div class="gis-card">
            <b>Último Escaneo LiDAR:</b> 04:00 AM<br>
            <b>Variación Volumétrica:</b> -0.02%<br>
            <b>Estado:</b> Sin cambios estructurales.
        </div>
        """, unsafe_allow_html=True)

def render_core():
    st.markdown("## 🧠 El Cerebro: Inferencia de Riesgo (IRC)")
    st.metric("IRC GLOBAL", "45.8%", "+1.6% (Geotécnico)")
    st.write("---")
    # Radar de Riesgo actualizado con GIS
    fig = go.Figure(go.Scatterpolar(r=[30, 25, 20, 40, 60, 30], theta=['Gases','Sismo','PHM','Humano','Energía','GIS'], fill='toself'))
    fig.update_layout(height=350, margin=dict(t=0,b=0,l=0,r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- 3. EJECUCIÓN MAESTRA (NAVEGACIÓN) ---
def main():
    apply_style()
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=50)
        sel = st.radio("SISTEMAS REINTEGRADOS:", [
            "💎 EL CEREBRO", 
            "🗺️ GIS TALUDES (M09)",
            "⚡ ENERGÍA (M08)",
            "🧬 BIOMETRÍA (M07)", 
            "💨 GASES (M06)", 
            "🌪️ ADMS", 
            "🌍 SISMO", 
            "⚙️ ACTIVOS"
        ])
        st.divider()
        st.caption(f"V17.0 | M09 GIS Activo | {datetime.now().strftime('%H:%M')}")

    if sel == "💎 EL CEREBRO": render_core()
    elif sel == "🗺️ GIS TALUDES (M09)": render_gis_taludes()
    elif sel == "⚡ ENERGÍA (M08)": st.info("Módulo Energía Blindado.")
    elif sel == "🧬 BIOMETRÍA (M07)": st.info("Módulo Biometría Blindado.")
    elif sel == "💨 GASES (M06)": st.info("Módulo Gases Blindado.")
    elif sel == "🌪️ ADMS)": st.info("Módulo ADMS Blindado.")
    elif sel == "🌍 SISMO": st.info("Módulo Sismo Blindado.")
    elif sel == "⚙️ ACTIVOS": st.info("Módulo Activos Blindado.")

if __name__ == "__main__":
    main()
