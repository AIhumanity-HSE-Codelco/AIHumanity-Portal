import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="AIH MASTER V81", layout="wide")

# --- ESTILO BÚNKER (CSS INYECTADO) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    section[data-testid="stSidebar"] { width: 450px !important; border-right: 4px solid #0071E3; }
    .stRadio div[role="radiogroup"] label { font-size: 1.2rem !important; font-weight: 800; border-bottom: 1px solid #DDD; padding: 10px; }
    .decision-bunker { border-radius: 20px; padding: 25px; margin-bottom: 20px; border: 2px solid #EEE; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .critical { border-left: 12px solid #FF3B30; background-color: #FFF5F5; }
    .safe { border-left: 12px solid #34C759; background-color: #F5FFF7; }
    h1 { font-size: 3rem !important; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- BÓVEDA ESTÁTICA ---
BOVEDA = {f"{str(i).zfill(2)}": f"ANALIZADOR {str(i).zfill(2)}" for i in range(1, 81)}
BOVEDA["01"] = "💎 EL CEREBRO (IRC-80)"

# --- LÓGICA DE DATOS ---
if 'data' not in st.session_state:
    st.session_state.data = np.random.randint(10, 90, 80)

# --- SIDEBAR ---
with st.sidebar:
    st.title("AIH MASTER")
    st.caption(f"V81 | {datetime.now().strftime('%H:%M')}")
    sel = st.radio("SISTEMA:", [f"{k} - {v}" for k, v in BOVEDA.items()], label_visibility="collapsed")
    id_sel = sel.split(" - ")[0]

# --- DASHBOARD CENTRAL ---
if id_sel == "01":
    st.title("💎 Gobernanza Central")
    c1, c2 = st.columns([1.5, 1])
    
    with c1:
        # Gráfica simplificada para evitar errores de memoria
        fig = go.Figure(go.Scatterpolar(
            r=np.append(st.session_state.data, st.session_state.data[0]),
            theta=np.append(list(BOVEDA.keys()), "01"),
            fill='toself', line=dict(color='#0071E3', width=2)
        ))
        fig.update_layout(height=700, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)
        
    
    with c2:
        st.subheader("🧠 Sentencias")
        st.markdown(f"""<div class="decision-bunker safe"><h2>ESTADO NOMINAL</h2><p>IRC: {st.session_state.data.mean():.1f}%</p><b>ACCIÓN: OPERACIÓN NORMAL</b></div>""", unsafe_allow_html=True)
        st.metric("NODOS", "70,000", "SYNC")

else:
    idx = int(id_sel) - 1
    val = st.session_state.data[idx]
    st.title(f"M{id_sel} | {BOVEDA[id_sel]}")
    st.metric("VALOR ACTUAL", f"{val}%")
    st.line_chart(np.random.normal(val, 5, 50))
    st.markdown(f"""<div class="decision-bunker safe"><h4>ORDEN DE MANDO</h4><p>Sincronía RTK verificada en nodo {id_sel}.</p></div>""", unsafe_allow_html=True)
