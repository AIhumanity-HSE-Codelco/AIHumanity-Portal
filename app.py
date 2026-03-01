import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH MASTER | V18.0", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 20px; border-radius: 12px; }
        .module-header { color: #0071E3; font-weight: 600; border-bottom: 2px solid #0071E3; margin-bottom: 20px; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. FUNCIONES DE RENDERIZADO (LOS 9 MÓDULOS) ---

def mod_01_cerebro():
    st.markdown("<h2 class='module-header'>01 💎 EL CEREBRO (IRC)</h2>", unsafe_allow_html=True)
    st.columns(4)[0].metric("IRC GLOBAL", "42.5%", "Estable")
    fig = go.Figure(go.Scatterpolar(r=[40, 30, 25, 60, 20, 30, 15, 45, 10], 
        theta=['Gases','Bio','Energía','GIS','Sismo','PHM','ADMS','Humano','Clima'], fill='toself', line_color='#0071E3'))
    st.plotly_chart(fig, use_container_width=True)
    

def mod_02_gases():
    st.markdown("<h2 class='module-header'>02 💨 GASES CRÍTICOS (M06)</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.metric("O2", "20.8%", "Normal")
    c2.metric("CO", "14 ppm", "Safe")
    

def mod_03_biometria():
    st.markdown("<h2 class='module-header'>03 🧬 BIOMETRÍA & FATIGA (M07)</h2>", unsafe_allow_html=True)
    st.metric("Score Fatiga", "15%", "Bajo")
    

def mod_04_energia():
    st.markdown("<h2 class='module-header'>04 ⚡ ENERGÍA & FLOTA (M08)</h2>", unsafe_allow_html=True)
    st.metric("Consumo KwH", "450", "-2.1%")

def mod_05_gis():
    st.markdown("<h2 class='module-header'>05 🗺️ GIS & TALUDES (M09)</h2>", unsafe_allow_html=True)
    st.metric("Estabilidad FoS", "1.45", "Ok")
    

def mod_06_adms():
    st.markdown("<h2 class='module-header'>06 🌪️ ADMS & POLVO</h2>", unsafe_allow_html=True)
    st.metric("MP10", "42 µg/m³", "Normal")
    

def mod_07_sismo():
    st.markdown("<h2 class='module-header'>07 🌍 SISMO (LIVE)</h2>", unsafe_allow_html=True)
    st.info("Sincronizado con USGS.")

def mod_08_activos():
    st.markdown("<h2 class='module-header'>08 ⚙️ ACTIVOS (PHM)</h2>", unsafe_allow_html=True)
    st.line_chart(np.random.randn(20))

def mod_09_emergencia():
    st.markdown("<h2 class='module-header'>09 🚨 EMERGENCIAS</h2>", unsafe_allow_html=True)
    st.error("Protocolos HSE Listos.")

# --- 3. NAVEGACIÓN Y RENDERIZADO MAESTRO ---
def main():
    apply_style()
    
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=50)
        
        # EL SELECTOR MAESTRO (ENUMERADO)
        modulo_sel = st.selectbox("LISTA DE MÓDULOS BLINDADOS:", [
            "01 💎 EL CEREBRO",
            "02 💨 GASES (M06)",
            "03 🧬 BIOMETRÍA (M07)",
            "04 ⚡ ENERGÍA (M08)",
            "05 🗺️ GIS/TALUDES (M09)",
            "06 🌪️ ADMS/POLVO",
            "07 🌍 SISMO",
            "08 ⚙️ ACTIVOS (PHM)",
            "09 🚨 EMERGENCIAS"
        ])
        st.divider()
        st.caption(f"V18.0 | TRL-4 FULL | {datetime.now().strftime('%H:%M')}")

    # ROUTER DE SEGURIDAD (Cada uno tiene su IF)
    if modulo_sel == "01 💎 EL CEREBRO": mod_01_cerebro()
    elif modulo_sel == "02 💨 GASES (M06)": mod_02_gases()
    elif modulo_sel == "03 🧬 BIOMETRÍA (M07)": mod_03_biometria()
    elif modulo_sel == "04 ⚡ ENERGÍA (M08)": mod_04_energia()
    elif modulo_sel == "05 🗺️ GIS/TALUDES (M09)": mod_05_gis()
    elif modulo_sel == "06 🌪️ ADMS/POLVO": mod_06_adms()
    elif modulo_sel == "07 🌍 SISMO": mod_07_sismo()
    elif modulo_sel == "08 ⚙️ ACTIVOS (PHM)": mod_08_activos()
    elif modulo_sel == "09 🚨 EMERGENCIAS": mod_09_emergencia()

if __name__ == "__main__":
    main()
