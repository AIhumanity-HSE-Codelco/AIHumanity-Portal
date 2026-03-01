import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# --- CUPERTINO & MINING ORANGE DESIGN SYSTEM ---
st.set_page_config(page_title="AIHumanity Master HSE", layout="wide", initial_sidebar_state="collapsed")

def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'SF Pro Display', sans-serif; background-color: #000000; color: #ffffff; }
    
    /* Cupertino Glassmorphism Card */
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
    }
    
    /* Mining Orange Welcome Screen */
    .welcome-card {
        background: linear-gradient(135deg, #FF6B00 0%, #CC5500 100%);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(255, 107, 0, 0.3);
    }
    
    .status-bar {
        background: #111;
        padding: 10px 20px;
        border-radius: 50px;
        border: 1px solid #333;
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# --- LOGIN / GATEWAY SYSTEM ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None

if not st.session_state.authenticated:
    st.markdown("<div class='welcome-card'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/1063/1063319.png", width=100) # Placeholder Icon
    st.title("AIHumanity HSE System")
    st.subheader("Mining Operations Control Center")
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("OPERATOR ACCESS", use_container_width=True):
            st.session_state.role = "Operator"
            st.session_state.authenticated = True
            st.rerun()
    with col2:
        if st.button("ADMINISTRATOR (DIAGNOSTIC)", use_container_width=True):
            st.session_state.role = "Admin"
            st.session_state.authenticated = True
            st.rerun()
    st.stop()

# --- STATUS BAR (CONNECTIVITY & ENVIRONMENT) ---
st.markdown(f"""
<div class='status-bar'>
    <span>🟢 CONNECTIVITY: GLOBAL-NET (70k NODES)</span>
    <span>📊 TRAFFIC: 4.2 GB/s</span>
    <span>📍 CODELCO NORTH</span>
    <span>🌡️ 28°C</span>
    <span>💨 WIND: 14 KM/H NE</span>
    <span>🕒 {datetime.now().strftime('%H:%M:%S')}</span>
</div>
""", unsafe_allow_html=True)

# --- DASHBOARD NAVIGATION ---
if st.session_state.role == "Operator":
    st.title("Operator HSE View")
    
    # Critical Variables Priority Visual
    c1, c2, c3 = st.columns(3)
    c1.metric("HSE STATUS", "SECURE", delta="Normal")
    c2.metric("PM 10 (DUST)", "15.4 µg/m³", delta="-2.1")
    c3.metric("PM 2.5 (DUST)", "6.8 µg/m³", delta="0.5", delta_color="inverse")
    
    # Real-time Waves
    st.subheader("Risk Control Index (ICR) - Wave Analysis")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Dust', 'Vibration', 'Traffic'])
    st.line_chart(chart_data)

else:
    st.title("Admin Diagnostic Center")
    st.sidebar.success("ADMIN MODE ACTIVE")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("### AI Diagnostics")
        st.info("Invoking OpenAI Analysis Engine...")
        st.write("> Tendency identified: Erosion in Sector 4 increased by 0.5%. Risk: Low.")
    with col2:
        st.write("### Network Health")
        st.progress(98, text="Node Sync Progress (68,540 / 70,000)")
        st.code("TRL-4: ESP32 Latency = 12ms | RSSI = -45dBm")

if st.button("LOGOUT"):
    st.session_state.authenticated = False
    st.rerun()
