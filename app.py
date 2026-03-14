# 💎 AIDeepMiner | Industrial HSE Ecosystem
> **TRL 3-4 Prototype** - Sistema de monitoreo ambiental preventivo para minería (Codelco/BHP).

---

## 🖥️ Interfaz del Software
| Dashboard Operativo | Análisis de Riesgo |
| :--- | :--- |
| ![Preview](https://via.placeholder.com/600x350/0b0e14/00d4ff?text=AIDeepMiner+Live+Dashboard) | ![Status](https://via.placeholder.com/600x350/0b0e14/ff4444?text=Critical+Dust+Alert+System) |

### 🚀 Funcionalidades Clave
* **Monitoreo Real-Time:** Ingestión de datos vía WebSockets (PM10, PM2.5, Viento).
* **Risk Engine:** Algoritmo predictivo de dispersión de polvo.
* **UI Industrial:** Diseño de alto contraste para visibilidad en terreno.
* **Gestión Offline:** Buffer de datos para zonas con baja conectividad.

---

## 🛠️ Stack Tecnológico
* **Backend:** Python 3.10 + Flask + SocketIO
* **Frontend:** HTML5, CSS3 (Flexbox/Grid), Chart.js
* **Hardware:** ESP32 (AIDeepMiner Node)
* **Servidor:** DigitalOcean Droplet (Ubuntu 22.04)

---

## 📦 Instalación Rápida
```bash
# Clonar repositorio
git clone [https://github.com/tu-usuario/AIDeepMiner-Portal.git](https://github.com/tu-usuario/AIDeepMiner-Portal.git)

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en modo desarrollo
python app.py
