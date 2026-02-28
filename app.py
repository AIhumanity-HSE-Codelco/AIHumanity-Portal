import streamlit as st

# PANEL CENTRAL DE GOBERNANZA
st.markdown('<h1 style="text-align:center;">🛰️ AIHumanity Central Node</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Luz (D32)", "740 pts", delta="Estable")
    st.write("Fotorresistencia Activa")

with col2:
    st.metric("Temperatura (D26)", "26.8°C", delta="Normal")
    st.write("Módulo DHT11 Sync")

with col3:
    if casco_puesto: # Lógica de D25
        st.success("CASCO: PUESTO")
    else:
        st.error("CASCO: DESCONECTADO")
    st.write("Infrarrojo IR D25")



st.divider()
st.info("Protocolo de Red: telenet 5E4ED | Nodo: AIDeepMiner-ESP32")
