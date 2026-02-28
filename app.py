import streamlit as st
import requests
from openai import OpenAI
import time

# --- 1. CONFIGURACIÓN Y ESTILO (Protocolo Cupertino) ---
st.set_page_config(page_title="AIHumanity Master", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; color: #FFFFFF; }</style>", unsafe_allow_html=True)

# --- 2. INICIALIZACIÓN DE MOTORES (Bóveda de Secrets) ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
URL_FIREBASE = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

st.title("🛡️ AIHumanity | DataStream Master")

# --- 3. CAPTURA Y VALIDACIÓN DE DATOS ---
try:
    response = requests.get(URL_FIREBASE, timeout=5)
    data = response.json()
    
    if data:
        # Definimos las variables AQUÍ para evitar el NameError
        luz = data.get('luz', 0)
        temp = data.get('temp', 0)
        puesto = data.get('puesto', False)

        # Visualización de Métricas
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("ILUMINACIÓN", f"{luz} lx")
        with col2: st.metric("TEMPERATURA", f"{temp} °C")
        with col3: st.metric("ESTADO EPP", "PROTEGIDO" if puesto else "PELIGRO")

        # --- LÓGICA DE INTERVENCIÓN (Ahora sí es segura) ---
        if temp > 35:
            st.error(f"🚨 ALERTA TÉRMICA: {temp}°C excede el límite de seguridad.")
        
        if not puesto:
            st.warning("⚠️ PROTOCOLO VIOLADO: Operario sin casco detectado.")

        st.divider()

        # --- BOTÓN DE CONSULTA IA ---
        if st.button("🔍 EJECUTAR ANÁLISIS PREDICTIVO"):
            with st.spinner("IA procesando 70k nodos..."):
                prompt = f"Analiza: Temp {temp}C, Luz {luz}lx, EPP: {puesto}. Dame un dictamen HSE corto."
                res = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "Eres AIHumanity-Master."},
                              {"role": "user", "content": prompt}]
                )
                st.info(res.choices[0].message.content)
    else:
        st.info("📡 Buscando señal del hardware ESP32...")

except Exception as e:
    st.error(f"Falla en la red de sensores: {e}")

# --- 4. CICLO DE ACTUALIZACIÓN ---
time.sleep(10)
st.rerun()
