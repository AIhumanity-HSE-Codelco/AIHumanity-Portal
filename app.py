import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AIH MASTER - 200 NODOS", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background: #000000; color: white; }
    .status-card { background: rgba(255,255,255,0.05); border-radius: 20px; padding: 20px; border: 1px solid rgba(255,255,255,0.1); }
    .neon-purple { color: #bf5af2; text-shadow: 0 0 10px #bf5af2; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🛡️ AIHUMANITY <span class='neon-purple'>MASTER</span> CONTROL</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("### ANALIZADORES 1-100")
    df1 = pd.DataFrame(np.random.uniform(20, 150, size=(50, 2)), columns=['A', 'B'])
    st.dataframe(df1, height=600)

with col2:
    st.markdown("<div style='height: 400px; border: 2px dashed #333; border-radius: 30px; display: flex; align-items: center; justify-content: center;'>VIEWPORT CENTRAL</div>", unsafe_allow_html=True)
    st.metric("SISTEMA", "TRL 4", delta="READY")

with col3:
    st.write("### ANALIZADORES 101-200")
    df2 = pd.DataFrame(np.random.uniform(20, 150, size=(50, 2)), columns=['C', 'D'])
    st.dataframe(df2, height=400)
    st.success("ESTADO HSE: NOMINAL")
