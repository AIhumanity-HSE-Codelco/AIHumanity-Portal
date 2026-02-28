import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURACIÓN DE INTERFAZ ---
st.set_page_config(
    page_title="AIHumanity - HSE Master Control",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILO PERSONALIZADO (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0d1117; color: #8b949e; text-align: center; padding: 5px; font-size: 12px; border-top: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- MÓDULO 1: IDENTIDAD CORPORATIVA ---
with st.container():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("🛡️ AIHumanity - HSE Master Control")
        st.write("### **Organization:** Codelco")
    with col2:
        st.markdown(f"**Version:** `v2.0.4-TRL3`  \n**Integrator:** `AIH-Master`  \n**Status:** 🟢 ONLINE")

st.divider()

# --- ESPACIO PARA SIGUIENTES MÓDULOS ---
st.info("SISTEMA CONFIGURADO: Esperando carga de Módulo 2 (Telemetría y Nodos)")

# --- PIE DE PÁGINA ---
st.markdown('<div class="footer">By Uniting Technology | Belgium</div>', unsafe_allow_html=True)
