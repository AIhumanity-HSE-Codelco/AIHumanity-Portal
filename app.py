import streamlit as st
import os
from dotenv import load_dotenv

# --- CONFIGURACIÓN DE INTERFAZ (DEBE IR PRIMERO) ---
st.set_page_config(page_title="AIHumanity Master", layout="wide")

st.markdown("""
    <style>
    reportview-container { background: #000000; }
    .stApp { background-color: #000000; color: #FFFFFF; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ AIHumanity | Status Check")

# --- PROTOCOLO DE RASTREO DE LLAVES ---
# Probamos las 3 rutas posibles en Windows (Local, OneDrive y Raíz)
rutas_posibles = [
    os.path.join(os.path.expanduser("~"), "Desktop", "API'S", ".env"),
    os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", "API'S", ".env"),
    "C:/Users/easer/Desktop/API'S/.env"
]

llave_encontrada = False

for ruta in rutas_posibles:
    if os.path.exists(ruta):
        load_dotenv(ruta)
        st.success(f"✅ Bóveda detectada en: {ruta}")
        llave_encontrada = True
        break

if not llave_encontrada:
    st.warning("⚠️ Carpeta API'S no detectada en las rutas estándar.")
    st.info("Buscando archivos en el directorio actual...")
    st.code(f"Directorios en Escritorio: {os.listdir(os.path.join(os.path.expanduser('~'), 'Desktop'))}")

# --- INTENTO DE CARGA DE OPENAI ---
try:
    from openai import OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = OpenAI(api_key=api_key)
        st.write("🧠 **Cerebro IA:** Sincronizado y listo.")
    else:
        st.error("❌ La carpeta existe pero el archivo .env no tiene la variable OPENAI_API_KEY")
except Exception as e:
    st.error(f"❌ Error de Software: {e}")

st.divider()
st.button("RE-ESCANEAR SISTEMA")
