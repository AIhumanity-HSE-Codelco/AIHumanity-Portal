import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN DE NÚCLEO INMUNE ---
st.set_page_config(page_title="AIH CORE-BRAIN V45", layout="wide", initial_sidebar_state="expanded")

# --- 2. BLINDAJE VISUAL: INTERFAZ DE GOBIERNO XL ---
def apply_bunker_ui():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: -apple-system, sans-serif; }
        section[data-testid="stSidebar"] { background-color: #F5F5F7; border-right: 2px solid #D2D2D7; width: 450px !important; }
        
        /* Analizadores Izquierda XL */
        .stRadio div[role="radiogroup"] label {
            font-size: 1.2rem !important; font-weight: 600; padding: 12px 10px !important;
            color: #1D1D1F !important; border-bottom: 1px solid #E5E5E7;
        }
        
        /* Panel Central de Decisiones */
        .decision-card {
            background-color: #FBFBFD; border: 2px solid #0071E3; border-radius: 24px;
            padding: 25px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,113,227,0.1);
        }
        .hazard-text { color: #FF3B30; font-weight: 700; font-size: 1.5rem; }
        .action-text { color: #34C759; font-weight: 600; font-size: 1.2rem; }
        
        /* Métricas de Inferencia */
        div[data-testid="stMetricValue"] { font-size: 3.5rem !important; font-weight: 800 !important; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. BÓVEDA ESTÁTICA 01-80 ---
BOVEDA_80 = {f"{str(i).zfill(2)}": f"ANALIZADOR {str(i).zfill(2)}" for i in range(1, 81)}
# Nombres críticos para lógica de cruce
BOVEDA_80.update({
    "01": "💎 EL CEREBRO (IRC-80)", "02": "💨 GASES (M06)", "03": "🧬 BIOMETRÍA", "05": "🗺️ GIS / TALUDES",
    "07": "🌍 SISMO", "21": "🌪️ VENTILACIÓN 3D", "22": "🚜 COLISIÓN H-M", "26": "🛰️ RADAR SUBSIDENCIA",
    "57": "🛰️ GNSS RTK", "80": "♾️ ENTROPÍA"
})

# --- 4. MOTOR DE INFERENCIA (LÓGICA DE CRUCE) ---
def analyze_risks(data):
    alerts = []
    # Simulación de Cruce 1: Gas + Ventilación
    if data[1] > 70 and data[20] < 40:
        alerts.append({"tipo": "CRÍTICO", "msg": "ALTA CONCENTRACIÓN GAS + FALLA VENTILACIÓN", "icon": "🚨", "color": "#FF3B30"})
    
    # Simulación de Cruce 2: Sismo + Talud
    if data[6] > 65 and data[25] > 60:
        alerts.append({"tipo": "AVISO", "msg": "ACTIVIDAD SÍSMICA CON DEFORMACIÓN DE TALUD", "icon": "⚠️", "color": "#FF9500"})
    
    # Simulación de Cruce 3: Biometría + Proximidad
    if data[2] > 75 and data[21] > 70:
        alerts.append({"tipo": "PREVENTIVO", "msg": "FATIGA DETECTADA EN ZONA DE TRÁNSITO PESADO", "icon": "👷", "color": "#0071E3"})
        
    return alerts

# --- 5. RENDERIZADO CENTRAL ---
def render_core_brain():
    st.title("💎 Gobernanza AIH-Master")
    st.subheader("Orquestador de Decisiones en Tiempo Real")
    
    # Datos de los 80 (Sincronizados)
    np.random.seed(99)
    current_data = st.session_state.get('live_data', np.random.randint(10, 95, 80))
    
    # Layout Central: Radar e Inferencias
    col_graph, col_logic = st.columns([1.5, 1])
    
    with col_graph:
        ids = list(BOVEDA_80.keys())
        fig = go.Figure(go.Scatterpolar(
            r=np.append(current_data, current_data[0]),
            theta=np.append(ids, ids[0]),
            fill='toself', line=dict(color='#0071E3', width=3),
            fillcolor='rgba(0, 113, 227, 0.1)'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=False), angularaxis=dict(tickfont=dict(size=8))),
                          height=700, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)
        

    with col_logic:
        st.markdown("### 🧠 Inferencias del Cerebro")
        alertas = analyze_risks(current_data)
        
        if not alertas:
            st.success("SISTEMA EN EQUILIBRIO - Sin cruces de riesgo detectados.")
        else:
            for a in alertas:
                st.markdown(f"""
                <div class="decision-card" style="border-left: 10px solid {a['color']};">
                    <span style="font-size: 0.8rem; color: #86868B;">NIVEL: {a['tipo']}</span><br>
                    <span class="hazard-text">{a['icon']} {a['msg']}</span><br>
                    <hr>
                    <span class="action-text">ACCIÓN RECOMENDADA: Activar Protocolo HSE-0{current_data[0]//20}</span>
                </div>
                """, unsafe_allow_html=True)

    st.divider()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("IRC PROMEDIO", f"{current_data.mean():.1f}%")
    c2.metric("ENTROPÍA (M80)", f"{current_data[79]}%", "-2%")
    c3.metric("NODOS MESH", "70,000", "Sinc")
    c4.metric("ESTADO GPS", "RTK FIX", "1.2cm")

# --- 6. NAVEGACIÓN Y MAIN ---
def main():
    apply_bunker_ui()
    
    with st.sidebar:
        st.markdown("<h1>AIH MASTER</h1>", unsafe_allow_html=True)
        st.caption(f"80 ANALIZADORES | TRL-4 | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        opciones = [f"{k} - {v}" for k, v in BOVEDA_80.items()]
        seleccion = st.radio("ANALIZADORES (01-80):", opciones, label_visibility="collapsed")
        id_sel = seleccion.split(" - ")[0]

    if id_sel == "01":
        render_core_brain()
    else:
        st.title(f"{id_sel} | {BOVEDA_80[id_sel]}")
        st.write("#### Telemetría Directa del Nodo")
        st.line_chart(np.random.normal(50, 5, 50), color="#0071E3")
        st.metric("Integridad de Datos", "100%", "Sync")

if __name__ == "__main__":
    main()
