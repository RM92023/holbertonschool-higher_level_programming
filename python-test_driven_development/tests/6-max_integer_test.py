import unittest
"""Define a test in file 6-max-integers"""


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Adding functions to test"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40, -50]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 10, -15, 20, -25]), 20)
        self.assertEqual(max_integer([0, 10, -5, 15, 5]), 15)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-3, -3, -3, -3, -3]), -3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 2.1, 0.9]), 3.2)
        self.assertEqual(max_integer([-1.5, -2.7, -3.2, -2.1, -0.9]), -0.9)

if __name__ == '__main__':
    unittest.main()


