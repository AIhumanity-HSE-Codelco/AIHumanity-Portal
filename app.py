import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import time

# --- CONFIGURACIÓN DE ALTA GAMA ---
st.set_page_config(page_title="AIHumanity OS", layout="wide", initial_sidebar_state="expanded")

# --- ESTILO CUPERTINO DARK (GLASSMORPHISM V2) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@200;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'SF Pro Display', sans-serif; background-color: #000000; color: #f5f5f7; }
    
    /* Sidebar Estilo Apple */
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 10, 0.8); border-right: 1px solid rgba(255,255,255,0.1); }
    
    /* Tarjetas de Datos */
    .stMetric { 
        background: rgba(255, 255, 255, 0.03); 
        border-radius: 24px; 
        padding: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
    }
    
    /* Botones Gradiente Morado/Rosa */
    .stButton>button {
        background: linear-gradient(135deg, #BF5AF2 0%, #FF2D55 100%);
        color: white; border: none; border-radius: 12px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 8px 24px rgba(191, 90, 242, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN (PÁGINAS SIMULADAS) ---
with st.sidebar:
    st.markdown("<h1 style='color: #BF5AF2; font-size: 24px;'>AIHumanity <span style='font-weight:200;'>OS</span></h1>", unsafe_allow_html=True)
    st.caption("TRL3 Master Architecture")
    menu = st.radio("SISTEMA OPERATIVO", ["❖ Dashboard Real-Time", "📈 Análisis de Tendencia", "⚠️ Protocolos HSE", "⚙ Configuración Nodo"])
    st.divider()
    st.info(f"Nodo: AIDeepMiner-01\nLatencia: 42ms\nBatería: 88%")

# URL del ESP32
URL = "https://aihumanity-tr3-default-rtdb.firebaseio.com/nodo1.json"

# --- PÁGINA 1: DASHBOARD REAL-TIME ---
if menu == "❖ Dashboard Real-Time":
    st.markdown("<h1 style='font-weight:200;'>DataStream <span style='font-weight:600; color:#BF5AF2;'>Center 1.0</span></h1>", unsafe_allow_html=True)
    
    try:
        r = requests.get(URL, timeout=2)
        data = r.json()
        
        if data:
            # Indicadores Principales
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.metric("LUMINOSIDAD", f"{data.get('luz', 0)} lx", delta="Normal")
            with c2:
                st.metric("TEMPERATURA", f"{data.get('temp', 0)} °C", delta="Estable")
            with c3:
                puesto = data.get('puesto', False)
                st.markdown(f"<div style='text-align:center;'><b>ESTATUS EPP</b><br><h2 style='color:{'#32D74B' if puesto else '#FF2D55'};'>{'PUESTO' if puesto else 'ALERTA'}</h2></div>", unsafe_allow_html=True)
            with c4:
                st.metric("GAS (SIM)", "0.02 ppm", delta="-0.01", delta_color="inverse")

            # Visualización Potenciada con Plotly
            st.divider()
            col_chart, col_radar = st.columns([2, 1])
            
            with col_chart:
                st.subheader("Flujo de Datos Fotométricos")
                # Simulamos serie de tiempo con el dato real
                y = np.random.normal(data.get('luz', 0), 10, size=50)
                fig = go.Figure()
                fig.add_trace(go.Scatter(y=y, mode='lines', line=dict(color='#BF5AF2', width=3), fill='tozeroy'))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0,r=0,t=0,b=0), height=300, font=dict(color="white"))
                st.plotly_chart(fig, use_container_width=True)

            with col_radar:
                st.subheader("Riesgo Proactivo")
                st.markdown("""
                <div style='background: rgba(191,90,242,0.1); padding:20px; border-radius:20px; border: 1px solid #BF5AF2;'>
                <p style='color:#BF5AF2; margin:0;'>PREDICCIÓN DE SEGURIDAD</p>
                <h2 style='margin:0;'>98.2%</h2>
                <small>Operación Optimizada</small>
                </div>
                """, unsafe_allow_html=True)
                if st.button("ACTUALIZAR NODO"):
                    st.rerun()

    except:
        st.error("Conexión perdida con el AIDeepMiner. Intentando reconexión...")

# --- PÁGINA 2: ANÁLISIS DE TENDENCIA ---
elif menu == "📈 Análisis de Tendencia":
    st.title("Inteligencia Predictiva")
    st.write("Análisis histórico de nodos en rajo abierto y subterráneo.")
    # Aquí puedes sumar Pandas para leer archivos CSV de la mina
    df = pd.DataFrame(np.random.randn(20, 3), columns=['Polvo', 'Gas', 'Vibración'])
    st.line_chart(df)

# --- PÁGINA 3: PROTOCOLOS HSE ---
elif menu == "⚠️ Protocolos HSE":
    st.title("Gobernanza de Seguridad")
    st.markdown("""
    - **Protocolo Alfa:** Evacuación por gas (Inactivo)
    - **Protocolo Beta:** Caída de operario (Detección por acelerómetro)
    - **Estado del Nodo:** Luz Azul Fija (Sincronizado)
    """)
    st.image("https://img.icons8.com/fluency/144/security-shield.png", width=100)

# Auto-refresh cada 3 segundos
time.sleep(3)
st.rerun()
