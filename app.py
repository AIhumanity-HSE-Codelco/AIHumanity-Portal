import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página estilo "Tesla Full Screen"
st.set_page_config(page_title="AIH | TESLA OPERATIONAL CONTROL", layout="wide", initial_sidebar_state="collapsed")

# CSS: Tesla Design Language (Cyber-Industrial)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;600&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        color: #E6E6E6;
        font-family: 'Inter', sans-serif;
    }
    
    .stMetric {
        background-color: #0A0A0A;
        border: 1px solid #222;
        padding: 20px;
        border-radius: 2px;
    }
    
    [data-testid="stMetricValue"] {
        font-family: 'Orbitron', sans-serif;
        color: #FFFFFF !important;
        font-size: 32px !important;
    }

    /* Estilo de barra de progreso Tesla */
    .stProgress > div > div > div > div {
        background-color: #E82127; /* Rojo Tesla */
    }

    .sensor-grid-unit {
        height: 8px;
        width: 100%;
        margin-bottom: 2px;
        border-radius: 1px;
    }
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .status-card {
        border-left: 4px solid #E82127;
        background: linear-gradient(90deg, #111 0%, #000 100%);
        padding: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL SUPERIOR (NAVBAR) ---
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown("# AIH × TESLA ENERGY")
    st.markdown("<p style='color: #666;'>HSE MINING PREDICTIVE UNIT | TRL 4 | NODE-04-NYC</p>", unsafe_allow_html=True)
with c2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg", width=120)

st.divider()

# --- MÉTRICAS DE IMPACTO ---
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("POWER LOAD", "98%", "OPTIMAL")
with m2:
    st.metric("AIR QUALITY (MP10)", "24.5", "-4.2")
with m3:
    st.metric("TALUD STABILITY", "99.2%", "STABLE")
with m4:
    st.metric("HSE STATUS", "NOMINAL", delta_color="off")

# --- VISUALIZACIÓN DE LOS 200 ANALIZADORES (MATRIZ CYBERTRUCK) ---
st.markdown("### ANALYZER MATRIX [200 UNITS]")

# Simulación de datos técnica
cols_per_row = 25
rows = 8
data_values = np.random.uniform(0, 100, 200)

for r in range(rows):
    cols = st.columns(cols_per_row)
    for c in range(cols_per_row):
        idx = r * cols_per_row + c
        if idx < 200:
            val = data_values[idx]
            # Escala de grises y rojos (Tesla Style)
            bg_color = "#E82127" if val > 90 else "#333" if val > 20 else "#111"
            cols[c].markdown(f'<div class="sensor-grid-unit" style="background-color: {bg_color};"></div>', unsafe_allow_html=True)

st.divider()

# --- SECCIÓN OPERATIVA: STOCKPILES & DOZING ---
t1, t2 = st.columns([2, 1])
with t1:
    st.markdown("### OPERATIONAL TELEMETRY")
    # Gráfico de área oscuro
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Dozing', 'Chancado', 'Stockpiles']
    )
    st.area_chart(chart_data)

with t2:
    st.markdown("<div class='status-card'><strong>SYSTEM LOGS</strong><br><small>Re-encrypting Node 104.236.210.4...<br>Syncing with GitHub Main...<br>HSE Protocol Active.</small></div>", unsafe_allow_html=True)
    if st.button("RUN DIAGNOSTIC"):
        st.write("Checking 70k Nodes...")
        st.progress(0.7)
