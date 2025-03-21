# Date: 2025-03-20
# File: tarea2_particulas.py

class Particula:
    def __init__(self, nombre, masa, carga):
        self.nombre = nombre
        self.masa = masa
        self.carga = carga

    def informacion(self):
        return f"Partícula: {self.nombre}, Masa: {self.masa} kg, Carga: {self.carga} C"

class Electron(Particula):
    def __init__(self):
        super().__init__("Electrón", 9.109e-31, -1.602e-19)

    def giro(self):
        return "El electrón tiene un espín de ±1/2"

class Proton(Particula):
    def __init__(self):
        super().__init__("Protón", 1.673e-27, 1.602e-19)

    def interaccion_fuerte(self):
        return "El protón participa en la interacción nuclear fuerte."

class Neutron(Particula):
    def __init__(self):
        super().__init__("Neutrón", 1.675e-27, 0)

    def decaimiento_beta(self):
        return "El neutrón puede decaer en un protón, un electrón y un antineutrino."

# Instanciando
electron = Electron()
proton = Proton()
neutron = Neutron()

# Imprimiendo información de cada partícula
print(electron.informacion())  
print(electron.giro())         

print(proton.informacion())    
print(proton.interaccion_fuerte())  

print(neutron.informacion())   
print(neutron.decaimiento_beta())  
