import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. NÚCLEO INMUNE V47.1 (HIGH-AVAILABILITY) ---
st.set_page_config(page_title="AIH CORE-BRAIN | V81", layout="wide", initial_sidebar_state="expanded")

# --- 2. ESTILO INDUSTRIAL XL: BÚNKER UNIFICADO ---
def apply_ultra_bunker_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: -apple-system, sans-serif; }
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7; border-right: 4px solid #0071E3; width: 550px !important; 
        }
        .stRadio div[role="radiogroup"] label {
            font-size: 1.4rem !important; font-weight: 800 !important;
            padding: 18px 15px !important; color: #1D1D1F !important;
            border-bottom: 2px solid #E5E5E7;
        }
        .decision-bunker {
            background-color: #FFFFFF; border-radius: 28px; padding: 35px;
            margin-bottom: 25px; border: 2px solid #E5E5E7;
            box-shadow: 0 15px 50px rgba(0,0,0,0.08);
        }
        .critical-alert { border-left: 15px solid #FF3B30 !important; background-color: #FFF5F5; }
        .warning-alert { border-left: 15px solid #FF9500 !important; background-color: #FFF9F2; }
        .safe-alert { border-left: 15px solid #34C759 !important; background-color: #F5FFF7; }
        h1 { font-size: 4rem !important; font-weight: 900 !important; letter-spacing: -0.07em; }
        h2 { font-size: 2.5rem !important; font-weight: 700; color: #1D1D1F; }
        div[data-testid="stMetricValue"] { font-size: 4rem !important; font-weight: 900 !important; color: #0071E3; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. BÓVEDA INMUTABLE 01-80 ---
BOVEDA_81 = {f"{str(i).zfill(2)}": f"ANALIZADOR {str(i).zfill(2)}" for i in range(1, 81)}
BOVEDA_81.update({
    "01": "💎 EL CEREBRO (IRC-80)", "02": "💨 GASES (M06)", "03": "🧬 BIOMETRÍA", "04": "⚡ ENERGÍA",
    "05": "🗺️ GIS / TALUDES", "06": "🌪️ ADMS / POLVO", "07": "🌍 SISMO", "21": "🌪️ VENTILACIÓN 3D",
    "22": "🚜 COLISIÓN H-M", "26": "🛰️ RADAR SUBSIDENCIA", "57": "🛰️ GNSS RTK", "80": "♾️ ENTROPÍA"
})

# --- 4. MOTOR DE INFERENCIA ---
def get_command_sentence(id_mod, data_val):
    if data_val > 80:
        return {"clase": "critical-alert", "titulo": "SENTENCIA CRÍTICA", "msg": f"Módulo {id_mod} superó umbral (80%).", "accion": "INTERVENCIÓN INMEDIATA"}
    elif data_val > 50:
        return {"clase": "warning-alert", "titulo": "AVISO PREVENTIVO", "msg": f"Tendencia al alza en {id_mod}.", "accion": "REVISIÓN DE PROTOCOLO"}
    return {"clase": "safe-alert", "titulo": "ESTADO NOMINAL", "msg": f"Variable {id_mod} bajo control.", "accion": "OPERACIÓN NORMAL"}

# --- 5. RENDERIZADO CEREBRO ---
def render_master_brain(data):
    st.title("💎 Gobernanza Central")
    col_radar, col_sentencias = st.columns([1.5, 1])
    with col_radar:
        ids = list(BOVEDA_81.keys())
        fig = go.Figure(go.Scatterpolar(
            r=np.append(data, data[0]), theta=np.append(ids, ids[0]),
            fill='toself', line=dict(color='#0071E3', width=4), fillcolor='rgba(0, 113, 227, 0.15)'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=False), angularaxis=dict(tickfont=dict(size=10, weight='bold'))),
                          height=850, margin=dict(t=50, b=50, l=50, r=50), paper_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)
    
    with col_sentencias:
        st.subheader("🧠 Decisiones de Gobierno")
        inf = get_command_sentence("01", data.mean())
        st.markdown(f"""
            <div class="decision-bunker {inf['clase']}">
                <h2 style='margin:0;'>{inf['titulo']}</h2>
                <p style='font-size:1.4rem; color:#1D1D1F;'>{inf['msg']}</p>
                <h3 style='color:#0071E3; margin-top:10px;'>ACCIÓN: {inf['accion']}</h3>
            </div>
        """, unsafe_allow_html=True)
        st.metric("IRC AGREGADO", f"{data.mean():.1f}%")

# --- 6. PANELES 02-80 ---
def render_analyzer_module(id_mod, val_mod):
    st.title(f"{id_mod} | {BOVEDA_81[id_mod]}")
    inf = get_command_sentence(id_mod, val_mod)
    col_data, col_mando = st.columns([1.5, 1])
    with col_data:
        st.write("### Comportamiento Telemetría (70k Nodos)")
        st.line_chart(np.random.normal(val_mod, 5, 100), color="#0071E3")
        st.metric("LECTURA ACTUAL", f"{val_mod}%")
    with col_mando:
        st.markdown(f"""
            <div class="decision-bunker {inf['clase']}">
                <h2 style='margin:0;'>{inf['titulo']}</h2>
                <p style='font-size:1.4rem; color:#1D1D1F;'>{inf['msg']}</p>
                <h3 style='color:#0071E3; margin-top:10px;'>ORDEN: {inf['accion']}</h3>
            </div>
        """, unsafe_allow_html=True)

# --- 7. MAIN ---
def main():
    apply_ultra_bunker_style()
    if 'vault_81' not in st.session_state:
        np.random.seed(81)
        st.session_state.vault_81 = np.random.randint(10, 95, 80)

    with st.sidebar:
        st.markdown("<h1 style='font-size: 2.5rem; color:#0071E3;'>AIH MASTER</h1>", unsafe_allow_html=True)
        st.caption(f"BÓVEDA BLINDADA 81 | {datetime.now().strftime('%H:%M')}")
        st.divider()
        lista = [f"{k} - {v}" for k, v in BOVEDA_81.items()]
        seleccion = st.radio("SISTEMA DE GOBIERNO:", lista, label_visibility="collapsed")
        id_sel = seleccion.split(" - ")[0]

    if id_sel == "01":
        render_master_brain(st.session_state.vault_81)
    else:
        idx = int(id_sel) - 1
        render_analyzer_module(id_sel, st.session_state.vault_81[idx])

if __name__ == "__main__":
    main()
