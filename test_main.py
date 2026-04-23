import unittest

from main import addition, division, int_division, subtraction, multiplication, sqrt

class MainTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 1), 2)

    def test_division(self):
        self.assertEqual(division(4, 2), 2)
    def test_divide_by_zero(self):
        self.assertEqual(division(4, 0), 0)

    def test_negative_sqrt(self):
        self.assertEqual(sqrt(-9))

    def test_int_division(self):
        self.assertEqual(int_division(2, 3), 0)

    def test_multiplation(self):
         self.assertEqual(multiplication(4, 4), 16)

    def test_subtraction(self):
        self.assertEqual(subtraction(8, 2), 6)
    

if __name__ == "__main__":
        unittest.main()





