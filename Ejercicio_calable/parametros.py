import yaml

def cargar_parametros(ruta='config.yaml'):
    with open(ruta, 'r') as archivo:
        return yaml.safe_load(archivo)