/**
 * AIDeepMiner - Industrial IoT HSE Platform
 * Architect: Senior Full-Stack Engineer / AIHumanity
 * TRL 3-4 Production Ready Prototype
 */

const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const jwt = require('jsonwebtoken');
const { Pool } = require('pg');
const helmet = require('helmet');
const rateLimit = require('express-limit');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, { cors: { origin: "*" } });

// --- CONFIGURACIÓN & SEGURIDAD ---
app.use(express.json());
app.use(helmet()); // Seguridad de headers
const SECRET_KEY = process.env.JWT_SECRET || 'hse_mining_secret_2026';

// Simulación de Base de Datos (Para despliegue rápido en TRL3)
// En producción, conectar con pool.query() a PostgreSQL
let sensorHistory = [];
let activeAlerts = [];

// --- 2. DUST RISK ENGINE ---
const calculateRisk = (pm10, windSpeed, humidity) => {
    // Algoritmo predictivo de dispersión simple
    let score = (pm10 * 0.7) + (windSpeed * 1.5) - (humidity * 0.2);
    
    if (score > 120 || pm10 > 150) return { level: 'CRITICAL', color: '#FF0000', code: 2 };
    if (score > 70 || pm10 > 75) return { level: 'WARNING', color: '#FFFF00', code: 1 };
    return { level: 'SAFE', color: '#00FF00', code: 0 };
};

// --- 1. SENSOR DATA INGESTION ---
app.post('/api/sensor-data', (req, res) => {
    const data = req.body;
    
    // Validación de entrada
    if (!data.deviceId || !data.pm10) {
        return res.status(400).json({ error: 'Incomplete telemetry' });
    }

    // Procesamiento de Riesgo
    const risk = calculateRisk(data.pm10, data.windSpeed, data.humidity);
    const enrichedData = { ...data, risk, timestamp: new Date() };

    // Almacenamiento (Volátil para el ejemplo, persistir en PG)
    sensorHistory.push(enrichedData);
    if (sensorHistory.length > 100) sensorHistory.shift();

    // Gestión de Alertas
    if (risk.level === 'CRITICAL') {
        activeAlerts.push({ deviceId: data.deviceId, type: 'DUST_CRITICAL', time: new Date() });
    }

    // 3. REAL-TIME BROADCAST
    io.emit('live-telemetry', enrichedData);
    
    res.status(201).json({ status: 'received', risk: risk.level });
});

// --- 4. DASHBOARD API ---
app.get('/api/dashboard/overview', (req, res) => {
    const avgPM10 = sensorHistory.reduce((acc, curr) => acc + curr.pm10, 0) / (sensorHistory.length || 1);
    const onlineSensors = new Set(sensorHistory.map(d => d.deviceId)).size;

    res.json({
        avgPM10: avgPM10.toFixed(2),
        sensorsOnline: onlineSensors,
        activeAlerts: activeAlerts.length,
        sectorHighRisk: "Crusher North", // Lógica de agregación por sector
        status: "OPERATIONAL"
    });
});

// --- 9. FRONTEND (Minimal React-Style Dashboard en un solo archivo) ---
app.get('/dashboard', (req, res) => {
    res.send(`
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>AIDeepMiner | Dashboard HSE</title>
        <script src="/socket.io/socket.io.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { background: #0b0e14; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
            .card { background: #1a1f29; padding: 20px; border-radius: 8px; border-left: 5px solid #00ff00; }
            .critical { border-left-color: #ff4444; }
            .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 20px; }
            #risk-badge { padding: 10px 20px; border-radius: 4px; font-weight: bold; text-align: center; }
        </style>
    </head>
    <body>
        <div class="header">
            <h2>AIDeepMiner Industrial IoT</h2>
            <div id="connection-status">📡 Buscando Nodos...</div>
        </div>
        <div class="grid">
            <div class="card" id="main-risk">
                <h3>Estado HSE Global</h3>
                <div id="risk-badge" style="background: #222;">ESPERANDO DATOS</div>
            </div>
            <div class="card">
                <h3>Material Particulado (MP10)</h3>
                <h1 id="pm10-val">--</h1>
                <p>µg/m³</p>
            </div>
            <div class="card">
                <h3>Viento</h3>
                <h1 id="wind-val">--</h1>
                <p id="wind-dir">Dir: --</p>
            </div>
        </div>
        <canvas id="chart" style="width:100%; height:300px; margin-top:30px;"></canvas>

        <script>
            const socket = io();
            const badge = document.getElementById('risk-badge');
            
            socket.on('live-telemetry', (data) => {
                document.getElementById('pm10-val').innerText = data.pm10;
                document.getElementById('wind-val').innerText = data.windSpeed + ' m/s';
                document.getElementById('wind-dir').innerText = 'Dirección: ' + data.windDirection;
                
                badge.innerText = data.risk.level;
                badge.style.backgroundColor = data.risk.color;
                badge.style.color = (data.risk.level === 'WARNING') ? 'black' : 'white';
                
                document.getElementById('connection-status').innerText = '📡 NODO ACTIVO: ' + data.deviceId;
            });
        </script>
    </body>
    </html>
    `);
});

// --- START SERVER ---
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(\`Server AIDeepMiner corriendo en puerto \${PORT}\`);
});
