cat <<EOF > /root/ai_humanity/app.py
from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Estado inicial
monitor = {"activo": False, "last_seen": 0, "mp10": 20.0}

@app.route('/api/update', methods=['POST'])
def update():
    global monitor
    data = request.get_json()
    monitor["mp10"] = data.get("mp10", 20.0)
    monitor["last_seen"] = time.time()
    monitor["activo"] = True
    return jsonify({"status": "ok"}), 200

@app.route('/api/status')
def status():
    # Si pasan más de 5 segundos sin recibir datos del ESP32, vuelve a rojo
    if time.time() - monitor["last_seen"] > 5:
        monitor["activo"] = False
    return jsonify(monitor)

@app.route('/')
def ui():
    return render_template_string("""
    <body style="background:#050505;color:white;text-align:center;padding-top:50px;font-family:sans-serif;">
        <h1>AIHUMANITY <span style="color:#666;">HSE LIVE</span></h1>
        <div id="btn" style="width:220px;height:220px;border-radius:50%;margin:20px auto;display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:bold;transition:0.3s;border:8px solid #222;">Cargando...</div>
        <div style="font-size:2rem;color:#00d4ff;">SENSOR IR: <span id="val">--</span></div>
        <script>
            async function poll() {
                try {
                    const r = await fetch('/api/status');
                    const d = await r.json();
                    const b = document.getElementById('btn');
                    b.style.background = d.activo ? (d.mp10 > 50 ? '#00ff00' : '#444') : '#ff0000';
                    b.style.boxShadow = d.activo ? (d.mp10 > 50 ? '0 0 50px #00ff00' : 'none') : '0 0 20px #ff0000';
                    b.innerText = d.activo ? (d.mp10 > 50 ? 'PELIGRO' : 'DESPEJADO') : 'DESCONECTADO';
                    document.getElementById('val').innerText = d.mp10;
                } catch(e) {}
            }
            setInterval(poll, 500); // Refresco ultra rápido cada medio segundo
        </script>
    </body>""")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
EOF
