import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from main import countWellFormedParenthesis

class TestWellFormedParenthesis(unittest.TestCase):
    def test_known_values(self):
        known = {
            0: 1,
            1: 1,
            2: 2,
            3: 5,
            4: 14,
            5: 42,
            6: 132,
            7: 429,
            8: 1430,
            9: 4862,
            10: 16796,
            15: 9694845
        }
        for n, result in known.items():
            self.assertEqual(countWellFormedParenthesis(n), result)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            countWellFormedParenthesis(-1)