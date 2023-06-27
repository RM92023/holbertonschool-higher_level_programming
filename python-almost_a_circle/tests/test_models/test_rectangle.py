import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io


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

    def test_rectangle_display(self):
        rect = Rectangle(5, 3, 2, 1)
        expected_output = "#####\n#####\n#####\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_rectangle_str(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(rect), expected_output)

    def test_rectangle_update_with_args(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(2, 6, 7, 1, 4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_with_kwargs(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(id=2, width=6, height=7, x=1, y=4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_with_args_and_kwargs(self):
        rect = Rectangle(4, 5, 2, 3, 1)
        rect.update(2, width=6, height=7, y=4)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)


if __name__ == '__main__':
    unittest.main()
