import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AIH MASTER | V27 CUPERTINO", layout="wide")

# --- 2. INYECCIÓN DE ESTILO ELEGANTE (CUPERTINO WHITE) ---
def apply_cupertino_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
        
        /* Fondo y Fuente */
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: 'Inter', sans-serif; }
        
        /* Sidebar Estilo Apple */
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7 !important; 
            border-right: 1px solid #D2D2D7; 
            width: 320px !important;
        }
        
        /* Tarjetas de Métricas (Glassmorphism suave) */
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 20px !important; 
            border-radius: 16px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        }
        
        /* Botones y Radio Selectors */
        .stRadio > label { font-weight: 600 !important; color: #1D1D1F !important; }
        .stRadio div[role="radiogroup"] { gap: 4px; }
        
        /* Títulos */
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; letter-spacing: -0.5px; }
        .module-label { color: #0071E3; font-size: 0.8em; font-weight: 700; text-transform: uppercase; margin-top: 20px; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. ESTRUCTURA DE NAVEGACIÓN DESPLEGADA ---
ANALIZADORES = {
    "💎 ESTRATÉGICO": ["01 EL CEREBRO (IRC)", "13 REPORTES BI", "19 AUDITORÍA", "25 MESH STATUS"],
    "💨 AMBIENTAL": ["02 GASES (M06)", "06 ADMS/POLVO", "07 SISMO", "11 ACÚSTICA", "21 VENTILACIÓN 3D"],
    "🧬 HUMANO": ["03 BIOMETRÍA", "10 BEHAVIOR", "14 OCULOMETRÍA", "15 CARGA COGNITIVA", "16 ESTRÉS TÉRMICO"],
    "⚙️ OPERATIVO": ["04 ENERGÍA", "05 GIS/TALUDES", "08 ACTIVOS", "12 MANTENIMIENTO", "22 COLISIÓN H-M", "23 STOCKPILES", "24 CALIDAD ENERGÍA"],
    "🚨 CRÍTICO": ["09 EMERGENCIAS", "17 INCIDENTES", "18 CAUSA RAÍZ", "20 NOTIFICACIONES"]
}

# --- 4. RENDERIZADO DE MÓDULOS ---

def render_01_cerebro():
    st.title("01 💎 El Cerebro")
    st.markdown("---")
    # Radar de 25 Analizadores con colores suaves
    etiquetas = [m[:6] for sub in ANALIZADORES.values() for m in sub]
    valores = np.random.randint(30, 70, 25)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself', 
        line_color='#0071E3', fillcolor='rgba(0, 113, 227, 0.1)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#D2D2D7")),
        paper_bgcolor='rgba(0,0,0,0)', font=dict(color="#1D1D1F", size=10), margin=dict(t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3 = st.columns(3)
    c1.metric("IRC Global", f"{valores.mean():.1f}%", "Estable")
    c2.metric("Nodos Activos", "70,000", "Sync")
    c3.metric("Riesgo Crítico", "Bajo", "Seguro")

def render_generic(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Tendencia de Análisis")
        st.line_chart(np.random.normal(50, 5, 24), color="#0071E3")
    with c2:
        st.metric("Estado", "Óptimo", "Sync")
        st.info(f"Telemetría TRL-4 activa para {nombre}.")

# --- 5. NAVEGACIÓN Y MAIN ---
def main():
    apply_cupertino_style()
    
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F; font-size: 1.5em;'>AIH MASTER</h2>", unsafe_allow_html=True)
        st.caption(f"V27.0 | {datetime.now().strftime('%d %b, %H:%M')}")
        st.divider()
        
        # MENÚ DESPLEGADO TOTAL
        st.markdown("<p class='module-label'>Selección de Analizador</p>", unsafe_allow_html=True)
        
        # Recorremos el diccionario para crear un menú visualmente estructurado
        opciones_planas = [item for sublist in ANALIZADORES.values() for item in sublist]
        seleccion = st.radio("Módulos de la Bóveda:", opciones_planas, label_visibility="collapsed")
        
        st.divider()
        st.markdown("🌐 **Nodo:** SP32-Master\n\n🛡️ **Estado:** Blindado")

    # --- ROUTER ---
    if "01" in seleccion:
        render_01_cerebro()
    elif "17" in seleccion:
        st.title("17 📝 Incidentes")
        st.text_input("Localización")
        st.button("Registrar en Bóveda")
    elif "21" in seleccion:
        st.title("21 🌪️ Ventilación 3D")
        
    else:
        render_generic(seleccion)

if __name__ == "__main__":
    main()
