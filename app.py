import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN CORE Y BLINDAJE ---
st.set_page_config(page_title="AIH MASTER | V21.0", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 20px; border-radius: 14px; }
        .module-header { color: #0071E3; font-weight: 600; border-bottom: 2px solid #0071E3; margin-bottom: 20px; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. DEFINICIÓN DE LOS 13 PILARES (FUNCIONES) ---

def mod_01():
    st.markdown("<h2 class='module-header'>01 💎 EL CEREBRO (IRC)</h2>", unsafe_allow_html=True)
    st.metric("IRC GLOBAL", "46.2%", "Detección Crítica")
    fig = go.Figure(go.Scatterpolar(r=[40, 30, 25, 60, 20, 30, 15, 45, 10, 70, 35, 20, 10], 
        theta=['Gas','Bio','Eng','GIS','Sis','PHM','Polvo','Hum','Clima','Beh','Ruido','Main','BI'], fill='toself'))
    st.plotly_chart(fig, use_container_width=True)
    

def mod_02():
    st.markdown("<h2 class='module-header'>02 💨 GASES CRÍTICOS (M06)</h2>", unsafe_allow_html=True)
    st.columns(2)[0].metric("O2", "20.9%", "Nominal")
    st.columns(2)[1].metric("CO", "12 ppm", "Safe")
    

def mod_03():
    st.markdown("<h2 class='module-header'>03 🧬 BIOMETRÍA & FATIGA (M07)</h2>", unsafe_allow_html=True)
    st.metric("Fatiga Index", "14%", "Bajo")
    

def mod_04():
    st.markdown("<h2 class='module-header'>04 ⚡ ENERGÍA & FLOTA (M08)</h2>", unsafe_allow_html=True)
    st.metric("Eficiencia", "1.1 kWh/Ton", "Óptimo")

def mod_05():
    st.markdown("<h2 class='module-header'>05 🗺️ GIS & TALUDES (M09)</h2>", unsafe_allow_html=True)
    st.metric("FoS", "1.45", "Estable")
    

def mod_06():
    st.markdown("<h2 class='module-header'>06 🌪️ ADMS & POLVO</h2>", unsafe_allow_html=True)
    st.metric("MP10", "38 µg/m³", "Safe")
    

def mod_07():
    st.markdown("<h2 class='module-header'>07 🌍 SISMO (LIVE)</h2>", unsafe_allow_html=True)
    st.info("Sincronización USGS Activa.")

def mod_08():
    st.markdown("<h2 class='module-header'>08 ⚙️ ACTIVOS (PHM)</h2>", unsafe_allow_html=True)
    st.line_chart(np.random.randn(20))

def mod_09():
    st.markdown("<h2 class='module-header'>09 🚨 EMERGENCIAS</h2>", unsafe_allow_html=True)
    st.error("Protocolos de Evacuación Cargados.")

def mod_10():
    st.markdown("<h2 class='module-header'>10 👥 COMPORTAMIENTO PREDICTIVO</h2>", unsafe_allow_html=True)
    st.metric("Actitud Segura", "98%", "Alta")
    

def mod_11():
    st.markdown("<h2 class='module-header'>11 🔊 HIGIENE ACÚSTICA</h2>", unsafe_allow_html=True)
    st.metric("Ruido Leq", "82 dB(A)", "Bajo Límite")
    

def mod_12():
    st.markdown("<h2 class='module-header'>12 🛠️ MANTENIMIENTO (CMMS)</h2>", unsafe_allow_html=True)
    st.write("Órdenes de Trabajo Generadas: 2")

def mod_13():
    st.markdown("<h2 class='module-header'>13 📊 REPORTABILIDAD (BI)</h2>", unsafe_allow_html=True)
    st.button("Generar Reporte Consolidado V21.0")

# --- 3. DICCIONARIO DE ENRUTAMIENTO (EL MAPA MAESTRO) ---
MAPA_MODULOS = {
    "01 💎 EL CEREBRO": mod_01,
    "02 💨 GASES (M06)": mod_02,
    "03 🧬 BIOMETRÍA (M07)": mod_03,
    "04 ⚡ ENERGÍA (M08)": mod_04,
    "05 🗺️ GIS/TALUDES (M09)": mod_05,
    "06 🌪️ ADMS/POLVO": mod_06,
    "07 🌍 SISMO": mod_07,
    "08 ⚙️ ACTIVOS (PHM)": mod_08,
    "09 🚨 EMERGENCIAS": mod_09,
    "10 👥 COMPORTAMIENTO": mod_10,
    "11 🔊 ACÚSTICA": mod_11,
    "12 🛠️ MANTENIMIENTO": mod_12,
    "13 📊 REPORTES": mod_13
}

# --- 4. EJECUCIÓN MAESTRA ---
def main():
    apply_style()
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=50)
        # Selección Forzada y Blindada
        seleccion = st.selectbox("LISTA DE 13 MÓDULOS:", list(MAPA_MODULOS.keys()))
        st.divider()
        st.caption(f"V21.0 | Bóveda Recuperada | {datetime.now().strftime('%H:%M')}")

    # Ejecución dinámica: Llama a la función según la llave del diccionario
    MAPA_MODULOS[seleccion]()

if __name__ == "__main__":
    main()
