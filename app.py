import streamlit as st
import requests

# URL de la base de datos (La misma que pusiste en el ESP32)
DB_URL = "https://aihumanity-hse-default-rtdb.firebaseio.com/nodo1.json"

st.title("🛰️ AIHumanity Master Portal")

try:
    # Intentar obtener datos reales del ESP32
    response = requests.get(DB_URL, timeout=5)
    data = response.json()

    # Si la data existe, la mostramos
    if data:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Usamos .get() para evitar errores si una llave no existe
            luz = data.get('luz', 0)
            st.metric("Luz (D32)", f"{luz} lx")
            
        with col2:
            temp = data.get('temp', 0.0)
            st.metric("Temperatura (D26)", f"{temp} °C")
            
        with col3:
            puesto = data.get('puesto', False)
            if puesto:
                st.success("CASCO PUESTO")
            else:
                st.error("CASCO FUERA")
    else:
        st.warning("Esperando datos del nodo AIDeepMiner...")

except Exception as e:
    st.info("📡 Nodo en modo Standby. Asegúrese de que el ESP32 tenga la LUZ AZUL FIJA.")
    # Valores por defecto para que la interfaz no de error
    st.metric("Luz (D32)", "0 lx")
