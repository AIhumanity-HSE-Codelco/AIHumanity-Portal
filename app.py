import streamlit as st
import time

# Forzado de configuración para romper caché
st.set_page_config(page_title="AIH v2.0", layout="wide")

# DISEÑO CORPORATIVO AIHUMANITY (Fondo Blanco, Letras Negras, Acentos Rojos)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    h1 { color: #1A1A1A !important; border-bottom: 4px solid #FF4B4B; }
    .card { background-color: #F0F2F6; padding: 20px; border-radius: 10px; border: 1px solid #D1D5DB; color: #1A1A1A; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🛡️ AIHUMANITY: MISSION CONTROL v2.0</h1>", unsafe_allow_html=True)
st.write("### LOG: SYSTEM UPDATED - TRL3 STATUS")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><b>AIDeepMiner Node</b><br>Status: ONLINE<br>Mode: Simulation</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><b>ADMS Module</b><br>Dust Level: 14.5 mg/m³<br>Action: STABLE</div>', unsafe_allow_html=True)

# Auto-refresco para mantener el túnel vivo
time.sleep(2)
st.rerun()