<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>AIH MASTER | DASHBOARD HSE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #050505; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; margin: 0; }
        .header-minero { border-bottom: 2px solid #ffcc00; padding: 15px; background: #111; }
        .grid-dashboard { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; padding: 20px; }
        
        /* CARD PRINCIPAL: ESTADO HSE */
        .card-hse { grid-column: span 2; background: #1a1a1a; border: 1px solid #333; padding: 30px; border-radius: 8px; text-align: center; }
        .status-box { display: inline-block; padding: 10px 40px; border: 3px solid #00ff00; color: #00ff00; font-size: 2.5rem; font-weight: bold; border-radius: 50px; margin-top: 10px; }
        
        /* CARDS DE SENSORES */
        .card-sensor { background: #1a1a1a; border-left: 6px solid #ffcc00; padding: 20px; border-radius: 5px; }
        .label { color: #888; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1.5px; margin-bottom: 5px; }
        .value { font-size: 3.5rem; font-weight: bold; color: #66fcf1; line-height: 1; }
        .unit { font-size: 1.2rem; color: #45a29e; margin-left: 5px; }

        /* ANIMACIÓN DE PULSO PARA CONECTIVIDAD */
        .dot { height: 12px; width: 12px; background-color: #007bff; border-radius: 50%; display: inline-block; margin-right: 10px; box-shadow: 0 0 8px #007bff; }
    </style>
</head>
<body>
    <div class="header-minero d-flex justify-content-between align-items-center">
        <h3 class="m-0" style="color: #ffcc00;">AIHUMANITY | CONTROL DE RIESGO PREVENTIVO</h3>
        <div class="text-info"><span class="dot"></span>SISTEMA ONLINE (TRL-3)</div>
    </div>

    <div class="grid-dashboard">
        <div class="card-hse">
            <p class="label">Estado de Alerta de Seguridad</p>
            <div id="hse-status" class="status-box">NORMAL</div>
        </div>

        <div class="card-sensor">
            <p class="label">Material Particulado MP10</p>
            <div class="value" id="val-mp10">42.5<span class="unit">µg/m³</span></div>
        </div>

        <div class="card-sensor">
            <p class="label">Material Particulado MP2.5</p>
            <div class="value" id="val-mp25">13.8<span class="unit">µg/m³</span></div>
        </div>

        <div class="card-sensor" style="border-left-color: #007bff;">
            <p class="label">Velocidad Viento</p>
            <div class="value" id="val-viento">18<span class="unit">km/h</span></div>
        </div>
        <div class="card-sensor" style="border-left-color: #ff4444;">
            <p class="label">Estabilidad Talud</p>
            <div class="value" id="val-talud" style="color: #ff4444;">OK</div>
        </div>
    </div>

    <script>
        // SIMULACIÓN DE DATOS PARA PRESENTACIÓN
        function updateSensors() {
            const mp10 = (40 + Math.random() * 10).toFixed(1);
            const mp25 = (10 + Math.random() * 5).toFixed(1);
            const viento = (15 + Math.random() * 10).toFixed(0);
            
            document.getElementById('val-mp10').innerHTML = mp10 + '<span class="unit">µg/m³</span>';
            document.getElementById('val-mp25').innerHTML = mp25 + '<span class="unit">µg/m³</span>';
            document.getElementById('val-viento').innerHTML = viento + '<span class="unit">km/h</span>';
        }
        setInterval(updateSensors, 3000);
    </script>
</body>
</html>
