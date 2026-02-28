import streamlit as st
import requests

# DEBE SER LA MISMA QUE EN EL ESP32
URL = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

st.title("🛰️ AIHumanity: Panel de Control")

if st.button('🔄 ACTUALIZAR'):
    st.rerun()

try:
    r = requests.get(URL)
    data = r.json()
    if data:
        st.metric("LUZ", data['luz'])
        st.metric("TEMP", data['temp'])
        st.success("SISTEMA ONLINE")
    else:
        st.error("No hay datos en la nube")
except:
    st.write("Conectando...")
