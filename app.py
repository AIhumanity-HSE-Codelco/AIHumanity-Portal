import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO INMUNE ---
st.set_page_config(page_title="AIH MASTER | V81 SOVEREIGN", layout="wide", initial_sidebar_state="expanded")

# --- 2. ESTILO INDUSTRIAL XL: BÚNKER CUPERTINO ---
def apply_ui():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: -apple-system, sans-serif; }
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7; border-right: 6px solid #0071E3; width: 550px !important; 
        }
        .stRadio div[role="radiogroup"] label {
            font-size: 1.4rem !important; font-weight: 900 !important;
            padding: 15px 10px !important; color: #1D1D1F !important;
            border-bottom: 2px solid #E5E5E7; letter-spacing: -0.02em;
        }
        .mando-bunker {
            background-color: #FFFFFF; border-radius: 30px; padding: 35px;
            margin-bottom: 25px; border: 3px solid #E5E5E7;
            box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        }
        .critical { border-left: 20px solid #FF3B30 !important; background-color: #FFF5F5; }
        .nominal { border-left: 20px solid #34C759 !important; background-color: #F5FFF7; }
        h1 { font-size: 4rem !important; font-weight: 900 !important; letter-spacing: -0.06em; }
        h2 { font-size: 2.5rem !important; font-weight: 800; }
        div[data-testid="stMetricValue"] { font-size: 4rem !important; font-weight: 900 !important; color: #0071E3; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. LA BÓVEDA DE LOS 81 (DECLARACIÓN EXPLÍCITA) ---
BOVEDA_81 = {
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
    "41": "☢️ DOSIMETRÍA", "42": "🌫️ GAS RADÓN", "43": "🧪 XRF SPECTROMETRY", "44": "💧 HIDROQUÍMICA",
    "45": "🧬 BIO-LIXIVIACIÓN", "46": "🌋 VAPOR MERCURIO", "47": "💨 QUÍMICA AIRE", "48": "🧪 REACTIVOS",
    "49": "🛰️ SATELITAL LEO", "50": "📻 RADIO VHF/UHF", "51": "🌐 TRAFFIC INSPECTOR", "52": "📶 5G PRIVATE",
    "53": "🕸️ MESH HEALTH", "54": "🛡️ FIREWALL OT", "55": "🔌 POWERLINE PLC", "56": "📉 QoS/LATENCIA",
    "57": "🛰️ GNSS RTK", "58": "🚁 UTM TRAFFIC", "59": "🛡️ ANTI-DRONE", "60": "📡 RADAR METEO",
    "61": "🛰️ InSAR SPACE", "62": "🔦 LiDAR MAPPING", "63": "🛡️ ADS-B AIRSPACE", "64": "🌌 SPACE WEATHER",
    "65": "🌡️ GRADIENTE GEOTÉRMICO", "66": "🕸️ MICRO-SISMICIDAD", "67": "🧪 ISÓTOPOS AGUA", "68": "🦠 MICROBIOLOGÍA",
    "69": "📢 PSICO-ACÚSTICA", "70": "📉 VOLATILIDAD", "71": "❄️ CRIÓSFERA", "72": "🛰️ ALBEDO",
    "73": "⛓️ TENSIÓN CABLES", "74": "⚡ CAMPOS EM", "75": "🌪️ PLUMA TRONADURA", "76": "🧠 FATIGA MATERIALES",
    "77": "🚢 LOGÍSTICA", "78": "⚖️ COMPLIANCE", "79": "🛡️ DEEP-FAKE DEFENSE", "80": "♾️ ENTROPÍA",
    "81": "🛡️ BLINDAJE SOBERANO"
}

# --- 4. MOTOR DE PERSISTENCIA ---
if 'vault' not in st.session_state:
    st.session_state.vault = [random.randint(30, 80) for _ in range(81)]

apply_ui()

# --- 5. SIDEBAR (LA COLUMNA DE PODER) ---
with st.sidebar:
    st.markdown("<h1 style='font-size: 2.5rem; color:#0071E3;'>AIH MASTER</h1>", unsafe_allow_html=True)
    st.write(f"V81 | BÓVEDA BLINDADA | {datetime.now().strftime('%H:%M')}")
    st.divider()
    
    opciones = [f"{k} - {v}" for k, v in BOVEDA_81.items()]
    seleccion = st.radio("SISTEMA DE MANDO:", opciones, label_visibility="collapsed")
    id_sel = seleccion.split(" - ")[0]

# --- 6. PANEL CENTRAL: EL CEREBRO 01 ---
if id_sel == "01":
    st.title("💎 Gobernanza Central")
    col_rad, col_sent = st.columns([1.6, 1])
    
    with col_rad:
        labels = list(BOVEDA_81.keys())
        values = st.session_state.vault
        fig = go.Figure(go.Scatterpolar(
            r=values + [values[0]], theta=labels + [labels[0]],
            fill='toself', line=dict(color='#0071E3', width=4),
            fillcolor='rgba(0, 113, 227, 0.12)'
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=False), angularaxis=dict(tickfont=dict(size=10))),
            height=850, margin=dict(t=50, b=50, l=50, r=50)
        )
        st.plotly_chart(fig, use_container_width=True)
        

    with col_sent:
        avg = sum(st.session_state.vault) / 81
        clase = "critical" if avg > 70 else "nominal"
        st.markdown(f"""
            <div class="mando-bunker {clase}">
                <h2 style='margin:0;'>ESTADO: {'PELIGRO' if avg > 70 else 'NOMINAL'}</h2>
                <p style='font-size:1.6rem;'>IRC GLOBAL: {avg:.1f}%</p>
                <h3 style='color:#0071E3;'>ACCIÓN: GOBIERNO ACTIVO</h3>
            </div>
        """, unsafe_allow_html=True)
        st.metric("NODOS MESH", "70,000", "SINC FIX")
        st.metric("SISTEMAS", "81/81", "ONLINE")

# --- 7. PANEL INDIVIDUAL ANALIZADORES (02-81) ---
else:
    idx = int(id_sel) - 1
    val = st.session_state.vault[idx]
    st.title(f"{id_sel} | {BOVEDA_81[id_sel]}")
    
    cl, cr = st.columns([1.5, 1])
    with cl:
        st.write("### Telemetría de Alta Precisión")
        dummy = [val + random.uniform(-4,4) for _ in range(50)]
        st.line_chart(dummy, color="#0071E3")
        st.metric("LECTURA ACTUAL", f"{val}%")
        
    with cr:
        clase = "critical" if val > 75 else "nominal"
        st.markdown(f"""
            <div class="mando-bunker {clase}">
                <h2 style='margin:0;'>SENTENCIA M{id_sel}</h2>
                <p style='font-size:1.5rem;'>Módulo verificado en red Mesh.</p>
                <h3 style='color:#0071E3;'>ORDEN: MONITOREO</h3>
            </div>
        """, unsafe_allow_html=True)
