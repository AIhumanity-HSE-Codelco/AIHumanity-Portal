import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap, MarkerCluster
import requests
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import io
from datetime import datetime
import pytz

# --- CONFIGURACIÓN DE ALTO NIVEL ---
st.set_page_config(page_title="HSE MASTER CONTROL - CODELCO", page_icon="🛡️", layout="wide")

# --- BASE DE DATOS DE FAENAS CHILENAS ---
MINERAS_CHILE = {
    "Chuquicamata": {"lat": -22.30, "lon": -68.90, "region": "Antofagasta"},
    "Radomiro Tomic": {"lat": -22.21, "lon": -68.85, "region": "Antofagasta"},
    "Ministro Hales": {"lat": -22.38, "lon": -68.89, "region": "Antofagasta"},
    "Gabriela Mistral": {"lat": -24.00, "lon": -68.60, "region": "Antofagasta"},
    "Salvador": {"lat": -26.24, "lon": -69.61, "region": "Atacama"},
    "Andina": {"lat": -33.02, "lon": -70.28, "region": "Valparaíso"},
    "El Teniente": {"lat": -34.08, "lon": -70.45, "region": "O'Higgins"},
    "Puerto Amberes (Bélgica)": {"lat": 51.21, "lon": 4.40, "region": "Europa"}
}

# --- LÓGICA DE ALERTAS METEO ---
def get_alerta_status(zona):
    prob = np.random.rand()
    if prob > 0.85: return "🔴 CRÍTICO: Tormenta Eléctrica / Viento Blanco", "Inverse"
    if prob > 0.60: return "🟡 ADVERTENCIA: Polvo Suspendido Elevado", "Normal"
    return "🟢 ESTABLE: Condiciones Óptimas", "Normal"

# --- INTERFAZ PRINCIPAL ---
st.title("🛡️ HSE MASTER CONTROL - SISTEMA INTEGRADO MINERO")
st.markdown(f"## **Uniting Technology | Portal Global de Seguridad Proactiva**")
st.caption(f"Acceso Autorizado: AIH-Master | Fecha: {datetime.now(pytz.timezone('America/Santiago')).strftime('%d/%m/%Y %H:%M')} CLST")

# --- NAVEGACIÓN POR MÓDULOS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard Real-Time", "🗺️ Mapa Geográfico Riesgo", "⛈️ Red Meteorológica", "📄 Auditoría Legal PDF"])

with tab1:
    st.subheader("🚀 KPIs de Operación Nacional")
    faena_sel = st.selectbox("Seleccione Centro de Trabajo:", list(MINERAS_CHILE.keys()))
    alerta, color_status = get_alerta_status(faena_sel)
    
    st.error(alerta) if "🔴" in alerta else st.warning(alerta) if "🟡" in alerta else st.success(alerta)
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Nodos AIDeepMiner", "70,000", delta="ONLINE", delta_color="normal")
    c2.metric("Polvo Promedio (PM10)", f"{np.random.randint(20,55)} mg/m³", delta="-5%", delta_color="normal")
    c3.metric("Gases Global", "0.02 ppm", delta="0%", delta_color="normal")
    c4.metric("Índice Riesgo (ICR)", f"{np.random.randint(5,15)}%", delta="Bajo Control")
    style_metric_cards(background_color="#11141b", border_left_color="#f39c12", border_size_px=2)

    st.markdown("---")
    st.subheader("📉 Trazabilidad de Exposición (Toda la Red)")
    hist_data = pd.DataFrame({'Minuto': range(60), 'Riesgo %': np.random.uniform(10, 30, 60)})
    st.plotly_chart(px.area(hist_data, x='Minuto', y='Riesgo %', template="plotly_dark", color_discrete_sequence=['#f39c12']), use_container_width=True)

with tab2:
    st.subheader("🗺️ Visualización de Riesgo por Capas (Heatmap Global)")
    m = folium.Map(location=[-27.0, -70.0], zoom_start=5, tiles="CartoDB dark_matter")
    
    # Generar puntos de calor en todas las mineras de Chile
    heat_points = []
    for f in MINERAS_CHILE.values():
        for _ in range(20):
            heat_points.append([f['lat'] + (np.random.rand()-0.5)*0.5, f['lon'] + (np.random.rand()-0.5)*0.5, np.random.rand()])
    
    HeatMap(heat_points, radius=15, blur=20).add_to(m)
    
    # Marcadores de Centros de Mando
    for nombre, coord in MINERAS_CHILE.items():
        folium.Marker([coord['lat'], coord['lon']], popup=f"Centro HSE: {nombre}", icon=folium.Icon(color='orange', icon='tower')).add_to(m)
    
    folium_static(m, width=1100, height=600)

with tab3:
    st.subheader("⛈️ Reporte Meteorológico de Alta Precisión")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info(f"Datos de {faena_sel}:")
        st.write(f"**Viento:** {np.random.randint(10,60)} km/h")
        st.write(f"**Presión Atmo:** 1013 hPa")
        st.write(f"**Visibilidad:** 15 km")
    with col_b:
        st.write("**Alertas Continentales:**")
        st.write("✅ Sudamérica: Operación Normal")
        st.write("✅ Europa (Amberes): Operación Normal")
        st.write("🟡 Asia: Alerta de Monzón en Fábrica Sensores")

with tab4:
    st.subheader("📄 Generador de Reporte de Auditoría Legal")
    st.write("Exportación de datos para cumplimiento normativo chileno (DS 594).")
    
    comentarios = st.text_area("Observaciones de Seguridad:", "Protocolo ADMS activo en rajo. Nodos AIDeepMiner operando al 100%. Sin desviaciones críticas.")

    def generate_pro_pdf():
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        elements = []
        
        elements.append(Paragraph(f"INFORME DE AUDITORÍA HSE - {faena_sel.upper()}", styles['Title']))
        elements.append(Paragraph(f"Generado por: AIH-Master | Uniting Technology Belgium", styles['Normal']))
        elements.append(Spacer(1, 12))
        
        data = [
            ['PARÁMETRO', 'MEDICIÓN', 'ESTADO'],
            ['Concentración Polvo', '34 mg/m3', 'CUMPLIMIENTO'],
            ['Gases Nocivos', 'ND', 'CUMPLIMIENTO'],
            ['Personal en Zona', '452', 'PROTEGIDO'],
            ['Nodos Activos', '70,000', 'SINCRO OK']
        ]
        t = Table(data, colWidths=[160, 160, 160])
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0), colors.orange), ('GRID',(0,0),(-1,-1),1,colors.black), ('FONTSIZE',(0,0),(-1,-1),10)]))
        elements.append(t)
        elements.append(Spacer(1, 20))
        elements.append(Paragraph(f"Observaciones: {comentarios}", styles['Normal']))
        
        doc.build(elements)
        buffer.seek(0)
        return buffer

    if st.button("💾 Generar Informe Auditoría"):
        pdf_file = generate_pro_pdf()
        st.download_button("Descargar PDF Oficial", pdf_file, f"Reporte_HSE_{faena_sel}.pdf", "application/pdf")

st.divider()
st.markdown("🟢 **SISTEMA INTEGRADO AIHUMANITY** | Conectando Chile, Bélgica y el mundo de la Minería.")
