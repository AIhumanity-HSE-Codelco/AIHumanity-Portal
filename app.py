import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE ---
st.set_page_config(page_title="AIH MASTER | BÚNKER V28", layout="wide")

# --- 2. INYECCIÓN DE BLINDAJE VISUAL (CUPERTINO WHITE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        /* Base Blanca y Tipografía Apple */
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important; }
        
        /* Sidebar Blindada (Gris F5) */
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 350px !important; }
        
        /* Tarjetas de Métricas Elegantes */
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; 
            border: 1px solid #D2D2D7 !important; 
            padding: 22px !important; 
            border-radius: 18px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
        }
        
        /* Títulos y Divisores */
        h1, h2, h3 { color: #1D1D1F !important; font-weight: 600 !important; letter-spacing: -0.02em !important; }
        .stRadio > label { font-size: 1.1em !important; font-weight: 700 !important; color: #86868B !important; margin-bottom: 15px !important; }
        
        /* Scrollbar Fina */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #D2D2D7; border-radius: 10px; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. DICCIONARIO PLANO DE 25 ANALIZADORES ---
# (Lista inalterable para el Router)
MODULOS_25 = [
    "01 💎 EL CEREBRO (IRC)", "02 💨 GASES (M06)", "03 🧬 BIOMETRÍA", "04 ⚡ ENERGÍA", 
    "05 🗺️ GIS/TALUDES", "06 🌪️ ADMS/POLVO", "07 🌍 SISMO", "08 ⚙️ ACTIVOS", 
    "09 🚨 EMERGENCIAS", "10 👥 BEHAVIOR", "11 🔊 ACÚSTICA", "12 🛠️ MANTENIMIENTO", 
    "13 📊 REPORTES BI", "14 👁️ OCULOMETRÍA", "15 🧠 CARGA COGNITIVA", "16 🌡️ ESTRÉS TÉRMICO",
    "17 📝 INCIDENTES", "18 📉 CAUSA RAÍZ", "19 ⚖️ AUDITORÍA", "20 📢 NOTIFICACIONES",
    "21 🌪️ VENTILACIÓN 3D", "22 🚜 COLISIÓN H-M", "23 📦 STOCKPILES", "24 ⚡ CALIDAD ENERGÍA",
    "25 📡 MESH STATUS"
]

# --- 4. RENDERIZADO DE MÓDULOS ---

def render_01_cerebro():
    st.title("01 💎 Inferencia de Riesgo Compuesto (IRC)")
    st.write("### Vista de Gobernanza 360°")
    
    etiquetas = [m[:6] for m in MODULOS_25]
    valores = np.random.randint(35, 65, 25)
    
    fig = go.Figure(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself', 
        line_color='#0071E3', fillcolor='rgba(0, 113, 227, 0.08)'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=False), angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=9))),
        paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=30, b=30)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC PROMEDIO", f"{valores.mean():.1f}%", "Estable")
    c2.metric("SALUD DE RED", "99.9%", "Sync")
    c3.metric("NODOS TRL-4", "70,000", "Activos")
    c4.metric("ALERTA HSE", "0", "Seguro")

def render_fallback(nombre):
    st.title(nombre)
    st.markdown("---")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### Telemetría Crítica")
        st.line_chart(np.random.normal(50, 4, 24), color="#0071E3")
    with c2:
        st.metric("Estado Analizador", "ACTIVO", "Sync")
        st.info(f"Módulo {nombre} operando bajo protocolos de blindaje TRL-4.")

# --- 5. MOTOR DE NAVEGACIÓN Y MAIN ---
def main():
    apply_bunker_style()
    
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F; font-size: 1.6em;'>AIH MASTER</h2>", unsafe_allow_html=True)
        st.caption(f"MODO BÚNKER | {datetime.now().strftime('%H:%M:%S')}")
        st.divider()
        
        # MENÚ DESPLEGADO (25 ANALIZADORES)
        st.markdown("**SISTEMA DE GOBERNANZA**")
        seleccion = st.radio("Lista de Analizadores:", MODULOS_25, label_visibility="collapsed")
        
        st.divider()
        st.markdown("🛡️ **Blindaje:** Nivel 4 Activo\n\n🌐 **Célula:** SP32-Master")

    # --- ROUTER DE EMERGENCIA ---
    if "01" in seleccion:
        render_01_cerebro()
    elif "17" in seleccion:
        st.title("17 📝 Reporte de Incidentes")
        st.text_input("Localización del Evento")
        st.button("Registrar en Bóveda")
    elif "21" in seleccion:
        st.title("21 🌪️ Ventilación 3D")
        
        st.info("Simulación de flujos de aire activa.")
    else:
        # Si no tiene vista especial, usa el dashboard seguro
        render_fallback(seleccion)

if __name__ == "__main__":
    main()
