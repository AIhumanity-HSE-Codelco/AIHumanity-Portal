import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.express as px
from datetime import datetime
import pytz

# --- CONFIGURACIÓN DE ALTA VISIBILIDAD ---
st.set_page_config(page_title="AIHumanity Global Master", layout="wide")

# --- BASE DE DATOS MAESTRA (JERÁRQUICA) ---
# Expandible a nivel mundial
DATA_MINERA = {
    "Chile": {
        "Antofagasta": ["Chuquicamata", "Radomiro Tomic", "Ministro Hales"],
        "O'Higgins": ["El Teniente"],
        "Atacama": ["Salvador"]
    },
    "Bélgica": {
        "Amberes": ["Puerto Logístico AIH"]
    },
    "Australia": {
        "Pilbara": ["Rio Tinto Iron", "BHP Western"]
    }
}

# --- ESTILO CSS INDUSTRIAL ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e272e; }
    [data-testid="stMetric"] { background-color: #ffffff; border: 1px solid #ced4da; padding: 15px; border-radius: 10px; border-left: 5px solid #f39c12; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: COMANDOS DE BÚSQUEDA Y FILTROS ---
st.sidebar.title("🎛️ Centro de Mando")
pais_sel = st.sidebar.selectbox("Seleccione País:", list(DATA_MINERA.keys()))
region_sel = st.sidebar.selectbox("Región/Zona:", list(DATA_MINERA[pais_sel].keys()))
faena_sel = st.sidebar.selectbox("Faena Minera:", DATA_MINERA[pais_sel][region_sel])
turno_sel = st.sidebar.radio("Turno Actual:", ["A (Día)", "B (Noche)", "C (Relevo)"])

# --- CÁLCULO DE RIESGO (MOTOR AIH) ---
viento = np.random.randint(5, 75)
polvo = np.random.randint(10, 80)
riesgo_global = (viento * 0.4) + (polvo * 0.6)

# --- INTERFAZ PRINCIPAL ---
st.title(f"🛡️ HSE MASTER CONTROL - {faena_sel.upper()}")
st.caption(f"Coordenadas Globales Activas | Integrador: AIH-Master | {datetime.now().strftime('%H:%M:%S')} UTC")

# --- ALERTAS CRÍTICAS ---
if riesgo_global > 60:
    st.error(f"🛑 ALERTA DE PARADA OPERACIONAL: Riesgo Crítico en {faena_sel}. Condiciones climáticas afectan seguridad de vida.")
elif riesgo_global > 40:
    st.warning(f"⚠️ PRECAUCIÓN: Riesgo Moderado. Activar protocolos de mitigación de polvo.")
else:
    st.success(f"🟢 OPERACIÓN NORMAL: Parámetros de seguridad dentro de norma.")

# --- KPIs DINÁMICOS ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Viento Real", f"{viento} km/h", "Alertas Meteo")
c2.metric("Polvo (PM10)", f"{polvo} mg/m³", "AIDeepMiner")
c3.metric("Nodos en Zona", "4,200", "Activos")
c4.metric("Prob. Incidente", f"{int(riesgo_global)}%", "Predictivo", delta_color="inverse")

st.divider()

# --- NAVEGACIÓN POR PESTAÑAS ---
t1, t2, t3 = st.tabs(["🗺️ Mapa Satelital de Riesgo", "📈 Análisis de Movimiento", "📄 Auditoría Mundial"])

with t1:
    st.subheader("Visualización Satelital y Meteorológica")
    # Simulación de coordenadas según la faena
    lat, lon = (-22.3, -68.9) if pais_sel == "Chile" else (51.2, 4.4)
    
    # MAPA SATELITAL REAL
    m = folium.Map(location=[lat, lon], zoom_start=12, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Satélite')
    
    # Capa de Riesgo (Heatmap simulado sobre la faena)
    heat_data = [[lat + (np.random.rand()-0.5)*0.01, lon + (np.random.rand()-0.5)*0.01, np.random.rand()] for _ in range(50)]
    folium.plugins.HeatMap(heat_data, radius=15, gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'}).add_to(m)
    
    folium.Marker([lat, lon], popup=f"Centro de Operaciones {faena_sel}", icon=folium.Icon(color='red')).add_to(m)
    
    folium_static(m, width=1100, height=500)
    st.info("Capa Activa: Satelital + Heatmap de Riesgo Particulado AIDeepMiner.")

with t2:
    st.subheader("Cruce de Datos: Clima vs Producción")
    df_tendencia = pd.DataFrame({
        'Tiempo': pd.date_range(start='now', periods=24, freq='H'),
        'Riesgo Ambiental': np.random.uniform(20, 70, 24),
        'Viento': np.random.uniform(10, 60, 24)
    })
    fig = px.line(df_tendencia, x='Tiempo', y=['Riesgo Ambiental', 'Viento'], 
                  title="Correlación Trazable para Auditoría",
                  color_discrete_map={'Riesgo Ambiental': '#e67e22', 'Viento': '#3498db'})
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

with t3:
    st.subheader("Reporte Consolidado de Faena")
    st.write(f"**Pais:** {pais_sel} | **Región:** {region_sel} | **Faena:** {faena_sel}")
    st.table(pd.DataFrame({
        "Indicador": ["Normativa DS594", "Standard BHP/Codelco", "Protocolo Uniting"],
        "Estado": ["Cumple", "Cumple con Observación", "Certificado"],
        "Valor": [polvo, "Nivel B", "A+"]
    }))
    st.button("📦 Exportar Auditoría PDF Mundial")

st.markdown("---")
st.caption("AIHumanity Global Control System | Uniting Technology Belgium")
