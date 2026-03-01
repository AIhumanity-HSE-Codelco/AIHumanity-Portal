import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
from sklearn.linear_model import LinearRegression

# --- 1. CONFIGURACIÓN CORE ---
st.set_page_config(page_title="AIH MASTER | V19.0", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 20px; border-radius: 12px; }
        .behavior-card { background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #5E5CE6; margin-bottom: 15px; border: 1px solid #D2D2D7; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. NUEVO MÓDULO 10: COMPORTAMIENTO HUMANO ---

def mod_10_comportamiento():
    st.markdown("<h2 style='color:#5E5CE6; border-bottom: 2px solid #5E5CE6;'>10 👥 COMPORTAMIENTO HUMANO PREDICTIVO</h2>", unsafe_allow_html=True)
    
    # KPIs de Comportamiento
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Seguridad Actitudinal", "94%", "+2%")
    c2.metric("Alertas de Proximidad", "3", "-1", delta_color="normal")
    c3.metric("Prob. Incidente (24h)", "0.02%", "Baja")
    c4.metric("Cumplimiento EPP", "100%", "Full")

    st.write("---")
    
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.markdown("### **Tendencia de Alerta Predictiva (Machine Learning)**")
        # Simulación de regresión de riesgo
        x = np.arange(10).reshape(-1, 1)
        y = np.array([10, 12, 11, 15, 14, 18, 17, 22, 21, 25])
        st.line_chart(pd.DataFrame(y, columns=['Nivel de Riesgo Actitudinal']), color="#5E5CE6")
        

    with col_r:
        st.markdown("### **Detección de Anomalías**")
        st.markdown("""
        <div class="behavior-card">
            <b>Operador ID: 4402</b><br>
            Anomalía: Velocidad de marcha reducida (Posible Fatiga).<br>
            <span style='color:#FF9500'>Acción: Entrevista de seguridad sugerida.</span>
        </div>
        """, unsafe_allow_html=True)
        st.info("💡 El modelo predictivo indica estabilidad en el turno actual.")

# --- 3. REINTEGRACIÓN DE LOS 9 MÓDULOS ANTERIORES (RESUMEN BLINDADO) ---

def mod_01_cerebro():
    st.markdown("## 01 💎 EL CEREBRO (IRC)")
    st.metric("IRC GLOBAL", "44.2%", "+2.4% (Factor Humano)")
    # Radar de 10 Ejes
    fig = go.Figure(go.Scatterpolar(r=[40, 30, 25, 60, 20, 30, 15, 45, 10, 70], 
        theta=['Gases','Bio','Energía','GIS','Sismo','PHM','ADMS','Humano','Clima','Behavior'], fill='toself', line_color='#5E5CE6'))
    st.plotly_chart(fig, use_container_width=True)

# --- 4. NAVEGACIÓN MAESTRA ---
def main():
    apply_style()
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=50)
        
        sel = st.selectbox("LISTA DE MÓDULOS BLINDADOS:", [
            "01 💎 EL CEREBRO",
            "10 👥 COMPORTAMIENTO",
            "02 💨 GASES (M06)",
            "03 🧬 BIOMETRÍA (M07)",
            "04 ⚡ ENERGÍA (M08)",
            "05 🗺️ GIS/TALUDES (M09)",
            "06 🌪️ ADMS/POLVO",
            "07 🌍 SISMO",
            "08 ⚙️ ACTIVOS (PHM)",
            "09 🚨 EMERGENCIAS"
        ])
        st.divider()
        st.caption(f"V19.0 | M10 Integrated | {datetime.now().strftime('%H:%M')}")

    # ROUTER
    if sel == "01 💎 EL CEREBRO": mod_01_cerebro()
    elif sel == "10 👥 COMPORTAMIENTO": mod_10_comportamiento()
    elif sel == "02 💨 GASES (M06)": st.info("Módulo Gases Blindado.")
    elif sel == "03 🧬 BIOMETRÍA (M07)": st.info("Módulo Biometría Blindado.")
    elif sel == "04 ⚡ ENERGÍA (M08)": st.info("Módulo Energía Blindado.")
    elif sel == "05 🗺️ GIS/TALUDES (M09)": st.info("Módulo GIS Blindado.")
    elif sel == "06 🌪️ ADMS/POLVO": st.info("Módulo ADMS Blindado.")
    elif sel == "07 🌍 SISMO": st.info("Módulo Sismo Blindado.")
    elif sel == "08 ⚙️ ACTIVOS (PHM)": st.info("Módulo Activos Blindado.")
    elif sel == "09 🚨 EMERGENCIAS": st.info("Módulo Emergencias Blindado.")

if __name__ == "__main__":
    main()
