import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AIHumanity HSE", page_icon="🛡️", layout="wide")

# --- MÓDULO 1: IDENTIDAD ---
st.title("🛡️ AIHumanity - HSE Master Control")
st.markdown("### **Organization:** Codelco | **Version:** v2.0.4-TRL3")
st.write("**Integrator:** AIH-Master | **Status:** 🟢 ONLINE")
st.divider()

# --- MÓDULO 2: TELEMETRÍA ELEGANTE ---
st.subheader("📊 Telemetría de Riesgo (AIDeepMiner)")

col1, col2, col3 = st.columns(3)
col1.metric(label="💨 Polvo PM10", value="32 mg/m³", delta="-2.1%")
col2.metric(label="⚠️ Gases CO/NO2", value="12 ppm", delta="Normal")
col3.metric(label="💓 Biometría", value="78 BPM", delta="+2 BPM")

# Aplicar diseño Pro a las tarjetas
style_metric_cards(background_color="#1d2129", border_left_color="#00ff00", border_size_px=1)

# --- MÓDULO 3: GRÁFICO DE ALTA GAMA ---
st.markdown("---")
st.subheader("📈 Tendencia Predictiva de Exposición")

# Crear datos simulados para el gráfico
df_sim = pd.DataFrame({
    'Tiempo': pd.date_range(start='2026-02-28', periods=24, freq='H'),
    'Nivel de Riesgo': np.random.uniform(10, 45, 24)
})

# Crear gráfico interactivo con Plotly
fig = px.area(df_sim, x='Tiempo', y='Nivel de Riesgo', 
              title="Análisis Proactivo de Seguridad (ICR)",
              color_discrete_sequence=['#00cc96'])
fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')

st.plotly_chart(fig, use_container_width=True)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("By Uniting Technology | Belgium")
