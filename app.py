import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime

# --- CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH-GLOBAL COMMAND CENTER", layout="wide")

# --- BASE DE DATOS ESTRUCTURADA ---
LISTA_MINERAS = ["Chuquicamata", "El Teniente", "Escondida", "Collahuasi", "Los Bronces", "Andina", "Salvador"]

# --- MOTOR DE RIESGO CON DETECCIÓN DE CRISIS ---
def get_global_engine():
    status_data = []
    crisis_activa = False
    minera_en_crisis = ""
    
    for m in LISTA_MINERAS:
        # Simulación: Chuquicamata simulará un evento grave para este ejemplo
        if m == "Chuquicamata":
            riesgo = 88 # Forzamos Crisis
        else:
            riesgo = np.random.randint(10, 50)
            
        nivel = "CRÍTICO" if riesgo > 75 else "ALERTA" if riesgo > 45 else "ESTABLE"
        if nivel == "CRÍTICO":
            crisis_activa = True
            minera_en_crisis = m
            
        status_data.append({
            "Minera": m, 
            "Riesgo": riesgo, 
            "Nivel": nivel, 
            "Color": "red" if nivel == "CRÍTICO" else "orange" if nivel == "ALERTA" else "green",
            "Icono": "🚫" if nivel == "CRÍTICO" else "⚠️" if nivel == "ALERTA" else "✅"
        })
    return pd.DataFrame(status_data), crisis_activa, minera_en_crisis

# --- INTERFAZ DE USUARIO ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ AIH-MASTER CORE")
    perfil = st.radio("MODO DE VISUALIZACIÓN:", ["MASTER GLOBAL", "FAENA LOCAL"])
    st.divider()
    if perfil == "FAENA LOCAL":
        faena_sel = st.selectbox("Unidad:", LISTA_MINERAS)
    else:
        faena_sel = "GLOBAL"

# --- PROCESAMIENTO DE DATOS ---
df_global, hay_crisis, unidad_crisis = get_global_engine()

# --- PANTALLA MASTER GLOBAL ---
if perfil == "MASTER GLOBAL":
    st.title("🌐 PANEL DE CONTROL GENERAL - GOBERNANZA")
    
    # BANNER DE ALERTA CRUZADA (Si hay crisis en cualquier unidad)
    if hay_crisis:
        st.error(f"""
            ### 🚨 PROTOCOLO DE CRISIS ACTIVO: EVENTO GRAVE DETECTADO
            **Unidad Afectada:** {unidad_crisis} | **Riesgo:** {df_global[df_global['Minera']==unidad_crisis]['Riesgo'].values[0]}%
            
            **AVISO A TODA LA RED:** Se notificó a todas las unidades mineras. Activar Protocolo de Seguridad Estándar (DS594). 
            Personal de soporte Uniting Technology en alerta.
        """)
    
    # KPIs GENERALES POR SECTOR
    st.subheader("📊 Monitoreo General por Sector")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Nodos AIDeepMiner", "70,000", "SINCRO OK")
    with c2: st.metric("Unidades Críticas", len(df_global[df_global['Nivel'] == "CRÍTICO"]), delta_color="inverse")
    with c3: st.metric("Promedio Riesgo Red", f"{int(df_global['Riesgo'].mean())}%")
    with c4: st.metric("Protocolos Activos", "SOP-09 / SOP-12")

    st.divider()

    # VISUALIZACIÓN DE EVENTOS POR SECTOR (MAPA + TABLA)
    col_map, col_table = st.columns([2, 1])
    
    with col_map:
        st.subheader("🗺️ Localización de Eventos")
        m = folium.Map(location=[-27.0, -70.0], zoom_start=5, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
        coords = {"Chuquicamata": [-22.3, -68.9], "El Teniente": [-34.1, -70.4], "Escondida": [-24.2, -69.0], "Collahuasi": [-20.9, -68.6], "Los Bronces": [-33.1, -70.3], "Andina": [-33.0, -70.2], "Salvador": [-26.2, -69.6]}
        
        for _, row in df_global.iterrows():
            folium.Marker(
                location=coords[row['Minera']],
                popup=f"{row['Minera']}: {row['Nivel']}",
                icon=folium.Icon(color=row['Color'], icon='warning')
            ).add_to(m)
        folium_static(m, width=800, height=450)

    with col_table:
        st.subheader("📋 Resumen de Unidades")
        st.dataframe(df_global[['Icono', 'Minera', 'Nivel', 'Riesgo']], use_container_width=True)

    # GRÁFICO DE ANÁLISIS DE RIESGO
    st.subheader("📈 Análisis de Carga de Riesgo por Minera")
    fig = px.bar(df_global, x='Minera', y='Riesgo', color='Nivel', 
                 color_discrete_map={'CRÍTICO': '#ff4b4b', 'ALERTA': '#f39c12', 'ESTABLE': '#2ecc71'})
    st.plotly_chart(fig, use_container_width=True)

# --- PANTALLA FAENA LOCAL ---
else:
    st.title(f"🏢 PORTAL HSE: {faena_sel.upper()}")
    
    # AVISO DE SEGURIDAD EXTERNA (Si otra minera está en crisis)
    if hay_crisis and unidad_crisis != faena_sel:
        st.warning(f"⚠️ NOTIFICACIÓN DE RED: Evento grave en curso en **{unidad_crisis}**. Mantener alerta en protocolos de comunicación.")
    elif hay_crisis and unidad_crisis == faena_sel:
        st.error(f"🛑 UNIDAD EN ESTADO CRÍTICO: Detención de operaciones sugerida. Reportar a Master Control.")

    st.divider()
    st.subheader("Análisis de Riesgo Local (Señales Correlacionadas)")
    # Gráfico de Radar para ver factores
    riesgo_local = df_global[df_global['Minera'] == faena_sel]['Riesgo'].values[0]
    fig_radar = go.Figure(go.Scatterpolar(
        r=[riesgo_local, np.random.randint(10,90), 95, 20, 10],
        theta=['Polvo', 'Viento', 'Biometría', 'Gases', 'Sismo'],
        fill='toself', line_color='orange'
    ))
    st.plotly_chart(fig_radar, use_container_width=True)

st.divider()
st.caption("AIH-MASTER COMMAND CENTER | Sistema de Interconexión de Emergencia | Uniting Technology")
