# 🛰️ AIHumanity - USB Master Gateway (TRL-4)
### Sistema de Extracción de Telemetría para ESP32 en Faena Minera

Este sistema permite la lectura de sensores MP10/2.5 y variables de taludes mediante conexión USB directa, eliminando la dependencia de redes WiFi inestables.

## 🚀 Ejecución en 2 Pasos
1. **Lanzar Extractor:** `python extractor.py` (Conecta el ESP32 al PC).
2. **Lanzar Dashboard:** `streamlit run dashboard.py` (Visualiza y descarga la data).

## 📊 Capacidades
* **Datalogging:** Guardado automático en `data_live.csv`.
* **Exportación:** Botón de descarga de reportes HSE.
* **Alta Visibilidad:** Interfaz diseñada para condiciones de luz extrema en rajo abierto.
