import streamlit as st
import pandas as pd
import numpy as np

# Configuración de nivel industrial
st.set_page_config(
    page_title="AIH - Master Control v3",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inyección de CSS para Alto Contraste y Estética Minera
st.markdown("""
    <style>
    body { background-color: #050505; }
    [data-testid="stMetricValue"] { font-size: 28px; color: #E0E0E0; }
    .sensor-card {
        border: 1px solid #333;
        padding: 10px;
        border-radius: 5px;
        background-color: #111;
        text-align: center;
    }
    .status-red { color: #FF4B4B; font-weight: bold; }
    .status-green { color: #00FF00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE SEGURIDAD HSE ---
st.markdown("### 🛡️ CONTROL OPERACIONAL AIHUMANITY | TRL 4")
h1, h2, h3, h4 = st.columns(4)
with h1:
    st.metric("ESTADO HSE", "CRÍTICO", delta="-5%", delta_color="inverse")
with h2:
    st.metric("NODOS ACTIVOS", "198/200", delta="ONLINE")
with h3:
    st.metric("ZONA DE TRÁNSITO", "VEL: 12km/h", delta="NORMAL")
with h4:
    st.metric("TALUDES", "RAVELING", delta="ALERTA", delta_color="off")

st.divider()

# --- PANEL DE ANALIZADORES 1-200 (MATRIZ DE RIESGO) ---
st.subheader("📊 MONITOREO DE ANALIZADORES MP10/MP2.5")

# Generación de datos simulados para 200 sensores
sensor_ids = [f"NODE-{i:03d}" for i in range(1, 201)]
mp10_values = np.random.uniform(10, 85, 200).round(2)
status = ["Green" if v < 50 else "Yellow" if v < 75 else "Red" for v in mp10_values]

# Vista en rejilla (Grid) de alta densidad
cols_per_row = 10
for i in range(0, 200, cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        idx = i + j
        if idx < 200:
            color = "#00FF00" if status[idx] == "Green" else "#FFFF00" if status[idx] == "Yellow" else "#FF0000"
            with cols[j]:
                st.markdown(f"""
                <div style="background-color: {color}; height: 15px; border-radius: 3px; margin-bottom: 5px;" 
                     title="Sensor {sensor_ids[idx]}: {mp10_values[idx]} µg/m³">
                </div>
                """, unsafe_allow_html=True)

st.divider()

# --- ÁREA TÉCNICA: CHANCADO Y STOCKPILES ---
t1, t2 = st.columns([2, 1])
with t1:
    st.subheader("📈 TENDENCIA HISTÓRICA (POLVO & VIENTO)")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Dozing', 'Chancado', 'Stockpiles'])
    st.line_chart(chart_data)

with t2:
    st.subheader("🛠️ DIAGNÓSTICO ADMIN")
    st.write("**Latencia:** 12ms")
    st.write("**Buffer Offline:** 0%")
    st.write("**Uptime:** 99.9%")
    if st.button("REINICIAR BUFFER"):
        st.warning("Reiniciando memoria de sensores...")
