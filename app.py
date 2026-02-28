import streamlit as st
import requests
import time

# Configuración Estructural
st.set_page_config(page_title="AIH Master Console", layout="wide", initial_sidebar_state="collapsed")

# --- PALETA DE COLORES CUPERTINO PREMIUM ---
# Fondo: #000000 | Acento 1: #BF5AF2 (Morado) | Acento 2: #FF375F (Rosa)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@100;300;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'SF Pro Display', -apple-system, sans-serif;
        background-color: #000000;
        color: #FFFFFF;
    }

    /* Contenedores Glassmorphism */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 22px;
        padding: 25px;
        backdrop-filter: blur(20px);
    }

    /* Texto de métricas en Blanco Puro */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 2.5rem !important;
    }

    /* Botones con gradiente refinado Morado-Rosa */
    .stButton>button {
        background: linear-gradient(135deg, #BF5AF2 0%, #FF375F 100%);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 12px 30px;
        font-weight: 300;
        letter-spacing: 1px;
        transition: all 0.4s ease;
    }
    
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(191, 86, 242, 0.4);
        transform: translateY(-2px);
    }

    /* Barras de progreso ultra-delgadas */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #BF5AF2, #FF375F);
        height: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Conexión
URL = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

# --- HEADER MINIMALISTA ---
st.markdown("<p style='text-align:center; color:#BF5AF2; letter-spacing:4px; font-weight:100; margin-bottom:0;'>AIHUMANITY</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; font-weight:100; margin-top:0;'>DataStream <span style='font-weight:600;'>Master</span></h1>", unsafe_allow_html=True)

st.divider()

try:
    r = requests.get(URL, timeout=2)
    data = r.json()
    
    if data:
        # Layout Simétrico
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.metric("LUZ (D32)", f"{data.get('luz', 0)} lx")
            st.progress(min(data.get('luz', 0)/4095, 1.0))
            
        with c2:
            st.metric("TEMP (D26)", f"{data.get('temp', 0)} °C")
            st.markdown("<div style='height:4px; width:100%; background:rgba(255,255,255,0.1); border-radius:2px;'></div>", unsafe_allow_html=True)
            
        with c3:
            puesto = data.get('puesto', False)
            color_status = "#BF5AF2" if puesto else "#FF375F"
            st.markdown(f"""
                <div style='border: 1px solid {color_status}; border-radius:18px; padding:20px; text-align:center; background:rgba(255,255,255,0.01);'>
                    <p style='color:{color_status}; margin:0; font-size:0.8rem;'>STATUS EPP</p>
                    <h3 style='margin:0; color:{color_status};'>{'PROTECCIÓN OK' if puesto else 'ALERTA CRÍTICA'}</h3>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Botón Centralizado
        _, col_btn, _ = st.columns([1,1,1])
        with col_btn:
            if st.button("SINCRONIZAR NODO"):
                st.rerun()

    else:
        st.markdown("<p style='text-align:center; color:#8E8E93;'>Esperando latido del hardware...</p>", unsafe_allow_html=True)

except:
    st.error("Enlace interrumpido.")

# Refresh discreto
time.sleep(4)
st.rerun()
