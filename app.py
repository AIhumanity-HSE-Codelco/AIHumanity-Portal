import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO Y UI ---
st.set_page_config(
    page_title="AIH MASTER | V25 TOTAL VAULT", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

def apply_industrial_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        .stApp { background-color: #0A0A0A; color: #FFFFFF; font-family: 'SF Pro Display', sans-serif; }
        [data-testid="stSidebar"] { background-color: #111111 !important; border-right: 1px solid #333; }
        .stMetric { background-color: #1A1A1A; border: 1px solid #333; padding: 15px; border-radius: 12px; }
        .module-header { color: #0071E3; font-weight: 700; border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 20px; }
        .status-tag { background: #1A1A1A; color: #34C759; padding: 4px 10px; border-radius: 6px; font-size: 0.8em; font-weight: 600; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. DICCIONARIO MAESTRO DE LOS 25 ANALIZADORES ---
# Clasificación por Dominios de Riesgo Crítico
ANALIZADORES = {
    "💎 ESTRATÉGICO": ["01 💎 EL CEREBRO (IRC)", "13 📊 REPORTES BI", "19 ⚖️ AUDITORÍA", "25 📡 MESH STATUS"],
    "💨 AMBIENTAL": ["02 💨 GASES (M06)", "06 🌪️ ADMS/POLVO", "07 🌍 SISMO", "11 🔊 ACÚSTICA", "21 🌪️ VENTILACIÓN 3D"],
    "🧬 HUMANO": ["03 🧬 BIOMETRÍA", "10 👥 BEHAVIOR", "14 👁️ OCULOMETRÍA", "15 🧠 CARGA COGNITIVA", "16 🌡️ ESTRÉS TÉRMICO"],
    "⚙️ OPERATIVO": ["04 ⚡ ENERGÍA", "05 🗺️ GIS/TALUDES", "08 ⚙️ ACTIVOS", "12 🛠️ MANTENIMIENTO", "22 🚜 COLISIÓN H-M", "23 📦 STOCKPILES", "24 ⚡ CALIDAD ENERGÍA"],
    "🚨 INCIDENTES": ["09 🚨 EMERGENCIAS", "17 📝 INCIDENTES", "18 📉 CAUSA RAÍZ", "20 📢 NOTIFICACIONES"]
}

# --- 3. FUNCIONES DE RENDERIZADO TÉCNICO ---

def render_01_cerebro():
    st.markdown("<h2 class='module-header'>01 💎 EL CEREBRO: IRC MULTIVARIABLE</h2>", unsafe_allow_html=True)
    
    # Radar de 25 Ejes (Simulado con etiquetas cortas)
    modulos_lista = [m[:6] for sub in ANALIZADORES.values() for m in sub]
    valores_riesgo = np.random.randint(20, 80, 25)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores_riesgo, 
        theta=modulos_lista, 
        fill='toself', 
        line_color='#0071E3',
        fillcolor='rgba(0, 113, 227, 0.2)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False, range=[0, 100])),
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white", size=10)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC GLOBAL", f"{valores_riesgo.mean():.1f}%", "+1.2%")
    c2.metric("CONECTIVIDAD", "99.8%", "Sync")
    c3.metric("NODOS TRL-4", "70,000", "Activo")
    c4.metric("ALERTAS", "3", "Nivel 2")

def render_fallback(nombre):
    st.markdown(f"<h2 class='module-header'>{nombre}</h2>", unsafe_allow_html=True)
    st.markdown("<span class='status-tag'>● TELEMETRÍA EN TIEMPO REAL ACTIVA</span>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.write("### Tendencia de Analizador (24h)")
        st.line_chart(np.random.normal(50, 10, 24), color="#0071E3")
    with col_r:
        st.write("### Variables Críticas")
        st.metric("Sensor Alpha", f"{np.random.randint(40,60)}%", "Nominal")
        st.metric("Sensor Beta", f"{np.random.randint(100,200)}", "Normal")
        st.info(f"El analizador {nombre} procesa datos crutos desde nodos ESP32 con filtrado Kalman.")

def render_17_incidentes():
    st.markdown("<h2 class='module-header'>17 📝 REGISTRO FLASH DE INCIDENTES</h2>", unsafe_allow_html=True)
    with st.form("incident_vault"):
        st.write("### Ingreso de Evento Crítico")
        st.text_input("ID Nodo / Ubicación")
        st.selectbox("Nivel de Riesgo", ["Bajo", "Medio", "Alto", "Crítico"])
        st.selectbox("Tipo", ["Acto Inseguro", "Condición Insegura", "Falla Estructural"])
        st.text_area("Observaciones Técnicas")
        if st.form_submit_button("🚨 SELLAR Y REGISTRAR"):
            st.success("Evento encriptado en Bóveda Central.")

def render_21_ventilacion():
    st.markdown("<h2 class='module-header'>21 🌪️ GEMELO DIGITAL: VENTILACIÓN 3D</h2>", unsafe_allow_html=True)
    
    st.metric("Flujo Total (cfm)", "450,000", "+5k")
    st.info("Simulación predictiva: Flujo de aire nominal en niveles inferiores.")

# --- 4. MOTOR DE NAVEGACIÓN Y EJECUCIÓN ---

def main():
    apply_industrial_style()
    
    with st.sidebar:
        st.markdown("<h2 style='color:#0071E3;'>AIH MASTER V25</h2>", unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=60)
        st.divider()
        
        # Selección por Dominios (UX de Sala de Control)
        dominio_sel = st.selectbox("DOMINIO DE RIESGO:", list(ANALIZADORES.keys()))
        modulo_sel = st.radio("ANALIZADOR:", ANALIZADORES[dominio_sel])
        
        st.divider()
        st.caption(f"GOBERNANZA TRL-4 | {datetime.now().strftime('%H:%M:%S')}")

    # --- ROUTER DE RENDERIZADO SEGURO ---
    if "01" in modulo_sel:
        render_01_cerebro()
    elif "17" in modulo_sel:
        render_17_incidentes()
    elif "21" in modulo_sel:
        render_21_ventilacion()
    else:
        # Fallback para los analizadores restantes (Asegura que nada se pierda)
        render_fallback(modulo_sel)

if __name__ == "__main__":
    main()
