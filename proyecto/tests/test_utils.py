import unittest
from processing.utils import Vector2D

class TestVector2D(unittest.TestCase):

    def test_addition(self):
        vec1 = Vector2D(1, 1)
        vec2 = Vector2D(2, 2)
        result = vec1 + vec2
        self.assertEqual(result.x, 3)
        self.assertEqual(result.y, 3)

    def test_multiplication(self):
        vec = Vector2D(1, 1)
        result = vec * 2
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 2)