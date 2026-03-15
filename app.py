cat <<EOF > /root/ai_humanity/app.py
from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Estado persistente
monitor = {"activo": False, "last_seen": 0, "valor": 20.0}

@app.route('/api/update', methods=['POST'])
def update():
    global monitor
    data = request.get_json()
    monitor["valor"] = data.get("mp10", 20.0)
    monitor["last_seen"] = time.time()
    monitor["activo"] = True
    return jsonify({"status": "ok"}), 200

@app.route('/api/status')
def status():
    # Si pasan más de 4 segundos sin datos, consideramos pérdida de enlace
    is_online = (time.time() - monitor["last_seen"]) < 4
    return jsonify({
        "activo": is_online,
        "valor": monitor["valor"],
        "color": "#00ff00" if monitor["valor"] > 50 else "#444"
    })

@app.route('/')
def ui():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AIHUMANITY HSE</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { background: #0a0a0a; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, sans-serif; text-align: center; margin: 0; overflow: hidden; }
            .container { height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; }
            #indicator { 
                width: 280px; height: 280px; border-radius: 50%; 
                display: flex; flex-direction: column; align-items: center; justify-content: center;
                transition: all 0.15s ease-in-out; border: 10px solid #1a1a1a;
                box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
            }
            .status-label { font-size: 0.8rem; letter-spacing: 2px; margin-bottom: 5px; color: #888; }
            .value-label { font-size: 3.5rem; font-weight: bold; }
            .unit { font-size: 1rem; color: #666; }
            #status-text { margin-top: 20px; font-weight: bold; letter-spacing: 1px; }
            .grid { position: absolute; width: 100%; height: 100%; background-image: radial-gradient(#222 1px, transparent 1px); background-size: 30px 30px; z-index: -1; opacity: 0.5; }
        </style>
    </head>
    <body>
        <div class="grid"></div>
        <div class="container">
            <h2 style="color:#00d4ff; margin-bottom:40px;">SISTEMA DE ALERTA TEMPRANA HSE</h2>
            <div id="indicator">
                <span class="status-label">NIVEL RIESGO</span>
                <span id="val" class="value-label">--</span>
                <span class="unit">TRL3 SENSOR IR</span>
            </div>
            <div id="status-text">ESPERANDO NODO...</div>
        </div>

        <script>
            async function update() {
                try {
                    const r = await fetch('/api/status');
                    const d = await r.json();
                    const ind = document.getElementById('indicator');
                    const valTxt = document.getElementById('val');
                    const statusTxt = document.getElementById('status-text');

                    valTxt.innerText = d.valor;

                    if (!d.activo) {
                        ind.style.background = '#330000';
                        ind.style.borderColor = '#ff0000';
                        ind.style.boxShadow = '0 0 40px #ff0000';
                        statusTxt.innerText = '⚠️ NODO DESCONECTADO';
                        statusTxt.style.color = '#ff0000';
                    } else if (d.valor > 50) {
                        ind.style.background = '#003300';
                        ind.style.borderColor = '#00ff00';
                        ind.style.boxShadow = '0 0 60px #00ff00';
                        statusTxt.innerText = '🛡️ DETECCIÓN ACTIVA';
                        statusTxt.style.color = '#00ff00';
                    } else {
                        ind.style.background = '#111';
                        ind.style.borderColor = '#444';
                        ind.style.boxShadow = 'none';
                        statusTxt.innerText = '✅ CAMINO DESPEJADO';
                        statusTxt.style.color = '#888';
                    }
                } catch(e) {}
            }
            setInterval(update, 200); // Sensibilidad extrema: 5 veces por segundo
        </script>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
EOF
