#!/usr/bin/python3
""" test module for base """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class CheckNumbers(unittest.TestCase):
    """ tests for base class """

    def test_id_as_positive(self):
        test_instance = Base(24)
        self.assertEqual(test_instance.id, 24)
