import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# 1. SETUP CUPERTINO INDUSTRIAL
st.set_page_config(page_title="AIH | Trazabilidad Teniente", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE ALTO IMPACTO (APPLE WHITE + STATUS COLORS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F8F9FA; }
    .stApp { background-color: #F8F9FA; }
    .card-trazabilidad { background: white; padding: 20px; border-radius: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #5E5CE6; margin-bottom: 15px; }
    .status-badge { padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; color: white; }
    .bg-safe { background-color: #30D158; }
    .bg-warning { background-color: #FF9500; }
    .bg-danger { background-color: #FF3B30; }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER OPERATIVO
t1, t2 = st.columns([3, 1])
with t1:
    st.markdown("<h1 style='color:#1D1D1F; margin:0;'>🛡️ AIHUMANITY | CONTROL DE PERSONAL</h1>", unsafe_allow_html=True)
    st.caption(f"📍 EL TENIENTE - NIVEL RESERVA | {datetime.now().strftime('%H:%M:%S')} CLT")
with t2:
    st.button("📥 GENERAR REPORTE TRAZABILIDAD")

st.divider()

# 4. DASHBOARD DE TRAZABILIDAD Y CHECKEO
col_personal, col_radar, col_check = st.columns([1.2, 1.5, 1.2])

# --- COLUMNA 1: TRAZABILIDAD DE PERSONAL (QUIÉN ESTÁ DENTRO) ---
with col_personal:
    st.subheader("👥 Trazabilidad en Tiempo Real")
    
    # Simulación de Personal en Faena
    personal = [
        {"nombre": "Juan Pérez", "zona": "Galería N-4", "status": "Seguro", "color": "bg-safe"},
        {"nombre": "Carlos Ruiz", "zona": "Chancado P-1", "status": "Alerta MP10", "color": "bg-warning"},
        {"nombre": "Luis Mora", "zona": "Sector Alpha", "status": "Sin Check", "color": "bg-danger"},
    ]
    
    for p in personal:
        st.markdown(f"""
        <div class="card-trazabilidad">
            <div style="display:flex; justify-content:space-between;">
                <b>{p['nombre']}</b>
                <span class="status-badge {p['color']}">{p['status']}</span>
            </div>
            <p style="margin:5px 0 0 0; font-size:0.85rem; color:grey;">📍 Ubicación: {p['zona']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- COLUMNA 2: RADAR DE RIESGO INTEGRADO (HOMBRE + AMBIENTE) ---
with col_radar:
    st.markdown("<p style='text-align:center; font-weight:bold;'>ÍNDICE DE RIESGO OPERATIVO (IRO)</p>", unsafe_allow_html=True)
    
    fig = go.Figure()
    # Ejes: Polvo, Gases, Fatiga Humana, Cumplimiento Protocolo, Estabilidad
    fig.add_trace(go.Scatterpolar(
        r=[45, 20, 30, 85, 95],
        theta=['MP10', 'Gases', 'Fatiga (Bio)', 'Protocolos', 'Talud'],
        fill='toself', fillcolor='rgba(94, 92, 230, 0.2)', line=dict(color='#5E5CE6', width=3)
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=400, margin=dict(t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("**ANÁLISIS PREDICTIVO:** El riesgo aumenta en Galería N-4 por baja ventilación.")

# --- COLUMNA 3: CHECKEO DIGITAL HSE (CONTROL DE ACCESO) ---
with col_check:
    st.subheader("📝 Checkeo Preventivo")
    with st.expander("✅ CONTROL DE ACCESO TURNO B", expanded=True):
        st.checkbox("Uso de Respirador N95/N100", value=True)
        st.checkbox("Lámpara Minera Operativa", value=True)
        st.checkbox("Auto-Rescatador vigente", value=True)
        st.checkbox("Charla de 5 min realizada", value=False)
        
        if st.button("FINALIZAR CHECKEO"):
            st.success("Personal Habilitado")

    st.divider()
    st.subheader("📊 Metas Cero")
    st.metric("Meta Cero Mensual", "92%", "+1.2%")
    st.progress(0.92)

# 5. GEOLOCALIZACIÓN DE ADEEPMINERS (MAPA DE CALOR)
st.write("### 📍 Geolocalización y Cobertura de Nodos")
# Generamos puntos aleatorios simulando nodos en las galerías
map_data = pd.DataFrame(
    np.random.randn(10, 2) / [200, 200] + [-34.05, -70.45],
    columns=['lat', 'lon']
)
st.map(map_data)

# 6. FOOTER Y BOTÓN CRÍTICO
st.divider()
c_f1, c_f2 = st.columns([3, 1])
with c_f1:
    st.caption("AIHumanity v4.2 | Sistema Integrado de Trazabilidad, Sensores y Checkeo HSE | El Teniente 2026")
with c_f2:
    if st.button("🚨 STOP-WORK AUTHORITY"):
        st.error("Protocolo de Detención Activado")
