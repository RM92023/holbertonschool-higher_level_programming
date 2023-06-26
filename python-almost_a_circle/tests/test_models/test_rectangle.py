import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

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

    def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)
        rect.width = 10
        rect.height = 3
        self.assertEqual(rect.area(), 30)


if __name__ == '__main__':
    unittest.main()
