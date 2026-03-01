import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
from sqlalchemy import create_engine # Para Blindaje de DB M12

# --- 1. CONFIGURACIÓN Y BLINDAJE DE ENTORNO ---
st.set_page_config(page_title="AIH MASTER | THE VAULT V20.1", layout="wide", initial_sidebar_state="expanded")

def apply_blindaje_cupertino():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 20px; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
        .stButton>button { border-radius: 12px; background-color: #0071E3; color: white; border: none; font-weight: 600; width: 100%; height: 3.5em; }
        .module-card { background: white; padding: 25px; border-radius: 18px; border: 1px solid #D2D2D7; margin-bottom: 20px; }
        .id-badge { background: #E5E5EA; color: #1D1D1F; padding: 4px 10px; border-radius: 6px; font-size: 0.8em; font-weight: 600; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. FUNCIONES DE MÓDULOS BLINDADOS (LÓGICA INMUTABLE) ---

def render_m11_acustica():
    st.markdown("## <span class='id-badge'>M11</span> 🔊 Higiene Acústica", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.metric("Nivel Sonoro (Leq)", "84.2 dB(A)", "Límite 85", delta_color="inverse")
        st.info("💡 Exposición máxima permitida: 8.5 horas.")
    with c2:
        st.markdown("### **Espectro de Frecuencia (Análisis FFT)**")
        st.line_chart(np.random.normal(70, 15, 50), color="#FF9500")
        

def render_m12_mantenimiento():
    st.markdown("## <span class='id-badge'>M12</span> 🛠️ Mantenimiento (CMMS)", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Disponibilidad Flota", "91.5%", "+0.5%")
    with col_b:
        st.metric("MTBF Promedio", "142 hrs", "Estable")
    
    st.write("### Backlog de Órdenes de Trabajo (Blindado)")
    ots = pd.DataFrame({
        "ID": ["OT-99", "OT-102"], "Activo": ["Faja 04", "Motor 22"], 
        "Causa": ["Vibración M08", "Consumo M04"], "Prioridad": ["ALTA", "MEDIA"]
    })
    st.table(ots)

def render_m13_reportes():
    st.markdown("## <span class='id-badge'>M13</span> 📊 Reportabilidad Legal & BI", unsafe_allow_html=
