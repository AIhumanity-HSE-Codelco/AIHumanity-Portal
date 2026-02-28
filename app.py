import pandas as pd
import requests

# URL de la base de datos que el ESP32 está alimentando
DB_URL = "https://aihumanity-hse-default-rtdb.firebaseio.com/nodo1.json"

def get_realtime_data():
    response = requests.get(DB_URL)
    return response.json()

data = get_realtime_data()

# Ahora las métricas son REALES
st.metric("Luz (D32)", f"{data['luz']} lx")
if data['puesto']:
    st.success("CASCO PUESTO")
else:
    st.error("CASCO FUERA")
