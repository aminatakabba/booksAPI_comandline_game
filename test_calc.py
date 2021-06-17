import unittest
import test2


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test2.add(10, 5), 15)
        self.assertEqual(test2.add(-1, 1), 0)
        self.assertEqual(test2.add(-1, -1), -2)