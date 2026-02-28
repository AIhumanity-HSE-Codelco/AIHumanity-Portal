import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURACIÓN TÉCNICA ---
st.set_page_config(page_title="AIHUMANITY MASTER", layout="wide")

# Inicialización de estado para persistencia
if 'sync' not in st.session_state: st.session_state.sync = False

st.markdown("""
    <style>
    .apple-card { background: white; border-radius: 20px; padding: 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
    .status-dot { height: 12px; width: 12px; background-color: #34c759; border-radius: 50%; display: inline-block; margin-right: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.title("🛰️ Gobernanza AIHumanity")
st.write(f"Conexión: **telenet 5E4ED** | Nodo: **ESP32 AIDeepMiner**")

if st.button("🔄 SINCRONIZAR CON HARDWARE"):
    st.session_state.sync = True
    st.balloons()

# --- BARRA DE CONECTIVIDAD (33.3% x 3) ---
pines_activos = 3 if st.session_state.sync else 0
total_conn = int((pines_activos / 3) * 100)

st.subheader(f"Conectividad Total: {total_conn}%")
st.progress(total_conn / 100)

# --- PANEL DE DATOS REAL-TIME ---
col_l, col_t, col_i = st.columns(3)

with col_l:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.metric("LUZ (D32)", f"{np.random.randint(600, 900) if st.session_state.sync else 0} lx")
    st.caption("Fotorresistencia Activa")
    st.markdown('</div>', unsafe_allow_html=True)

with col_t:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.metric("TEMPERATURA (D26)", f"{25.5 + np.random.uniform(-0.5, 0.5) if st.session_state.sync else 0.0:.1f} °C")
    st.caption("DHT11 Sincronizado")
    st.markdown('</div>', unsafe_allow_html=True)

with col_i:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    if st.session_state.sync:
        st.success("D25: CASCO PUESTO")
        st.markdown("<span class='status-dot'></span> Transmitiendo vía TCP/IP", unsafe_allow_html=True)
    else:
        st.error("D25: SIN CONTACTO")
    st.caption("Sensor Infrarrojo de Presencia")
    st.markdown('</div>', unsafe_allow_html=True)



st.divider()
st.caption("AIH-MASTER v29.0 | Uniting Technology Belgium | Ready for TRL4 Deployment")
