import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE V35.1 ---
st.set_page_config(page_title="AIH MASTER | RECOVERY 80", layout="wide")

# --- 2. BLINDAJE VISUAL DE ALTO CONTRASTE (FONDO OSCURO) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #0E1117 !important; color: #FFFFFF !important; }
        section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 1px solid #30363D !important; width: 450px !important; }
        div[data-testid="stMetric"] { 
            background-color: #1C2128 !important; border: 1px solid #30363D !important; 
            padding: 15px !important; border-radius: 12px !important;
        }
        h1, h2, h3 { color: #58A6FF !important; font-weight: 700 !important; }
        .stRadio > label { color: #8B949E !important; font-size: 0.8em !important; font-weight: bold !important; }
        /* Fix para que la gráfica no desaparezca */
        .js-plotly-plot { background-color: transparent !important; border-radius: 15px !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. DICCIONARIO MAESTRO DE LOS 80 ANALIZADORES (RESUMEN ESTRATÉGICO) ---
# Se cargan dinámicamente para no saturar el sidebar
MODULOS_80 = [f"{str(i).zfill(2)} Analizador" for i in range(1, 81)]
NOMBRES_EPICOS = {
    "01": "💎 EL CEREBRO (IRC-80)", "21": "🌪️ VENTILACIÓN 3D", "41": "☢️ RADIACTIVIDAD",
    "57": "🛰️ GPS RTK PRECISION", "66": "🕸️ MICRO-SISMICIDAD", "80": "♾️ ENTROPÍA"
}

# --- 4. MOTOR DE LA GRÁFICA INDESTRUCTIBLE ---

def render_radar_80():
    st.title("01 💎 Cerebro de Riesgo Total (IRC-80)")
    
    # Generación de 80 puntos de datos reales/simulados
    etiquetas = [str(i).zfill(2) for i in range(1, 81)]
    valores = np.random.randint(20, 95, 80)
    # Cerramos el círculo para que la gráfica sea perfecta
    valores = np.append(valores, valores[0])
    etiquetas = np.append(etiquetas, etiquetas[0])
    
    fig = go.Figure()
    
    # Capa 1: El Área de Riesgo
    fig.add_trace(go.Scatterpolar(
        r=valores, theta=etiquetas, fill='toself',
        name='Perfil de Riesgo AIH',
        line=dict(color='#58A6FF', width=2),
        fillcolor='rgba(88, 166, 255, 0.2)'
    ))
    
    # Capa 2: Puntos de Control (Nodos)
    fig.add_trace(go.Scatterpolar(
        r=valores, theta=etiquetas, mode='markers',
        marker=dict(size=4, color='#34D399')
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="#161B22",
            radialaxis=dict(visible=True, showline=False, gridcolor="#30363D", tickfont=dict(color="#8B949E", size=8)),
            angularaxis=dict(gridcolor="#30363D", tickfont=dict(color="#8B949E", size=7), rotation=90)
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=900,
        margin=dict(t=30, b=30, l=50, r=50)
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    

    # KPIs de Control
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC PROMEDIO", f"{valores.mean():.1f}%", "Estable")
    c2.metric("VAR. CRÍTICAS", "80 Analizadores", "Full Sync")
    c3.metric("NODOS MESH", "70,000", "Activos")
    c4.metric("PRECISIÓN GPS", "1.2 cm", "RTK FIX")

# --- 5. NAVEGACIÓN Y MAIN ---
def main():
    apply_bunker_style()
    
    with st.sidebar:
        st.markdown("<h2 style='color:#58A6FF;'>AIH MASTER V35.1</h2>", unsafe_allow_html=True)
        st.caption(f"MODO RECUPERACIÓN GRÁFICA | {datetime.now().strftime('%H:%M:%S')}")
        st.divider()
        
        # Filtro rápido para no perderse en los 80 módulos
        grupo = st.selectbox("Categoría de Análisis:", ["Operaciones", "HSE / Nuclear", "Comunicaciones / Aero", "Caos / Entropía"])
        
        # El radio ahora es dinámico para no saturar
        seleccion = st.radio("Analizador Seleccionado:", MODULOS_80[:20], label_visibility="collapsed")
        
        st.divider()
        st.info("Gráfica Blindada: Si desaparece, use 'R' para refrescar el búnker.")

    # ROUTER DE RENDERIZADO
    if "01" in seleccion or "Analizador" in seleccion:
        render_radar_80()
    else:
        st.warning("Seleccione Módulo 01 para ver la gráfica total.")

if __name__ == "__main__":
    main()
