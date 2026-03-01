import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE ---
st.set_page_config(page_title="AIH MASTER | TOTAL VAULT V30", layout="wide")

# --- 2. BLINDAJE VISUAL ATÓMICO (CUPERTINO WHITE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 380px !important; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 20px !important; 
            border-radius: 18px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
        }
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; }
        .stRadio > label { font-size: 0.9em !important; font-weight: 700 !important; color: #86868B !important; margin-bottom: 10px !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. LISTA MAESTRA UNIFICADA (32 ANALIZADORES) ---
MODULOS_TOTALES = [
    "01 💎 EL CEREBRO (IRC)", "02 💨 GASES (M06)", "03 🧬 BIOMETRÍA", "04 ⚡ ENERGÍA", 
    "05 🗺️ GIS/TALUDES", "06 🌪️ ADMS/POLVO", "07 🌍 SISMO", "08 ⚙️ ACTIVOS", 
    "09 🚨 EMERGENCIAS", "10 👥 BEHAVIOR", "11 🔊 ACÚSTICA", "12 🛠️ MANTENIMIENTO", 
    "13 📊 REPORTES BI", "14 👁️ OCULOMETRÍA", "15 🧠 CARGA COGNITIVA", "16 🌡️ ESTRÉS TÉRMICO",
    "17 📝 INCIDENTES", "18 📉 CAUSA RAÍZ", "19 ⚖️ AUDITORÍA", "20 📢 NOTIFICACIONES",
    "21 🌪️ VENTILACIÓN 3D", "22 🚜 COLISIÓN H-M", "23 📦 STOCKPILES", "24 ⚡ CALIDAD ENERGÍA",
    "25 📡 MESH STATUS", 
    # Módulos de Expansión Integrados
    "26 🛰️ RADAR SUBSIDENCIA", "27 🚒 SUPRESIÓN INCENDIO", "28 👷 ROCKBURST", 
    "29 🚛 FATIGA ACTIVOS", "30 ☁️ INVERSIÓN TÉRMICA", "31 🛤️ CONTROL LHD", "32 🌊 GESTIÓN RELAVES"
]

# --- 4. MOTOR DE RENDERIZADO ---

def render_01_cerebro():
    st.title("01 💎 Inferencia de Riesgo Compuesto (IRC-32)")
    st.write("### Gobernanza Holística Rajo y Subterránea")
    
    # Radar de 32 Analizadores
    etiquetas = [m[:6] for m in MODULOS_TOTALES]
    valores = np.random.randint(25, 75, 32)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself', 
        line_color='#0071E3', fillcolor='rgba(0,113,227,0.1)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=8))),
        paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=30, b=30)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC AGREGADO", f"{valores.mean():.1f}%", "Estable")
    c2.metric("COBERTURA", "32 Módulos", "Máxima")
    c3.metric("NODOS", "70,000", "Sync")
    c4.metric("ALERTA", "Verde", "Seguro")

def render_fallback(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría de Analizador")
        st.line_chart(np.random.normal(50, 5, 24), color="#0071E3")
    with c2:
        st.metric("Sincronización", "100%", "Sync")
        st.info(f"Analizador {nombre} integrando datos bajo protocolo TRL-4.")

# --- 5. EJECUCIÓN ---
def main():
    apply_bunker_style()
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F;'>AIH MASTER V30</h2>", unsafe_allow_html=True)
        st.caption(f"32 ANALIZADORES | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        # MENÚ DESPLEGADO TOTAL
        seleccion = st.radio("Lista de Analizadores:", MODULOS_TOTALES, label_visibility="collapsed")
        
        st.divider()
        st.markdown("🛠️ **Soporte:** Dual Rajo/Cerrado\n🛡️ **Protocolo:** Búker Inmutable")

    # ROUTER
    if "01" in seleccion:
        render_01_cerebro()
    else:
        render_fallback(seleccion)

if __name__ == "__main__":
    main()
