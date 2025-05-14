from processing.utils import Vector2D
import unittest

class TestVector2D(unittest.TestCase):

    def test_initialization(self):
        v = Vector2D(3, 4)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4)

    def test_addition(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        result = v1 + v2
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 6)

    def test_multiplication(self):
        v = Vector2D(2, 3)
        result = v * 1.5
        self.assertEqual(result.x, 3.0)
        self.assertEqual(result.y, 4.5)

