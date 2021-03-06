"""
Tests for default_operators.py
"""
import unittest
import sys

sys.path.append("../")
try:
    from data.default_operators import *
except Exception:
    raise


class OperatorsTest(unittest.TestCase):
    """
    Test for operators
    """
    def test_operators(self):
        """
        testing all operators to work fine
        """
        self.assertEqual(operators["+"](3, 2), 5)
        self.assertEqual(operators["-"](3, 2), 1)
        self.assertEqual(operators["*"](3, 2), 6)
        self.assertEqual(operators["/"](6, 2), 3)
        self.assertEqual(operators["//"](14, 5), 2)
        self.assertEqual(operators["%"](14, 5), 4)
        self.assertEqual(operators["**"](5, 2), 25)
        self.assertEqual(operators["^"](5, 2), 25)
        self.assertEqual(operators["~"](5), -5)
        self.assertEqual(operators["#"](5), 5)

        self.assertEqual(operators["=="](3, 3), True)
        self.assertEqual(operators["!="](3, 2), True)
        self.assertEqual(operators[">"](6, 2), True)
        self.assertEqual(operators["<"](2, 6), True)
        self.assertEqual(operators[">="](6, 2), True)
        self.assertEqual(operators[">="](2, 2), True)
        self.assertEqual(operators["<="](2, 6), True)
        self.assertEqual(operators["<="](2, 2), True)


if __name__ == "__main__":
    unittest.main()
