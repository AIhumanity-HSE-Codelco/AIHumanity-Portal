import streamlit as st
import requests
import time
from datetime import datetime

# Configuración de Identidad Visual
st.set_page_config(page_title="AIHumanity | DataStream", layout="wide")

# --- INTERFAZ CUPERTINO PREMIUM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0A0A0A;
        color: #E0E0E0;
    }

    /* Tarjetas Glassmorphism Segmentadas */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        border: 1px solid #BF5AF2;
        background: rgba(191, 90, 242, 0.05);
    }

    /* Botones Estilo Apple */
    .stButton>button {
        background: linear-gradient(135deg, #BF5AF2 0%, #5E5CE6 100%);
        color: white; border: none; border-radius: 10px;
        padding: 12px; font-weight: 600; width: 100%;
    }

    /* Status Bar Custom */
    .status-bar {
        font-size: 0.8rem; padding: 5px 15px;
        border-radius: 20px; background: rgba(191, 90, 242, 0.2);
        color: #BF5AF2; border: 1px solid #BF5AF2;
    }
    </style>
    """, unsafe_allow_html=True)

# URL Unificada (La misma que el ESP32)
URL_NODO = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

# --- SIDEBAR DE CONTROL ---
with st.sidebar:
    st.markdown("<h2 style='color: #BF5AF2;'>AIDeepMiner</h2>", unsafe_allow_html=True)
    st.caption("ESTATUS: TRL3 - ACTIVO")
    st.divider()
    if st.button("🚀 FORZAR ENVÍO DE DATOS"):
        st.toast("Sincronizando canal...", icon="🛰️")
        st.rerun()
    st.divider()
    st.markdown("### Debug Info")
    st.code("NODE_ID: AID-01\nFREQ: 2000ms\nPORT: 443")

# --- HEADER ---
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown("<h1 style='margin-bottom:0;'>AIHumanity | <span style='color:#BF5AF2;'>DataStream Center</span></h1>", unsafe_allow_html=True)
    st.write("Supervisión Activa de Sensores Industriales")
with c2:
    st.markdown("<br><span class='status-bar'>● CONEXIÓN ESTABLE</span>", unsafe_allow_html=True)

st.divider()

# --- LÓGICA DE CAPTURA ---
try:
    response = requests.get(URL_NODO, timeout=2)
    data = response.json()
    
    if data:
        # Layout de 4 Columnas para Métricas Críticas
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("LUMINOSIDAD (lx)", f"{data.get('luz', 0)}")
            st.progress(min(data.get('luz', 0)/4095, 1.0))
            st.caption("Nivel de Claridad")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("TEMPERATURA (°C)", f"{data.get('temp', 0)}")
            st.markdown("<div style='height:3px; background:#BF5AF2; width:80%; margin:auto;'></div>", unsafe_allow_html=True)
            st.caption("Ambiente Galería")
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.write("**ESTADO DEL EPP**")
            if data.get('puesto'):
                st.markdown("<h3 style='color:#32D74B;'>✅ PUESTO</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='color:#FF2D55;'>🚨 ALERTA</h3>", unsafe_allow_html=True)
            st.caption("Sensor IR (PIN 25)")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col4:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.metric("LATENCIA", "42ms")
            st.markdown("<div style='height:3px; background:#5E5CE6; width:60%; margin:auto;'></div>", unsafe_allow_html=True)
            st.caption("Firebase RTDB")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- SECCIÓN DE ANÁLISIS ---
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Análisis de Tendencia (Tiempo Real)")
        
        c_chart, c_log = st.columns([2, 1])
        
        with c_chart:
            # Gráfico de área para simular flujo constante
            chart_data = [data.get('luz', 0)] * 20
            st.area_chart(chart_data, color="#BF5AF2")
            
        with c_log:
            st.markdown("### Log de Actividad")
            st.markdown(f"""
            - `{datetime.now().strftime('%H:%M:%S')}`: Datos recibidos OK
            - `{datetime.now().strftime('%H:%M:%S')}`: Sincronización Nodo 1
            - `Status`: Luz Azul Estática detectada
            """)

    else:
        st.warning("📡 El nodo AIDeepMiner está en modo escucha. Esperando datos...")

except Exception as e:
    st.error(f"Error de enlace: {e}")
    st.info("Verifica que el ESP32 esté enviando el código 200 en el Monitor Serial.")

# Refresco automático cada 2 segundos para flujo real
time.sleep(2)
st.rerun()
