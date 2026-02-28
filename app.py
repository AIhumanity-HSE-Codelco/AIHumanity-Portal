import streamlit as st
import requests

st.title("🛡️ AIHumanity | Panel HSE")
st.write("Estado de los 70k nodos en tiempo real")

# Conexión con la base de datos (Donde el ESP32 deja sus mensajes)
URL = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

try:
    datos = requests.get(URL).json()
    if datos:
        st.metric("Temperatura", f"{datos['temp']} °C")
        st.metric("Luz", f"{datos['luz']} lx")
        st.success("✅ Sistema Operativo")
    else:
        st.warning("Esperando señal del sensor...")
except:
    st.error("Error de conexión")
