import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pydeck as pdk
from datetime import datetime

# --- 1. CONFIGURACIÓN DE SEGURIDAD Y UI ---
st.set_page_config(page_title="AIH MASTER | THE VAULT V17.2", layout="wide", initial_sidebar_state="expanded")

def apply_vault_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        /* Blindaje de Tarjetas */
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
        .module-header { color: #0071E3; font-weight: 600; border-bottom: 2px solid #0071E3; margin-bottom: 20px; padding-bottom: 5px; }
        .stSidebar { background-color: #FFFFFF !important; border-right: 1px solid #D2D2D7; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. MOTOR DE GOBERNANZA (IRC) ---
def render_cerebro_v17():
    st.markdown("<h2 class='module-header'>01 💎 EL CEREBRO: INFERENCIA DE RIESGO</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC GLOBAL", "41.8%", "+2.1%")
    c2.metric("CONECTIVIDAD", "98%", "OPTIMAL")
    c3.metric("ALERTAS ACTIVAS", "2", "BAJO")
    c4.metric("TRL LEVEL", "4.2", "STABLE")
    
    st.write("---")
    # Radar de 9 Ejes (Representación de la Bóveda)
    fig = go.Figure(go.Scatterpolar(
        r=[40, 30, 20, 55, 25, 15, 30, 45, 10],
        theta=['Gases','Bio','Energía','GIS','Sismo','PHM','ADMS','Humano','Clima'],
        fill='toself', line_color='#0071E3', marker=dict(size=8)
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0, 100])), showlegend=False, height=500)
    st.plotly_chart(fig, use_container_width=True)
    

# --- 3. FUNCIONES DE MÓDULOS ENUMERADOS ---
def render_m06_gases():
    st.markdown("<h2 class='module-header'>02 💨 M06: GASES CRÍTICOS</h2>", unsafe_allow_html=True)
    st.columns(2)[0].metric("CO (Monóxido)", "14 ppm", "Safe")
    st.columns(2)[1].metric("O2 (Oxígeno)", "20.9%", "Nominal")
    

def render_m07_bio():
    st.markdown("<h2 class='module-header'>03 🧬 M07: BIOMETRÍA & FATIGA</h2>", unsafe_allow_html=True)
    st.metric("Score Fatiga Promedio", "18%", "Bajo")
    

def render_m08_energia():
    st.markdown("<h2 class='module-header'>04 ⚡ M08: ENERGÍA & FLOTA</h2>", unsafe_allow_html=True)
    st.metric("Carga Flota LHD", "88%", "Sincronizada")

def render_m09_gis():
    st.markdown("<h2 class='module-header'>05 🗺️ M09: GIS & TALUDES</h2>", unsafe_allow_html=True)
    st.metric("Estabilidad FoS", "1.42", "Estable")
    

# --- 4. CONTROL DE NAVEGACIÓN Y DESPLIEGUE ---
def main():
    apply_vault_style()
    
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.
