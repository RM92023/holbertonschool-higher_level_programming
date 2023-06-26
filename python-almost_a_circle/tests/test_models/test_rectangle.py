import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def multiples_args(self):
        b1 = Rectangle()
        b2 = Rectangle()
        self.assertEqual(b1.id, b2.id - 1)

        b3 = Rectangle()
        self.assertEqual(b1.id, b2.id, b3.id - 2)

        b1 = Rectangle(None)
        b2 = Rectangle(None)
        self.assertEqual(b1.id, b2.id - 1)

        self.assertEqual(20, Rectangle().id)

    def test_rectangle_initialization(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNone(rect.id)

    def test_rectangle_width_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid", 10)
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_rectangle_height_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_rectangle_x_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -1)

    def test_rectangle_y_validation(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 0, "invalid")
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 0, -1)


if __name__ == '__main__':
    unittest.main()
