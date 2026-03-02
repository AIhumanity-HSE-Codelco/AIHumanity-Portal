import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import random

# --- 1. CORE BRAIN BLINDADO ---
st.set_page_config(page_title="AIH MASTER V81", layout="wide")

# --- 2. CSS DE ALTO CONTRASTE (CUPERTINO BÚNKER) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    section[data-testid="stSidebar"] { width: 500px !important; border-right: 5px solid #0071E3; background-color: #F5F5F7; }
    
    /* ANALIZADORES XL */
    .stRadio div[role="radiogroup"] label { 
        font-size: 1.5rem !important; font-weight: 800; 
        color: #1D1D1F; border-bottom: 2px solid #E5E5E7; padding: 15px;
    }
    
    /* SENTENCIAS DE MANDO UNIFICADAS */
    .mando-bunker {
        border-radius: 30px; padding: 40px; margin-bottom: 25px;
        border: 3px solid #E5E5E7; box-shadow: 0 20px 60px rgba(0,0,0,0.1);
    }
    .critico { border-left: 20px solid #FF3B30 !important; background-color: #FFF5F5; }
    .nominal { border-left: 20px solid #34C759 !important; background-color: #F5FFF7; }
    
    h1 { font-size: 4.5rem !important; font-weight: 900; letter-spacing: -0.05em; }
    .metric-xl { font-size: 5rem !important; font-weight: 900; color: #0071E3; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BÓVEDA DE 80 ANALIZADORES (ORDEN LÓGICO) ---
BOVEDA = {f"{str(i).zfill(2)}": f"ANALIZADOR {str(i).zfill(2)}" for i in range(1, 81)}
BOVEDA["01"] = "💎 EL CEREBRO (IRC-80)"
BOVEDA["02"] = "💨 GASES (M06)"
BOVEDA["03"] = "🧬 BIOMETRÍA"
BOVEDA["07"] = "🌍 SISMO"
BOVEDA["80"] = "♾️ ENTROPÍA"

# --- 4. PERSISTENCIA DE DATOS ---
if 'vault' not in st.session_state:
    st.session_state.vault = [random.randint(20, 85) for _ in range(80)]

# --- 5. SIDEBAR IZQUIERDO ---
with st.sidebar:
    st.markdown("<h1 style='font-size: 3rem;'>AIH MASTER</h1>", unsafe_allow_html=True)
    st.write(f"V81-BÚNKER | {datetime.now().strftime('%H:%M')}")
    st.divider()
    opciones = [f"{k} - {v}" for k, v in BOVEDA.items()]
    seleccion = st.radio("ORDEN DE MANDO:", opciones, label_visibility="collapsed")
    id_sel = seleccion.split(" - ")[0]

# --- 6. PANEL CENTRAL DE GOBIERNO ---
if id_sel == "01":
    st.title("💎 Gobernanza Central")
    c1, c2 = st.columns([1.5, 1])
    
    with c1:
        # RADAR SEGURO (MÍNIMO CONSUMO RAM)
        labels = list(BOVEDA.keys())
        values = st.session_state.vault
        fig = go.Figure(go.Scatterpolar(
            r=values + [values[0]],
            theta=labels + [labels[0]],
            fill='toself', line=dict(color='#0071E3', width=4),
            fillcolor='rgba(0, 113, 227, 0.1)'
        ))
        fig.update_layout(height=800, polar=dict(radialaxis=dict(visible=False)), showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        

    with c2:
        st.markdown("### 🧠 SENTENCIAS DEL CEREBRO")
        avg_risk = sum(st.session_state.vault) / 80
        clase = "critico" if avg_risk > 70 else "nominal"
        estado = "PELIGRO CRÍTICO" if avg_risk > 70 else "ESTADO NOMINAL"
        
        st.markdown(f"""
            <div class="mando-bunker {clase}">
                <h1 style='margin:0;'>{estado}</h1>
                <p style='font-size:1.8rem;'>IRC PROMEDIO: {avg_risk:.1f}%</p>
                <h2 style='color:#0071E3;'>ACCIÓN: GOBIERNO AUTOMÁTICO ACTIVO</h2>
            </div>
        """, unsafe_allow_html=True)
        st.metric("NODOS SINC", "70,000", "FIX")

else:
    # VISTA ANALIZADOR INDIVIDUAL
    idx = int(id_sel) - 1
    val = st.session_state.vault[idx]
    st.title(f"{id_sel} | {BOVEDA[id_sel]}")
    
    c_left, c_right = st.columns([1.5, 1])
    with c_left:
        st.write("### Telemetría de Alta Frecuencia")
        dummy_data = [val + random.uniform(-5, 5) for _ in range(50)]
        st.line_chart(dummy_data, color="#0071E3")
        
    with c_right:
        clase = "critico" if val > 75 else "nominal"
        st.markdown(f"""
            <div class="mando-bunker {clase}">
                <h2 style='margin:0;'>SENTENCIA M{id_sel}</h2>
                <p style='font-size:1.5rem;'>Lectura actual: {val}%</p>
                <h3 style='color:#0071E3;'>ORDEN: MONITOREO RTK</h3>
            </div>
        """, unsafe_allow_html=True)
