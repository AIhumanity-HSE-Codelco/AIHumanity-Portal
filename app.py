import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN CORE Y SESIÓN ---
st.set_page_config(page_title="AIH MASTER | V23.0 MATRIX", layout="wide", initial_sidebar_state="expanded")

def apply_industrial_dark_style():
    st.markdown("""
        <style>
        .stApp { background-color: #0A0A0A; color: #E5E5E5; font-family: 'SF Pro Display', sans-serif; }
        [data-testid="stSidebar"] { background-color: #151515 !important; border-right: 1px solid #333; }
        .stMetric { background-color: #1A1A1A; border: 1px solid #333; padding: 15px; border-radius: 10px; }
        .category-box { padding: 10px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #0071E3; background: #1A1A1A; }
        /* Mejora de legibilidad en inputs */
        input, select, .stSelectbox { background-color: #222 !important; color: white !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. MAPA ESTRUCTURAL DE LOS 25 MÓDULOS ---
ESTRUCTURA_BÓVEDA = {
    "💎 ESTRATÉGICO": ["01 EL CEREBRO (IRC)", "13 REPORTES BI", "19 AUDITORÍA", "25 MESH STATUS"],
    "💨 AMBIENTAL": ["02 GASES (M06)", "06 ADMS/POLVO", "07 SISMO", "11 ACÚSTICA", "21 VENTILACIÓN 3D"],
    "🧬 HUMANO": ["03 BIOMETRÍA", "10 BEHAVIOR", "14 OCULOMETRÍA", "15 CARGA COGNITIVA", "16 ESTRÉS TÉRMICO"],
    "⚙️ OPERATIVO": ["04 ENERGÍA", "05 GIS/TALUDES", "08 ACTIVOS", "12 MANTENIMIENTO", "22 COLISIÓN H-M", "23 STOCKPILES", "24 CALIDAD ENERGÍA"],
    "🚨 CRÍTICO": ["09 EMERGENCIAS", "17 INCIDENTES", "18 CAUSA RAÍZ", "20 NOTIFICACIONES"]
}

# --- 3. FUNCIONES DE RENDERIZADO (EJEMPLOS DE CAPA 17-25) ---

def render_m17_incidentes():
    st.markdown("## 📝 M17: Registro Flash de Incidentes")
    c1, c2 = st.columns([1, 1])
    with c1:
        st.write("### Captura de Evento")
        tipo = st.selectbox("Clasificación", ["Cuasi-accidente", "Acto Inseguro", "Falla Mecánica"])
        obs = st.text_area("Descripción del hallazgo")
        if st.button("🚨 SELLAR INCIDENTE"):
            st.success("Registrado en Bóveda con ID: " + datetime.now().strftime("%Y%m%d%H%M"))
    with c2:
        st.write("### Historial de Turno")
        st.dataframe(pd.DataFrame({"Hora": ["14:20", "15:45"], "Evento": ["Derrame Aceite", "Ingreso zona restringida"]}))

def render_m21_ventilacion():
    st.markdown("## 🌪️ M21: Gemelo Digital de Ventilación (VOD)")
    
    col_v1, col_v2 = st.columns(2)
    col_v1.metric("Flujo de Aire Total", "450k cfm", "+5k")
    col_v2.metric("Eficiencia Ventiladores", "88%", "Estable")
    st.warning("⚠️ Simulación: Si falla el Ventilador Sur, el nivel 4 quedará sin O2 en 12 minutos.")

def render_m14_oculometria():
    st.markdown("## 👁️ M14: Oculometría y Vigilancia")
    
    st.metric("Índice de Parpadeo", "12/min", "Riesgo de Microsueño: BAJO")
    st.info("Algoritmo TensorFlow analizando puntos faciales en tiempo real.")

# --- 4. MOTOR DE NAVEGACIÓN CATEGORIZADA ---
def main():
    apply_industrial_dark_style()
    
    with st.sidebar:
        st.markdown("<h2 style='color:#0071E3;'>AIH MASTER V23</h2>", unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=60)
        
        st.markdown("---")
        # PASO 1: Seleccionar Dominio
        dominio = st.selectbox("DOMINIO DE RIESGO:", list(ESTRUCTURA_BÓVEDA.keys()))
        
        # PASO 2: Seleccionar Módulo dentro del Dominio
        modulo = st.radio("MÓDULOS EN " + dominio + ":", ESTRUCTURA_BÓVEDA[dominio])
        
        st.divider()
        st.caption(f"MODO: GOBERNANZA ACTIVA | {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # --- ROUTER DE RENDERIZADO ---
    if "01" in modulo:
        st.markdown("## 💎 01: EL CEREBRO (IRC)")
        
        st.metric("IRC GLOBAL", "42.1%", "+1.5%")
    elif "17" in modulo: render_m17_incidentes()
    elif "21" in modulo: render_m21_ventilacion()
    elif "14" in modulo: render_m14_oculometria()
    else:
        st.markdown(f"## {modulo}")
        st.info(f"Visualización de datos en tiempo real para {modulo}. Protocolos TRL-4 activos.")
        st.metric("Estado del Nodo", "Sincronizado", "99.8% Uptime")

if __name__ == "__main__":
    main()
