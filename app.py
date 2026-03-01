import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO INALTERABLE ---
st.set_page_config(page_title="AIH MASTER | BÚNKER V30.1", layout="wide")

# --- 2. INYECCIÓN DE ESTILO CUPERTINO WHITE (BLINDAJE V30) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 400px !important; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 22px !important; 
            border-radius: 18px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        }
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; }
        .stRadio > label { font-size: 1.1em !important; font-weight: 700 !important; color: #86868B !important; margin-bottom: 15px !important; }
        /* Scrollbar Apple Style */
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-thumb { background: #D2D2D7; border-radius: 10px; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. LISTA MAESTRA DE 32 ANALIZADORES (ORDEN ESTRATÉGICO) ---
MODULOS_TOTALES = [
    "01 💎 EL CEREBRO (IRC)", "02 💨 GASES (M06)", "03 🧬 BIOMETRÍA", "04 ⚡ ENERGÍA", 
    "05 🗺️ GIS/TALUDES", "06 🌪️ ADMS/POLVO", "07 🌍 SISMO", "08 ⚙️ ACTIVOS", 
    "09 🚨 EMERGENCIAS", "10 👥 BEHAVIOR", "11 🔊 ACÚSTICA", "12 🛠️ MANTENIMIENTO", 
    "13 📊 REPORTES BI", "14 👁️ OCULOMETRÍA", "15 🧠 CARGA COGNITIVA", "16 🌡️ ESTRÉS TÉRMICO",
    "17 📝 INCIDENTES", "18 📉 CAUSA RAÍZ", "19 ⚖️ AUDITORÍA", "20 📢 NOTIFICACIONES",
    "21 🌪️ VENTILACIÓN 3D", "22 🚜 COLISIÓN H-M", "23 📦 STOCKPILES", "24 ⚡ CALIDAD ENERGÍA",
    "25 📡 MESH STATUS", "26 🛰️ RADAR SUBSIDENCIA", "27 🚒 SUPRESIÓN INCENDIO", 
    "28 👷 ROCKBURST", "29 🚛 FATIGA ACTIVOS", "30 ☁️ INVERSIÓN TÉRMICA", 
    "31 🛤️ CONTROL LHD", "32 🌊 GESTIÓN RELAVES"
]

# --- 4. RENDERIZADO DE INTERFAZ DE GOBERNANZA ---

def render_01_cerebro_32():
    st.title("01 💎 Cerebro de Riesgo Compuesto (IRC-32)")
    st.write("### Gobernanza Holística Rajo y Subterránea")
    
    # Radar de 32 Analizadores
    etiquetas = [m[:6] for m in MODULOS_TOTALES]
    valores = np.random.randint(30, 75, 32)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself', 
        line_color='#0071E3', fillcolor='rgba(0,113,227,0.1)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=8))),
        paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=40, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC AGREGADO", f"{valores.mean():.1f}%", "Estable")
    c2.metric("COBERTURA", "32 Módulos", "Máxima")
    c3.metric("NODOS SINC", "70k", "99.9%")
    c4.metric("ALERTA IRC", "Óptima", "Sync")

def render_fallback(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría de Analizador")
        st.line_chart(np.random.normal(50, 4, 24), color="#0071E3")
    with c2:
        st.metric("Sincronización", "100%", "Sync")
        st.metric("Estado TRL", "TRL-4", "Evaluación")
        st.info(f"Módulo {nombre} blindado y operando.")

# --- 5. MOTOR DE NAVEGACIÓN ---
def main():
    apply_bunker_style()
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F;'>AIH MASTER V30</h2>", unsafe_allow_html=True)
        st.caption(f"32 ANALIZADORES | MODO BÚNKER | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        # MENÚ DESPLEGADO (Navegación instantánea)
        seleccion = st.radio("Dominios de Riesgo:", MODULOS_TOTALES, label_visibility="collapsed")
        
        st.divider()
        st.markdown("🌐 **Nodo:** SP32-Master\n🛡️ **Protocolo:** Inmune")

    # ROUTER DE SEGURIDAD
    if "01" in seleccion:
        render_01_cerebro_32()
    elif "21" in seleccion:
        st.title("21 🌪️ Ventilación 3D")
        
    elif "26" in seleccion:
        st.title("26 🛰️ Radar de Subsidencia")
        
    else:
        render_fallback(seleccion)

if __name__ == "__main__":
    main()
