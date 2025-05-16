import unittest
from processing.physics import Celestialbodies
from processing.objects import Planet
from processing.utils import Vector2D

class TestCelestialbodies(unittest.TestCase):
    def setUp(self):
        self.engine = Celestialbodies()
        self.planet1 = Planet(1000, Vector2D(0, 0), Vector2D(0, 0))
        self.planet2 = Planet(1000, Vector2D(3, 4), Vector2D(0, 0))  # Distancia 5 unidades
        self.engine.add_planet(self.planet1)
        self.engine.add_planet(self.planet2)

    def test_gravity_applied(self):
        """Verifica que la gravedad modifique las velocidades"""
        initial_velocity = self.planet1.velocity.x
        self.engine.apply_gravity(1.0)
        self.assertNotEqual(self.planet1.velocity.x, initial_velocity)

    def test_collision_handling(self):
        """Verifica que dos planetas se combinen correctamente"""
        initial_count = len(self.engine.planets)
        self.engine.handle_collision(self.planet1, self.planet2)
        self.assertEqual(len(self.engine.planets), initial_count - 1)
        self.assertEqual(self.engine.planets[0].mass, 2000)

if __name__ == '__main__':
    unittest.main()
