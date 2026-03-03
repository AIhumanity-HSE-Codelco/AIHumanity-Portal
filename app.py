import streamlit as st
import pandas as pd
import numpy as np
import time

# Configuración de Cabecera Industrial HSE
st.set_page_config(page_title="AIH MASTER - CODELCO/BHP", layout="wide")

# Estilo de Alto Contraste (Minería Rajo Abierto/Subterráneo)
st.markdown("""
    <style>
    .stApp {background-color: #0d1117; color: #00FF00;}
    .stMetric {background-color: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 5px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ AIHUMANITY MASTER: SISTEMA PREVENTIVO ICR")
st.write(f"**Ubicación de Control:** Bélgica-NYC-Chile | **Estado:** TRL 3-4 Operativo")

# 1. KPIs DE SEGURIDAD CRÍTICA
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("ESTADO HSE", "SEGURO", delta="Óptimo")
with col2: st.metric("NODOS MP10", "200/200", delta="Online")
with col3: st.metric("RIESGO TALUD", "BAJO", delta="-0.02mm")
with col4: st.metric("TRANSITO", "FLUIDO", delta="0 Alertas")

# 2. GENERACIÓN DE LA MATRIZ DE 200 SENSORES
# Simulación de arquitectura de datos para 200 nodos (10 filas x 20 columnas)
nodos = 200
columnas = 20
filas = 10

data = np.random.uniform(30.0, 150.0, size=(filas, columnas))
df = pd.DataFrame(data, columns=[f"C{i}" for i in range(1, columnas + 1)])

# 3. VISTA OPERADOR (ALTO CONTRASTE)
st.subheader("📊 MATRIZ DE RIESGO PREVENTIVO (Polvo/Gases/Vibración)")

def color_vial(val):
    if val > 120: color = '#ff4b4b' # Rojo: Peligro
    elif val > 80: color = '#ffff33' # Amarillo: Precaución
    else: color = '#00ff00'          # Verde: Seguro
    return f'background-color: {color}; color: black; font-weight: bold'

st.dataframe(df.style.applymap(color_vial).format("{:.1f}"), use_container_width=True)

# 4. ANÁLISIS PREDICTIVO (MODO ADMIN)
with st.expander("🔍 DIAGNÓSTICO DE RED Y TRL"):
    st.write("---")
    st.write("**Arquitectura:** Centralizada en IP 45.55.165.70")
    st.write("**Buffer de datos:** Activo (Offline/Online Sync)")
    st.json({"TRL": 3.4, "Nodos_Activos": 200, "Latencia_Bélgica_NYC": "164ms"})
