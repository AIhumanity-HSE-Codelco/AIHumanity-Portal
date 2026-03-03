import streamlit as st
import pandas as pd
import numpy as np

# 1. Configuración de Escala Industrial
st.set_page_config(page_title="AIH MASTER - HSE CONTROL", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS de Alto Impacto (Fondo Negro Absoluto + Neon)
st.markdown("""
    <style>
    .stApp {background-color: #000000;}
    h1 {color: #ffffff !important; font-family: 'Courier New', monospace; font-weight: bold; border-bottom: 2px solid #ff4b4b;}
    .css-10trblm {color: #ffffff !important;}
    /* Tarjetas de Métricas */
    [data-testid="stMetricValue"] { color: #00ff00 !important; font-size: 32px !important; }
    [data-testid="stMetricDelta"] { color: #ff4b4b !important; }
    /* Ajuste de Matriz */
    .stDataFrame { border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado Prioritario Visual (Estado HSE -> MP10 -> MP2.5 -> Conectividad)
st.title("🛡️ AIHUMANITY MASTER | CONTROL PREVENTIVO")

c1, c2, c3, c4 = st.columns([1.5, 1, 1, 1])
with c1:
    st.metric("ESTADO HSE", "OPERACIÓN SEGURA", delta="Sin Incidentes")
with c2:
    st.metric("MP10 AVG", "42 µg/m³", delta="NORMAL")
with c3:
    st.metric("MP2.5 AVG", "12 µg/m³", delta="ESTABLE")
with c4:
    st.metric("CONECTIVIDAD", "100%", delta="200 NODOS")

st.markdown("---")

# 4. Matriz de Sensores (200 Nodos: 10x20)
st.subheader("📊 MATRIZ DE RIESGO PREVENTIVO - 200 NODOS (TRL 3-4)")

# Generar datos de 200 sensores
data = np.random.uniform(20.0, 150.0, size=(10, 20))
df = pd.DataFrame(data, columns=[f"N{i+1}" for i in range(20)])

# Función de mapeo de colores (Verde/Amarillo/Rojo)
def apply_color_matrix(val):
    if val > 130: color = '#ff0000' # Alarma Crítica
    elif val > 90: color = '#ffff00' # Precaución
    else: color = '#008000'          # Seguro (Verde Oscuro para contraste)
    return f'background-color: {color}; color: white; font-weight: bold; border: 1px solid black;'

# Mostrar matriz compacta
st.dataframe(
    df.style.applymap(apply_color_matrix).format("{:.0f}"),
    use_container_width=True,
    height=400
)

# 5. Panel Lateral de Diagnóstico (Vista Admin)
with st.sidebar:
    st.header("⚙️ ADMIN DIAGNÓSTICO")
    st.info("📡 Servidor: NYC-45.55.165.70")
    st.warning("📍 Origen Control: Bélgica")
    st.write("**Sensores Activos:**")
    st.write("- MP10 / MP2.5")
    st.write("- Viento (Vel/Dir)")
    st.write("- Taludes (Raveling/Erosión)")
    if st.button("REINICIAR BUFFER"):
        st.success("Buffer limpiado.")
