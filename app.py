import streamlit as st
import pandas as pd
import numpy as np

# 1. INYECCIÓN DE ESTILO (Aquí es donde va tu CSS sin errores)
st.markdown("""
    <style>
    /* Fondo y texto general */
    .stApp { background-color: #050505; color: #e0e0e0; }
    
    /* Encabezado Minero personalizado */
    .header-minero { 
        border-bottom: 3px solid #ffcc00; 
        padding: 20px; 
        background-color: #111; 
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Ajuste de métricas para Alto Contraste */
    div[data-testid="stMetricValue"] { color: #66fcf1 !important; font-size: 3.5rem !important; }
    div[data-testid="stMetricLabel"] { color: #ffcc00 !important; text-transform: uppercase; }
    </style>
    
    <div class="header-minero">
        <h1 style="color: #ffcc00; margin:0;">AIHUMANITY | CONTROL HSE MINERO</h1>
        <p style="color: #66fcf1; margin:0;">ESTADO DE RIESGO PREVENTIVO - TRL-3</p>
    </div>
    """, unsafe_allow_html=True)

# 2. LÓGICA DE DATOS (Prioridad Visual)
# Prioridad 1: Estado Crítico
st.success("✅ ESTADO ACTUAL: OPERACIÓN SEGURA")

# Prioridad 2, 3 y 4: Métricas en Columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="MP10 (Polvo)", value="42.8", delta="-1.2 µg/m³")
with col2:
    st.metric(label="MP2.5 (Fino)", value="14.1", delta="0.5 µg/m³")
with col3:
    st.metric(label="Viento", value="18 km/h", delta="NE")

# 3. VISTA OPERADOR (Gráfico de Tendencia)
st.divider()
st.subheader("📊 Tendencia de Estabilidad de Taludes")
chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['Estabilidad'])
st.area_chart(chart_data)

# 4. MODO ADMIN (Diagnóstico)
with st.sidebar:
    st.header("⚙️ Admin Diagnóstico")
    st.write("Nodo: **ESP32-MASTER-01**")
    st.write("Conectividad: **100%**")
    st.progress(92, text="Batería Nodo")
