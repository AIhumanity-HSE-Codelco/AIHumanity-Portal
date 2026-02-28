import streamlit as st
import requests
import time

# Configuración de Identidad AIH Master
st.set_page_config(page_title="AIHumanity HSE Portal", layout="wide", initial_sidebar_state="collapsed")

# Estilos CSS para simular entorno minero (Dark Mode Industrial)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #374151; }
    </style>
    """, unsafe_allow_html=True)

# URL de la Nube (La misma que el ESP32)
URL_NODO = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

# --- CABECERA ---
col_logo, col_tit = st.columns([1, 4])
with col_tit:
    st.title("🛰️ AIHumanity: Control de Riesgo Proactivo")
    st.write("Monitor de Nodo AIDeepMiner | Estatus: **TRL3 - Activo**")

st.divider()

# --- LÓGICA DE DATOS ---
try:
    response = requests.get(URL_NODO, timeout=3)
    data = response.json()
    
    if data:
        # Extraer variables del JSON del ESP32
        luz_val = data.get('luz', 0)
        temp_val = data.get('temp', 0)
        casco_puesto = data.get('puesto', False)

        # --- FILA 1: MÉTRICAS Y BARRAS ---
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("INTENSIDAD DE LUZ", f"{luz_val} lx")
            # Barra de estatus de visibilidad (Normalizando de 0 a 4095 del ESP32)
            progreso_luz = min(luz_val / 4095, 1.0)
            st.progress(progreso_luz, text="Nivel de Iluminación en Galería")
            
        with col2:
            st.metric("TEMPERATURA AMBIENTE", f"{temp_val} °C")
            # Alerta visual si sube de 35 grados
            if temp_val > 35:
                st.warning("⚠️ ESTRÉS TÉRMICO DETECTADO")
            else:
                st.info("🌡️ Temperatura dentro de rango")

        with col3:
            st.write("**ESTATUS DE EPP (CASCO):**")
            if casco_puesto:
                st.success("✅ CASCO DETECTADO (PUESTO)")
            else:
                st.error("🚨 ALERTA: CASCO NO DETECTADO")
                st.toast("¡PELIGRO: Operario sin protección!")

        # --- FILA 2: ACCIONES DE GOBERNANZA ---
        st.divider()
        c_sync, c_info = st.columns([1, 3])
        
        with c_sync:
            if st.button("🔄 FORZAR SINCRONIZACIÓN", use_container_width=True):
                st.toast("Sincronizando con AIDeepMiner...")
                time.sleep(1)
                st.rerun()
        
        with c_info:
            st.caption(f"Último latido recibido del nodo: {time.strftime('%H:%M:%S')}")

    else:
        st.warning("📡 Nodo en espera de transmisión... Verifique luz azul en ESP32.")

except Exception as e:
    st.error(f"Error de Enlace: {e}")

# Auto-refresco cada 5 segundos para mantener el alineamiento
time.sleep(5)
st.rerun()
