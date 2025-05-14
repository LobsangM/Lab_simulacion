# $(PYTHON) proyecto/main.py

# Configuración
PYTHON = python3
PIP = pip

# Comandos
.PHONY: run clean setup test shawn

# Inicializar entorno virtual e instalar dependencias
setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Ejecutar la simulación
run:
	$(PYTHON) main.py

# Eliminar archivos temporales y el entorno virtual
clean:
	rm -rf __pycache__ .pytest_cache
	rm -rf $(VENV)

# Instalar pygame (si no está en requirements.txt)
install-pygame:
	$(PIP) install pygame

# Ejecutar tests (si tienes)
test:
	$(PYTHON) -m pytest tests/

