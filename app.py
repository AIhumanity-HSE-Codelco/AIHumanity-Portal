import streamlit as st
from openai import OpenAI
import requests
import time
import os

# 1. Configuración de Seguridad (Carga la llave de forma invisible)
# En local busca en el sistema, en Streamlit Cloud busca en 'Secrets'
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# --- FUNCIÓN DE ANÁLISIS PREDICTIVO ---
def analizar_riesgo_ia(luz, temp, puesto):
    try:
        prompt = f"""Analiza como Ingeniero HSE de Mina: 
        Luminosidad: {luz}lx, Temperatura: {temp}C, Casco detectado: {puesto}.
        Genera un dictamen técnico de 2 líneas sobre el riesgo operativo actual."""
        
        response = client.chat.completions.create(
            model="gpt-4o", # O el modelo que prefiera
            messages=[{"role": "system", "content": "Eres AIHumanity-Master."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Esperando conexión con el cerebro IA..."

# --- INTERFAZ MORADA / NEGRO (CUPERTINO) ---
st.markdown("<h1 style='color:#BF5AF2; font-weight:100;'>AIHumanity <span style='font-weight:600;'>Intelligence</span></h1>", unsafe_allow_html=True)

# Supongamos que ya recibimos 'data' del ESP32 como en los pasos anteriores
# Aquí insertamos el cuadro de análisis IA debajo de las métricas
st.divider()
st.subheader("🧠 Dictamen de IA Proactiva")

if st.button("EJECUTAR ESCANEO DE 70K NODOS"):
    with st.spinner("Procesando tendencias de riesgo..."):
        # Usamos datos reales del ESP32 si están disponibles
        resultado = analizar_riesgo_ia(1200, 24, True) # Valores de prueba
        st.markdown(f"""
            <div style='background:rgba(191,90,242,0.05); border:1px solid #BF5AF2; padding:20px; border-radius:15px;'>
                <p style='color:#BF5AF2; font-size:0.8rem; margin:0;'>REPORTE DE INGENIERÍA:</p>
                <p style='font-style:italic;'>"{resultado}"</p>
            </div>
        """, unsafe_allow_html=True)
