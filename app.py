import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. CONFIGURACIÓN DE NÚCLEO INMUNE ---
st.set_page_config(page_title="AIH MASTER | 80 MODULOS FIX", layout="wide")

# --- 2. BLINDAJE VISUAL CUPERTINO ---
def apply_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF !important; color: #1D1D1F !important; font-family: -apple-system, sans-serif !important; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7 !important; border-right: 1px solid #D2D2D7 !important; width: 380px !important; }
        div[data-testid="stMetric"] { background-color: #FFFFFF !important; border: 1px solid #D2D2D7 !important; border-radius: 12px !important; padding: 15px !important; }
        h1 { font-weight: 700; color: #1D1D1F; }
        /* Forzar visibilidad de la gráfica */
        .js-plotly-plot { border: 1px solid #F0F0F2 !important; border-radius: 15px; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. DECLARACIÓN INMUTABLE DE LOS 80 ANALIZADORES ---
# Esto evita que desaparezcan al subir a GitHub
MODULOS_80 = [str(i).zfill(2) for i in range(1, 81)]

# Diccionario de nombres clave para asegurar permanencia
NOMBRES_CONTROL = {
    "01": "💎 EL CEREBRO (IRC)", "02": "💨 GASES", "41": "☢️ RADIACTIVIDAD",
    "57": "🛰️ GPS RTK", "64": "🌌 CLIMA SOLAR", "80": "♾️ ENTROPÍA"
}

# --- 4. MOTOR DE RENDERIZADO IRC-80 (FORCE RENDER) ---

def render_80_radar():
    st.title("01 💎 Cerebro de Riesgo Compuesto (IRC-80)")
    
    # Generación de datos persistente
    np.random.seed(100) # Semilla para que la gráfica sea consistente en la web
    valores = np.random.randint(25, 85, 80)
    
    # Cerrar geometría (81 puntos para cerrar el círculo de 80)
    v_plot = np.append(valores, valores[0])
    e_plot = np.append(MODULOS_80, MODULOS_80[0])
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=v_plot, theta=e_plot, fill='toself',
        line=dict(color='#0071E3', width=1.2),
        fillcolor='rgba(0, 113, 227, 0.08)',
        hoverinfo='r+theta'
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="white",
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="#F0F0F2", tickfont=dict(size=8)),
            angularaxis=dict(gridcolor="#F0F0F2", tickfont=dict(size=5), rotation=90, direction="clockwise")
        ),
        paper_bgcolor='white',
        height=750,
        margin=dict(t=40, b=40, l=40, r=40)
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    

    c1, c2, c3 = st.columns(3)
    c1.metric("IRC GLOBAL", f"{valores.mean():.1f}%", "Nominal")
    c2.metric("BÓVEDA SINC", "80 / 80", "Completa")
    c3.metric("NODOS", "70,000", "Sync")

# --- 5. NAVEGACIÓN Y MAIN ---
def main():
    apply_bunker_style()
    
    with st.sidebar:
        st.markdown("<h1>AIH MASTER</h1>", unsafe_allow_html=True)
        st.caption(f"80 ANALIZADORES BLINDADOS | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        # Selector de rango para no saturar el menú lateral pero mantener los 80
        rango = st.radio("SECCIÓN DE BÓVEDA:", ["Módulos 01-20", "Módulos 21-40", "Módulos 41-60", "Módulos 61-80"])
        
        if "01-20" in rango:
            seleccion = st.selectbox("ANALIZADOR:", MODULOS_80[0:20])
        elif "21-40" in rango:
            seleccion = st.selectbox("ANALIZADOR:", MODULOS_80[20:40])
        elif "41-60" in rango:
            seleccion = st.selectbox("ANALIZADOR:", MODULOS_80[40:60])
        else:
            seleccion = st.selectbox("ANALIZADOR:", MODULOS_80[60:80])
            
        st.divider()
        st.info(f"Visualizando: Módulo {seleccion}")

    # RENDERIZADO
    if seleccion == "01":
        render_80_radar()
    else:
        st.title(f"Módulo {seleccion}: {NOMBRES_CONTROL.get(seleccion, 'Telemetría Detallada')}")
        st.line_chart(np.random.normal(50, 5, 24), color="#0071E3")
        st.metric("Integridad de Datos", "100%", "Sync")

if __name__ == "__main__":
    from datetime import datetime
    main()
