import unittest
from my_math_lib.geometry import circle_area, rectangle_area

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), 3.141592653589793)
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        with self.assertRaises(ValueError):
            rectangle_area(-1, 3)

if __name__ == '__main__':
    unittest.main()
