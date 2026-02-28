import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# --- PROTOCOLO DE LOCALIZACIÓN DE LLAVES ---
# Definimos la ruta a tu carpeta en el escritorio
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "API'S", ".env")

# Cargamos las llaves desde esa ruta específica
if os.path.exists(desktop_path):
    load_dotenv(desktop_path)
    api_key = os.getenv("OPENAI_API_KEY")
    st.success("🔒 Llaves de Seguridad Cargadas desde el Escritorio")
else:
    # Si falla la ruta local, intenta leer de los Secrets de Streamlit (Para la Nube)
    api_key = st.secrets.get("OPENAI_API_KEY")
    if not api_key:
        st.error("🚨 ERROR: No se encontró el archivo .env en Desktop/API'S")

# Inicializamos el cliente si hay llave
if api_key:
    client = OpenAI(api_key=api_key)
