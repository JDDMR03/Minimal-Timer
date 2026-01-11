# Terminal Timer CLI (Python 3.12)

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)

Un temporizador de terminal de alto impacto visual diseñado con una arquitectura modular y optimizado para entornos Linux (Arch Linux). Este proyecto implementa renderizado de arte ASCII dinámico y gestión de estados cromáticos mediante secuencias ANSI.

## 🛠️ Especificaciones Técnicas

### Arquitectura de Software
El proyecto sigue una separación estricta de responsabilidades (SoC):

* main.py: Orquestador del ciclo de vida, gestión del loop de eventos y señales de usuario (KeyboardInterrupt).
* src/logic.py: Motor de cálculo. Implementa funciones puras para parsing de tiempo, lógica de barra de progreso y transformaciones de segundos a componentes H:M:S.
* src/ui.py: Capa de presentación. Gestiona la limpieza selectiva del buffer, detección de dimensiones de terminal (shutil) y renderizado de matrices ASCII.
* src/constants.py: Almacén central de activos estáticos, incluyendo el mapa de bits para los dígitos ASCII y constantes de color ANSI.

### Características del Stack
- Versión: Python 3.12.
- Visualización: Feedback visual mediante umbrales de color (Verde > 50%, Amarillo > 20%, Rojo < 20%).
- UI Adaptativa: El centrado y los márgenes se recalculan dinámicamente en cada frame según el tamaño de la ventana.

## 🚀 Instalación y Uso

### Ejecución Directa
1. Clonar el repositorio:
   ```
   git clone https://github.com/tu-usuario/terminal-timer.git
   ```
2. Entrar al directorio:
   ```
   cd terminal-timer
   ```
3. Ejecutar:
   ```
   python main.py
   ```

### Compilación en Arch Linux (Binario Nativo)
Para generar un binario independiente en Arch Linux utilizando PyInstaller:

1. Instalar PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Generar el ejecutable:
   ```
   pyinstaller --onefile --name "t-timer" main.py
   ```

3. Instalación en el sistema:
   ```
   sudo cp dist/t-timer /usr/local/bin/
   ```

## ⚙️ Estructura del Proyecto
```
.
├── main.py              # Entrada principal
├── src/
│   ├── constants.py     # Colores y fuentes ASCII
│   ├── logic.py         # Cálculos matemáticos
│   └── ui.py            # Renderizado de pantalla
└── README.md
```
