import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE ---
st.set_page_config(page_title="AIH MASTER | TOTALITY 80", layout="wide")

# --- 2. BLINDAJE VISUAL CUPERTINO (PC/TABLET/MOBILE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, system-ui, sans-serif !important; }
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7 !important; 
            border-right: 1px solid #D2D2D7 !important; 
            width: clamp(300px, 25vw, 450px) !important; 
        }
        h1 { font-size: clamp(1.2rem, 3vw, 2.2rem) !important; font-weight: 700 !important; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; border: 1px solid #D2D2D7 !important; 
            border-radius: 12px !important; padding: 10px !important;
        }
        /* Estabilizador de Gráfica */
        .js-plotly-plot { border-radius: 20px !important; overflow: hidden !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. BASE DE DATOS ESTRUCTURAL DE 80 ANALIZADORES ---
# Generamos los 80 módulos internamente para asegurar que el radar siempre los lea
ANALYSER_DB = {f"{str(i).zfill(2)}": f"Analizador {str(i).zfill(2)}" for i in range(1, 81)}

# Mapeo de Nombres Críticos para el Menú
CATEGORIAS_MASTER = {
    "💎 Estratégico & Riesgo": ["01", "13", "80"],
    "💨 HSE, Química & Nuclear": ["02", "41", "42", "43", "46", "47"],
    "🛰️ Com, Aero & GPS": ["49", "50", "52", "57", "58", "63", "64"],
    "🌍 Geotecnia & Energía": ["05", "07", "26", "28", "32", "66"],
    "🚜 Operaciones & Caos": ["08", "21", "29", "39", "75", "76"]
}

# --- 4. MOTOR DE RENDERIZADO IRC-80 INDESTRUCTIBLE ---

def render_radar_80():
    st.title("01 💎 Cerebro de Riesgo Compuesto (IRC-80)")
    
    # Datos persistentes de los 80 ejes
    etiquetas = [str(i).zfill(2) for i in range(1, 81)]
    # Simulación de datos estables para evitar parpadeo
    np.random.seed(42) 
    valores = np.random.randint(30, 80, 80)
    
    # Cerrar geometría del radar
    v_plot = np.append(valores, valores[0])
    e_plot = np.append(etiquetas, etiquetas[0])
    
    fig = go.Figure()
    
    # Capa de Riesgo Forense
    fig.add_trace(go.Scatterpolar(
        r=v_plot, theta=e_plot, fill='toself',
        line=dict(color='#0071E3', width=1),
        fillcolor='rgba(0, 113, 227, 0.1)',
        hoverinfo='r+theta',
        name="Línea Base IRC"
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="white",
            radialaxis=dict(visible=True, gridcolor="#F0F0F2", tickfont=dict(size=7, color="#86868B")),
            angularaxis=dict(gridcolor="#F0F0F2", tickfont=dict(size=6, color="#86868B"))
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        height=750,
        margin=dict(t=30, b=30, l=30, r=30)
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    

    # KPIs de Estado de Bóveda
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC GLOBAL", f"{valores.mean():.1f}%", "Estable")
    c2.metric("MÓDULOS ACT", "80 / 80", "Full Sync")
    c3.metric("NODOS MESH", "70,000", "Online")
    c4.metric("SISTEMA", "V37.0", "Blindado")

# --- 5. NAVEGACIÓN Y MAIN ---
def main():
    apply_bunker_style()
    
    with st.sidebar:
        st.markdown("<h1 style='color:#1D1D1F;'>AIH MASTER V37</h1>", unsafe_allow_html=True)
        st.caption(f"80 ANALIZADORES SINCRONIZADOS | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        # MENÚ MEJORADO: Selección por Dominio para no perder módulos
        st.write("### 🧭 Explorador de Bóveda")
        cat_select = st.selectbox("Seleccione Dominio:", list(CATEGORIAS_MASTER.keys()))
        
        # Lista los módulos del dominio pero permite ver el 01 siempre
        opciones_menu = CATEGORIAS_MASTER[cat_select]
        mod_id = st.radio("Analizador Activo:", opciones_menu, format_func=lambda x: f"Módulo {x}")
        
        st.divider()
        st.info("💡 **Tip:** El Radar siempre procesa los 80 ejes, aunque usted navegue por módulos específicos.")

    # ROUTER DE SECCIONES
    if mod_id == "01":
        render_radar_80()
    else:
        st.title(f"Módulo {mod_id}: {ANALYSER_DB[mod_id]}")
        st.markdown("---")
        c1, c2 = st.columns([2, 1])
        with c1:
            st.write("#### Telemetría en Tiempo Real")
            st.line_chart(np.random.normal(50, 5, 24), color="#0071E3")
        with c2:
            st.metric("Estado de Sensor", "Sync", "100%")
            st.write("**Protocolo:** TRL-4")
            st.write("**Ubicación:** Nodo Master")

if __name__ == "__main__":
    main()
