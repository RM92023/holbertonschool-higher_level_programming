import unittest
from models.base import Base



class TestBase(unittest.TestCase):

    
    def multiples_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

        b3 = Base()
        self.assertEqual(b1.id, b2.id, b3.id - 2)

        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

        self.assertEqual(20, Base().id)

if __name__ == '__main__':
    unittest.main()