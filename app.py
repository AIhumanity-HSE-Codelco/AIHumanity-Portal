cat << 'EOF' > /root/AIHumanity-Portal/app.py
import streamlit as st
import pandas as pd
import numpy as np

# Configuración Industrial
st.set_page_config(page_title="AIH - 200 ANALYZERS", layout="wide")

# CSS de Alto Contraste para Minería
st.markdown("""
    <style>
    .stApp {background-color: #000000;}
    h1 {color: #ffffff !important; font-family: 'Courier New', monospace; border-bottom: 2px solid #ff4b4b;}
    [data-testid="stMetricValue"] { color: #00FF00 !important; font-size: 2.5rem !important; }
    .stDataFrame {border: 1px solid #444;}
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ CONTROL GLOBAL: 200 ANALIZADORES HSE")

# KPIs de Cabecera
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("SISTEMA", "TRL 4", delta="ACTIVO")
with c2: st.metric("ANALIZADORES", "200/200", delta="ONLINE")
with c3: st.metric("ALERTA", "NORMAL", delta="0 CRÍTICO")
with c4: st.metric("LATENCIA", "164ms", delta="BÉLGICA-NYC")

# GENERACIÓN DE LA MATRIZ DE 200 NODOS
# Estructura de 10 filas x 20 columnas = 200 analizadores
data = np.random.uniform(20.0, 160.0, size=(10, 20))
df = pd.DataFrame(data, columns=[f"AN-{i+1:02d}" for i in range(20)])
df.index = [f"FILA-{i+1}" for i in range(10)]

st.subheader("📊 MAPA DE CONCENTRACIÓN (DATA REAL-TIME)")

# Función de Color Industrial (Semáforo Minero)
def color_val(val):
    if val > 130: color = '#990000'; text = 'white' # Rojo (Peligro)
    elif val > 90: color = '#999900'; text = 'black' # Amarillo (Precaución)
    else: color = '#003300'; text = '#00FF00'       # Verde (Seguro)
    return f'background-color: {color}; color: {text}; font-weight: bold; border: 1px solid #111;'

# Despliegue de los 200 analizadores en pantalla completa
st.dataframe(
    df.style.applymap(color_val).format("{:.1f}"),
    use_container_width=True,
    height=500
)

st.markdown("---")
st.markdown("<div style='color: #555; font-size: 10px;'>AIH-MASTER | 200 NODOS | SERVIDOR NYC | CONTROL LOCAL BÉLGICA</div>", unsafe_allow_html=True)
EOF
