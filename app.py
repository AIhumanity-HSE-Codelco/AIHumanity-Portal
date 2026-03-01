import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO INMUNE ---
st.set_page_config(page_title="AIH MASTER | MULTI-DEVICE", layout="wide")

# --- 2. BLINDAJE VISUAL DINÁMICO (PC / TABLET / MOBILE) ---
def apply_bunker_style():
    st.markdown("""
        <style>
        /* Base Cupertino White */
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, system-ui, sans-serif !important; }
        
        /* Sidebar Optimizado para Touch y Click */
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7 !important; 
            border-right: 1px solid #D2D2D7 !important; 
            width: clamp(280px, 20vw, 400px) !important; 
        }

        /* Tipografía Optimizada: Responsiva */
        h1 { font-size: clamp(1.5rem, 4vw, 2.5rem) !important; font-weight: 700 !important; color: #1D1D1F !important; }
        h3 { font-size: clamp(1rem, 2.5vw, 1.5rem) !important; color: #86868B !important; }
        
        /* Métricas Estilo Card Apple */
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF !important; border: 1px solid #D2D2D7 !important; 
            padding: clamp(10px, 2vw, 20px) !important; border-radius: 16px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        }

        /* Ajuste de Números y Letras en Gráficos */
        .js-plotly-plot .plotly .modebar { display: none !important; }
        
        /* Ocultar etiquetas del radar si son > 40 para evitar colapso visual en móviles */
        @media (max-width: 768px) {
            .stPlotlyChart { height: 400px !important; }
        }
        </style>
        """, unsafe_allow_html=True)

# --- 3. DICCIONARIO DE GOBERNANZA (GRUPOS LÓGICOS) ---
CATEGORIAS = {
    "💎 ESTRATÉGICO": ["01 💎 EL CEREBRO (IRC-80)", "13 📊 REPORTES BI", "80 ♾️ ENTROPÍA"],
    "💨 HSE & QUÍMICA": ["02 💨 GASES", "41 ☢️ RADIACTIVIDAD", "42 🌫️ RADÓN", "43 🧪 XRF", "48 🧪 REACTIVOS"],
    "🛰️ COM & AERO": ["49 🛰️ SATELITAL", "57 🛰️ GPS RTK", "58 🚁 UTM DRONES", "63 🛡️ ADS-B"],
    "🌍 GEOTECNIA": ["05 🗺️ GIS", "07 🌍 SISMO", "26 🛰️ RADAR SUBSIDENCIA", "66 🕸️ MICRO-SISMO"],
    "🚜 OPERACIONES": ["08 ⚙️ ACTIVOS", "21 🌪️ VENTILACIÓN", "29 🚛 FATIGA", "39 🤖 AUTÓNOMOS"]
}

# --- 4. MOTOR DE RENDERIZADO IRC-80 (BLINDADO) ---

def render_radar_cupertino_80():
    st.title("01 💎 Cerebro de Riesgo Total (IRC-80)")
    
    # Generar datos para los 80 ejes
    etiquetas = [str(i).zfill(2) for i in range(1, 81)]
    valores = np.random.randint(25, 85, 80)
    
    # Cerrar el trazado
    v_plot = np.append(valores, valores[0])
    e_plot = np.append(etiquetas, etiquetas[0])
    
    fig = go.Figure()
    
    # Capa de Riesgo Compuesto
    fig.add_trace(go.Scatterpolar(
        r=v_plot, theta=e_plot, fill='toself',
        line=dict(color='#0071E3', width=1.5),
        fillcolor='rgba(0, 113, 227, 0.08)',
        hoverinfo='r+theta'
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="white",
            radialaxis=dict(visible=True, showline=False, gridcolor="#E5E5E5", tickfont=dict(size=8, color="#86868B")),
            angularaxis=dict(gridcolor="#E5E5E5", tickfont=dict(size=6, color="#86868B"))
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=40, b=40, l=40, r=40),
        height=700 if st.sidebar.checkbox("Expandir Radar", True) else 400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    

    # KPIs Responsivos
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1: st.metric("IRC AGREGADO", f"{valores.mean():.1f}%", "Nominal")
    with c2: st.metric("ESTADO GPS", "FIX RTK", "1.2cm")
    with c3: st.metric("NODOS MESH", "70,000", "Sync")

# --- 5. NAVEGACIÓN Y MAIN ---
def main():
    apply_bunker_style()
    
    with st.sidebar:
        st.markdown("<h2 style='color:#1D1D1F;'>AIH MASTER V36</h2>", unsafe_allow_html=True)
        st.caption(f"80 ANALIZADORES | TRL-4 | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        # MEJORA DE MENÚ: Navegación por Grupo
        cat_select = st.selectbox("DOMINIO DE ANÁLISIS:", list(CATEGORIAS.keys()))
        mod_select = st.radio("ANALIZADOR:", CATEGORIAS[cat_select])
        
        st.divider()
        st.caption("📱 Dispositivo: Optimizado para PC/Tablet/Móvil")

    # ROUTER DE SECCIONES
    if "01" in mod_select:
        render_radar_cupertino_80()
    else:
        st.title(mod_select)
        st.write("### Telemetría de Analizador")
        st.line_chart(np.random.normal(50, 10, 24), color="#0071E3")
        st.info("Visualización optimizada para campo.")

if __name__ == "__main__":
    main()
