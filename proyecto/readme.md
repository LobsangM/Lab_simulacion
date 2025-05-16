# Simulación Gravitacional en Python

Este proyecto implementa una simulación visual basada en la gravitación clásica de cuerpos celestes. Utiliza **Python**, **Pygame** y principios de la física newtoniana para simular la atracción gravitacional entre planetas y lunas. Los parámetros físicos y visuales se configuran fácilmente a través de un archivo `config.yaml`.

> **Autores**: Lobsang y Shawn  
> **Curso**: Laboratorio de Simulación  
> **Lenguaje**: Python 3  
> **Entorno visual**: Pygame

---

## Características principales

- Cuerpos con masa y velocidad inicial generados aleatoriamente
- Cálculo de fuerzas gravitacionales entre todos los cuerpos
- Colisiones con fusión de masas (opcional)
- Añadir lunas a planetas (opcional)
- Visualización en tiempo real con formas y colores variados
- Configuración flexible desde un archivo `.yaml`

---

## Estructura del Proyecto

Laboratorio_de_simulacion/
├── venv/                               # Entorno virtual (fuera de 'proyecto')
├── proyecto/                           # Carpeta principal del proyecto
│ ├── main.py                           # Script principal que corre la simulación
│ ├── config.yaml                       # Archivo de configuración
│ ├── Makefile                          # Comandos útiles con make
│ ├── requirements.txt                  # Lista de dependencias
│ ├── README.md                         # Este documento
│ ├── processing/                       # Lógica principal del simulador
│ │ ├── init.py
│ │ ├── simulation.py                   # Clase Simulation
│ │ ├── objects.py                      # Definición de Planet y Moon
│ │ ├── physics.py                      # Lógica de gravedad y colisiones
│ │ └── utils.py                        # Clase Vector2D y utilidades
│ └── tests/                            # Pruebas unitarias
│ ├── init.py
│ ├── test_objects.py
│ ├── test_physics.py
│ └── test_utils.py


---

## Instalación

1. Abre una terminal en la carpeta `Las_simulacion/` (donde está `proyecto/`)
2. Crea y activa el entorno virtual:

```bash
make venv
source ../venv/bin/activate

Instala las dependencias:

make install


Corre la simulación con:

make run


Puedes personalizar los parámetros en el archivo proyecto/config.yaml, incluyendo:

Número de cuerpos celestes
Constante gravitacional
Dimensiones de la ventana
Distribuciones de masa, velocidad y posición
Opciones visuales (formas, colores, tamaño)
Activación de lunas y colisiones

El proyecto incluye pruebas unitarias con unittest. Puedes ejecutar pruebas individuales o todas:

make test_objects     # Testea objetos Planet y Moon
make test_physics     # Testea interacciones gravitacionales y colisiones
make test_utils       # Testea la clase Vector2D
make test_all         # Corre todos los tests


