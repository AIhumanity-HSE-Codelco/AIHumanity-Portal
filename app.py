import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(page_title="AIH-MASTER SUPERUSER", layout="wide")

# --- 2. BASE DE DATOS MAESTRA (70K NODOS & UBICACIONES) ---
MINERIA_CHILE = {
    "Norte": {"Chuquicamata": [-22.3, -68.9], "Radomiro Tomic": [-22.2, -68.8], "Escondida": [-24.2, -69.0]},
    "Centro": {"El Teniente": [-34.1, -70.4], "Andina": [-33.1, -70.2], "Los Bronces": [-33.1, -70.3]},
    "Sur": {"Salvador": [-26.2, -69.6]}
}

# --- 3. ESTILOS Y BLINDAJE VISUAL ---
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f6; }
    .report-card { background: white; padding: 20px; border-radius: 10px; border-top: 5px solid #2980b9; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .status-alert { padding: 10px; border-radius: 5px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: CONTROL DE PRIVILEGIOS ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=120)
    st.title("🛡️ AIH-GATEWAY")
    
    # RELOJ DE AUDITORÍA
    tz = pytz.timezone('America/Santiago')
    st.write(f"📅 {datetime.now(tz).strftime('%d/%m/%Y')} | 🕒 {datetime.now(tz).strftime('%H:%M:%S')}")
    
    st.divider()
    # DEFINICIÓN DE ROL
    rol = st.radio("NIVEL DE ACCESO:", ["👑 AIH-MASTER (SuperUser)", "🏗️ OPERACIÓN LOCAL"])
    
    if rol == "🏗️ OPERACIÓN LOCAL":
        sector = st.selectbox("Zona:", list(MINERIA_CHILE.keys()))
        faena = st.selectbox("Faena:", list(MINERIA_CHILE[sector].keys()))
    else:
        faena = "CENTRAL GLOBAL"
        st.warning("MODO AUDITORÍA TOTAL ACTIVO")

# --- 5. LÓGICA DE AUDITORÍA Y TRAZABILIDAD ---
def generar_log_auditoria():
    data = []
    for zona, faenas in MINERIA_CHILE.items():
        for f in faenas:
            data.append({
                "Fecha/Hora": datetime.now(tz).strftime("%Y-%m-%d %H:%M"),
                "Zona": zona,
                "Faena": f,
                "ICR": np.random.randint(10, 85),
                "Estado": "Cumplido",
                "Responsable": f"HSE_Admin_{f[:4]}"
            })
    return pd.DataFrame(data)

log_global = generar_log_auditoria()

# --- 6. ENTORNO MASTER CENTRAL (VISTA SUPER USUARIO) ---
if rol == "👑 AIH-MASTER (SuperUser)":
    st.title("🌐 PANEL CENTRAL DE AUDITORÍA & CONTABILIDAD")
    st.markdown("### Trazabilidad Total de Operaciones Chile")
    
    # DASHBOARD GLOBAL DE RIESGO
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Unidades en Red", "7", "🟢")
    c2.metric("Nodos Activos", "70,000", "Sincro OK")
    c3.metric("Riesgo Promedio", f"{int(log_global['ICR'].mean())}%")
    c4.metric("Auditorías Hoy", "24/24", "100%")

    st.divider()
    
    # MÓDULO DE REPORTES GENERALES
    st.subheader("📊 Consolidado General de PKIs y HSE")
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.write("Historial de Trazabilidad por Faena")
        st.dataframe(log_global, use_container_width=True)
        
    with col_b:
        st.markdown("### 📦 Descarga Maestra")
        st.download_button("📥 Descargar Todo (ZIP/Excel)", data=log_global.to_csv(), file_name="AUDITORIA_GLOBAL_AIH.csv")
        st.info("Correo de Salida: **aeserviseu@gmail.com**")
        email_dest = st.text_input("Enviar reporte consolidado a:", "director_hse@codelco.cl")
        if st.button("📧 Despachar Auditoría Global"):
            st.success(f"Protocolo de envío iniciado desde aeserviseu@gmail.com hacia {email_dest}")

# --- 7. ENTORNO LOCAL (VISTA SEGREGADA) ---
else:
    st.title(f"🏢 PORTAL LOCAL: {faena.upper()}")
    st.caption(f"Acceso restringido a datos de la unidad {faena}")
    
    # Datos Locales
    datos_faena = log_global[log_global['Faena'] == faena]
    riesgo_l = datos_faena['ICR'].values[0]
    
    # Barra de Riesgo (Mantenida)
    st.progress(riesgo_l / 100)
    st.write(f"Desviación Riesgo Cero: {riesgo_l}%")

    # Descargas Locales (Solo sus índices)
    st.divider()
    st.subheader(f"📄 Mis Reportes HSE: {faena}")
    st.download_button(f"📥 Descargar PKIs {faena}", data=datos_faena.to_csv(), file_name=f"HSE_{faena}.csv")
    
    # Mapa GPS Faena (Mantenido)
    m = folium.Map(location=MINERIA_CHILE[sector][faena], zoom_start=13, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium_static(m, width=1100, height=400)

st.divider()
st.caption("AIH-MASTER CORE v6.0 | Gobernanza Blindada | aeserviseu@gmail.com | Uniting Technology")
