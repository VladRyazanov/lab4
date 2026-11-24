import math
import unittest
import circle
import square


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_positive_int(self):
        self.assertAlmostEqual(circle.area(5), 78.53981633974483)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-5)

    def test_area_string_input(self):
        with self.assertRaises(TypeError):
            circle.area("5")

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_positive_int(self):
        self.assertAlmostEqual(circle.perimeter(5), 31.41592653589793)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(1.5), 3 * math.pi)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-3)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive_int(self):
        self.assertEqual(square.area(4), 16)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_area_large(self):
        self.assertEqual(square.area(10000), 100000000)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive_int(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)

    def test_perimeter_string_input(self):
        with self.assertRaises(TypeError):
            square.perimeter("4")


if __name__ == "__main__":
    unittest.main()