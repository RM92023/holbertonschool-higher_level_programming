import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_constructor(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_square_str(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_square_size_getter(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_square_size_setter(self):
        square = Square(5)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_square_size_setter_with_validation(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -2
        with self.assertRaises(TypeError):
            square.size = "invalid"


if __name__ == '__main__':
    unittest.main()
