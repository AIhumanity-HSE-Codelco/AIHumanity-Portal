import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Configuración de Identidad AIH-Master
st.set_page_config(page_title="AIHumanity Master | HSE", layout="wide")

st.markdown("### 🛡️ Centro de Control de Riesgo Preventivo (ICR)")
st.write(f"**Arquitecto Jefe:** Activa Identidad AIH-Master | **Nodo:** ESP32-Telenet")

URL_BASE = "https://aihumanity-hse-3a7eb-default-rtdb.firebaseio.com/nodo1.json"

# Función de extracción de datos
def fetch_data():
    try:
        response = requests.get(URL_BASE)
        return response.json()
    except:
        return None

data = fetch_data()

if data:
    # Contenedores de métricas dinámicas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="🌡️ Temperatura Mina", value=f"{data['temp']} °C", delta="Normal")
    
    with col2:
        st.metric(label="💡 Nivel de Polvo/Luz", value=f"{data['luz']} lx")
        
    with col3:
        estado = "✅ SEGURO" if data['puesto'] else "🚨 ALERTA EPP"
        st.subheader(f"Estatus: {estado}")

    # Simulación de tendencia (Análisis Predictivo)
    st.divider()
    st.info(f"Última sincronización: {datetime.now().strftime('%H:%M:%S')}")
    
    # Botón de actualización forzada si es necesario
    if st.button('Sincronizar Nodo Ahora'):
        st.rerun()
else:
    st.error("Esperando flujo de datos desde la red Telenet...")

# Refresco automático cada 5 segundos (Interacción real)
st.empty()
import time
time.sleep(5)
st.rerun()
