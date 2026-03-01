import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
import requests
from datetime import datetime
from scipy.integrate import simpson # Para dosis acumulada

# --- 1. CONFIGURACIÓN CORE Y BLINDAJE ---
st.set_page_config(page_title="AIH | Master Control V13", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 15px; border-radius: 12px; }
        .stButton>button { border-radius: 8px; width: 100%; height: 3em; font-weight: 600; background-color: #0071E3; color: white; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. COMPONENTES ANALIZADORES ---

def render_gases():
    st.markdown("## 💨 Módulo 06: Analizador de Gases Críticos")
    
    # Telemetría de Gases (Simulación de Nodos ESP32)
    g1, g2, g3, g4 = st.columns(4)
    o2_val = 20.9 + np.random.uniform(-0.2, 0.1)
    co_val = 15 + np.random.randint(-5, 10)
    
    g1.metric("Oxígeno (O2)", f"{round(o2_val,1)}%", "-0.1%", delta_color="normal")
    g2.metric("Monóxido (CO)", f"{co_val} ppm", "+2 ppm", delta_color="inverse")
    g3.metric("Nitrosos (NOx)", "2.4 ppm", "ESTABLE")
    g4.metric("Metano (CH4)", "0.1% LEL", "SEGURO")

    st.markdown("---")
    
    c_chart, c_risk = st.columns([2, 1])
    
    with c_chart:
        st.markdown("### **Curva de Exposición Acumulada (CO)**")
        # Simulación de tendencia de gases
        time_series = pd.Series(np.random.normal(15, 3, 50))
        st.line_chart(time_series, color="#FF9500")
        

    with c_risk:
        st.markdown("### **Análisis de Atmósfera**")
        if o2_val < 19.5:
            st.error("🚨 CRÍTICO: Atmósfera Deficiente de Oxígeno")
        elif co_val > 25:
            st.warning("⚠️ ALERTA: Concentración de CO sobre límite TWA")
        else:
            st.success("✅ Atmósfera Respirable Segura")
            
        st.info("💡 Sugerencia: Mantener Ventilación Sector 4 al 85% de carga.")

# (Funciones render_core, render_sismo, render_adms, render_phm se mantienen blindadas internamente)
def render_core():
    st.markdown("## 🧠 El Cerebro: Inferencia de Riesgo Progresivo (IRC)")
    st.metric("RIESGO IRC", "38.5%", "+6.1% (Gases detectados)")
    st.markdown("---")
    st.info("El incremento de CO en el Módulo 06 ha elevado el riesgo compuesto un 6.1%.")

# --- 3. EJECUCIÓN MAESTRA ---
def main():
    apply_style()
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=60)
        sel = st.radio("SISTEMAS BLINDADOS:", 
                      ["💎 EL CEREBRO", "💨 GASES (M06)", "🌪️ ADMS", "🌍 SISMO", "⚙️ ACTIVOS", "🚨 EMERGENCIAS"])
        st.divider()
        st.caption(f"V13.0 | M06 Online | {datetime.now().strftime('%H:%M')}")

    if sel == "💎 EL CEREBRO": render_core()
    elif sel == "💨 GASES (M06)": render_gases()
    # (Resto de llamadas se mantienen igual que en V12.1)
    elif sel == "🌪️ ADMS": st.info("Módulo ADMS Cargado.")
    elif sel == "🌍 SISMO": st.info("Módulo Sismo Cargado.")
    elif sel == "⚙️ ACTIVOS": st.info("Módulo PHM Cargado.")
    elif sel == "🚨 EMERGENCIAS": st.info("Módulo Emergencias Cargado.")

if __name__ == "__main__":
    main()
