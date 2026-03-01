import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
from sqlalchemy import create_engine

# --- 1. CONFIGURACIÓN CORE ---
st.set_page_config(page_title="AIH MASTER | V20.0 COMPLETE", layout="wide", initial_sidebar_state="expanded")

def apply_style():
    st.markdown("""
        <style>
        .stApp { background-color: #F5F5F7; color: #1D1D1F; font-family: 'SF Pro Display', sans-serif; }
        .report-card { background: #FFFFFF; padding: 20px; border-radius: 15px; border: 1px solid #D2D2D7; border-left: 5px solid #FF3B30; }
        .sidebar-title { font-size: 1.2em; font-weight: 600; color: #1D1D1F; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. NUEVOS MÓDULOS (11, 12, 13) ---

def mod_11_acustica():
    st.markdown("<h2 style='color:#FF9500;'>11 🔊 CONTAMINACIÓN ACÚSTICA</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Nivel Ruido (Leq)", "82.5 dB(A)", "Límite 85")
    c2.metric("Dosis Proyectada", "64%", "Normal")
    c3.metric("Frecuencia Dominante", "125 Hz", "Baja")
    st.area_chart(np.random.normal(80, 5, 24), color="#FF9500")

def mod_12_mantenimiento():
    st.markdown("<h2 style='color:#8E8E93;'>12 🛠️ MANTENIMIENTO (CMMS)</h2>", unsafe_allow_html=True)
    st.write("### Órdenes de Trabajo Activas")
    data_ot = {
        "OT ID": ["OT-440", "OT-441"],
        "Activo": ["Chancador 1", "Bomba 4"],
        "Prioridad": ["CRÍTICA", "MEDIA"],
        "Estado": ["En Repuestos", "Programada"]
    }
    st.table(pd.DataFrame(data_ot))

def mod_13_reportes():
    st.markdown("<h2 style='color:#0071E3;'>13 📊 REPORTABILIDAD & BI</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="report-card">
            <h4>Generar Reporte de Cumplimiento HSE</h4>
            <p>Periodo: Últimas 24 horas | Nodos: 70,000 | Integridad: 100%</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("📥 Descargar Reporte PDF"):
        st.success("Generando reporte inmutable V20.0...")

# --- 3. REINTEGRACIÓN DEL CEREBRO (IRC) ---
def mod_01_cerebro():
    st.markdown("## 01 💎 EL CEREBRO (IRC) - V20.0")
    # Radar de 13 Ejes
    fig = go.Figure(go.Scatterpolar(
        r=[40, 30, 25, 60, 20, 30, 15, 45, 10, 70, 35, 20, 10], 
        theta=['Gases','Bio','Energía','GIS','Sismo','PHM','ADMS','Humano','Clima','Behavior','Ruido','Maint','BI'],
        fill='toself', line_color='#0071E3'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=False, range=[0, 100])), height=500)
    st.plotly_chart(fig, use_container_width=True)

# --- 4. NAVEGACIÓN MAESTRA ---
def main():
    apply_style()
    with st.sidebar:
        st.markdown("<p class='sidebar-title'>AIH MASTER CONTROL</p>", unsafe_allow_html=True)
        sel = st.selectbox("ENUMERACIÓN DE MÓDULOS (1-13):", [
            "01 💎 EL CEREBRO", "11 🔊 ACÚSTICA", "12 🛠️ MANTENIMIENTO", "13 📊 REPORTES",
            "02 💨 GASES", "03 🧬 BIOMETRÍA", "04 ⚡ ENERGÍA", "05 🗺️ GIS", "10 👥 BEHAVIOR"
        ])
        st.divider()
        st.caption(f"V20.0 | FULL BÓVEDA | {datetime.now().strftime('%H:%M')}")

    if sel == "01 💎 EL CEREBRO": mod_01_cerebro()
    elif sel == "11 🔊 ACÚSTICA": mod_11_acustica()
    elif sel == "12 🛠️ MANTENIMIENTO": mod_12_mantenimiento()
    elif sel == "13 📊 REPORTES": mod_13_reportes()
    else: st.info(f"Módulo {sel} Blindado y Operativo.")

if __name__ == "__main__":
    main()
