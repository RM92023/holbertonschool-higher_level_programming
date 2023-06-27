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

if __name__ == '__main__':
    unittest.main()
