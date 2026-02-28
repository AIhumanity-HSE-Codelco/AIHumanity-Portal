import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH-MASTER CUPERTINO", layout="wide")

# --- 2. MOTOR DE TIEMPO CHILE ---
tz = pytz.timezone('America/Santiago')
now = datetime.now(tz)

# --- 3. BASE DE DATOS GPS ---
MINERIA = {
    "Antofagasta": {"Chuquicamata": [-22.3, -68.9], "Escondida": [-24.2, -69.0]},
    "O'Higgins": {"El Teniente": [-34.1, -70.4]},
    "Atacama": {"Salvador": [-26.2, -69.6]}
}

# --- 4. ESTILO APPLE (GLASSMORPHISM & CLEAN DESIGN) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif; background-color: #f5f5f7; color: #1d1d1f; }}
    
    /* Tarjetas estilo Apple */
    .apple-card {{ 
        background: rgba(255, 255, 255, 0.8); 
        padding: 24px; 
        border-radius: 20px; 
        box-shadow: 0 8px 30px rgba(0,0,0,0.04); 
        border: 1px solid rgba(255,255,255,0.3);
        margin-bottom: 20px;
    }}
    
    /* Barra de Porcentaje Elegante */
    .progress-bg {{ width: 100%; background: #e5e5ea; border-radius: 12px; height: 12px; margin: 15px 0; overflow: hidden; }}
    .progress-fill {{ height: 100%; border-radius: 12px; transition: width 1s ease-in-out; }}
    
    /* Botones y Sidebar */
    .stButton>button {{ border-radius: 12px; background-color: #0071e3; color: white; border: none; padding: 10px 20px; }}
    .stButton>button:hover {{ background-color: #0077ed; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR MINIMALISTA ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b1/Logo_Codelco.svg", width=90)
    st.markdown("### AIH Master Control")
    st.write(f"**{now.strftime('%A, %d %b')}**")
    st.write(f"**{now.strftime('%H:%M:%S')}**")
    st.divider()
    
    rol = st.select_slider("Acceso", options=["Local", "Master"])
    region = st.selectbox("Región", list(MINERIA.keys()))
    faena_sel = st.selectbox("Unidad", list(MINERIA[region].keys()))
    coords = MINERIA[region][faena_sel]

# --- 6. PROCESAMIENTO DE DATOS (70K NODOS) ---
np.random.seed(sum(map(ord, faena_sel)) + now.minute)
viento = np.random.randint(10, 80)
polvo = np.random.randint(20, 90)
riesgo = int((viento * 0.45) + (polvo * 0.55))
color_apple = "#34c759" if riesgo < 40 else "#ffcc00" if riesgo < 75 else "#ff3b30"

# --- 7. PANTALLA PRINCIPAL ---
st.title(f"{faena_sel}")
st.markdown(f"**Gobernanza de Seguridad Proactiva** | Nodos AIDeepMiner: 70,000")

# BARRA DE RIESGO CERO ESTILO APPLE
st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="font-weight: 600;">Índice de Riesgo Crítico</span>
        <span style="color: {color_apple}; font-weight: 600;">{riesgo}%</span>
    </div>
    <div class="progress-bg">
        <div class="progress-fill" style="width: {riesgo}%; background-color: {color_apple};"></div>
    </div>
""", unsafe_allow_html=True)

if riesgo > 75:
    st.warning("⚠️ **ALERTA DE SEGURIDAD:** Protocolo de intervención inmediata sugerido.")

st.divider()

# KPIs EN TARJETAS
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("💨 Polvo", f"{polvo} mg/m³")
with c2: st.metric("🌬️ Viento", f"{viento} km/h")
with c3: st.metric("⌚ Sincro", "Real-time")
with c4: st.metric("📍 GPS", "Active")

st.divider()

# DASHBOARD ESTRATÉGICO
t1, t2, t3 = st.tabs(["Dashboard de Análisis", "Teledetección Satelital", "Auditoría & Trazabilidad"])

with t1:
    col_rad, col_line = st.columns([1, 1.2])
    with col_rad:
        st.subheader("Radar de Riesgos")
        
        fig_rad = go.Figure(go.Scatterpolar(
            r=[polvo, viento, 95, 20, riesgo],
            theta=['Polvo', 'Viento', 'Bio', 'Gases', 'Riesgo'],
            fill='toself', line_color=color_apple
        ))
        fig_rad.update_layout(polar=dict(radialaxis=dict(visible=False)), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_rad, use_container_width=True)
        
    with col_line:
        st.subheader("Tendencia de Seguridad (24h)")
        df = pd.DataFrame({'H': range(24), 'R': np.random.randint(20, 85, 24)})
        fig_line = px.line(df, x='H', y='R', markers=True)
        fig_line.update_traces(line_color=color_apple)
        fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_line, use_container_width=True)

with t2:
    st.subheader(f"Localización Satelital: {faena_sel}")
    m = folium.Map(location=coords, zoom_start=14, tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', attr='Google Sat')
    folium.Circle(coords, radius=500, color=color_apple, fill=True).add_to(m)
    folium_static(m, width=1050, height=450)

with t3:
    st.subheader("Centro de Trazabilidad HSE")
    # Tabla de Auditoría Elegante
    audit = pd.DataFrame({
        "ID Registro": ["AIH-4492", "AIH-4493"],
        "Hora": [now.strftime("%H:%M"), "Anterior"],
        "Faena": [faena_sel, faena_sel],
        "Evento": ["Check Sincronizado", "Descarga Reporte"],
        "Responsable": ["aeserviseu@gmail.com", "Admin_Master"]
    })
    st.table(audit)
    
    st.divider()
    ca, cb = st.columns(2)
    with ca:
        st.download_button("📥 Descargar PKI Consolidado", data=audit.to_csv(), file_name="auditoria.csv")
    with cb:
        if st.button("📧 Enviar Reporte Global"):
            st.success(f"Reporte despachado desde **aeserviseu@gmail.com**")

st.divider()
st.caption("AIH MASTER CORE | v9.0 Cupertino | Uniting Technology Belgium")
