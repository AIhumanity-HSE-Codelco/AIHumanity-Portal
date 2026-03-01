import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE ---
st.set_page_config(page_title="AIH MASTER | TOTAL 40", layout="wide")

# --- 2. BLINDAJE VISUAL ATÓMICO (CUPERTINO WHITE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 420px !important; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 22px !important; 
            border-radius: 18px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        }
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; }
        .stRadio > label { font-size: 0.9em !important; font-weight: 700 !important; color: #86868B !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. LISTA MAESTRA DEFINITIVA (40 ANALIZADORES) ---
MODULOS_40 = [
    "01 💎 EL CEREBRO (IRC)", "02 💨 GASES (M06)", "03 🧬 BIOMETRÍA", "04 ⚡ ENERGÍA", 
    "05 🗺️ GIS/TALUDES", "06 🌪️ ADMS/POLVO", "07 🌍 SISMO", "08 ⚙️ ACTIVOS", 
    "09 🚨 EMERGENCIAS", "10 👥 BEHAVIOR", "11 🔊 ACÚSTICA", "12 🛠️ MANTENIMIENTO", 
    "13 📊 REPORTES BI", "14 👁️ OCULOMETRÍA", "15 🧠 CARGA COGNITIVA", "16 🌡️ ESTRÉS TÉRMICO",
    "17 📝 INCIDENTES", "18 📉 CAUSA RAÍZ", "19 ⚖️ AUDITORÍA", "20 📢 NOTIFICACIONES",
    "21 🌪️ VENTILACIÓN 3D", "22 🚜 COLISIÓN H-M", "23 📦 STOCKPILES", "24 ⚡ CALIDAD ENERGÍA",
    "25 📡 MESH STATUS", "26 🛰️ RADAR SUBSIDENCIA", "27 🚒 SUPRESIÓN INCENDIO", "28 👷 ROCKBURST", 
    "29 🚛 FATIGA ACTIVOS", "30 ☁️ INVERSIÓN TÉRMICA", "31 🛤️ CONTROL LHD", "32 🌊 GESTIÓN RELAVES",
    # --- LA FRONTERA FINAL (M33-M40) ---
    "33 🛡️ CIBERSEGURIDAD", "34 🔋 MICRO-REDES", "35 🧬 EPIGENÉTICA", "36 📉 FRAGMENTACIÓN", 
    "37 🕊️ COMUNIDADES", "38 ♻️ ECONOMÍA CIRCULAR", "39 🤖 FLOTA AUTÓNOMA", "40 🔮 ESCENARIOS 4D"
]

# --- 4. RENDERIZADO ---

def render_cerebro_40():
    st.title("01 💎 Cerebro de Riesgo Total (IRC-40)")
    # Radar de 40 Analizadores
    etiquetas = [m[:6] for m in MODULOS_40]
    valores = np.random.randint(20, 80, 40)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself', 
        line_color='#0071E3', fillcolor='rgba(0,113,227,0.1)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=7))),
        paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=50, b=50), height=700
    )
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC AGREGADO", f"{valores.mean():.1f}%", "Óptimo")
    c2.metric("COBERTURA", "100%", "Full Vault")
    c3.metric("INTEGRIDAD", "Alta", "Sync")
    c4.metric("ESCENARIOS", "4.2M", "Simulados")

def render_generic(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría Crítica")
        st.line_chart(np.random.normal(50, 10, 24), color="#0071E3")
    with c2:
        st.metric("Estado", "Sync", "100%")
        st.info(f"Analizador {nombre} operando bajo protocolos de blindaje TRL-5.")

# --- 5. MAIN ---
def main():
    apply_bunker_style()
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F;'>AIH MASTER V31</h2>", unsafe_allow_html=True)
        st.caption(f"40 ANALIZADORES | TOTAL FORTRESS | {datetime.now().strftime('%H:%M')}")
        st.divider()
        seleccion = st.radio("Bóveda de Analizadores:", MODULOS_40, label_visibility="collapsed")
        st.divider()
        st.markdown("🛡️ **Protocolo de Blindaje Nivel 5**")

    if "01" in seleccion:
        render_cerebro_40
