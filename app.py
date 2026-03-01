import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE V32 ---
st.set_page_config(page_title="AIH MASTER | NUCLEAR VAULT V32", layout="wide")

# --- 2. BLINDAJE VISUAL ATÓMICO ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 450px !important; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 20px !important; 
            border-radius: 18px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        }
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; }
        .stRadio > label { font-size: 0.85em !important; font-weight: 700 !important; color: #86868B !important; }
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
    # --- EXPANSIÓN QUÍMICA Y NUCLEAR (M41-M48) ---
    "41 ☢️ DOSIMETRÍA IONIZANTE", "42 🌫️ GAS RADÓN", "43 🧪 ESPECTROMETRÍA XRF", "44 💧 HIDROQUÍMICA", 
    "45 🧬 BIO-LIXIVIACIÓN", "46 🌋 VAPOR MERCURIO", "47 💨 QUÍMICA AIRE", "48 🧪 REACTIVOS"
]

# --- 4. RENDERIZADO ---

def render_01_nuclear_radar():
    st.title("01 💎 Cerebro de Riesgo Forense (IRC-48)")
    # Radar de 48 Analizadores
    etiquetas = [m[:6] for m in MODULOS_48]
    valores = np.random.randint(15, 85, 48)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself', 
        line_color='#FF3B30', fillcolor='rgba(255, 59, 48, 0.08)' # Rojo suave para alerta nuclear
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=6))),
        paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=50, b=50), height=800
    )
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC NUCLEAR", f"{valores.mean():.1f}%", "+0.2%")
    c2.metric("NIVEL RADIACIÓN", "0.15 µSv/h", "Normal")
    c3.metric("PH ACUÍFEROS", "7.2", "Estable")
    c4.metric("RADÓN MÁX", "120 Bq/m3", "Seguro")

def render_fallback(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría Geoquímica")
        st.line_chart(np.random.normal(50, 15, 24), color="#FF3B30" if "☢️" in nombre else "#0071E3")
    with c2:
        st.metric("Estado Sensor", "CALIBRADO", "Sync")
        st.info(f"Analizador {nombre} integrando trazas químicas y radiactividad.")

# --- 5. MAIN ---
def main():
    apply_bunker_style()
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F;'>AIH MASTER V32</h2>", unsafe_allow_html=True)
        st.caption(f"48 ANALIZADORES | NUCLEAR VAULT | {datetime.now().strftime('%H:%M')}")
        st.divider()
        seleccion = st.radio("Bóveda Total:", MODULOS_48, label_visibility="collapsed")
        st.divider()
        st.markdown("☢️ **Advertencia:** Sensores Nucleares Activos")

    if "01" in seleccion:
        render_01_nuclear_radar()
    elif "41" in seleccion:
        st.title("41 ☢️ Dosimetría Ionizante")
        
        st.metric("Tasa de Dosis Absorbida", "0.12 mSv/y", "Controlado")
    else:
        render_fallback(seleccion)

if __name__ == "__main__":
    main()
