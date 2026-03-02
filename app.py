import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. NÚCLEO INMUNE V43 ---
st.set_page_config(page_title="AIH MASTER | 80 ANALYZERS", layout="wide", initial_sidebar_state="expanded")

# --- 2. ESTILO INDUSTRIAL XL (CUPERTINO WHITE) ---
def apply_xl_style():
    st.markdown("""
        <style>
        /* Base Blanca Pura */
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: -apple-system, sans-serif; }
        
        /* Sidebar XL con Scroll Optimizado */
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7; 
            border-right: 1px solid #D2D2D7; 
            width: 500px !important; 
        }
        
        /* ANALIZADORES: Letra Muy Grande y Espaciada */
        .stRadio div[role="radiogroup"] label {
            font-size: 1.4rem !important; 
            font-weight: 600 !important;
            padding: 12px 10px !important;
            color: #1D1D1F !important;
            border-bottom: 1px solid #E5E5E7;
        }
        
        /* Títulos y Métricas de Alto Impacto */
        h1 { font-size: 3.5rem !important; font-weight: 800; color: #1D1D1F; }
        h3 { font-size: 2rem !important; color: #86868B; }
        
        /* Card de Métrica Cupertino */
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF; border: 2px solid #D2D2D7; 
            border-radius: 24px; padding: 30px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.04); 
        }
        div[data-testid="stMetricValue"] { font-size: 3rem !important; color: #0071E3 !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. DICCIONARIO MAESTRO: LA BÓVEDA DE LOS 80 ---
# Definición explícita para asegurar que NADA se pierda en el despliegue
BODEGA_80 = {
    "01": "💎 EL CEREBRO (IRC-80)", "02": "💨 GASES (M06)", "03": "🧬 BIOMETRÍA", "04": "⚡ ENERGÍA",
    "05": "🗺️ GIS / TALUDES", "06": "🌪️ ADMS / POLVO", "07": "🌍 SISMO", "08": "⚙️ ACTIVOS",
    "09": "🚨 EMERGENCIAS", "10": "👥 BEHAVIOR", "11": "🔊 ACÚSTICA", "12": "🛠️ MANTENIMIENTO",
    "13": "📊 REPORTES BI", "14": "👁️ OCULOMETRÍA", "15": "🧠 CARGA COGNITIVA", "16": "🌡️ ESTRÉS TÉRMICO",
    "17": "📝 INCIDENTES", "18": "📉 CAUSA RAÍZ", "19": "⚖️ AUDITORÍA", "20": "📢 NOTIFICACIONES",
    "21": "🌪️ VENTILACIÓN 3D", "22": "🚜 COLISIÓN H-M", "23": "📦 STOCKPILES", "24": "⚡ CALIDAD ENERGÍA",
    "25": "📡 MESH STATUS", "26": "🛰️ RADAR SUBSIDENCIA", "27": "🚒 SUPRESIÓN INCENDIO", "28": "👷 ROCKBURST",
    "29": "🚛 FATIGA ACTIVOS", "30": "☁️ INVERSIÓN TÉRMICA", "31": "🛤️ CONTROL LHD", "32": "🌊 GESTIÓN RELAVES",
    "33": "🛡️ CIBERSEGURIDAD", "34": "🔋 MICRO-REDES", "35": "🧬 EPIGENÉTICA", "36": "📉 FRAGMENTACIÓN",
    "37": "🕊️ COMUNIDADES", "38": "♻️ ECONOMÍA CIRCULAR", "39": "🤖 FLOTA AUTÓNOMA", "40": "🔮 ESCENARIOS 4D",
    "41": "☢️ DOSIMETRÍA", "42": "🌫️ GAS RADÓN", "43": "🧪 ESPECTROMETRÍA XRF", "44": "💧 HIDROQUÍMICA",
    "45": "🧬 BIO-LIXIVIACIÓN", "46": "🌋 VAPOR MERCURIO", "47": "💨 QUÍMICA AIRE", "48": "🧪 REACTIVOS",
    "49": "🛰️ SATELITAL LEO", "50": "📻 RADIO VHF/UHF", "51": "🌐 TRAFFIC INSPECTOR", "52": "📶 5G PRIVATE",
    "53": "🕸️ MESH HEALTH", "54": "🛡️ FIREWALL OT", "55": "🔌 POWERLINE PLC", "56": "📉 QoS/LATENCIA",
    "57": "🛰️ GNSS RTK", "58": "🚁 UTM TRAFFIC", "59": "🛡️ ANTI-DRONE", "60": "📡 RADAR METEO",
    "61": "🛰️ InSAR SPACE", "62": "🔦 LiDAR MAPPING", "63": "🛡️ ADS-B AIRSPACE", "64": "🌌 SPACE WEATHER",
    "65": "🌡️ GRADIENTE GEOTÉRMICO", "66": "🕸️ MICRO-SISMICIDAD", "67": "🧪 ISÓTOPOS AGUA", "68": "🦠 MICROBIOLOGÍA",
    "69": "📢 PSICO-ACÚSTICA", "70": "📉 VOLATILIDAD", "71": "❄️ CRIÓSFERA", "72": "🛰️ ALBEDO",
    "73": "⛓️ TENSIÓN CABLES", "74": "⚡ CAMPOS EM", "75": "🌪️ PLUMA TRONADURA", "76": "🧠 FATIGA MATERIALES",
    "77": "🚢 LOGÍSTICA", "78": "⚖️ COMPLIANCE", "79": "🛡️ DEEP-FAKE DEFENSE", "80": "♾️ ENTROPÍA"
}

# --- 4. MOTOR RADAR IRC-80 ---
def draw_radar(data):
    ids = list(BODEGA_80.keys())
    fig = go.Figure(go.Scatterpolar(
        r=np.append(data, data[0]),
        theta=np.append(ids, ids[0]),
        fill='toself',
        line=dict(color='#0071E3', width=3),
        fillcolor='rgba(0, 113, 227, 0.12)'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="#F0F0F2", tickfont=dict(size=12)),
            angularaxis=dict(gridcolor="#F0F0F2", tickfont=dict(size=10, weight='bold'))
        ),
        height=900, paper_bgcolor='white',
        margin=dict(t=80, b=80, l=80, r=80)
    )
    st.plotly_chart(fig, use_container_width=True)
    

# --- 5. LÓGICA DE NAVEGACIÓN ---
def main():
    apply_xl_style()
    
    # Generación de datos persistente
    if 'data_80' not in st.session_state:
        np.random.seed(77)
        st.session_state.data_80 = np.random.randint(25, 90, 80)

    # SIDEBAR: EL COSTADO IZQUIERDO DE PODER
    with st.sidebar:
        st.markdown("<h1>AIH MASTER</h1>", unsafe_allow_html=True)
        st.markdown("### Bóveda de 80 Analizadores")
        st.divider()
        
        # Lista vertical 1 a 80
        opciones = [f"{k} - {v}" for k, v in BODEGA_80.items()]
        seleccion = st.radio("ANALIZADOR ACTIVO:", opciones, label_visibility="collapsed")
        id_actual = seleccion.split(" - ")[0]

    # DASHBOARD CENTRAL
    if id_actual == "01":
        st.title(BODEGA_80["01"])
        st.write("### Estado de Riesgo Global Sincronizado")
        draw_radar(st.session_state.data_80)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("IRC AGREGADO", f"{st.session_state.data_80.mean():.1f}%", "Nominal")
        c2.metric("NODOS MESH", "70,000", "Sync")
        c3.metric("GPS PRECISION", "1.2 cm", "RTK Fix")
    else:
        st.title(f"{id_actual} | {BODEGA_80[id_actual]}")
        st.markdown("---")
        
        ca, cb = st.columns([2, 1])
        with ca:
            st.write("#### Comportamiento del Analizador (24h)")
            st.line_chart(np.random.normal(50, 8, 50), color="#0071E3")
        with cb:
            st.metric("ESTADO SENSOR", "ONLINE", "Sinc")
            st.info(f"Monitoreando variable crítica {id_actual} en tiempo real.")

if __name__ == "__main__":
    main()
