# --- LÓGICA DE INTERVENCIÓN PROACTIVA ---
if temp > 35: # Umbral crítico de estrés térmico en mina
    st.error("🚨 ALERTA DE ESTRÉS TÉRMICO: Protocolo de Hidratación Activado.")
    
if not puesto:
    st.warning("⚠️ VIOLACIÓN DE SEGURIDAD: Operario sin Casco Detectado en Nodo 1.")

# --- BOTÓN DE CONSULTA PROFUNDA ---
if st.button("🔍 ESCANEO PREDICTIVO DE SEGURIDAD"):
    with st.spinner("IA analizando patrones de riesgo..."):
        # La IA ahora evalúa no solo el dato, sino la seguridad industrial
        prompt_tecnico = f"""
        Como experto HSE, evalúa: Temperatura {temp}°C (Límite 32°C), 
        Luz {luz}lx (Mínimo 500lx), EPP: {puesto}. 
        Dame 3 puntos de acción inmediata para el supervisor.
        """
        # ... (Tu llamada al client.chat.completions.create que ya configuramos)
