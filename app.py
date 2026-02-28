import streamlit as st
import requests
import time

st.set_page_config(page_title="AIHumanity Master Console", layout="wide")

# CSS Estructurado: Cupertino Dark Industrial
st.markdown("""
    <style>
    .main { background-color: #050505; }
    [data-testid="stMetricValue"] { color: #BF5AF2; font-family: 'SF Pro Display', sans-serif; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #BF5AF2 , #FF2D55); }
    .status-box { padding: 20px; border-radius: 15px; border: 1px solid #1f1f1f; background: #0f0f0f; }
    </style>
    """, unsafe_allow_html=True)

URL = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

# --- SIDEBAR DE GOBERNANZA ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/chip.png", width=80)
    st.title("Gobernanza AIH")
    st.info("Nodo: AIDeepMiner-01\nTRL: 3 (Prototipo)")
    if st.button("🔄 RE-SINCRONIZAR CANAL", use_container_width=True):
        st.rerun()
    st.divider()
    st.caption("Protocolo HSE Activo")

# --- PANEL PRINCIPAL ---
st.markdown("<h2 style='color: white;'>Consola de Monitoreo Predictivo</h2>", unsafe_allow_html=True)

try:
    r = requests.get(URL, timeout=3)
    data = r.json()
    
    if data:
        # Layout de Ingeniería (3 Columnas Simétricas)
        m1, m2, m3 = st.columns(3)
        
        with m1:
            st.metric("LUMINOSIDAD (D32)", f"{data.get('luz', 0)} lx")
            st.progress(min(data.get('luz', 0)/4095, 1.0))
            
        with m2:
            st.metric("TÉRMICO (D26)", f"{data.get('temp', 0)} °C")
            st.markdown("<div style='height:4px; background:#BF5AF2;'></div>", unsafe_allow_html=True)
            
        with m3:
            st.write("**INTEGRIDAD EPP**")
            if data.get('puesto'):
                st.success("CASCO PUESTO")
            else:
                st.error("ALERTA: CASCO AUSENTE")

        # --- SECCIÓN DE TENDENCIAS (Estructura HSE) ---
        st.divider()
        st.subheader("Análisis de Riesgo en Tiempo Real")
        col_chart, col_log = st.columns([2, 1])
        
        with col_chart:
            # Simulamos un radar de riesgo basado en los datos
            st.info(f"Nivel de riesgo actual: {'BAJO' if data.get('puesto') else 'CRÍTICO'}")
            
        with col_log:
            st.markdown("<div class='status-box'><b>LOG DE EVENTOS:</b><br><small>10:55 - Nodo Sincronizado<br>10:56 - Lectura Estable</small></div>", unsafe_allow_html=True)
            
    else:
        st.warning("⚠️ Sin flujo de datos. Verifique alimentación del ESP32.")

except:
    st.error("Error de comunicación con el puente Firebase.")

time.sleep(2)
st.rerun()
