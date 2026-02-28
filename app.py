import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
import folium
from streamlit_folium import folium_static
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AIHumanity HSE", page_icon="🛡️", layout="wide")

# --- MÓDULO 1: IDENTIDAD CORPORATIVA ---
st.title("🛡️ AIHumanity - HSE Master Control")
st.markdown("### **Organization:** Codelco | **Version:** v2.0.4-TRL3")
st.caption("By Uniting Technology | Belgium")
st.divider()

# --- ESTRUCTURA DE NAVEGACIÓN (HIPERLINKS/TABS) ---
tab1, tab2, tab3 = st.tabs(["📊 Panel de Control de Riesgo (ICR)", "📍 Mapa Global de Nodos", "📑 Reportes HSE"])

with tab1:
    st.header("Telemetría de Riesgo & KPIs Operacionales")
    
    # KPIs y Métricas de Riesgo
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="💨 Polvo PM10 Avg.", value="32 mg/m³", delta="-2.1%")
    col2.metric(label="⚠️ Gases CO/NO2 Avg.", value="12 ppm", delta="Normal")
    col3.metric(label="💓 Biometría Avg.", value="78 BPM", delta="+2 BPM")
    col4.metric(label="✅ Nodos OK", value="69,870", delta="130 Nodos Offline", delta_color="inverse")
    style_metric_cards(background_color="#1d2129", border_left_color="#00ff00", border_size_px=1)

    st.markdown("---")

    # Tendencia Predictiva & Análisis Proactivo (Gráfico de Alta Gama)
    st.subheader("📈 Tendencia Predictiva & Seguridad Proactiva")
    
    df_sim = pd.DataFrame({
        'Tiempo': pd.date_range(start=datetime.now() - pd.Timedelta(hours=24), periods=24, freq='H'),
        'Nivel de Riesgo': np.random.uniform(10, 45, 24)
    })

    fig = px.area(df_sim, x='Tiempo', y='Nivel de Riesgo', 
                  title="Proyección de Exposición (Próximas 24 Horas)",
                  color_discrete_sequence=['#00cc96'])
    fig.update_layout(template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig, use_container_width=True)
    
    st.success("✅ El modelo predictivo indica estabilidad para las próximas 4 horas en el sector actual. KPI: Desviación < 5%")

with tab2:
    st.header("📍 Mapa Global de Nodos AIDeepMiner")
    st.write("Visualización en tiempo real de los 70k nodos de Codelco / BHP.")

    # Simulación de la ubicación del usuario (Bélgica, Chile o China)
    # En un entorno real, esto se obtendría del navegador del usuario
    user_location = st.selectbox(
        "Simular Ubicación del Usuario:",
        ["Bélgica (Uniting HQ)", "Chile (Codelco Minera)", "China (Fábrica de Sensores)"]
    )

    if user_location == "Bélgica (Uniting HQ)":
        start_coords = (50.8503, 4.3517) # Bruselas, Bélgica
    elif user_location == "Chile (Codelco Minera)":
        start_coords = (-22.5647, -68.9135) # Chuquicamata, Chile
    elif user_location == "China (Fábrica de Sensores)":
        start_coords = (30.2741, 120.1551) # Hangzhou, China

    # Creación del mapa Folium
    m = folium.Map(location=start_coords, zoom_start=6, tiles="CartoDB dark_matter")

    # Simulación de nodos activos (cada vez que un nodo se active)
    # Latitudes y longitudes simuladas para cada ubicación
    node_locations = {
        "Bélgica (Uniting HQ)": [(50.8503 + np.random.rand()*0.1, 4.3517 + np.random.rand()*0.1) for _ in range(5)],
        "Chile (Codelco Minera)": [(-22.5647 + np.random.rand()*0.1, -68.9135 + np.random.rand()*0.1) for _ in range(15)],
        "China (Fábrica de Sensores)": [(30.2741 + np.random.rand()*0.1, 120.1551 + np.random.rand()*0.1) for _ in range(10)]
    }

    # Añadir marcadores de nodos
    for lat, lon in node_locations[user_location]:
        folium.Marker(
            [lat, lon], 
            popup=f"Nodo AIDeepMiner Activo - Riesgo: {np.random.randint(1,5)}",
            icon=folium.Icon(color="green" if np.random.rand() > 0.3 else "red", icon="info-sign")
        ).add_to(m)
        
    # Añadir marcador de la ubicación simulada del usuario
    folium.Marker(
        start_coords,
        popup=f"Tu Ubicación Simulada: {user_location}",
        icon=folium.Icon(color="blue", icon="home")
    ).add_to(m)

    # Mostrar el mapa
    folium_static(m, width=900, height=500)
    
    st.warning("🔄 Cada vez que un nodo se active (en China, Chile o Bélgica) será representado aquí.")

with tab3:
    st.header("📑 Generación de Reportes HSE")
    st.write("Genera informes completos en PDF para la gestión de seguridad de Codelco.")

    report_title = st.text_input("Título del Reporte", "Reporte HSE AIHumanity - Codelco")
    report_content = st.text_area("Contenido del Reporte", 
                                  "Este informe detalla las mediciones de telemetría, tendencias de riesgo y el estado de los nodos AIDeepMiner. "
                                  "Se adjuntan los KPIs operacionales clave para el período seleccionado.")

    # Generar PDF
    def create_pdf(title, content):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, 750, title)
        c.setFont("Helvetica", 12)
        textobject = c.beginText(50, 700)
        textobject.textLines(content.split('\n'))
        c.drawText(textobject)
        
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(50, 50, f"Generado por AIHumanity HSE Master Control | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        c.save()
        buffer.seek(0)
        return buffer

    if st.button("Generar Reporte PDF"):
        pdf_buffer = create_pdf(report_title, report_content)
        st.download_button(
            label="Descargar PDF",
            data=pdf_buffer,
            file_name=f"Reporte_HSE_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf"
        )
        st.success("✅ Reporte PDF generado con éxito. Descargue su informe.")
    
    st.markdown("---")
    st.subheader("Histórico de Incidentes")
    # Tabla simulada de incidentes (con AgGrid para interactividad)
    incident_data = pd.DataFrame({
        'ID': [1001, 1002, 1003, 1004],
        'Fecha': ['2026-02-27', '2026-02-26', '2026-02-25', '2026-02-24'],
        'Tipo': ['Exceso PM10', 'Falla Nodo', 'Alerta Gas CO', 'Fatiga Operador'],
        'Sector': ['Nivel 14', 'Rajo Norte', 'Túnel Principal', 'Sala de Control'],
        'Severidad': ['Alta', 'Media', 'Alta', 'Baja'],
        'Estado': ['Cerrado', 'Abierto', 'Abierto', 'Cerrado']
    })

    gb = GridOptionsBuilder.from_dataframe(incident_data)
    gb.configure_pagination(paginationAutoPageSize=True)
    gb.configure_columns(incident_data.columns, editable=True)
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren=True)
    gridOptions = gb.build()

    AgGrid(
        incident_data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=True,
        allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
        enable_enterprise_modules=True,
        height=350,
        width='100%',
        reload_data=True
    )
    st.caption("Filtre y edite incidentes directamente en esta tabla para la gestión HSE.")


# --- PIE DE PÁGINA FIJO ---
st.markdown("---")
st.markdown("**Integrator:** AIH-Master | **Status:** 🟢 SYSTEM ACTIVE")
