#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

// --- DATOS DE TU RED ---
const char* ssid = "telenet 5E4ED";
const char* password = "WPJQbZnb9aHM";

// --- DIRECCIÓN DE TU PORTAL AIHUMANITY ---
const char* serverName = "https://aihumanity-app-aihumanity-hse.streamlit.app/api/data";

#define PIN_LED 2
#define PIN_LUZ 32
#define PIN_TEMP 26
#define PIN_IR 25
#define DHTTYPE DHT11

DHT dht(PIN_TEMP, DHTTYPE);

void setup() {
  Serial.begin(115200);
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_IR, INPUT);
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.println("Conectando a Telenet...");
  
  // Si sigue parpadeando aquí, acerca el ESP32 al Router
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(PIN_LED, !digitalRead(PIN_LED));
    delay(200);
  }
  
  digitalWrite(PIN_LED, HIGH); // LUZ AZUL FIJA = ÉXITO
  Serial.println("Conectado a Internet OK");
}

void loop() {
  if(WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    http.begin(serverName); // Redirección al portal
    http.addHeader("Content-Type", "application/json");

    // Datos reales de tus pines
    int luz = analogRead(PIN_LUZ);
    float t = dht.readTemperature();
    bool puesto = (digitalRead(PIN_IR) == LOW); 

    String json = "{\"node\":\"AID-01\",\"luz\":" + String(luz) + 
                  ",\"temp\":" + String(t) + ",\"puesto\":" + String(puesto) + "}";
    
    // El "Latido" azul al enviar
    digitalWrite(PIN_LED, LOW);
    int httpResponseCode = http.POST(json); 
    digitalWrite(PIN_LED, HIGH);
    
    Serial.println("Código Respuesta HTTP: " + String(httpResponseCode));
    http.end();
  }
  delay(2000); 
}
