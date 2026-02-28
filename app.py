<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uniting Technology | AIHumanity Master</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Montserrat', sans-serif; }
        .hero-bg {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                        url('https://images.unsplash.com/photo-1578319439584-104c94d37305?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-900">

    <nav class="flex items-center justify-between px-10 py-6 bg-white shadow-sm sticky top-0 z-50">
        <div class="text-2xl font-bold text-blue-800 tracking-tighter">UNITING <span class="text-gray-500">TECHNOLOGY</span></div>
        <div class="hidden md:flex space-x-8 font-medium text-sm uppercase tracking-widest">
            <a href="#" class="hover:text-blue-600">Home</a>
            <a href="#servicios" class="hover:text-blue-600">Servicios HSE</a>
            <a href="#nodos" class="hover:text-blue-600">70K Nodos</a>
            <a href="#contacto" class="bg-blue-700 text-white px-5 py-2 rounded hover:bg-blue-800 transition">Contacto</a>
        </div>
    </nav>

    <header class="hero-bg h-[80vh] flex items-center justify-center text-center text-white px-4">
        <div class="max-w-4xl">
            <h1 class="text-5xl md:text-7xl font-bold mb-6">Predictive Risk Modeling</h1>
            <p class="text-xl md:text-2xl font-light mb-10 text-gray-300 italic">
                Transformando 70,000 puntos de datos en seguridad proactiva para CODELCO & BHP.
            </p>
            <div class="flex flex-col md:flex-row justify-center gap-4">
                <a href="#servicios" class="bg-blue-600 hover:bg-blue-700 px-8 py-4 rounded-full font-bold transition">Nuestros Modelos (ICR)</a>
                <a href="#nodos" class="border border-white hover:bg-white hover:text-black px-8 py-4 rounded-full font-bold transition">Tecnología SP32</a>
            </div>
        </div>
    </header>

    <section id="servicios" class="py-20 px-10 bg-white">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-blue-600 font-bold tracking-widest uppercase mb-2 text-sm">Protocolo AIH-Master</h2>
                <p class="text-4xl font-bold">Diagnóstico > Modelo > Intervención</p>
            </div>

            <div class="grid md:grid-cols-3 gap-12">
                <div class="p-8 border-t-4 border-blue-600 shadow-xl rounded-lg bg-gray-50">
                    <div class="text-blue-600 mb-4 text-3xl">📊</div>
                    <h3 class="text-xl font-bold mb-3">Modelos de Riesgo (ICR)</h3>
                    <p class="text-gray-600 text-sm leading-relaxed">Cálculo de Indicadores de Condición de Riesgo en tiempo real mediante análisis multivariable de entorno.</p>
                </div>
                <div class="p-8 border-t-4 border-blue-600 shadow-xl rounded-lg bg-gray-50">
                    <div class="text-blue-600 mb-4 text-3xl">📡</div>
                    <h3 class="text-xl font-bold mb-3">Sensores & Biometría</h3>
                    <p class="text-gray-600 text-sm leading-relaxed">Monitoreo crítico de polvo, gases y fatiga del operador mediante integración de nodos SP32 escalables.</p>
                </div>
                <div class="p-8 border-t-4 border-blue-600 shadow-xl rounded-lg bg-gray-50">
                    <div class="text-blue-600 mb-4 text-3xl">🛡️</div>
                    <h3 class="text-xl font-bold mb-3">HSE Predictivo</h3>
                    <p class="text-gray-600 text-sm leading-relaxed">Intervención automatizada antes del incidente. Seguridad proactiva diseñada para minería de rajo y subterránea.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="nodos" class="py-20 bg-slate-900 text-white px-10">
        <div class="max-w-5xl mx-auto flex flex-col md:flex-row items-center gap-10">
            <div class="md:w-1/2 text-center md:text-left">
                <h2 class="text-3xl font-bold mb-6 underline decoration-blue-500">Escalabilidad: 70k Nodos</h2>
                <p class="text-gray-400 mb-6 leading-relaxed">
                    Actualmente en fase <strong>TRL3</strong>, nuestra infraestructura está preparada para la transición masiva. Partiendo del nodo SP32, estamos diseñando el ecosistema AIDEEPMINERS para una cobertura total.
                </p>
                <ul class="text-sm space-y-3">
                    <li class="flex items-center"><span class="text-blue-400 mr-2">✓</span> Baja latencia en malla (Mesh)</li>
                    <li class="flex items-center"><span class="text-blue-400 mr-2">✓</span> Resistencia a condiciones extremas</li>
                    <li class="flex items-center"><span class="text-blue-400 mr-2">✓</span> Integración nativa con sistemas CODELCO/BHP</li>
                </ul>
            </div>
            <div class="md:w-1/2 grid grid-cols-2 gap-4">
                <div class="bg-slate-800 p-6 rounded text-center">
                    <div class="text-4xl font-bold text-blue-500">70K</div>
                    <div class="text-xs uppercase mt-2">Nodos Planificados</div>
                </div>
                <div class="bg-slate-800 p-6 rounded text-center">
                    <div class="text-4xl font-bold text-green-500">TRL3</div>
                    <div class="text-xs uppercase mt-2">Estado de Desarrollo</div>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-white py-10 border-t text-center">
        <p class="text-gray-400 text-xs tracking-widest uppercase">© 2026 Uniting Technology | AIHumanity Master Architecture</p>
    </footer>

</body>
</html>
