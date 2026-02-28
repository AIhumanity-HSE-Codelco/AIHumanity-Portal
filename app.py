import streamlit as st
import pandas as pd

# --- AIH-MASTER: MONITOR DE NODOS SINCRONIZADOS ---
st.set_page_config(page_title="AIH-MASTER | LIVE SYNC", layout="wide")

st.markdown("""
    <style>
    .apple-card { background: white; border-radius: 20px; padding: 25px; box-shadow: 0 8px 30px rgba(0,0,0,0.03); margin-bottom: 20px; }
    .status-online { color: #34c759; font-weight: 600; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# CABECERA DE CONECTIVIDAD
st.title("🌐 Network Governance Center")
st.markdown(f"**SSID Activo:** telenet 5E4ED | **Gateway:** AIHumanity Cloud")

col_net, col_sensors = st.columns([1, 2])

with col_net:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("Estado del Nodo")
    st.write("ID: **AIDeepMiner-01**")
    st.markdown("Status: <span class='status-online'>● ONLINE</span>", unsafe_allow_html=True)
    st.write("IP: 192.168.1.105")
    st.button("Reiniciar Conexión")
    st.markdown('</div>', unsafe_allow_html=True)

with col_sensors:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    st.subheader("Sensores Activados (Telemetry)")
    
    # Mapeo de Sensores en el Casco
    metrics = {
        "Módulo Polvo (PM10)": "ACTIVO",
        "Biometría (HR)": "ACTIVO",
        "Giroscopio (Caídas)": "SINCRO",
        "GPS Diferencial": "BUSCANDO..."
    }
    
    for sensor, state in metrics.items():
        st.write(f"{sensor}: **{state}**")
    
    st.divider()
    st.info("El nodo está transmitiendo exitosamente a través del Web Server configurado.")
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("AIH-MASTER v24.0 | Protocolo de Conectividad TRL4 | Uniting Technology Belgium")
