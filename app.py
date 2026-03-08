import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página - Look & Feel Limpio
st.set_page_config(page_title="AIH Master - Cupertino Edition", layout="wide")

# Estilo CSS: Cupertino Design System (Blanco, Sombras suaves, SF Pro)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF;
        color: #1D1D1F;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    .stMetric {
        background-color: #F5F5F7;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        border: 1px solid #E5E5E7;
    }
    
    [data-testid="stMetricLabel"] { color: #86868B !important; font-size: 14px !important; }
    [data-testid="stMetricValue"] { color: #1D1D1F !important; font-weight: 600 !important; }
    
    .sensor-dot {
        height: 12px;
        width: 12px;
        border-radius: 50%;
        display: inline-block;
        margin: 2px;
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    h1, h2, h3 { font-weight: 600 !important; color: #1D1D1F !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SUPERIOR ---
st.markdown("## AIH Portal v3")
st.markdown("<p style='color: #86868B;'>Control de Riesgo Predictivo · TRL 4</p>", unsafe_allow_html=True)

# --- MÉTRICAS CUERTINO ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label="ESTADO HSE", value="Nominal", delta="Seguro")
with c2:
    st.metric(label="MP10 (AVG)", value="34.2 µg/m³", delta="-2%")
with c3:
    st.metric(label="VIENTO", value="14 km/h", delta="NE")
with c4:
    st.metric(label="CONECTIVIDAD", value="99.9%", delta="Estable")

st.divider()

# --- GRILLA DE ANALIZADORES (200 NODOS) ---
st.subheader("Estado de Nodos (1-200)")

# Generar matriz de 200 sensores
cols_grid = 20  # 20 columnas x 10 filas
for row in range(10):
    cols = st.columns(cols_grid)
    for col in range(cols_grid):
        sensor_id = row * cols_grid + col
        # Lógica de color suave (Pasteles Cupertino)
        # Verde Apple: #34C759, Amarillo Apple: #FFCC00, Rojo Apple: #FF3B30
        val = np.random.rand()
        color = "#34C759" if val > 0.15 else "#FFCC00" if val > 0.05 else "#FF3B30"
        
        with cols[col]:
            st.markdown(f'<div class="sensor-dot" style="background-color: {color};" title="Nodo {sensor_id+1}"></div>', unsafe_allow_html=True)

st.divider()

# --- SECCIÓN OPERATIVA ---
t1, t2 = st.columns([2, 1])
with t1:
    st.markdown("### Tendencia de Particulado")
    chart_data = pd.DataFrame(np.random.randn(15, 2), columns=['MP10', 'MP2.5'])
    st.area_chart(chart_data, color=["#007AFF", "#5856D6"]) # Azul y Violeta Apple

with t2:
    st.markdown("### Diagnóstico")
    st.write("**Sistema:** AIHumanity-HSE-Uniting")
    st.write("**Ubicación:** NYC3 Cloud Instance")
    st.write("**Protocolo:** REST/JSON Over HTTP")
    if st.button("Exportar Reporte PDF"):
        st.info("Generando reporte ejecutivo...")
