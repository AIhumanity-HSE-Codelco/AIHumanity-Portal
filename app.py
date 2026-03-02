import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. NÚCLEO INMUNE V46 (ALTA DISPONIBILIDAD) ---
st.set_page_config(page_title="AIH CORE-BRAIN | BLINDADO", layout="wide", initial_sidebar_state="expanded")

# --- 2. ESTILO INDUSTRIAL XL: CUPERTINO BÚNKER ---
def apply_ironclad_style():
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: -apple-system, sans-serif; }
        
        /* Sidebar Blindado XL */
        section[data-testid="stSidebar"] { 
            background-color: #F5F5F7; border-right: 3px solid #D2D2D7; width: 550px !important; 
        }
        
        /* Analizadores Izquierda: Texto de Alta Visibilidad */
        .stRadio div[role="radiogroup"] label {
            font-size: 1.3rem !important; font-weight: 700 !important;
            padding: 15px 12px !important; color: #1D1D1F !important;
            border-bottom: 1px solid #E5E5E7;
        }

        /* Tarjetas de Decisión del Cerebro */
        .decision-bunker {
            background-color: #FFFFFF; border-radius: 24px; padding: 25px;
            margin-bottom: 20px; border: 2px solid #E5E5E7;
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        }
        .critical-alert { border-left: 12px solid #FF3B30 !important; }
        .warning-alert { border-left: 12px solid #FF9500 !important; }
        .safe-alert { border-left: 12px solid #34C759 !important; }
        
        /* Métricas de Mando */
        div[data-testid="stMetricValue"] { font-size: 3.5rem !important; font-weight: 800 !important; color: #0071E3; }
        </style>
        """, unsafe_allow_html=True)

# --- 3. DICCIONARIO INMUTABLE (80 ANALIZADORES) ---
BOVEDA_80 = {f"{str(i).zfill(2)}": f"ANALIZADOR {str(i).zfill(2)}" for i in range(1, 81)}
BOVEDA_80.update({
    "01": "💎 EL CEREBRO (IRC-80)", "02": "💨 GASES (M06)", "03": "🧬 BIOMETRÍA", "04": "⚡ ENERGÍA",
    "05": "🗺️ GIS / TALUDES", "06": "🌪️ ADMS / POLVO", "07": "🌍 SISMO", "21": "🌪️ VENTILACIÓN 3D",
    "22": "🚜 COLISIÓN H-M", "26": "🛰️ RADAR SUBSIDENCIA", "57": "🛰️ GNSS RTK", "80": "♾️ ENTROPÍA"
})

# --- 4. MOTOR DE GOBIERNO (INFERENCIA CRUZADA) ---
def get_inference_logic(data):
    inferencias = []
    # Lógica de Cruce: Si Gas (M02) > 70 y Ventilación (M21) < 40
    if data[1] > 70 and data[20] < 40:
        inferencias.append({"clase": "critical-alert", "titulo": "ALERTA DE EXPLOSIVIDAD", "msg": "Cruce detectado: Altas concentraciones de Gas con flujo de aire insuficiente.", "accion": "EVACUACIÓN NIVEL 4"})
    
    # Lógica de Cruce: Si Sismo (M07) > 50 y Talud (M26) > 50
    if data[6] > 50 and data[25] > 50:
        inferencias.append({"clase": "warning-alert", "titulo": "RIESGO DE DESPRENDIMIENTO", "msg": "Micro-sismicidad afectando estabilidad de banca detectada por Radar.", "accion": "RESTRICCIÓN DE CARGA"})
    
    if not inferencias:
        inferencias.append({"clase": "safe-alert", "titulo": "SISTEMA NOMINAL", "msg": "Los 80 analizadores reportan valores dentro del umbral de seguridad.", "accion": "CONTINUAR OPERACIÓN"})
    
    return inferencias

# --- 5. RENDERIZADO DEL CEREBRO CENTRAL ---
def render_core_brain():
    st.title("💎 Cerebro de Inferencia (IRC-80)")
    st.subheader("Gobernanza y Orquestación de Peligros")

    # Radar de 80 Ejes (Datos Persistentes)
    current_data = st.session_state.vault_data
    
    col_left, col_right = st.columns([1.5, 1])
    
    with col_left:
        # Gráfica Radar Profesional
        fig = go.Figure(go.Scatterpolar(
            r=np.append(current_data, current_data[0]),
            theta=np.append(list(BOVEDA_80.keys()), "01"),
            fill='toself', line=dict(color='#0071E3', width=3),
            fillcolor='rgba(0, 113, 227, 0.12)'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=False), angularaxis=dict(tickfont=dict(size=9))),
                          height=800, margin=dict(t=30, b=30, l=30, r=30), paper_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        

    with col_right:
        st.markdown("### 🧠 Sentencias de Mando")
        inferencias = get_inference_logic(current_data)
        for inf in inferencias:
            st.markdown(f"""
                <div class="decision-bunker {inf['clase']}">
                    <h4 style='margin:0; color:#1D1D1F;'>{inf['titulo']}</h4>
                    <p style='font-size:1.1rem; color:#86868B;'>{inf['msg']}</p>
                    <b style='color:#0071E3;'>ACCIÓN: {inf['accion']}</b>
                </div>
            """, unsafe_allow_html=True)
            
        st.divider()
        st.metric("IRC PROMEDIO", f"{current_data.mean():.1f}%", "Estable")
        st.metric("CONECTIVIDAD MESH", "70,000 NODOS", "FIX")

# --- 6. EJECUCIÓN ---
def main():
    apply_ironclad_style()
    
    # Inicialización de Datos Blindados
    if 'vault_data' not in st.session_state:
        np.random.seed(101)
        st.session_state.vault_data = np.random.randint(15, 90, 80)

    # BARRA LATERAL (IZQUIERDA)
    with st.sidebar:
        st.markdown("<h1 style='font-size: 2.2rem;'>AIH MASTER</h1>", unsafe_allow_html=True)
        st.caption(f"BÓVEDA 80 | {datetime.now().strftime('%H:%M')}")
        st.divider()
        
        lista_analizadores = [f"{k} - {v}" for k, v in BOVEDA_80.items()]
        seleccion = st.radio("SISTEMA DE ANÁLISIS:", lista_analizadores, label_visibility="collapsed")
        id_sel = seleccion.split(" - ")[0]

    # PANEL CENTRAL (DECISIONES)
    if id_sel == "01":
        render_core_brain()
    else:
        st.title(f"{id_sel} | {BOVEDA_80[id_sel]}")
        st.markdown("---")
        st.write("#### Telemetría de Nodo Crítico")
        st.line_chart(np.random.normal(50, 10, 60), color="#0071E3")
        st.metric("Estado del Sensor", "SYNC", "Online")

if __name__ == "__main__":
    main()
