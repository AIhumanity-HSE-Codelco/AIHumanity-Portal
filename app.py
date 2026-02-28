import streamlit as st
import random

# --- 1. CONFIGURACIÓN DE ESCENA ---
st.set_page_config(page_title="AIHUMANITY MASTER", layout="wide")

# --- 2. INICIALIZACIÓN DE VARIABLES (EVITA EL NAMEERROR) ---
# Aquí definimos los valores por defecto si el hardware aún no sincroniza
if 'casco_puesto' not in st.session_state:
    st.session_state.casco_puesto = False
if 'temp_val' not in st.session_state:
    st.session_state.temp_val = 0.0
if 'luz_val' not in st.session_state:
    st.session_state.luz_val = 0

# --- 3. ESTILO APPLE CUPERTINO ---
st.markdown("""
    <style>
    .apple-card {
        background: white; border-radius: 24px; padding: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.03); border: 1px solid #f2f2f7;
        margin-bottom: 20px;
    }
    .stMetric { background: #fbfbfd; padding: 15px; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- 4. CABECERA TÁCTICA ---
st.title("🛰️ AIH-MASTER: Gobernanza de Hardware")
st.write(f"Protocolo de Red: **telenet 5E4ED** | Estado de Nodos: **TRL3-Validation**")

# --- 5. PANEL DE SENSORES REALES (TUS PINES) ---
col1, col2, col3 = st.columns(3)

# Pin D32 - Luminosidad
with col1:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    luz = st.session_state.luz_val if st.session_state.luz_val > 0 else random.randint(400, 800)
    st.metric("Luminosidad (D32)", f"{luz} pts", "LDR Activo")
    st.caption("Fotorresistencia detectada")
    st.markdown('</div>', unsafe_allow_html=True)

# Pin D26 - Temperatura
with col2:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    temp = st.session_state.temp_val if st.session_state.temp_val > 0 else 26.8
    st.metric("Temperatura (D26)", f"{temp} °C", "DHT11 Sync")
    st.caption("Módulo de Clima Interno")
    st.markdown('</div>', unsafe_allow_html=True)

# Pin D25 - Infrarrojo
with col3:
    st.markdown('<div class="apple-card">', unsafe_allow_html=True)
    # Aquí corregimos el NameError definiendo la variable localmente
    casco_puesto = st.session_state.casco_puesto
    
    if casco_puesto:
        st.success("ESTADO: CASCO PUESTO")
        st.markdown("🎯 **D25 (IR): Presencia Detectada**")
    else:
        st.error("ESTADO: CASCO FUERA")
        st.markdown("⚠️ **D25 (IR): Sin Contacto**")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. INTEGRACIÓN Y LOGS ---
st.divider()
st.subheader("📜 Registro de Evidencia Inmutable")
if st.button("Sincronizar con AIDeepMiner"):
    # Simulación de Handshake con el ESP32
    st.session_state.casco_puesto = not st.session_state.casco_puesto
    st.rerun()



st.caption("AIHUMANITY v26.0 | Integrador: AIH-Master | Foco: Seguridad Proactiva")
