import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap
import requests
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import io
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AIHumanity HSE Master", page_icon="🛡️", layout="wide")

# --- FUNCIÓN METEOROLOGÍA (SIMULADA TRL3 / API READY) ---
def get_weather(lat, lon):
    # En producción usar: f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=YOUR_API_KEY"
    return {
        "temp": f"{np.random.randint(15, 35)}°C",
        "viento": f"{np.random.randint(5, 40)} km/h",
        "humedad": f"{np.random.randint(10, 60)}%",
        "condicion": "Despejado" if np.random.rand() > 0.3 else "Tormenta de Polvo"
    }

# --- MÓDULO 1: IDENTIDAD ---
st.title("🛡️ AIHumanity - HSE Master Control")
st.markdown(f"### **Codelco / BHP** | **Portal de Auditoría en Tiempo Real**")
st.caption("By Uniting Technology | Belgium | v2.0.4-PRO")

# --- NAVEGACIÓN ---
tab1, tab2, tab3 = st.tabs(["📊 Control & Clima", "🗺️ Mapa de Riesgo 3D", "📄 Auditoría & PDF"])

with tab1:
    st.subheader("🌦️ Reporte Meteorológico & KPIs")
    
    # Simulación por zonas mineras
    zona = st.selectbox("Seleccione Zona de Monitoreo:", ["Chuquicamata", "El Teniente", "Radomiro Tomic", "Puerto Amberes"])
    w = get_weather(-22.5, -68.9)
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Temperatura", w['temp'])
    c2.metric("Viento (Vector)", w['viento'], delta="Alerta Ráfagas" if int(w['viento'].split()[0]) > 30 else "Estable")
    c3.metric("Humedad Relativa", w['humedad'])
    c4.metric("Status AIH-Node", "ACTIVO", delta="70k Nodos")
    style_metric_cards(background_color="#1d2129", border_left_color="#ff4b4b")

    st.markdown("---")
    st.subheader("📈 Análisis de Exposición Proactiva")
    df = pd.DataFrame({'Hora': range(24), 'Riesgo': np.random.uniform(5, 50, 24)})
    fig = px.line(df, x='Hora', y='Riesgo', title="Trazabilidad de Riesgo 24h", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("🗺️ Capas de Riesgo Geográfico (Heatmap)")
    st.info("Visualización de trazabilidad: Los colores indican acumulación de material particulado.")
    
    m = folium.Map(location=[-22.56, -68.91], zoom_start=13, tiles="CartoDB dark_matter")
    
    # Generar puntos de calor (Heatmap) simulando sensores AIDeepMiner
    heat_data = [[-22.56 + (np.random.rand()-0.5)*0.02, -68.91 + (np.random.rand()-0.5)*0.02, np.random.rand()] for _ in range(100)]
    HeatMap(heat_data).add_to(m)
    
    folium_static(m, width=1000)

with tab3:
    st.header("📄 Generador de Informes de Auditoría")
    st.write("Documentos optimizados para impresión legal (PDF A4).")
    
    obs = st.text_area("Observaciones del Ingeniero HSE:", "Sin incidentes críticos. Control de polvo ADMS activo.")

    def build_pdf():
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
        styles = getSampleStyleSheet()
        elements = []

        # Título y Encabezado
        elements.append(Paragraph("INFORME DE AUDITORÍA HSE - AIHUMANITY", styles['Title']))
        elements.append(Paragraph(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
        elements.append(Paragraph(f"Organización: CODELCO / BHP", styles['Normal']))
        elements.append(Spacer(1, 20))

        # Tabla de Datos
        data = [['KPI', 'Valor', 'Estado'],
                ['Polvo PM10', '32 mg/m3', 'Bajo Control'],
                ['Gases', '12 ppm', 'Normal'],
                ['Nodos Activos', '69,870', '99.8%']]
        
        t = Table(data, colWidths=[150, 150, 150])
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        elements.append(t)
        elements.append(Spacer(1, 20))
        
        # Observaciones (Sin salirse del margen)
        elements.append(Paragraph("Observaciones Técnicas:", styles['Heading2']))
        elements.append(Paragraph(obs, styles['Normal']))
        
        elements.append(Spacer(1, 40))
        elements.append(Paragraph("__________________________", styles['Normal']))
        elements.append(Paragraph("Firma AIH-Master Jefe de Turno", styles['Normal']))

        doc.build(elements)
        buffer.seek(0)
        return buffer

    if st.button("💾 Generar y Validar PDF"):
        pdf = build_pdf()
        st.download_button("Descargar Reporte PDF Auditable", pdf, "Reporte_HSE_Oficial.pdf", "application/pdf")

st.divider()
st.markdown("🟢 **Sincronización Global Activa** | Bélgica - Chile - China")
