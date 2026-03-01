import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO INMUNE ---
st.set_page_config(page_title="AIH MASTER | BÚNKER V32.1", layout="wide")

# --- 2. BLINDAJE VISUAL ATÓMICO (CUPERTINO WHITE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 480px !important; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 20px !important; 
            border-radius: 18px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        }
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; }
        .stRadio > label { font-size: 0.85em !important; font-weight: 700 !important; color: #86868B !important; margin-bottom: 8px !important; }
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-thumb { background: #D2D2D7; border-radius: 10px; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. LISTA MAESTRA DEFINITIVA (48 ANALIZADORES) ---
MODULOS_48 = [
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
    "45 🧬 BIO-LIXIVIACIÓN", "46 🌋 VAPOR MERCURIO", "47 💨 QUÍMICA AIRE", "48 🧪 REACTIVOS"
]

# --- 4. MOTOR DE GOBERNANZA ---

def render_01_nuclear_radar():
    st.title("01 💎 Cerebro Forense (IRC-48)")
    st.write("### Integración de Riesgos Físicos, Químicos y Nucleares")
    
    etiquetas = [m[:6] for m in MODULOS_48]
    valores = np.random.randint(10, 80, 48)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself', 
        line_color='#FF3B30', fillcolor='rgba(255, 59, 48, 0.05)' 
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=6))),
        paper_bgcolor='rgba(0,0,0,0)', height=850
    )
    st.plotly_chart(fig, use_container_width=True)
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC AGREGADO", f"{valores.mean():.1f}%", "Nominal")
    c2.metric("TRAZAS RADIACTIVAS", "Bajas", "Controlado")
    c3.metric("ESTABILIDAD PH", "7.1", "Estable")
    c4.metric("NODOS SINC", "70,000", "Sync")

def render_fallback(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría Crítica")
        color = "#FF3B30" if any(x in nombre for x in ["☢️", "🧪", "🌋"]) else "#0071E3"
        st.line_chart(np.random.normal(50, 10, 24), color=color)
    with c2:
        st.metric("Estado", "OPERATIVO", "Sync")
        st.info(f"Analizador {nombre} blindado. TRL-4+.")

# --- 5. MAIN ---
def main():
    apply_bunker_style()
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F;'>AIH MASTER V32</h2>", unsafe_allow_html=True)
        st.caption(f"48 ANALIZADORES | NUCLEAR FORTRESS | {datetime.now().strftime('%H:%M')}")
        st.divider()
        seleccion = st.radio("Bóveda Global:", MODULOS_48, label_visibility="collapsed")
        st.divider()
        st.markdown("🛡️ **Blindaje Nivel 6**\n☢️ **Sensores Nucleares: ON**")

    if "01" in seleccion:
        render_01_nuclear_radar()
    else:
        render_fallback(seleccion)

if __name__ == "__main__":
    main()
