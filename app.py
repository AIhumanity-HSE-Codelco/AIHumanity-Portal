import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime

# --- CONFIGURACIÓN DE SEGURIDAD Y BLINDAJE ---
st.set_page_config(page_title="AIH-MASTER GLOBAL CORE", layout="wide")

# --- MOTOR DE DATOS JERÁRQUICO (Simulando Base de Datos Segregada) ---
def get_faena_data(nombre_faena):
    """
    Simula la captura y gobernanza de múltiples señales de campo.
    Construye el Indicador Compuesto de Riesgo Proactivo (ICRP).
    """
    np.random.seed(sum(map(ord, nombre_faena))) # Semilla única por faena
    
    # Señales de Campo (Raw Signals)
    polvo = np.random.randint(20, 85)
    viento = np.random.randint(5, 70)
    biometria = np.random.uniform(90, 100) # Porcentaje de personal apto
    sismos = np.random.uniform(0, 5)
    
    # Cálculo de Indicador Compuesto (Gobernanza)
    # El riesgo aumenta exponencialmente si el viento y el polvo suben juntos
    icrp = (polvo * 0.4) + (viento * 0.3) + ((100 - biometria) * 2) + (sismos * 10)
    
    return {
        "polvo": polvo,
        "viento": viento,
        "biometria": round(biometria, 1),
        "sismos": round(sismos, 1),
        "icrp": round(min(icrp, 100), 1)
    }

# --- LÓGICA DE ACCESO (ENTORNOS ÚNICOS) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ AIH-GATEWAY")
    
    # Simulación de Login/Filtro por Faena
    st.subheader("Autenticación de Entorno")
    faena_activa = st.selectbox("Seleccione su Unidad Minera:", 
        ["Chuquicamata", "El Teniente", "Escondida", "Collahuasi", "Los Bronces", "SQM Salar"])
    
    st.divider()
    st.markdown(f"**Usuario:** HSE_Manager_{faena_activa.split()[0]}")
    st.markdown(f"**Acceso:** Nivel de Seguridad 4")

# --- CAPTURA DE SEÑALES EN TIEMPO REAL ---
data = get_faena_data(faena_activa)

# --- PANEL DE CONTROL PRINCIPAL (ALARMAS) ---
st.title(f"PORTAL OPERATIVO: {faena_activa.upper()}")
st.caption(f"Gobernanza de Datos Proactiva | AIH-Master Core v4.0 | ID_FAENA: {hash(faena_activa)}")

# Semáforo de Riesgo Compuesto
if data['icrp'] >= 75:
    color_alerta = "#FF0000" # ROJO
    msg = "🛑 STOP WORK ORDERED: Riesgo Compuesto Crítico"
    st.error(msg)
elif data['icrp'] >= 45:
    color_alerta = "#FFD700" # AMARILLO
    msg = "⚠️ ALERTA PREVENTIVA: Monitoreo de Señales en Curso"
    st.warning(msg)
else:
    color_alerta = "#00FF00" # VERDE
    msg = "🟢 OPERACIÓN NORMAL: Parámetros bajo control"
    st.success(msg)

# --- VISUALIZACIÓN DE SEÑALES CORRELACIONADAS ---
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("💨 Polvo (PM10)", f"{data['polvo']} mg/m³")
with col2: st.metric("🌬️ Viento (Señal)", f"{data['viento']} km/h")
with col3: st.metric("💓 Bio-Status", f"{data['biometria']}%")
with col4: st.metric("🛰️ Sismología", f"{data['sismos']} Mw")

st.divider()

# --- GRÁFICO DE RIESGO PROGRESIVO ---
c_left, c_right = st.columns([2, 1])

with c_left:
    st.subheader("📈 Correlación de Riesgo Progresivo (ICRP)")
    # 
    # Generar tendencia basada en la señal de la faena
    history = pd.DataFrame({
        'Tiempo (min)': np.arange(0, 60, 5),
        'Riesgo Compuesto': np.random.uniform(data['icrp']-10, data['icrp']+5, 12)
    })
    fig = px.area(history, x='Tiempo (min)', y='Riesgo Compuesto', 
                  color_discrete_sequence=[color_alerta])
    fig.update_layout(template="plotly_white", yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

with c_right:
    st.subheader("🎯 Matriz de Gobernanza")
    # Gráfico de radar para ver qué señal está empujando el riesgo
    categories = ['Polvo', 'Viento', 'Biometría', 'Sismos', 'Infraest.']
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[data['polvo'], data['viento'], 100-data['biometria'], data['sismos']*20, 30],
        theta=categories, fill='toself', name='Perfil de Riesgo',
        line_color=color_alerta
    ))
    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
    st.plotly_chart(fig_radar, use_container_width=True)

# --- MAPA SATELITAL DE NODOS (AISLADO) ---
st.subheader("📍 Despliegue de Nodos AIDeepMiner en Faena")
m = folium.Map(location=[-22.3, -68.9], zoom_start=14, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
# Solo mostrar nodos de esta faena
for i in range(10):
    folium.CircleMarker(
        location=[-22.3 + np.random.normal(0, 0.005), -68.9 + np.random.normal(0, 0.005)],
        radius=5, color=color_alerta, fill=True
    ).add_to(m)
folium_static(m, width=1100)

st.divider()
st.caption("PROPIEDAD INTELECTUAL AIHUMANITY | ACCESO RESTRINGIDO POR FAENA")
