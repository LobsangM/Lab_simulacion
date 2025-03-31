from abc import ABC
from abc import abstractmethod
from math import pi 
from math import pow

class CuerpoCeleste(ABC):
    def __init__(self, nombre, masa, radio, coordenadas):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.coordenadas = coordenadas

        @abstractmethod
        def info(self):
            pass
        
        
class luna(CuerpoCeleste):
    def __init__(self, nombre, masa, radio, coordenadas):
        super().__init__(nombre, masa, radio, coordenadas)
        self.luna = []

class planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, radio, coordenadas, luna):
        super().__init__(nombre, masa, radio, coordenadas)
        self.luna = luna

    def info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Masa: {self.masa}")
        print(f"Radio: {self.radio}")
        print(f"Coordenadas: {self.coordenadas}")
        #print("\n")

    def gravedad(self):
        return (6.674 * pow(10, -11) * self.masa) / pow(self.radio, 2)
    
    def cantidad_lunas(self):
        return len(self.luna)
    

# Para la tierra
if __name__ == "__main__":

    luna_satelite = luna(nombre="Luna", masa= 7.349e22, radio=1737.4, coordenadas=(0.1, 0.2, 0.3))    
    tierra = planeta(nombre="Tierra", masa=5.972e24, radio=6371*10e2, coordenadas=(0, 0, 0), luna=[luna_satelite])
    
    #print(f"Información de la Tierra: {tierra.info()}")   
    tierra.info()
    print(f"La gravedad del planeta es: {tierra.gravedad()} m/s^2")
    print(f"Número total de lunas: {tierra.cantidad_lunas()}")