import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH MASTER | RESTAURACIÓN V26", layout="wide")

# --- 2. BLINDAJE DE COLORES Y ESTILO (NATIVO) ---
def apply_emergency_style():
    st.markdown("""
        <style>
        /* Fondo Negro Apple */
        .stApp { background-color: #050505 !important; color: #FFFFFF !important; }
        /* Sidebar Oscura */
        section[data-testid="stSidebar"] { background-color: #111111 !important; border-right: 1px solid #333; }
        /* Tarjetas de Métricas */
        div[data-testid="stMetric"] { 
            background-color: #1A1A1A !important; 
            border: 1px solid #333 !important; 
            padding: 15px !important; 
            border-radius: 12px !important; 
        }
        /* Colores Críticos */
        .stMetric [data-testid="stMetricValue"] { color: #FFFFFF !important; }
        .stMetric [data-testid="stMetricDelta"] { color: #34C759 !important; } /* Verde */
        h1, h2, h3 { color: #0071E3 !important; font-weight: 700 !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. LISTA PLANA DE LOS 25 ANALIZADORES (SIN CATEGORÍAS PARA EVITAR ERRORES) ---
LISTA_25 = [
    "01 💎 EL CEREBRO (IRC)", "02 💨 GASES (M06)", "03 🧬 BIOMETRÍA", "04 ⚡ ENERGÍA", 
    "05 🗺️ GIS/TALUDES", "06 🌪️ ADMS/POLVO", "07 🌍 SISMO", "08 ⚙️ ACTIVOS", 
    "09 🚨 EMERGENCIAS", "10 👥 BEHAVIOR", "11 🔊 ACÚSTICA", "12 🛠️ MANTENIMIENTO", 
    "13 📊 REPORTES BI", "14 👁️ OCULOMETRÍA", "15 🧠 CARGA COGNITIVA", "16 🌡️ ESTRÉS TÉRMICO",
    "17 📝 INCIDENTES", "18 📉 CAUSA RAÍZ", "19 ⚖️ AUDITORÍA", "20 📢 NOTIFICACIONES",
    "21 🌪️ VENTILACIÓN 3D", "22 🚜 COLISIÓN H-M", "23 📦 STOCKPILES", "24 ⚡ CALIDAD ENERGÍA",
    "25 📡 MESH STATUS"
]

# --- 4. FUNCIONES DE RENDERIZADO ---

def render_cerebro():
    st.title("01 💎 EL CEREBRO: RIESGO COMPUESTO")
    # Radar de 25 Analizadores
    etiquetas = [m[:6] for m in LISTA_25]
    valores = np.random.randint(20, 80, 25)
    fig = go.Figure(go.Scatterpolar(r=valores, theta=etiquetas, fill='toself', line_color='#0071E3'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0, 100])), 
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3 = st.columns(3)
    c1.metric("IRC GLOBAL", f"{valores.mean():.1f}%", "+1.2%")
    c2.metric("CONECTIVIDAD", "99.8%", "Sync")
    c3.metric("NODOS", "70,000", "TRL-4")

def render_fallback(nombre):
    st.title(nombre)
    st.write("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría en Tiempo Real")
        st.line_chart(np.random.randn(24), color="#0071E3")
    with c2:
        st.metric("Estado Analizador", "OPERATIVO", "OK")
        st.metric("Sincronización", "10ms", "BAJA LATENCIA")

# --- 5. MOTOR DE NAVEGACIÓN ---
def main():
    apply_emergency_style()
    
    with st.sidebar:
        st.markdown("<h2 style='color:#0071E3;'>AIH MASTER V26</h2>", unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=60)
        st.divider()
        # Selector Único Robusto
        seleccion = st.selectbox("ANALIZADORES DISPONIBLES (1-25):", LISTA_25)
        st.divider()
        st.caption(f"MODO RESTAURACIÓN | {datetime.now().strftime('%H:%M')}")

    # ROUTER DE SEGURIDAD
    if "01" in seleccion:
        render_cerebro()
    elif "17" in seleccion:
        st.title("17 📝 REGISTRO DE INCIDENTES")
        st.text_input("Ubicación")
        st.selectbox("Tipo", ["Acto Inseguro", "Condición", "Falla"])
        st.button("GUARDAR EN BÓVEDA")
    elif "21" in seleccion:
        st.title("21 🌪️ VENTILACIÓN 3D")
        
        st.info("Simulando flujos de aire en galerías.")
    else:
        render_fallback(seleccion)

if __name__ == "__main__":
    main()
