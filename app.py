cat << 'EOF' > /root/AIHumanity-Portal/app.py
import streamlit as st
import pandas as pd
import numpy as np

# CONFIGURACIÓN TÉCNICA E IDENTIDAD AIH
st.set_page_config(page_title="AIH MASTER - 200 ANALYZERS", layout="wide", initial_sidebar_state="collapsed")

# CSS BLINDADO - CUPERTINO DARK NEON
st.markdown("""
    <style>
    .stApp { background: #000000; font-family: -apple-system, sans-serif; }
    h1 { color: #ffffff !important; font-weight: 800; text-align: center; letter-spacing: -1px; text-shadow: 0px 0px 15px #bf5af2; }
    .neon-purple { color: #bf5af2; }
    .neon-orange { color: #ff9f0a; }
    .neon-green { color: #30d158; }
    /* Contenedores Estilo Cupertino */
    .cupertino-card { background: rgba(255, 255, 255, 0.05); border-radius: 20px; padding: 15px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 10px; }
    /* Estilo de la data */
    .stDataFrame { border: 1px solid #333 !important; border-radius: 10px; }
    [data-testid="stMetricValue"] { color: #30d158 !important; font-size: 2rem !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🛡️ AIHUMANITY <span class='neon-purple'>MASTER</span> CONTROL</h1>", unsafe_allow_html=True)

# LÓGICA DE COLOR (SEMÁFORO MINERO HSE)
def color_val(val):
    if val > 130: color = '#990000'; text = 'white' # Rojo Crítico
    elif val > 90: color = '#999900'; text = 'black' # Amarillo Precaución
    else: color = '#003300'; text = '#30d158'        # Verde Seguro
    return f'background-color: {color}; color: {text}; font-weight: bold;'

# --- LAYOUT DE 3 COLUMNAS (PROTOCOLO INDUSTRIAL) ---
col_izq, col_cen, col_der = st.columns([1.2, 2, 1.2])

with col_izq:
    st.markdown("### <span class='neon-purple'>NODOS 1-100</span>", unsafe_allow_html=True)
    data_izq = np.random.uniform(20.0, 160.0, size=(50, 2))
    df_izq = pd.DataFrame(data_izq, columns=['AN-L1', 'AN-L2'], index=[f"ID-{i+1:03}" for i in range(50)])
    st.dataframe(df_izq.style.applymap(color_val).format("{:.1f}"), height=650, use_container_width=True)

with col_cen:
    # VIEWPORT CENTRAL VACÍO (PARA FUTURO RENDERIZADO 3D/MAPEADO)
    st.markdown("<div style='height: 450px; border: 2px dashed #444; border-radius: 40px; display: flex; align-items: center; justify-content: center; background: rgba(191,90,242,0.02);'>"
                "<h3 style='color: rgba(255,255,255,0.1); letter-spacing: 5px;'>VIEWPORT CENTRAL (VOID)</h3></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # KPIs DE CABECERA NOMINAL
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("SISTEMA", "TRL 4", delta="READY")
    with c2: st.metric("LATENCIA", "164ms", delta="NYC-BEL")
    with c3: st.metric("NODOS", "200/200", delta="ONLINE")

with col_der:
    st.markdown("### <span class='neon-orange'>NODOS 101-200</span>", unsafe_allow_html=True)
    data_der = np.random.uniform(20.0, 160.0, size=(50, 2))
    df_der = pd.DataFrame(data_der, columns=['AN-R1', 'AN-R2'], index=[f"ID-{i+101:03}" for i in range(50)])
    st.dataframe(df_der.style.applymap(color_val).format("{:.1f}"), height=450, use_container_width=True)
    
    # MODULOS ESTADO NOMINAL (COSTADO DERECHO)
    st.markdown("<div class='cupertino-card'>", unsafe_allow_html=True)
    st.markdown("<h4>ESTADO NOMINAL HSE</h4>", unsafe_allow_html=True)
    st.write("🌬️ Viento: <span class='neon-green'>12 km/h SE</span>", unsafe_allow_html=True)
    st.write("💧 Humedad: <span class='neon-green'>45%</span>", unsafe_allow_html=True)
    st.write("⚠️ Taludes: <span class='neon-orange'>Vigilancia</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='color: #444; font-size: 10px; text-align: center;'>AIH-MASTER MASTER INTEGRATOR | 200 NODOS | TRL 4</div>", unsafe_allow_html=True)
EOF

# ACTIVACIÓN DEL MOTOR
source /root/aih_env/bin/activate
fuser -k 80/tcp
nohup streamlit run /root/AIHumanity-Portal/app.py --server.port 80 --server.address 0.0.0.0 > log_portal.txt 2>&1 &
