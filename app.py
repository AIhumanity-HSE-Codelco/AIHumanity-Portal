import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- 1. CONFIGURACIÓN Y ESTILO ---
st.set_page_config(page_title="AIH | Master Control V16", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 15px; border-radius: 12px; }
        .energy-card { background: white; padding: 15px; border-radius: 12px; border-top: 5px solid #34C759; margin-bottom: 10px; border-left: 1px solid #D2D2D7; border-right: 1px solid #D2D2D7; border-bottom: 1px solid #D2D2D7; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. COMPONENTES ANALIZADORES ---

def render_energia():
    st.markdown("## ⚡ Módulo 08: Eficiencia Energética & Flota")
    
    # KPIs de Energía
    e1, e2, e3, e4 = st.columns(4)
    cons_total = 450 + np.random.randint(-20, 50)
    e1.metric("Consumo Total", f"{cons_total} kW", "+12 kW")
    e2.metric("Factor de Potencia", "0.96", "Óptimo")
    e3.metric("Eficiencia", "1.2 kWh/Ton", "-0.1")
    e4.metric("Flota Operativa", "85%", "3 en Mant.")

    st.write("---")
    
    col_chart, col_fleet = st.columns([2, 1])
    
    with col_chart:
        st.markdown("### **Demanda Eléctrica en Tiempo Real**")
        chart_data = pd.DataFrame(np.random.normal(cons_total, 10, 24), columns=['Demanda (kW)'])
        st.area_chart(chart_data, color="#34C759")
        

    with col_fleet:
        st.markdown("### **Estado Flota Eléctrica (LHD)**")
        st.markdown("""
        <div class="energy-card">
            <b>LHD-01 (Sandvik)</b><br>
            Batería: <span style='color:#34C759'>82%</span><br>
            Estado: Cargando (Nivel 4)
        </div>
        <div class="energy-card">
            <b>LHD-02 (Sandvik)</b><br>
            Batería: <span style='color:#FF9500'>45%</span><br>
            Estado: Operativo (Rampa)
        </div>
        """, unsafe_allow_html=True)
        st.info("💡 **Peak Shaving:** Sugerencia de pausar carga de LHD-01 para evitar sobrecosto en punta.")

def render_core():
    st.markdown("## 🧠 El Cerebro: Inferencia de Riesgo (IRC)")
    # El IRC ahora incluye eficiencia y fatiga
    st.metric("IRC GLOBAL", "44.2%", "+1.7% (Demanda Alta)")
    st.write("---")
    st.markdown("### **Distribución de Riesgo por Módulo**")
    fig = go.Figure(go.Pie(labels=['Gases','Sismo','PHM','Humano','Energía'], values=[20, 15, 10, 35, 20], hole=.4))
    fig.update_layout(height=300, margin=dict(t=0,b=0,l=0,r=0))
    st.plotly_chart(fig, use_container_width=True)

# --- 3. EJECUCIÓN MAESTRA (NAVEGACIÓN BLINDADA) ---
def main():
    apply_style()
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/3253/3253907.png", width=50)
        sel = st.radio("SISTEMAS REINTEGRADOS:", [
            "💎 EL CEREBRO", 
            "⚡ ENERGÍA (M08)",
            "🧬 BIOMETRÍA (M07)", 
            "💨 GASES (M06)", 
            "🌪️ ADMS", 
            "🌍 SISMO", 
            "⚙️ ACTIVOS", 
            "🚨 EMERGENCIAS"
        ])
        st.divider()
        st.caption(f"V16.0 | M08 Energía Activo | {datetime.now().strftime('%H:%M')}")

    # Switch de Navegación Blindado
    if sel == "💎 EL CEREBRO": render_core()
    elif sel == "⚡ ENERGÍA (M08)": render_energia()
    elif sel == "🧬 BIOMETRÍA (M07)": 
        st.markdown("## 🧬 M07: Biometría Activa"); st.info("Módulo Blindado.")
    elif sel == "💨 GASES (M06)": 
        st.markdown("## 💨 M06: Gases Activo"); st.info("Módulo Blindado.")
    elif sel == "🌪️ ADMS": 
        st.markdown("## 🌪️ ADMS Activo"); st.info("Módulo Blindado.")
    elif sel == "🌍 SISMO": 
        st.markdown("## 🌍 Sismo Activo"); st.info("Módulo Blindado.")
    elif sel == "⚙️ ACTIVOS": 
        st.markdown("## ⚙️ Activos Activo"); st.info("Módulo Blindado.")
    elif sel == "🚨 EMERGENCIAS": 
        st.markdown("## 🚨 Emergencias Activo"); st.info("Módulo Blindado.")

if __name__ == "__main__":
    main()
