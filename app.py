import streamlit as st
import requests

st.set_page_config(page_title="AIHumanity Master", page_icon="🛡️")
st.title("🛡️ AIHumanity | Panel HSE Codelco")

# URL que usted acaba de encontrar
URL_BASE = "https://aihumanity-hse-3a7eb-default-rtdb.firebaseio.com/nodo1.json"

try:
    response = requests.get(URL_BASE)
    data = response.json()
    
    if data:
        col1, col2 = st.columns(2)
        col1.metric("Temperatura Mina", f"{data['temp']} °C")
        col2.metric("Nivel de Luz", f"{data['luz']} lx")
        
        if data['puesto']:
            st.success("✅ Operario con EPP detectado")
        else:
            st.error("🚨 ALERTA: Operario sin casco")
    else:
        st.info("📡 Sincronizando... esperando datos del ESP32.")
except Exception as e:
    st.error(f"Error de conexión: {e}")

st.button("Actualizar datos")
