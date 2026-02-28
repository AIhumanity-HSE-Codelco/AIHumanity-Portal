import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

st.set_page_config(page_title="AIHumanity Master", layout="wide")

# --- ESTILO NEGRO PURO ---
st.markdown("<style>.stApp {background-color: #000000; color: #FFFFFF;}</style>", unsafe_allow_html=True)
st.title("🛡️ AIHumanity | Status Check")

# --- PROTOCOLO DE CONEXIÓN HÍBRIDO ---
api_key = None

# Intento 1: Buscar en el Escritorio Local (Solo funciona en tu PC)
ruta_local = os.path.join(os.path.expanduser("~"), "Desktop", "API'S", ".env")
if os.path.exists(ruta_local):
    load_dotenv(ruta_local)
    api_key = os.getenv("OPENAI_API_KEY")
    st.success("✅ Bóveda Local detectada en Escritorio.")

# Intento 2: Si falla el local, buscar en los Secrets de la Nube (Streamlit Cloud)
if not api_key:
    api_key = st.secrets.get("OPENAI_API_KEY")
    if api_key:
        st.info("☁️ Conectado mediante Secrets de la Nube.")

# --- INVOCACIÓN DEL MOTOR IA ---
if api_key:
    try:
        client = OpenAI(api_key=api_key)
        st.write("🧠 **Cerebro IA:** Sincronizado y operativo.")
        
        # Prueba de vida de la IA
        if st.button("PROBAR RESPUESTA IA"):
            res = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": "Status reporte AIH"}]
            )
            st.success(res.choices[0].message.content)
            
    except Exception as e:
        st.error(f"❌ Error de autenticación: {e}")
else:
    st.error("🚨 CRÍTICO: No se detectó ninguna API KEY.")
    st.warning("Si estás en la nube, ve a 'Manage App' > 'Settings' > 'Secrets' y pega: OPENAI_API_KEY='tu_llave'")
