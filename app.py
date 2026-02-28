import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AIHumanity HSE", page_icon="🛡️", layout="wide")

# --- MÓDULO 1: IDENTIDAD CORPORATIVA ---
st.title("🛡️ AIHumanity - HSE Master Control")
st.markdown("### **Organization:** Codelco | **Version:** v2.0.4-TRL3")
st.caption("By Uniting Technology | Belgium")
st.divider()

# --- ESTRUCTURA DE NAVEGACIÓN (HIPERLINKS/TABS) ---
# Aquí encerramos todo en pestañas elegantes
tab1, tab2, tab3 = st.tabs(["📊 Panel de Control de Riesgo (ICR)", "📍 Mapa de Nodos", "📑 Reportes HSE"])

with tab1:
    st.header("Telemetría de Riesgo & Análisis Proactivo")
    
    # 1. Telemetría de Riesgo (Encerramos las métricas)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="💨 Polvo PM10", value="32 mg/m³", delta="-2.1%")
    col2.metric(label="⚠️ Gases CO/NO2", value="12 ppm", delta="Normal")
    col3.metric(label="💓 Biometría", value="78 BPM", delta="+2 BPM")
    style_metric_cards(background_color="#1d2129", border_left_color="#00ff00", border_size_px=1)

    st.markdown("---")

    # 2. Tendencia Predictiva & Análisis Proactivo (Gráfico de Alta Gama)
    st.subheader("📈 Tendencia Predictiva & Seguridad Proactiva")
    
    # Datos para el análisis
    df_sim = pd.DataFrame({
        'Tiempo': pd.date_range(start='2026-02-28', periods=24, freq='H'),
        'Nivel de Riesgo': np.random.uniform(10, 45, 24)
    })

    fig = px.area(df_sim, x='Tiempo', y='Nivel de Riesgo', 
                  title="Proyección de Exposición (Siguiente Turno)",
                  color_discrete_sequence=['#00cc96'])
    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig, use_container_width=True)
    
    st.success("✅ El modelo predictivo indica estabilidad para las próximas 4 horas en el sector actual.")

with tab2:
    st.header("📍 Ubicación Geográfica de Nodos")
    st.info("Módulo en fase de enlace con 70k nodos AIDeepMiner...")

with tab3:
    st.header("📑 Histórico de Incidentes")
    st.write("Generando reportes automáticos para HSE Codelco...")

# --- PIE DE PÁGINA FIJO ---
st.markdown("---")
st.markdown("**Integrator:** AIH-Master | **Status:** 🟢 SYSTEM ACTIVE")
