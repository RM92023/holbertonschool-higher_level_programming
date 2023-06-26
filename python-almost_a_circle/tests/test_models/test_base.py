import unittest
from models.base import Base

def test_no_arguments(self):
    b1 = Base()
    b2 = Base()
    self.assertEqual(b1.id, b2.id - 1)

def test_three_arguments(self):
    b1 = Base()
    b2 = Base()
    b3 = Base()
    self.assertEqual(b1.id, b2.id, b3.id - 2)

def test_none_id(self):
    b1 = Base(None)
    b2 = Base(None)
    self.assertEqual(b1.id, b2.id - 1)

def test_unique_id(self):
    self.assertEqual(20, Base().id)
