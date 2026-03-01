import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO INMUNE V34 ---
st.set_page_config(page_title="AIH MASTER | AERO FORTRESS V34", layout="wide")

# --- 2. BLINDAJE VISUAL ATÓMICO (CUPERTINO WHITE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 500px !important; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 15px !important; 
            border-radius: 12px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important;
        }
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; }
        .stRadio > label { font-size: 0.8em !important; font-weight: 700 !important; color: #86868B !important; }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-thumb { background: #0071E3; border-radius: 10px; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. LISTA MAESTRA DEFINITIVA (64 ANALIZADORES) ---
MODULOS_64 = [
    "01 💎 EL CEREBRO (IRC)", "02 💨 GASES (M06)", "03 🧬 BIOMETRÍA", "04 ⚡ ENERGÍA", 
    "05 🗺️ GIS/TALUDES", "06 🌪️ ADMS/POLVO", "07 🌍 SISMO", "08 ⚙️ ACTIVOS", 
    "09 🚨 EMERGENCIAS", "10 👥 BEHAVIOR", "11 🔊 ACÚSTICA", "12 🛠️ MANTENIMIENTO", 
    "13 📊 REPORTES BI", "14 👁️ OCULOMETRÍA", "15 🧠 CARGA COGNITIVA", "16 🌡️ ESTRÉS TÉRMICO",
    "17 📝 INCIDENTES", "18 📉 CAUSA RAÍZ", "19 ⚖️ AUDITORÍA", "20 📢 NOTIFICACIONES",
    "21 🌪️ VENTILACIÓN 3D", "22 🚜 COLISIÓN H-M", "23 📦 STOCKPILES", "24 ⚡ CALIDAD ENERGÍA",
    "25 📡 MESH STATUS", "26 🛰️ RADAR SUBSIDENCIA", "27 🚒 SUPRESIÓN INCENDIO", "28 👷 ROCKBURST", 
    "29 🚛 FATIGA ACTIVOS", "30 ☁️ INVERSIÓN TÉRMICA", "31 🛤️ CONTROL LHD", "32 🌊 GESTIÓN RELAVES",
    "33 🛡️ CIBERSEGURIDAD", "34 🔋 MICRO-REDES", "35 🧬 EPIGENÉTICA", "36 📉 FRAGMENTACIÓN", 
    "37 🕊️ COMUNIDADES", "38 ♻️ ECONOMÍA CIRCULAR", "39 🤖 FLOTA AUTÓNOMA", "40 🔮 ESCENARIOS 4D",
    "41 ☢️ DOSIMETRÍA IONIZANTE", "42 🌫️ GAS RADÓN", "43 🧪 ESPECTROMETRÍA XRF", "44 💧 HIDROQUÍMICA", 
    "45 🧬 BIO-LIXIVIACIÓN", "46 🌋 VAPOR MERCURIO", "47 💨 QUÍMICA AIRE", "48 🧪 REACTIVOS",
    "49 🛰️ SATELITAL LEO", "50 📻 RADIO VHF/UHF", "51 🌐 TRAFFIC INSPECTOR", "52 📶 5G PRIVATE",
    "53 🕸️ MESH HEALTH", "54 🛡️ FIREWALL OT", "55 🔌 POWERLINE PLC", "56 📉 QoS/LATENCIA",
    # --- CAPA AEROESPACIAL (M57-M64) ---
    "57 🛰️ GNSS RTK PRECISION", "58 🚁 UTM TRAFFIC", "59 🛡️ ANTI-DRONE", "60 📡 RADAR METEO",
    "61 🛰️ InSAR SPACE GEOTECH", "62 🔦 LiDAR MAPPING", "63 🛡️ ADS-B AIRSPACE", "64 🌌 SPACE WEATHER"
]

# --- 4. MOTOR DE GOBERNANZA AÉREA ---

def render_01_aero_radar():
    st.title("01 💎 Cerebro de Riesgo Aeroespacial (IRC-64)")
    etiquetas = [m[:6] for m in MODULOS_64]
    valores = np.random.randint(10, 95, 64)
    
    fig = go.Figure(go.Scatterpolar(r=valores, theta=etiquetas, fill='toself', line_color='#0071E3', fillcolor='rgba(0,113,227,0.05)'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=4))), height=1000)
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("ESTADO ESPACIO AÉREO", "Limpio", "Ok")
    c2.metric("DRONES ACTIVOS", "12", "+2")
    c3.metric("PRECISIÓN RTK", "1.2 cm", "Sync")
    c4.metric("ALERTA SOLAR", "G1 (Menor)", "Safe")

def render_fallback(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría de Alta Altura")
        st.line_chart(np.random.normal(50, 10, 24), color="#0071E3")
    with c2:
        st.metric("Sincronización Satelital", "100%", "Sync")
        st.info(f"Analizador Aeroespacial {nombre} blindado. Nivel TRL-5.")

# --- 5. MAIN ---
def main():
    apply_bunker_style()
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F;'>AIH MASTER V34</h2>", unsafe_allow_html=True)
        st.caption(f"64 ANALIZADORES | AERO FORTRESS | {datetime.now().strftime('%H:%M')}")
        st.divider()
        seleccion = st.radio("Bóveda Global:", MODULOS_64, label_visibility="collapsed")
        st.divider()
        st.markdown("🛰️ **GNSS:** Sincronizado\n🛡️ **Espacio Aéreo:** Monitoreado")

    if "01" in seleccion: render_01_aero_radar()
    elif "58" in seleccion:
        st.title("58 🚁 UTM: Gestión de Tráfico de Drones")
        
    else: render_fallback(seleccion)

if __name__ == "__main__":
    main()
