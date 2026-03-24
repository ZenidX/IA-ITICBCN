# Sesión de Asistencia con Snake en Pygame

## Resumen

Creación de un minijuego clásico Snake utilizando Python y la librería Pygame, demostrando capacidades de asistencia de código con LLM.

## Interacción

### 1. Inicio de Sesión
- Usuario inicia conversación en catalán: "Que tal? Màquina!"
- Asistente responde saludos y pregunta cómo ayudar

### 2. Exploración del Workspace
- Se listan los archivos del directorio de trabajo
- Se verifica el contenido del directorio `docs`
- Discusión breve sobre inconsistencias en la lista de archivos

### 3. Solicitud del Juego
- Usuario pregunta: "Eres capáz de hacer un minijuego en pygame?"
- Asistente ofrece varias opciones (Pong, Snake, Breakout, etc.)
- Usuario solicita específicamente Snake

### 4. Desarrollo del Juego

**Estructura del código implementado:**

```python
# Componentes principales
├── Snake (clase)
│   ├── reset() - Reinicia la serpiente
│   ├── cambiar_direccion() - Controla movimiento
│   ├── mover() - Actualiza posición
│   ├── crece() - Aumenta longitud
│   ├── choca_consigo() - Detección de colisiones internas
│   ├── choca_bordes() - Detección de bordes
│   └── dibujar() - Renderizado visual
├── Food (clase)
│   ├── aleatorizar_posicion() - Posición aleatoria
│   └── dibujar() - Renderizado de comida
└── Funciones auxiliares
    ├── mostrar_puntuacion()
    └── main() - Bucle principal del juego
```

**Configuración:**
- Ventana: 600x400 píxeles
- Cuadro: 20x20 píxeles
- Velocidad: 10 FPS
- Controles: WASD/Flechas + R (reiniciar) + Q (salir)

### 5. Depuración

**Error detectado:** El método `aleatorizar_posicion()` retornaba `None` en lugar de la coordenada.

**Solución:**
```python
# Antes:
def aleatorizar_posicion(...):
    while True:
        # ...
        self.posicion = (x, y)
        break

# Después:
def aleatorizar_posicion(...):
    while True:
        # ...
        return (x, y)
```

### 6. Ejecución

**Comando ejecutado:**
```bash
python snake.py
```

**Resultado:**
- Juego se ejecuta exitosamente
- Ventana de pygame se abre correctamente
- Advertencia de `pkg_resources` (no crítica, de librería pygame)

### 7. Controles del Juego

| Tecla | Acción |
|-------|--------|
| `W` / `↑` | Mover arriba |
| `S` / `↓` | Mover abajo |
| `A` / `←` | Mover izquierda |
| `D` / `→` | Mover derecha |
| `R` | Reiniciar juego al perder |
| `Q` | Salir del juego |

## Habilidades Demostradas

1. **Exploración de contexto**: Listado y navegación del workspace
2. **Gestión de dependencias**: Pygame como librería requerida
3. **Desarrollo de código completo**: Estructura OOP completa
4. **Detección de errores**: Identificación de `NoneType` exception
5. **Corrección de bugs**: Implementación del return correcto
6. **Ejecución exitosa**: Juego completamente funcional
7. **Documentación de interacción**: Transcripción completa de la sesión

## Salida del Juego

El juego muestra:
- Fondo negro
- Serpiente verde (cabeza verde oscuro)
- Comida roja
- Puntuación en esquina superior izquierda
- Pantalla de "GAME OVER" al perder
- Instrucciones de reinicio/escapar

---

**Fecha de sesión**: 2026-03-24  
**Archivo creado**: `SESION_SNAKE.md`  
**Estado**: ✅ Completado exitosamente
