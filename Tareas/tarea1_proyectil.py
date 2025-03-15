import math
import time
import pygame
import random
 
pygame.init()

# esta parte se comenta porque asi acepta varios proyectiles con números random 
#initial_angle = 45
#initial_speed = 70
#mass = 5
 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Launcher Simulator")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

g = 9.81  # Gravity
dt = 0.005  # Time step

#Hice la clase para que calcule cada proyectil de manera individua, lo que quiere decir es que cada bolita tendra una propia velocidad, angulo y masa a la hora de ejecutarse
class Proyectil:
    def __init__(self, velocidad, angulo, masa):
        self.velocidad = velocidad
        self.angulo = angulo
        self.masa = masa
        self.x = 50
        self.y = 50
        self.trayectoria = [(self.x, self.y)]
        self.vx = self.velocidad * math.cos(math.radians(self.angulo))
        self.vy = self.velocidad * math.sin(math.radians(self.angulo))
        
    # aca se actualiza la posicion del proyectil y su velocidad, se comenta la parte anterior del codigo
    #while x < WIDTH:
     #   x += vx * dt
      #  vy -= g * dt
       # y += vy * dt
        
        #if y <= 50:
         #   y = 50
          #  coef_rebote = coef_rebote_masa(mass)  # Obtener coef. según masa
           # vy = -vy * coef_rebote
    def actualizar(self):
        self.x += self.vx * dt
        self.vy -= g * dt
        self.y += self.vy * dt
        self.trayectoria.append((self.x, self.y))
# en general, actualiza todos los datos del proyectil, como la velocidad en y, velocidad en x, posicion en y...., entonces se guardan las nuevas posiciones del proyectil en una lista 

        if self.y >= HEIGHT - 50:
            return False
        return True
    #aca comprueba que toque el piso, al no haber rebote, la bolita cae completamente y para

    def convertir_coordenadas(self):
        return int(self.x), HEIGHT - int(self.y)

def main():
    running = True


    proyectiles = []
    #este valor se puede cambiar, yo puse 10 para que se vean varias
    for _ in range(10): 
        velocidad = random.randint(40, 100)
        angulo = random.randint(15, 75)
        masa = random.randint(1, 10)
        proyectiles.append(Proyectil(velocidad, angulo, masa))
    
    index = 0
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for p in proyectiles:
            if index < len(p.trayectoria):
                pygame.draw.circle(screen, RED, p.convertir_coordenadas(), p.masa * 2)
                p.actualizar()
        
        pygame.display.flip()
        time.sleep(dt/10)  

    pygame.quit()

if __name__ == "__main__":
    main()
