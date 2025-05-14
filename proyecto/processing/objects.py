import pygame
from .utils import Vector2D, random_color, random_shape
import random


class PhysicalProperties:
    def __init__(self, mass: float, position: Vector2D, velocity: Vector2D):
        self._mass = mass   
        self._position = position   
        self._velocity = velocity  

    @property
    def mass(self):
        return self._mass

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity


class GraphicalProperties:
    def __init__(self, color: tuple, size: int, shape: str):
        self.color = color
        self.size = size
        self.shape = shape

    def draw(self, surface):
        pos_tuple = (int(self.position.x), int(self.position.y))  # Convertir Vector2D a tupla
        if self.shape == "circle":
            pygame.draw.circle(surface, self.color, pos_tuple, self.size)
        elif self.shape == "square":
            pygame.draw.rect(surface, self.color, (pos_tuple[0], pos_tuple[1], self.size * 2, self.size * 2))
        elif self.shape == "triangle":
            points = [
                (pos_tuple[0], pos_tuple[1] - self.size),
                (pos_tuple[0] - self.size, pos_tuple[1] + self.size),
                (pos_tuple[0] + self.size, pos_tuple[1] + self.size)
            ]
            pygame.draw.polygon(surface, self.color, points)


class Planet(PhysicalProperties, GraphicalProperties):
    def __init__(self, mass, position, velocity):
        color = random_color()
        size = int(mass ** (1/3) * 1)  # Relación masa-tamaño ------------------ Aqui podemos cambiarle el tamaño
        shape = random_shape()
        
        PhysicalProperties.__init__(self, mass, position, velocity)
        GraphicalProperties.__init__(self, color, size, shape)
        self.moons = []

    @classmethod
    def from_config(cls, config):
        dist_cfg = config["planet"]

        # Masa
        mass_cfg = dist_cfg["mass"]
        if mass_cfg["type"] == "normal":
            mass = random.gauss(mass_cfg["mean"], mass_cfg["stddev"])
            mass = max(min(mass, mass_cfg["max"]), mass_cfg["min"])
        else:
            raise ValueError("Tipo de distribución de masa no soportado")

        # Posición
        pos_cfg = dist_cfg["position"]
        if pos_cfg["type"] == "uniform":
            x = random.uniform(pos_cfg["x_min"], pos_cfg["x_max"])
            y = random.uniform(pos_cfg["y_min"], pos_cfg["y_max"])
        else:
            raise ValueError("Tipo de distribución de posición no soportado")
        position = Vector2D(x, y)

        # Velocidad
        vel_cfg = dist_cfg["velocity"]
        if vel_cfg["type"] == "uniform":
            vx = random.uniform(vel_cfg["vx_min"], vel_cfg["vx_max"])
            vy = random.uniform(vel_cfg["vy_min"], vel_cfg["vy_max"])
        else:
            raise ValueError("Tipo de distribución de velocidad no soportado")
        velocity = Vector2D(vx, vy)

        return cls(mass, position, velocity)
    
    def add_moon(self, moon):
        self.moons.append(moon)

    def __str__(self):
        return f"Planeta - Masa: {self.mass}, Posición: {self.position}, Velocidad: {self.velocity}"

    def update(self, bodies, gravity, dt, screen_width=800, screen_height=800):
        for moon in self.moons:
            dx = moon.position.x - self.position.x
            dy = moon.position.y - self.position.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            force = gravity * self.mass * moon.mass / (distance ** 2)
            fx = force * (dx / distance)
            fy = force * (dy / distance)
            moon._velocity = moon._velocity + Vector2D(fx / moon.mass, fy / moon.mass)
        self._position = self._position + self._velocity * dt


class Moon(PhysicalProperties, GraphicalProperties):
    def __init__(self, mass, position, velocity, orbit_center: Planet):
        color = random_color()
        size = int(mass ** (1/3) * 1) # Relación masa-tamaño ------------------ Aqui podemos cambiarle el tamaño
        shape = random_shape()

        super().__init__(mass, position, velocity)
        GraphicalProperties.__init__(self, color, size, shape)
        self.orbit_center = orbit_center

    def update(self, dt, gravity, bodies, screen_width=800, screen_height=800):
        dx = self.orbit_center.position.x - self.position.x
        dy = self.orbit_center.position.y - self.position.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        force = gravity * self.mass * self.orbit_center.mass / (distance ** 2)
        fx = force * (dx / distance)
        fy = force * (dy / distance)
        self._velocity = self._velocity + Vector2D(fx / self.mass, fy / self.mass)
        self._position = self._position + self._velocity * dt
