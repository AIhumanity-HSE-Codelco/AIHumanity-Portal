import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE V38 ---
st.set_page_config(page_title="AIH MASTER | V38 RECOVERY", layout="wide")

# --- 2. BLINDAJE VISUAL CUPERTINO (RESPONSIVE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 350px !important; 
        }
        /* Optimización de métricas para Tablets/Phones */
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; border: 1px solid #D2D2D7 !important; 
            border-radius: 12px !important; padding: 15px !important;
        }
        h1 { font-size: 1.8rem !important; font-weight: 700 !important; color: #1D1D1F !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. ESTRUCTURA DE DATOS (80 ANALIZADORES) ---
MODULOS_80 = [f"{str(i).zfill(2)}" for i in range(1, 81)]

# Grupos de Navegación (Para que el menú sea limpio)
GRUPOS = {
    "💎 ESTRATÉGICO": ["01", "13", "80"],
    "💨 HSE / QUÍMICA": ["02", "06", "41", "42", "47"],
    "🛰️ COMM / AERO": ["49", "52", "57", "58", "64"],
    "🌍 GEOTECNIA": ["05", "07", "26", "61", "66"],
    "🚜 OPERACIONES": ["08", "21", "29", "31", "39"]
}

# --- 4. RENDERIZADO DEL RADAR INDESTRUCTIBLE ---

def render_radar_master():
    st.title("01 💎 Cerebro de Riesgo Compuesto (IRC-80)")
    
    # Datos para los 80 ejes (Backend Fuerte)
    etiquetas = [f"M{i}" for i in MODULOS_80]
    np.random.seed(99) # Semilla fija para evitar parpadeos
    valores = np.random.randint(30, 85, 80)
    
    # Geometría cerrada
    v_plot = np.append(valores, valores[0])
    e_plot = np.append(etiquetas, etiquetas[0])
    
    fig = go.Figure()
    
    # El "Músculo" de la gráfica: Área de Riesgo
    fig.add_trace(go.Scatterpolar(
        r=v_plot, theta=e_plot, fill='toself',
        line=dict(color='#0071E3', width=1),
        fillcolor='rgba(0, 113, 227, 0.12)',
        hoverinfo='r+theta'
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="white",
            radialaxis=dict(visible=True, gridcolor="#E5E5E5", range=[0, 100], tickfont=dict(size=8)),
            angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=6), tickangle=0)
        ),
        showlegend=False,
        paper_bgcolor='white',
        height=700,
        margin=dict(t=20, b=20, l=10, r=10)
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    

    # Panel de Estado (Métricas Apple)
    c1, c2, c3 = st.columns(3)
    c1.metric("IRC PROMEDIO", f"{valores.mean():.1f}%", "Estable")
    c2.metric("SINCRO NODOS", "70,000", "100%")
    c3.metric("BÓVEDA", "V38-Full", "Online")

# --- 5. NAVEGACIÓN Y MAIN ---
def main():
    apply_bunker_style()
    
    with st.sidebar:
        st.markdown("<h1>AIH MASTER</h1>", unsafe_allow_html=True)
        st.caption(f"80 ANALIZADORES | BÓVEDA ACTIVA | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        # Selector de Categoría para evitar el colapso del menú
        cat = st.selectbox("DOMINIO DE RIESGO:", list(GRUPOS.keys()))
        mod = st.radio("ANALIZADOR:", GRUPOS[cat], format_func=lambda x: f"Módulo {x}")
        
        st.divider()
        st.info("Sincronización GPS RTK (M57): Activa")

    # ROUTER
    if mod == "01":
        render_radar_master()
    else:
        st.title(f"Módulo {mod}: Telemetría")
        st.line_chart(np.random.normal(50, 5, 24
