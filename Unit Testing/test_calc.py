import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self): # name should start with test
        self.assertEqual(calc.add(12, -1), 11)
        self.assertEqual(calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(12, -1), 13)
        self.assertEqual(calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(12, -1), -12)
        self.assertEqual(calc.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(-10, 2), -5)
        self.assertAlmostEqual(calc.divide(2.4, 12), 0.2, 2)

        # check exception
        # method 1
        self.assertRaises(ValueError, calc.divide, 10, 0)
        # method 2
        with self.assertRaises(ValueError):
            calc.divide(109, 0)

if __name__ == "__main__":
    unittest.main()