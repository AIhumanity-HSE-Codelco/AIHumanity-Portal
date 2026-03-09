#include <WiFi.h>
#include <WebServer.h>

// --- CONFIGURACIÓN DE RED ---
const char* ssid = "Debbie HSE";
const char* password = "12345678"; 
const int buttonPin = 4; // PIN 4 y GND

WebServer server(80);

// --- INTERFAZ DE ESTADO PERMANENTE ---
const char* htmlContent = R"=====(
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { margin: 0; background: #800080; color: white; font-family: sans-serif; 
               display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        #box { width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; 
               background-color: #800080; transition: background 0.1s; }
        h1 { font-size: 5rem; margin: 0; text-transform: uppercase; }
    </style>
</head>
<body onclick="activarAudio()">
    <div id="box"><h1>MARJAN</h1></div>

    <script>
        const words = [
            {t: "WATER", c: "#0040FF"}, {t: "DEBBIE", c: "#FF0080"},
            {t: "JUF", c: "#FFFF00"}, {t: "APPEL", c: "#00FF00"},
            {t: "PIJN", c: "#FF0000"}, {t: "PAPA", c: "#FF8000"}
        ];

        let audioListo = false;
        function activarAudio() { audioListo = true; }

        function cambiarPalabra() {
            const item = words[Math.floor(Math.random() * words.length)];
            const box = document.getElementById('box');
            
            box.style.backgroundColor = item.c;
            box.innerHTML = `<h1>${item.t}</h1>`;
            
            if(audioListo) {
                const msg = new SpeechSynthesisUtterance(item.t);
                msg.lang = 'nl-NL';
                window.speechSynthesis.speak(msg);
            }
        }

        setInterval(() => {
            fetch('/status').then(r => r.text()).then(data => {
                if(data === "1") cambiarPalabra();
            });
        }, 40);
    </script>
</body>
</html>
)=====";

volatile bool pulsado = false;

void setup() {
    pinMode(buttonPin, INPUT_PULLUP);
    WiFi.softAP(ssid, password);
    
    server.on("/", []() {
        server.send(200, "text/html", htmlContent);
    });

    server.on("/status", []() {
        if(pulsado) {
            server.send(200, "text/plain", "1");
            pulsado = false;
        } else {
            server.send(200, "text/plain", "0");
        }
    });

    server.begin();
}

void loop() {
    server.handleClient();

    // Reacciona al cerrar el botón (contacto físico)
    if (digitalRead(buttonPin) == LOW) {
        pulsado = true;
        // Se queda aquí hasta que suelte el botón para evitar cambios infinitos
        while(digitalRead(buttonPin) == LOW) {
            server.handleClient();
            delay(10);
        }
    }
}
