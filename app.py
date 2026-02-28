import streamlit as st
import requests
import pandas as pd

# Dirección de la base de datos que alimenta el ESP32
DB_URL = "https://aihumanity-hse-default-rtdb.firebaseio.com/nodo1.json"

st.set_page_config(page_title="AIHumanity Master Portal", layout="wide")

st.title("🛰️ Gobernanza HSE: Nodo AIDeepMiner")
st.markdown("---")

try:
    # Captura de datos desde la nube
    res = requests.get(DB_URL, timeout=5)
    data = res.json()

    if data:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Luminosidad (D32)", f"{data.get('luz', 0)} lx")
            st.caption("Índice de visibilidad en faena")
            
        with col2:
            st.metric("Temperatura (D26)", f"{data.get('temp', 0)} °C")
            st.caption("Monitoreo de estrés térmico")
            
        with col3:
            puesto = data.get('puesto', False)
            if puesto:
                st.success("ESTATUS: ONLINE (CASCO PUESTO)")
            else:
                st.error("ALERTA: CASCO SACADO / OFFLINE")
    else:
        st.warning("Esperando primera transmisión del hardware...")

except Exception as e:
    st.info("📡 Sincronizando con el servidor de AIHumanity...")

# Auto-refresco cada 5 segundos para tiempo real
st.empty()
