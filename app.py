import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN INMUTABLE V41 ---
st.set_page_config(page_title="AIH MASTER | TOTALITY V41", layout="wide", initial_sidebar_state="expanded")

# --- 2. AMBIENTE CUPERTINO HIGH-END ---
def apply_cupertino_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: -apple-system, system-ui, sans-serif; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7; border-right: 1px solid #D2D2D7; width: 400px !important; }
        .stSelectbox, .stRadio { background-color: #FFFFFF; border-radius: 10px; }
        div[data-testid="stMetric"] { 
            background-color: #FFFFFF; border: 1px solid #D2D2D7; 
            border-radius: 18px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); 
        }
        h1 { font-weight: 700; letter-spacing: -0.02em; color: #1D1D1F; }
        .category-header { color: #0071E3; font-weight: 600; font-size: 0.9em; margin-bottom: 10px; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. DICCIONARIO MAESTRO DE IDENTIDAD (80 ANALIZADORES) ---
DOMINIOS = {
    "Dominio I: Estratégico": {
        "01": "💎 EL CEREBRO (IRC-80)", "02": "💨 GASES (M06)", "03": "🧬 BIOMETRÍA", 
        "04": "⚡ ENERGÍA", "05": "🗺️ GIS / TALUDES", "06": "🌪️ ADMS / POLVO", 
        "07": "🌍 SISMO", "08": "⚙️ ACTIVOS", "09": "🚨 EMERGENCIAS", "10": "👥 BEHAVIOR"
    },
    "Dominio II: Salud e Higiene": {
        "11": "🔊 ACÚSTICA", "12": "🛠️ MANTENIMIENTO", "13": "📊 REPORTES BI", 
        "14": "👁️ OCULOMETRÍA", "15": "🧠 CARGA COGNITIVA", "16": "🌡️ ESTRÉS TÉRMICO", 
        "17": "📝 INCIDENTES", "18": "📉 CAUSA RAÍZ", "19": "⚖️ AUDITORÍA", "20": "📢 NOTIFICACIONES"
    },
    "Dominio III: Infraestructura": {
        "21": "🌪️ VENTILACIÓN 3D", "22": "🚜 COLISIÓN H-M", "23": "📦 STOCKPILES", 
        "24": "⚡ CALIDAD ENERGÍA", "25": "📡 MESH STATUS", "26": "🛰️ RADAR SUBSIDENCIA", 
        "27": "🚒 SUPRESIÓN INCENDIO", "28": "👷 ROCKBURST", "29": "🚛 FATIGA ACTIVOS", "30": "☁️ INVERSIÓN TÉRMICA"
    },
    "Dominio IV: Geotecnia y MA": {
        "31": "🛤️ CONTROL LHD", "32": "🌊 GESTIÓN RELAVES", "33": "🛡️ CIBERSEGURIDAD", 
        "34": "🔋 MICRO-REDES", "35": "🧬 EPIGENÉTICA", "36": "📉 FRAGMENTACIÓN", 
        "37": "🕊️ COMUNIDADES", "38": "♻️ ECONOMÍA CIRCULAR", "39": "🤖 FLOTA AUTÓNOMA", "40": "🔮 ESCENARIOS 4D"
    },
    "Dominio V: Química y Nuclear": {
        "41": "☢️ DOSIMETRÍA", "42": "🌫️ GAS RADÓN", "43": "🧪 ESPECTROMETRÍA XRF", 
        "44": "💧 HIDROQUÍMICA", "45": "🧬 BIO-LIXIVIACIÓN", "46": "🌋 VAPOR MERCURIO", 
        "47": "💨 QUÍMICA AIRE", "48": "🧪 REACTIVOS", "49": "🛰️ SATELITAL LEO", "50": "📻 RADIO VHF/UHF"
    },
    "Dominio VI: Conectividad": {
        "51": "🌐 TRAFFIC INSPECTOR", "52": "📶 5G PRIVATE", "53": "🕸️ MESH HEALTH", 
        "54": "🛡️ FIREWALL OT", "55": "🔌 POWERLINE PLC", "56": "📉 QoS/LATENCIA", 
        "57": "🛰️ GNSS RTK", "58": "🚁 UTM TRAFFIC", "59": "🛡️ ANTI-DRONE", "60": "📡 RADAR METEO"
    },
    "Dominio VII: Aeroespacial": {
        "61": "🛰️ InSAR SPACE", "62": "🔦 LiDAR MAPPING", "63": "🛡️ ADS-B AIRSPACE", 
        "64": "🌌 SPACE WEATHER", "65": "🌡️ GRADIENTE GEOTÉRMICO", "66": "🕸️ MICRO-SISMICIDAD", 
        "67": "🧪 ISÓTOPOS AGUA", "68": "🦠 MICROBIOLOGÍA", "69": "📢 PSICO-ACÚSTICA", "70": "📉 VOLATILIDAD"
    },
    "Dominio VIII: Caos y Entropía": {
        "71": "❄️ CRIÓSFERA", "72": "🛰️ ALBEDO", "73": "⛓️ TENSIÓN CABLES", 
        "74": "⚡ CAMPOS EM", "75": "🌪️ PLUMA TRONADURA", "76": "🧠 FATIGA MATERIALES", 
        "77": "🚢 LOGÍSTICA", "78": "⚖️ COMPLIANCE", "79": "🛡️ DEEP-FAKE DEFENSE", "80": "♾️ ENTROPÍA"
    }
}

# --- 4. MOTOR DE RENDERIZADO IRC-80 ---
def render_radar_totality(valores_80):
    all_labels = [str(i).zfill(2) for i in range(1, 81)]
    
    # Cerrar el círculo
    v_plot = np.append(valores_80, valores_80[0])
    e_plot = np.append(all_labels, all_labels[0])
    
    fig = go.Figure()
    
    # Capa de Riesgo con degradado Cupertino
    fig.add_trace(go.Scatterpolar(
        r=v_plot, theta=e_plot, fill='toself',
        line=dict(color='#0071E3', width=2),
        fillcolor='rgba(0, 113, 227, 0.15)',
        hoverinfo='r+theta',
        name="IRC Global"
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="white",
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="#F0F0F2", tickfont=dict(size=9, color="#86868B")),
            angularaxis=dict(gridcolor="#F0F0F2", tickfont=dict(size=7, color="#1D1D1F"), rotation=90)
        ),
        paper_bgcolor='white', height=800,
        margin=dict(t=50, b=50, l=50, r=50)
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    

# --- 5. INTERFAZ Y NAVEGACIÓN ---
def main():
    apply_cupertino_style()
    
    # Estado del sistema (Simulación de datos para los 80)
    if 'risk_data' not in st.session_state:
        np.random.seed(42)
        st.session_state.risk_data = np.random.randint(20, 85, 80)

    with st.sidebar:
        st.markdown("<h1 style='font-size: 1.5rem;'>AIH MASTER V41</h1>", unsafe_allow_html=True)
        st.caption(f"80 ANALIZADORES ACTIVOS | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        # Selector de Categoría (Dominio)
        dominio_nom = st.selectbox("📂 DOMINIO DE CONTROL:", list(DOMINIOS.keys()))
        
        # Selector de Analizador (Dinámico)
        dict_modulos = DOMINIOS[dominio_nom]
        mod_id = st.radio("🔍 ANALIZADOR:", list(dict_modulos.keys()), 
                          format_func=lambda x: f"{x} - {dict_modulos[x]}")
        
        st.divider()
        st.success("Sincronización: 100% (70k Nodos)")
        st.info("Protocolo HSE-Minero TRL 3/4")

    # --- RENDERIZADO PRINCIPAL ---
    if mod_id == "01":
        st.title("💎 Inferencia de Riesgo Compuesto (IRC-80)")
        st.write("### Análisis Holístico de los 8 Dominios de Seguridad")
        render_radar_totality(st.session_state.risk_data)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("IRC PROMEDIO", f"{st.session_state.risk_data.mean():.1f}%", "Estable")
        c2.metric("ALERTA MÁXIMA", f"M{np.argmax(st.session_state.risk_data)+1}", "Crítico")
        c3.metric("CONECTIVIDAD", "99.9%", "Starlink LEO")
    else:
        st.title(f"{mod_id} - {dict_modulos[mod_id]}")
        st.markdown("---")
        
        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.write("#### Histórico de Telemetría (24h)")
            chart_data = pd.DataFrame(np.random.randn(24, 1), columns=['Valor'])
            st.line_chart(chart_data, color="#0071E3")
        with col_b:
            st.metric("Estatus", "Sincronizado", "Fix")
            st.write(f"**Dominio:** {dominio_nom}")
            st.write("**Protocolo:** MQTT over Mesh")
            st.button("Descargar Reporte Forense")

if __name__ == "__main__":
    main()
