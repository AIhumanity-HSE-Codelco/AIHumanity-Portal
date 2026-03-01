import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# 1. CONFIGURACIÓN DE ESCENARIO INDUSTRIAL (MODO FULL WIDTH)
st.set_page_config(
    page_title="AIH MASTER | PORTAL HSE",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. INYECCIÓN DE ADN VISUAL (CSS SEGURO PARA ALTO CONTRASTE)
st.markdown("""
    <style>
    /* Fondo Negro Profundo y texto claro */
    .stApp { background-color: #050505; color: #e0e0e0; }
    
    /* Header Estilo Minero Rajo Abierto */
    .header-aih {
        border-bottom: 3px solid #ffcc00;
        padding: 20px;
        background-color: #111;
        margin-bottom: 30px;
        text-align: center;
        border-radius: 0 0 15px 15px;
    }
    
    /* Métricas Neón (Prioridad Visual MP10/MP2.5) */
    div[data-testid="stMetricValue"] { 
        color: #66fcf1 !important; 
        font-size: 3.8rem !important; 
        font-weight: bold; 
        text-shadow: 0 0 10px rgba(102, 252, 241, 0.3);
    }
    div[data-testid="stMetricLabel"] { 
        color: #ffcc00 !important; 
        text-transform: uppercase; 
        letter-spacing: 2px;
        font-size: 0.9rem !important;
    }
    
    /* Contenedor de Alerta HSE */
    .hse-card {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        border: 2px solid #00ff00;
        background-color: rgba(0, 255, 0, 0.05);
    }
    </style>
    
    <div class="header-aih">
        <h1 style="color: #ffcc00; margin: 0; font-family: 'Arial Black';">🛡️ AIHUMANITY | INTELLIGENCE HSE</h1>
        <p style="color: #66fcf1; margin: 0; font-size: 1.2rem; letter-spacing: 3px;">CENTRO DE CONTROL DE RIESGO PREVENTIVO - TRL-3/4</p>
    </div>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE DATOS DINÁMICOS (Simulación de Sensores)
# En TRL-5 esto se conectará a la DB local o MQTT
np.random.seed(int(time.time()))
mp10_val = round(40 + np.random.uniform(-2, 5), 1)
mp25_val = round(12 + np.random.uniform(-1, 3), 1)
viento_val = np.random.randint(15, 25)

# 4. PRIORIDAD 1: ESTADO CRÍTICO HSE (VISUALIZACIÓN TIPO ZYGHT PRO)
st.markdown(f"""
    <div class="hse-card">
        <h2 style="color: #00ff00; margin:0;">✅ STATUS: OPERACIÓN SEGURA</h2>
        <p style="color: #aaa; margin:5px 0 0 0;">Cumplimiento Estándares ICMM y Normativa Ambiental</p>
    </div>
    """, unsafe_allow_html=True)

# 5. PRIORIDAD 2 Y 3: KPI DE MATERIAL PARTICULADO Y CLIMA
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="MP10 (Polvo)", value=f"{mp10_val}", delta="-1.4 µg/m³", delta_color="inverse")
with col2:
    st.metric(label="MP2.5 (Fino)", value=f"{mp25_val}", delta="0.2 µg/m³", delta_color="inverse")
with col3:
    st.metric(label="Viento", value=f"{viento_val} km/h", delta="DIR: NE")
with col4:
    st.metric(label="Talud / Raveling", value="OK", delta="Estabilidad: 99.2%")

# 6. VISTA OPERADOR: GRÁFICAS DE TENDENCIA (ANÁLISIS PREDICTIVO)
st.divider()
st.write("### 📈 Análisis de Tendencia Histórica (Real-Time)")

# Generar data de simulación para las últimas 24 iteraciones
chart_data = pd.DataFrame(
    np.random.randn(24, 2),
    columns=['Polución (MP10)', 'Vibración Talud']
)

# Gráfico de área para visibilidad industrial
st.area_chart(chart_data, height=300, color=["#66fcf1", "#ffcc00"])



# 7. GESTIÓN DE RIESGOS (FOCO MINERO)
col_info, col_diag = st.columns([2, 1])

with col_info:
    st.info("""
    **NOTAS DE OPERACIÓN:**
    - Supresión de polvo activa en Sector Norte (Chancado).
    - Monitoreo de estabilidad en Fase 4 sin anomalías detectadas.
    - Protocolo HSE alineado con objetivos de sostenibilidad 2026.
    """)

with col_diag:
    with st.expander("🛠️ DIAGNÓSTICO DE NODO AIH"):
        st.write(f"**Último Pulso:** {datetime.now().strftime('%H:%M:%S')}")
        st.write("**Nodo:** ESP32-G4-MINA")
        st.write("**Red:** Híbrida (WiFi/LoRa)")
        st.progress(94, text="Carga de Batería")

# 8. FOOTER TÉCNICO
st.markdown("---")
st.caption("AIHumanity Master | Prototipo Funcional TRL-3 para CODELCO/BHP. Prohibida su reproducción sin autorización.")
