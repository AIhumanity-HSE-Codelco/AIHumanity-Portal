import streamlit as st
import requests
import pandas as pd
import time
from datetime import datetime

st.title("🛡️ AIHumanity Master | Monitor de Ondas HSE")

# Contenedor para el gráfico de flujo
if 'historico' not in st.session_state:
    st.session_state.historico = pd.DataFrame(columns=['Hora', 'Luz', 'Temp'])

URL = "https://aihumanity-hse-3a7eb-default-rtdb.firebaseio.com/nodo1.json"

def update():
    try:
        data = requests.get(URL).json()
        if data:
            # Añadir a la serie de tiempo para el gráfico de ondas
            nueva_fila = {'Hora': datetime.now(), 'Luz': data['luz'], 'Temp': data['temp']}
            st.session_state.historico = pd.concat([st.session_state.historico, pd.DataFrame([nueva_fila])]).tail(20)
            
            # Métricas en tiempo real
            c1, c2 = st.columns(2)
            c1.metric("LUZ (Sensor Real)", data['luz'])
            c2.metric("HORA SINCRONIZADA", data.get('hora', 'Error NTP'))

            # GRÁFICO DE ONDAS (FLUJO DE DATOS)
            st.subheader("📈 Flujo de Datos de Sensores (Ondas)")
            st.line_chart(st.session_state.historico.set_index('Hora')[['Luz']])
            
            # ANALISIS IA
            if data['luz'] < 100:
                st.warning("⚠️ ANALISIS IA: Baja visibilidad detectada en Nodo 1. Riesgo de incidente elevado.")
    except:
        st.error("Perdida de conexión con el flujo de datos.")

update()
time.sleep(1)
st.rerun()
