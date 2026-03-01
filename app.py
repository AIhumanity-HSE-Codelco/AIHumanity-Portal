import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
import requests
from datetime import datetime
import time

# 1. SETUP DE ALTA DENSIDAD (OPTIMIZADO LAPTOP/MÓVIL)
st.set_page_config(page_title="AIH | Global Intelligence", layout="wide", initial_sidebar_state="expanded")

# 2. MOTOR DE DATOS SÍSMICOS (USGS REAL-TIME)
@st.cache_data(ttl=300)
def get_global_seismic_data():
    try:
        # Sismos magnitud 4.5+ en las últimas 24h
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
        resp = requests.get(url).json()
        features = resp['features']
        data = []
        for f in features:
            coords = f['geometry']['coordinates']
            props = f['properties']
            data.append({
                "name": props['title'],
                "mag": props['mag'],
                "lat": coords[1],
                "lon": coords[0],
                "depth": coords[2],
                "time": datetime.fromtimestamp(props['time']/1000).strftime('%H:%M')
            })
        return pd.DataFrame(data)
    except:
        # Fallback en caso de error de red
        return pd.DataFrame(columns=["name", "mag", "lat", "lon", "depth", "time"])

# 3. CSS INDUSTRIAL (CUPERTINO DARK/LIGHT)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; font-size: 0.9rem; }
    .stMetric { background: white; padding: 10px; border-radius: 12px; border: 1px solid #EEE; }
    .module-card { background: white; padding: 15px; border-radius: 16px; border: 1px solid #E5E9F0; margin-bottom: 10px; }
    .emergency-btn { background-color: #FF3B30 !important; color: white !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 4. NAVEGADOR LATERAL
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2784/2784400.png", width=70)
    st.title("AIH COMMAND")
    modulo = st.radio("MÓDULO SELECCIONADO:", 
                     ["🏠 Dashboard Operativo", 
                      "🌪️ Analizador ADMS", 
                      "🚨 Despacho Emergencias", 
                      "🌍 Inteligencia Geofísica"])
    st.divider()
    st.caption("v8.0 | TRL-4 Global Ready")

# --- LÓGICA DE MÓDULOS ---

if modulo == "🌍 Inteligencia Geofísica":
    st.markdown("<h2 style='color:#5E5CE6;'>🌍 INTELIGENCIA GEOFÍSICA: CINTURÓN DE FUEGO</h2>", unsafe_allow_html=True)
    
    df_sismos = get_global_seismic_data()
    
    # KPIs Globales
    m1, m2, m3 = st.columns(3)
    m1.metric("Sismos Recientes (24h)", len(df_sismos), "Global")
    if not df_sismos.empty:
        max_mag = df_sismos['mag'].max()
        m2.metric("Magnitud Máxima", f"{max_mag} Mw", "Cinturón de Fuego")
        m3.metric("Estatus Tectónico", "ALERTA", "Actividad Alta", delta_color="inverse")

    col_mapa, col_lista = st.columns([2, 1])

    with col_mapa:
        # MAPA 3D (PYDECK) - Cinturón de Fuego
        layer = pdk.Layer(
            "ColumnLayer",
            df_sismos,
            get_position=["lon", "lat"],
            get_elevation="mag * 50000", # Elevación proporcional a la magnitud
            elevation_scale=1,
            radius=150000,
            get_fill_color=["mag * 40", "255 - (mag * 20)", 150, 200], # Color según magnitud
            pickable=True,
            auto_highlight=True,
        )
        
        view_state = pdk.ViewState(latitude=-15, longitude=-120, zoom=1, pitch=40)
        
        st.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            map_style="mapbox://styles/mapbox/light-v9",
            tooltip={"text": "{name}\nMagnitud: {mag}\nProfundidad: {depth}km"}
        ))
        st.caption("Visualización 3D: La altura y el color representan la magnitud del sismo.")

    with col_lista:
        st.markdown("### 📋 Feed Sísmico (USGS)")
        if df_sismos.empty:
            st.info("No se registran eventos mayores a 4.5 en las últimas horas.")
        else:
            for i, row in df_sismos.head(8).iterrows():
                st.markdown(f"""
                <div class="module-card">
                    <b>{row['mag']} Mw</b> - {row['name']}<br>
                    <small style='color:grey;'>Hora: {row['time']} | Prof: {row['depth']}km</small>
                </div>
                """, unsafe_allow_html=True)

elif modulo == "🏠 Dashboard Operativo":
    st.markdown("### 🛰️ CONTROL TOWER (TRAZABILIDAD)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("META CERO", "96%", "OK")
    c2.metric("MP10", "34.2", "-2.1")
    c3.metric("NODOS LIVE", "12/12", "OK")
    c4.metric("IRO", "12%", "BAJO")
    
    st.write("---")
    st_izq, st_der = st.columns(2)
    with st_izq:
        st.markdown("<b>👥 Trazabilidad Personal</b>", unsafe_allow_html=True)
        st.table(pd.DataFrame({"Operador": ["J. Pérez", "M. Soto"], "Zona": ["Nivel 4", "Rampa"], "Status": ["Seguro", "Seguro"]}))
    with st_der:
        st.markdown("<b>📈 Histórico Sismográfico Local</b>", unsafe_allow_html=True)
        st.line_chart(np.random.randn(20, 1) * 0.01, height=180)

elif modulo == "🚨 Despacho Emergencias":
    st.markdown("<h2 style='color:#FF3B30;'>🚨 GESTIÓN DE CRISIS Y RESCATE</h2>", unsafe_allow_html=True)
    b1, b2, b3, b4 = st.columns(4)
    b1.button("🚒 BOMBEROS", use_container_width=True)
    b2.button("🚑 AMBULANCIA", use_container_width=True)
    b3.button("👮 POLICÍA", use_container_width=True)
    b4.button("⛏️ RESCATE MINERO", use_container_width=True)
    
    st.divider()
    st.markdown("### 📝 Incidentes Activos")
    st.error("INC-092: Amago de Incendio en Nivel 4 - Brigada en ruta.")
    st.map(pd.DataFrame({'lat': [-34.05], 'lon': [-70.45]}), zoom=14, height=200)

elif modulo == "🌪️ Analizador ADMS":
    st.markdown("### 🌪️ MODELO ADMS (METEOROLOGÍA)")
    st.info("Monitorizando dispersión de polvo en El Teniente...")
    # Lógica de ADMS simplificada
    st.metric("Viento NE", "22 km/h", "ESTABLE")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Gaussian_Plume_Model.png/300px-Gaussian_Plume_Model.png")

# 5. FOOTER & AUTO-REFRESH
st.divider()
st.caption(f"AIHumanity Master | {datetime.now().strftime('%H:%M:%S')} | TRL-4")
time.sleep(2)
st.rerun()
