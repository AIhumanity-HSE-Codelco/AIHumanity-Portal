import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- BLINDAJE DE SESIÓN (Evita que la gráfica desaparezca al recargar) ---
if 'data' not in st.session_state:
    st.session_state.data = np.random.randint(30, 85, 80)

def main():
    st.set_page_config(page_title="AIH MASTER V38.1", layout="wide")
    
    # CSS CUPERTINO INYECTADO
    st.markdown("""
        <style>
        .stApp { background-color: #FFFFFF; color: #1D1D1F; font-family: -apple-system, sans-serif; }
        [data-testid="stSidebar"] { background-color: #F5F5F7; border-right: 1px solid #D2D2D7; width: 350px !important; }
        h1 { font-weight: 700; color: #1D1D1F; font-size: 2rem; }
        </style>
        """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("AIH MASTER")
        st.subheader("Bóveda 80 Analizadores")
        st.divider()
        # Navegación simplificada para no romper el CSS en móviles
        menu = st.radio("MENÚ PRINCIPAL", ["01 💎 EL CEREBRO (IRC)", "57 🛰️ GPS RTK", "80 ♾️ ENTROPÍA"])
        st.divider()
        st.info("Estado: Blindado V38.1")

    if "01" in menu:
        st.title("💎 Inferencia de Riesgo Compuesto (IRC-80)")
        
        # RADAR INDESTRUCTIBLE
        labels = [str(i).zfill(2) for i in range(1, 81)]
        values = st.session_state.data
        
        fig = go.Figure(go.Scatterpolar(
            r=np.append(values, values[0]),
            theta=np.append(labels, labels[0]),
            fill='toself',
            line=dict(color='#0071E3', width=1),
            fillcolor='rgba(0, 113, 227, 0.1)'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=False), angularaxis=dict(tickfont=dict(size=6))),
            margin=dict(t=20, b=20, l=20, r=20),
            height=650,
            paper_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        

        c1, c2 = st.columns(2)
        c1.metric("IRC GLOBAL", f"{values.mean():.1f}%")
        c2.metric("NODOS SINC", "70,000")

    else:
        st.title(menu)
        st.write("Módulo enlazado al Master.")

if __name__ == "__main__":
    main()
