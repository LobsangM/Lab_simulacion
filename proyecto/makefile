# Configuración
PYTHON = python3
PIP = pip
VENV = venv
VENV_DIR = $(VENV)/bin/$(PYTHON)

# Comandos
.PHONY: run test_objects test_physics test_utils activate lint

#crear un entorno virtual
create:
	$(PYTHON) -m venv $(VENV)
	@echo "Entorno virtual creado en $(VENV)"

#ejecutar el entorno virtual
activate:
	@echo "Activando el entorno virtual..."
	@echo "Ejecuta 'source $(VENV_DIR)' para activar el entorno virtual"
	@echo "Ejecuta 'make deactivate' para desactivar el entorno virtual"

# Desactivar el entorno virtual
deactivate:
	@echo "Desactivando el entorno virtual..."
	@echo "Ejecuta 'deactivate' para desactivar el entorno virtual"

# Limpiar archivos temporales
clean:
	@echo "Limpiando archivos temporales..."
	@rm -rf __pycache__/
	@rm -rf $(VENV)
	@echo "Archivos temporales eliminados"


# Instalar dependencias
install:
	$(PIP) install -r requirements.txt

# Ejecutar el archivo main.py de la simualación
run:
	$(PYTHON) main.py

# Ejecutar los tests individuales
test_objects:
	$(PYTHON) -m unittest tests/test_objects.py

test_physics:
	$(PYTHON) -m unittest tests/test_physics.py

test_utils:
	$(PYTHON) -m unittest tests/test_utils.py

# Ejecutar todos los tests
test_all:
	$(PYTHON) -m unittest discover -s tests

# Ejecutar chequeos estáticos

lint:
	$(PYTHON) -m pylint .
	$(PYTHON) -m flake8 *.py
	$(PYTHON) -m mypy *.py
