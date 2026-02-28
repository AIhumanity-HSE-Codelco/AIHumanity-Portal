import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime

# --- CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="AIH-MASTER CONTROL FINAL", layout="wide")

# --- BASE DE DATOS MAESTRA ---
LISTA_MINERAS = ["Chuquicamata", "El Teniente", "Escondida", "Collahuasi", "Los Bronces", "Andina", "Salvador"]

# --- MOTOR DE DATOS BLINDADO POR FAENA ---
def generar_datos_faena(nombre):
    """Genera datos ÚNICOS y persistentes para cada faena específica."""
    state = sum(map(ord, nombre)) # Llave única basada en el nombre
    np.random.seed(state)
    
    # Señales de Campo Específicas
    polvo = np.random.randint(25, 85)
    viento = np.random.randint(10, 90)
    biometria = np.random.randint(85, 100)
    gases = np.random.uniform(0.1, 5.0)
    sismo = np.random.uniform(0, 6)
    
    # Cálculo de Riesgo Compuesto (ICRP)
    icrp = (polvo * 0.3) + (viento * 0.25) + (gases * 10) + (sismo * 5)
    icrp = min(round(icrp, 1), 100.0)
    
    return {
        "polvo": polvo, "viento": viento, "biometria": biometria,
        "gases": round(gases, 2), "sismo": round(sismo, 1), "icrp": icrp
    }

# --- ESTILO INDUSTRIAL ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .kpi-box { background: white; padding: 15px; border-radius: 10px; border-left: 5px solid #f39c12; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    .alert-banner { padding: 20px; border-radius: 10px; font-weight: bold; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: CONTROL DE ACCESO ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ AIH-MASTER CORE")
    perfil = st.radio("SISTEMA:", ["🌍 MASTER GLOBAL", "🏢 PORTAL POR FAENA"])
    st.divider()
    if perfil == "🏢 PORTAL POR FAENA":
        faena_sel = st.selectbox("Seleccione Unidad Minera:", LISTA_MINERAS)
    else:
        faena_sel = "GLOBAL"

# --- LÓGICA DE VISUALIZACIÓN ---

if perfil == "🌍 MASTER GLOBAL":
    st.title("🌐 PANEL DE CONTROL GENERAL (Gobernanza)")
    
    # Recolectar estados de todas para el resumen
    resumen_global = []
    for m in LISTA_MINERAS:
        d = generar_datos_faena(m)
        resumen_global.append({"Minera": m, "Riesgo": d['icrp'], "Estado": "🔴 CRÍTICO" if d['icrp'] > 70 else "🟢 ESTABLE"})
    
    df_g = pd.DataFrame(resumen_global)
    
    # Alerta de Crisis Global
    crisis = df_g[df_g['Riesgo'] > 70]
    if not crisis.empty:
        st.error(f"🚨 ALERTA DE SISTEMA: {len(crisis)} unidad(es) en estado CRÍTICO. Protocolos de emergencia activos.")

    # KPIs de la Red
    c1, c2, c3 = st.columns(3)
    c1.metric("Nodos AIDeepMiner", "70,000", "ONLINE")
    c2.metric("Riesgo Promedio Red", f"{int(df_g['Riesgo'].mean())}%")
    c3.metric("Unidades Críticas", len(crisis))

    st.divider()
    
    # Mapa y Gráfico Comparativo
    col_map, col_bar = st.columns([1, 1])
    with col_map:
        st.subheader("📍 Ubicación y Alertas")
        m = folium.Map(location=[-27, -70], zoom_start=5, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
        folium_static(m, width=550, height=400)
    with col_bar:
        st.subheader("📊 Comparativa de Riesgo por Faena")
        fig = px.bar(df_g, x='Minera', y='Riesgo', color='Riesgo', color_continuous_scale='Reds')
        st.plotly_chart(fig, use_container_width=True)

else:
    # --- PORTAL ESPECÍFICO POR FAENA (RECUPERADO) ---
    data = generar_datos_faena(faena_sel)
    
    st.title(f"🏢 PORTAL HSE: {faena_sel.upper()}")
    st.caption(f"Unidad Autónoma | ID: {hash(faena_sel)} | Sincronizado con Master Control")
    
    # Indicador de Parada (STOP WORK)
    if data['icrp'] > 70:
        st.markdown("<div style='background-color:#ff4b4b; color:white; padding:20px; border-radius:10px; text-align:center; font-size:24px;'>🛑 STOP WORK AUTHORITY ACTIVO</div>", unsafe_allow_html=True)
        st.error(f"Riesgo de {data['icrp']}% excede los límites de seguridad en {faena_sel}.")
    
    st.divider()
    
    # KPIs Recuperados con Iconos
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("💨 Polvo (PM10)", f"{data['polvo']} mg/m³")
    k2.metric("🌬️ Viento", f"{data['viento']} km/h")
    k3.metric("🧬 Biometría", f"{data['biometria']}%")
    k4.metric("🌋 Sismo", f"{data['sismo']} Mw")

    st.divider()

    # Gráficos de Análisis Local
    g1, g2 = st.columns([2, 1])
    
    with g1:
        st.subheader("📈 Tendencia de Riesgo Progresivo")
        # Simular 24 horas de datos para esta faena
        np.random.seed(sum(map(ord, faena_sel)))
        df_hist = pd.DataFrame({'Hora': range(24), 'Riesgo': np.random.uniform(data['icrp']-10, data['icrp']+5, 24)})
        fig_line = px.area(df_hist, x='Hora', y='Riesgo', color_discrete_sequence=['#f39c12'])
        fig_line.update_layout(template="plotly_white", yaxis_range=[0, 100])
        st.plotly_chart(fig_line, use_container_width=True)
    
    with g2:
        st.subheader("🎯 Factores de Riesgo")
        fig_radar = go.Figure(go.Scatterpolar(
            r=[data['polvo'], data['viento'], 100-data['biometria'], data['gases']*20, data['sismo']*15],
            theta=['Polvo', 'Viento', 'Fatiga', 'Gases', 'Sismo'],
            fill='toself', line_color='red' if data['icrp'] > 70 else 'orange'
        ))
        st.plotly_chart(fig_radar, use_container_width=True)

    # Reportes HSE
    st.divider()
    st.subheader(f"📄 Centro de Reportes HSE - {faena_sel}")
    col_rep1, col_rep2 = st.columns(2)
    col_rep1.button(f"📥 Descargar Reporte Diario {faena_sel}")
    col_rep2.button(f"📥 Exportar Datos AIDeepMiner (70k)")

st.divider()
st.caption("AIH-MASTER CONTROL | Sistema de Gobernanza Blindada | Propiedad de Uniting Technology")
