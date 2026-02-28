import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium

# --- CONFIGURACIÓN ESTRUCTURAL ---
st.set_page_config(page_title="AIH-MASTER CONTROL GLOBAL", layout="wide")

# --- BASE DE DATOS MAESTRA DE MINERÍA CHILE ---
MINERIA_CHILE = {
    "Tarapacá": ["Cerro Colorado (BHP)", "Quebrada Blanca (Teck)", "Collahuasi"],
    "Antofagasta": ["Escondida (BHP)", "Chuquicamata (Codelco)", "Radomiro Tomic (Codelco)", "Spence (BHP)", "Sierra Gorda", "Centinela", "El Abra", "Gabriela Mistral (Codelco)", "Lomas Bayas", "Zaldívar"],
    "Atacama": ["Caserones", "Candelaria", "Salvador (Codelco)", "La Coipa", "Maricunga", "Cerro Negro Norte", "Los Colorados", "Salares Norte"],
    "Coquimbo": ["Los Pelambres", "Carmen de Andacollo", "El Romeral"],
    "Valparaíso/RM": ["Andina (Codelco)", "Los Bronces", "El Soldado", "Chagres"],
    "O'Higgins": ["El Teniente (Codelco)", "Minera Florida"],
    "No Metálica/Litio": ["SQM Salar de Atacama", "Nueva Victoria", "Pampa Blanca", "Surire (Quiborax)"]
}

# --- ESTILO CSS AVANZADO ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .kpi-card { background-color: white; padding: 20px; border-radius: 15px; border-left: 10px solid #f39c12; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stop-work-red { background-color: #ff4b4b; color: white; padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; animation: pulse 2s infinite; }
    @keyframes pulse { 0% {opacity: 1;} 50% {opacity: 0.7;} 100% {opacity: 1;} }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: SELECTOR JERÁRQUICO ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=100)
    st.title("🛡️ CONTROL MAESTRO")
    region = st.selectbox("📍 Seleccione Región:", list(MINERIA_CHILE.keys()))
    faena = st.selectbox("🏗️ Seleccione Faena:", MINERIA_CHILE[region])
    st.divider()
    st.info(f"Conectado a: {faena}\nNodos AIDeepMiner: 70k Activos")

# --- HEADER DINÁMICO ---
st.title(f"CENTRO DE CONTROL HSE: {faena.upper()}")
st.caption(f"Integrador: AIH-Master | Auditoría en Tiempo Real | Ubicación: Región de {region}")

# --- PESTAÑAS DE VISUALIZACIÓN ---
tab_dash, tab_map, tab_admin = st.tabs(["📊 DASHBOARD DE RIESGOS", "🛰️ TELEDETECCIÓN", "⚙️ GESTIÓN DE FAENAS"])

with tab_dash:
    # FILA 1: KPIs con Iconos
    c1, c2, c3, c4 = st.columns(4)
    riesgo_val = np.random.randint(10, 95)
    
    with c1: st.metric("💨 Polvo PM10", f"{np.random.randint(30,65)} mg/m³", "AIDeepMiner")
    with c2: st.metric("🌬️ Viento", f"{np.random.randint(10,80)} km/h", "Sismología")
    with c3: st.metric("💓 Biometría", "98% OK", "IA Humana")
    with c4: st.metric("📉 Índice Riesgo", f"{riesgo_val}%")

    st.divider()

    # FILA 2: STOP TO WORK HSE INDICATOR
    col_stop, col_graph = st.columns([1, 2])
    
    with col_stop:
        st.subheader("🛡️ Estatus Operativo")
        if riesgo_val > 75:
            st.markdown(f"<div class='stop-work-red'>🛑 STOP WORK ORDERED<br>Riesgo Crítico en {faena}</div>", unsafe_allow_html=True)
            st.error("Protocolo HSE: Evacuación de niveles críticos y cese de carguío.")
        else:
            st.success(f"🟢 OPERACIÓN SEGURA\nIndices dentro de norma en {faena}.")
        
        # Medidor de Riesgo
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = riesgo_val,
            title = {'text': "Nivel de Alerta HSE"},
            gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "orange"},
                     'steps': [{'range': [0, 50], 'color': "green"}, {'range': [50, 75], 'color': "yellow"}, {'range': [75, 100], 'color': "red"}]}
        ))
        fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_graph:
        st.subheader("📈 Proyección de Riesgo Proactivo")
        df_risk = pd.DataFrame({'Hora': range(12), 'Riesgo': np.random.uniform(20, riesgo_val+10, 12)})
        st.plotly_chart(px.line(df_risk, x='Hora', y='Riesgo', title="Trazabilidad 12h", color_discrete_sequence=['#f39c12']), use_container_width=True)

with tab_map:
    st.subheader(f"🛰️ Visualización Satelital: Sector {faena}")
    # Coordenadas simuladas para el ejemplo
    m = folium.Map(location=[-22.3, -68.9], zoom_start=13, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium.Marker([-22.3, -68.9], popup=f"Punto Cero {faena}", icon=folium.Icon(color='red', icon='warning')).add_to(m)
    folium_static(m, width=1100)

with tab_admin:
    st.subheader("📂 Directorio de Faenas con Hipervínculos")
    # Cuadro de faenas con iconos y nombres
    data_list = []
    for reg, faenas in MINERIA_CHILE.items():
        for f in faenas:
            data_list.append({"Región": reg, "Faena": f, "Link": "🌐 Acceso Nodo", "Status": "🟢 Conectado"})
    
    df_faenas = pd.DataFrame(data_list)
    st.dataframe(df_faenas, use_container_width=True)
    st.info("💡 Haga clic en la faena en el menú lateral para cargar sus AIDeepMiners específicos.")

st.divider()
st.caption("AIH-MASTER CONTROL | Uniting Technology Belgium | Sistema de Auditoría Legal y Proactiva")
