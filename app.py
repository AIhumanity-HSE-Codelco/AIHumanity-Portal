import streamlit as st
import requests
import time

# Configuración de página con estética Apple
st.set_page_config(page_title="AIHumanity | Luxe Control", layout="wide")

# --- CUSTOM CSS: ESTILO CUPERTINO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'SF Pro Display', sans-serif;
        background-color: #000000;
        color: #FFFFFF;
    }

    /* Tarjetas con efecto Glassmorphism */
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
    }
    .stMetric:hover {
        transform: translateY(-5px);
        border: 1px solid #BF5AF2; /* Morado Apple */
    }

    /* Botón Interactivo Morado/Rosa */
    .stButton>button {
        background: linear-gradient(135deg, #BF5AF2 0%, #FF2D55 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 25px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 20px rgba(191, 90, 242, 0.6);
        transform: scale(1.02);
    }

    /* Barras de progreso Rosadas */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #BF5AF2 , #FF2D55);
    }
    </style>
    """, unsafe_allow_html=True)

# URL de Conexión
URL_NODO = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

# --- HEADER FINO ---
st.markdown("<h1 style='text-align: center; color: #FFFFFF; font-weight: 200;'>AIHumanity <span style='color: #BF5AF2; font-weight: 600;'>Master</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8E8E93;'>Arquitectura de Riesgo Proactivo | Nodo AID-01</p>", unsafe_allow_html=True)

st.divider()

try:
    res = requests.get(URL_NODO, timeout=3)
    data = res.json()
    
    if data:
        luz = data.get('luz', 0)
        temp = data.get('temp', 0)
        puesto = data.get('puesto', False)

        # --- LAYOUT DE TRES COLUMNAS ---
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("LUMINOSIDAD", f"{luz} lx")
            st.progress(min(luz/4095, 1.0))
            st.caption("Sensor Óptico D32")

        with col2:
            st.metric("TEMPERATURA", f"{temp} °C")
            st.markdown(f"<div style='height: 4px; background: #32D74B; border-radius: 2px;'></div>", unsafe_allow_html=True)
            st.caption("Módulo Térmico D26")

        with col3:
            st.write("**ESTADO EPP**")
            if puesto:
                st.markdown("<div style='padding:15px; border-radius:15px; background:rgba(50, 215, 75, 0.1); border: 1px solid #32D74B; color:#32D74B; text-align:center; font-weight:600;'>CASCO DETECTADO</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div style='padding:15px; border-radius:15px; background:rgba(255, 45, 85, 0.1); border: 1px solid #FF2D55; color:#FF2D55; text-align:center; font-weight:600;'>ALERTA: SIN CASCO</div>", unsafe_allow_html=True)

        # --- BOTONERA INTERACTIVA ---
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 ACTUALIZAR SISTEMA"):
            st.toast("Sincronizando con el nodo...", icon="✨")
            time.sleep(1)
            st.rerun()

    else:
        st.info("Esperando el latido del sensor...")

except Exception as e:
    st.error("Error de enlace con el servidor.")

# Auto-refresh cada 5 segundos
time.sleep(5)
st.rerun()
