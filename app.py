import os

# Intentamos localizar la carpeta exacta
escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
carpeta_apis = os.path.join(escritorio, "API'S")

print(f"--- AUDITORÍA DE RUTAS AIHUMANITY ---")
print(f"1. Buscando en Escritorio: {escritorio}")

if os.path.exists(carpeta_apis):
    print(f"✅ CARPETA DETECTADA: {carpeta_apis}")
    archivos = os.listdir(carpeta_apis)
    print(f"2. Archivos encontrados dentro: {archivos}")
else:
    print(f"❌ ERROR: No se encuentra la carpeta 'API'S' en el Escritorio.")
    print("Sugerencia: Revisa si el nombre tiene tilde (APÍS) o si está en OneDrive.")
