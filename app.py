import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# --- 1. CONFIGURACIÓN Y BLINDAJE ---
st.set_page_config(page_title="AIH | Master Control V14", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        div[data-testid="stMetric"] { background-color: #FFFFFF; border: 1px solid #D2D2D7; padding: 15px; border-radius: 12px; }
        .biometric-card { background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #0071E3; margin-bottom: 10px; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. MOTOR DE ANÁLISIS BIOMÉTRICO (M07) ---
def calcular_score_fatiga(bpm, temp, horas_turno):
    # Lógica de riesgo: +BPM +Temp +Horas = Mayor Riesgo
    score = (bpm * 0.3) + (temp * 0.5) + (horas_turno * 2)
    risk = "BAJO"
    color = "#30D158"
    
    if score > 85: 
        risk = "CRÍTICO"; color = "#FF3B30"
    elif score > 65: 
        risk = "ALERTA"; color = "#FF9500"
        
    return round(score, 1), risk, color

# --- 3. COMPONENTES ANALIZADORES ---

def render_biometria():
    st.markdown("## 🧬 Módulo 07: Biometría y Fatiga Humana")
    
    # Simulación de Personal en Turno (Datos de Nodos Wearables)
    col1, col2, col3 = st.columns(3)
    
    # Caso Operador 01
    bpm_op1 = 78 + np.random.randint(-5, 15)
    temp_op1 = 36.6 + np.random.uniform(0, 1.5)
    score, risk, color = calcular_score_fatiga(bpm_op1, temp_op1, 10)
    
    with col1:
        st.markdown(f"""
        <div class="biometric-card" style="border-left-color: {color};">
            <p style="color: grey; margin:0;">OPERADOR: J. PÉREZ</p>
            <h3>FATIGA: {risk}</h3>
            <p>PULSO: {bpm_op1} BPM</p>
            <p>TEMP: {round(temp_op1,1)}°C</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### **Variabilidad Cardíaca (HRV)**")
        hrv_data = pd.DataFrame(np.random.normal(60, 5, 20), columns=['ms'])
        st.area_chart(hrv_data, height=150, color="#0071E3")

    with col3:
        st.markdown("### **Aptitud Operativa**")
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 100 - (score/2),
            gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': color}}
        ))
        fig.update_layout(height=200, margin=dict(t=0,b=0,l=0,r=0))
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.info("💡 **Gobernanza:** 3 Operadores en zona de fatiga 'ALERTA'. Se sugiere rotación de puesto en 30 min.")

def render_core():
    st.markdown("## 🧠 El Cerebro: Riesgo Compuesto (IRC)")
    # El cerebro ahora suma el riesgo de gases (M06) + fatiga (M07)
    r_gases = 10 
    r_fatiga = 15
    total_irc = 25 + r_gases + r_fatiga
    
    st.metric("IRC TOTAL", f"{total_irc}%", f"+{r_fatiga}% Fatiga Humana")
    st.markdown("---")
    st.write("### **Matriz de Intervención**")
    st.warning("Factor Humano detectado como principal vector de riesgo actual en Nivel 4.")

# --- 4. EJECUCIÓN MAESTRA ---
def main():
    apply_style()
    with st.sidebar:
        st.markdown("### **AIH MASTER CONTROL**")
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063205.png", width=50)
        sel = st.radio("SISTEMAS BLINDADOS:", 
                      ["💎 EL CEREBRO", "🧬 BIOMETRÍA (M07)", "💨 GASES (M06)", "🌪️ ADMS", "🌍 SISMO"])
        st.divider()
        st.caption(f"V14.0 | M07 Bio-Active | {datetime.now().strftime('%H:%M')}")

    if sel == "💎 EL CEREBRO": render_core()
    elif sel == "🧬 BIOMETRÍA (M07)": render_biometria()
    elif sel == "💨 GASES (M06)": st.info("Módulo Gases Activo.")
    elif sel == "🌪️ ADMS": st.info("Módulo ADMS Activo.")
    elif sel == "🌍 SISMO": st.info("Módulo Sismo Activo.")

if __name__ == "__main__":
    main()
