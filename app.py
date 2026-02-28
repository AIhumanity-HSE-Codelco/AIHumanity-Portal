import streamlit as st
import requests

# Configuración de Identidad Visual AIH
st.set_page_config(page_title="AIHumanity - Control de Nodo", layout="wide")

# URL de la base de datos (Tu puente de datos)
DB_URL = "https://aihumanity-hse-default-rtdb.firebaseio.com/nodo1.json"

# Interfaz de Usuario
st.title("🛰️ AIHumanity: Gestión HSE")
st.subheader("Monitoreo de Nodo AIDeepMiner (Fase TRL3)")

st.divider()

try:
    # Captura de datos en tiempo real
    response = requests.get(DB_URL, timeout=5)
    data = response.json()

    if data:
        # Layout de métricas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("LUMINOSIDAD", f"{data.get('luz', 0)} lx")
            st.caption("Módulo de Luz (D32)")
            
        with col2:
            st.metric("TEMPERATURA", f"{data.get('temp', 0)} °C")
            st.caption("Módulo Térmico (D26)")
            
        with col3:
            # Estatus de conexión basado en el sensor IR
            puesto = data.get('puesto', False)
            st.write("**ESTATUS DEL CASCO (D25):**")
            if puesto:
                st.success("ONLINE - CASCO PUESTO")
            else:
                st.error("ALERTA - CASCO SACADO")
    else:
        st.info("📡 Esperando datos del ESP32... (Luz azul debe estar fija)")

except Exception as e:
    st.error("Error de conexión con la base de datos.")

# Botón de Sincronización Manual
if st.button("🔄 Sincronizar Ahora"):
    st.rerun()
