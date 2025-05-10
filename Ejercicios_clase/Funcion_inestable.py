import random


def decorador(funcion,n=10):
    #ciclo de ejecucion
    def ciclo():
        for n in range(10): 
            try:
                funcion()
                break 
            except RuntimeError as e:
                print(f"Error: {e}. Reintentando...")
    return ciclo



@decorador
def funcion_inestable():
    if random.random() < 0.7:
        raise RuntimeError("Error aleatorio")
    print("Exito")

funcion_inestable()