import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime

# --- 1. CONFIGURACIÓN DE ENTORNO MAXIMIZADO ---
st.set_page_config(page_title="AIH-MASTER MAXIMIZED CORE", layout="wide", initial_sidebar_state="expanded")

# --- 2. BASE DE DATOS MAESTRA (70K NODOS & METAS HSE) ---
METAS_HSE = {"Polvo": 45, "Viento": 50, "Fatiga": 15, "Sismo": 4.0}
LISTA_MINERAS = ["Chuquicamata", "El Teniente", "Escondida", "Collahuasi", "Los Bronces", "Andina", "Salvador"]

# --- 3. ESTILO CSS PARA ALTA PRECISIÓN (MODO CONTRASTE) ---
st.markdown("""
    <style>
    .stApp { background-color: #f1f3f6; }
    .status-bar-container { width: 100%; background-color: #e0e0e0; border-radius: 25px; margin: 10px 0; }
    .status-bar-fill { height: 25px; border-radius: 25px; text-align: center; color: white; font-weight: bold; }
    .metric-card { background: white; padding: 15px; border-radius: 10px; border: 1px solid #d1d8e0; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. FUNCIONES DE CÁLCULO DE GOBERNANZA ---
def render_risk_bar(valor):
    """Renderiza la barra de porcentaje interactiva con colores de alerta."""
    color = "#2ecc71" if valor < 40 else "#f1c40f" if valor < 75 else "#e74c3c"
    st.markdown(f"""
        <div style="margin-bottom: 5px;"><strong>Potencial de Desviación Riesgo Cero: {valor}%</strong></div>
        <div class="status-bar-container">
            <div class="status-bar-fill" style="width: {valor}%; background-color: {color}; shadow: 0 2px 4px rgba(0,0,0,0.2);">
                {valor}%
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 5. PANEL DE CONTROL LATERAL ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ AIH-GATEWAY")
    modo_vista = st.radio("VISTA:", ["MASTER GLOBAL (Maximizado)", "ANÁLISIS POR FAENA"])
    st.divider()
    st.info("Objetivo: RIESGO CERO 2026\nEstatus: Monitoreo Activo")

# --- 6. VISTA MAXIMIZADA (SÍNTESIS GLOBAL) ---
if modo_vista == "MASTER GLOBAL (Maximizado)":
    st.title("🌐 PANEL ESTRATÉGICO: GOBERNANZA RIESGO CERO")
    
    # Simulación de datos globales
    data_global = pd.DataFrame({
        'Minera': LISTA_MINERAS,
        'Riesgo_Actual': [np.random.randint(10, 90) for _ in LISTA_MINERAS]
    }).sort_values('Riesgo_Actual', ascending=False)
    
    # SECCIÓN 1: CONTRIBUIDORES AL RIESGO GLOBAL
    col_top, col_low = st.columns(2)
    with col_top:
        st.subheader("⚠️ Mayor Aporte al Riesgo Global")
        fig_top = px.bar(data_global.head(3), x='Minera', y='Riesgo_Actual', color='Riesgo_Actual', 
                         color_continuous_scale='Reds', text_auto=True)
        st.plotly_chart(fig_top, use_container_width=True)
        
    with col_low:
        st.subheader("✅ Mayor Cumplimiento (Riesgo Cero)")
        fig_low = px.bar(data_global.tail(3), x='Minera', y='Riesgo_Actual', color='Riesgo_Actual', 
                         color_continuous_scale='Greens', text_auto=True)
        st.plotly_chart(fig_low, use_container_width=True)

    st.divider()

    # SECCIÓN 2: BARRA GLOBAL DE DESVIACIÓN
    avg_risk = int(data_global['Riesgo_Actual'].mean())
    st.subheader("📊 Estatus de Red Nacional (Consolidado)")
    render_risk_bar(avg_risk)

# --- 7. VISTA POR FAENA (DETALLE TÉCNICO) ---
else:
    faena_sel = st.selectbox("Unidad Minera:", LISTA_MINERAS)
    st.title(f"🏢 UNIDAD: {faena_sel.upper()}")
    
    # Datos de la Faena
    np.random.seed(sum(map(ord, faena_sel)))
    polvo_r, viento_r, bio_r = np.random.randint(20, 80), np.random.randint(10, 70), np.random.randint(80, 100)
    riesgo_f = int((polvo_r * 0.5) + (viento_r * 0.5))

    # BARRA INTERACTIVA LOCAL
    render_risk_bar(riesgo_f)
    
    st.divider()

    # CONTRASTE CON METAS HSE (KPIs IMPUESTOS)
    st.subheader("🎯 Contraste: Real vs. Meta HSE")
    k1, k2, k3 = st.columns(3)
    
    def delta_meta(real, meta):
        diff = real - meta
        return f"{diff} sobre meta" if diff > 0 else f"{abs(diff)} bajo meta"

    k1.metric("💨 Polvo (PM10)", f"{polvo_r} mg/m³", delta_meta(polvo_r, METAS_HSE['Polvo']), delta_color="inverse")
    k2.metric("🌬️ Viento", f"{viento_r} km/h", delta_meta(viento_r, METAS_HSE['Viento']), delta_color="inverse")
    k3.metric("💓 Biometría", f"{bio_r}%", f"{100-bio_r}% Desviación")

    st.divider()

    # MAPA Y RADAR (MÓDULOS MANTENIDOS)
    c_left, c_right = st.columns([1, 1])
    with c_left:
        st.subheader("🛰️ Ubicación Nodos")
        m = folium.Map(location=[-22.3, -68.9], zoom_start=13, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
        folium_static(m, width=500, height=350)
    with c_right:
        st.subheader("🎯 Radar de Correlación")
        fig_radar = go.Figure(go.Scatterpolar(
            r=[polvo_r, viento_r, bio_r, 30, riesgo_f],
            theta=['Polvo', 'Viento', 'Bio', 'Gases', 'Riesgo'],
            fill='toself', line_color='#e67e22'
        ))
        st.plotly_chart(fig_radar, use_container_width=True)

st.divider()
st.caption(f"AIH-MASTER MAXIMIZED | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Auditoría de Riesgo Cero")
