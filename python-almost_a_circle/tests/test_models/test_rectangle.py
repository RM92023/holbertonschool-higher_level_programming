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


if __name__ == '__main__':
    unittest.main()
