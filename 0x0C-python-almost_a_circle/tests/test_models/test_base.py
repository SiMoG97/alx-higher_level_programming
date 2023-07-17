#!/usr/bin/python3
"A module that tests Base Class"
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_1_init_with_id(self):
        base1 = Base(15)
        self.assertEqual(base1.id, 15)


if __name__ == "__main__":
    unittest.main()
