import unittest
import sys
from math import *

sys.path.append("../")
from utils.rpn_utils import *


def join_tokens(token_list):
    return " ".join([str(el) for el in token_list])


class ConversionTests(unittest.TestCase):

    def test_conversion(self):
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "+"), Token(Type.NUMBER, "3")]
        self.assertEqual(join_tokens(convert_to_rpn(sample)), "2 3 +")
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "+"), Token(Type.NUMBER, "3"),
                  Token(Type.OPERATOR, "-"), Token(Type.NUMBER, "4")]
        self.assertEqual(join_tokens(convert_to_rpn(sample)), "2 3 + 4 -")

    def test_priority(self):
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "+"), Token(Type.NUMBER, "2"),
                  Token(Type.OPERATOR, "*"), Token(Type.NUMBER, "2")]
        self.assertEqual(join_tokens(convert_to_rpn(sample)), "2 2 2 * +")
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "^"), Token(Type.NUMBER, "3"),
                  Token(Type.OPERATOR, "^"), Token(Type.NUMBER, "4")]
        self.assertEqual(join_tokens(convert_to_rpn(sample)), "2 3 4 ^ ^")
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "/"), Token(Type.NUMBER, "3"),
                  Token(Type.OPERATOR, "/"), Token(Type.NUMBER, "4")]
        self.assertEqual(join_tokens(convert_to_rpn(sample)), "2 3 / 4 /")

    def test_functions(self):
        sample = [FunctionToken("sin", sin), Token(Type.OPENING_BRACKET, "("), Token(Type.NUMBER, "2"),
                  Token(Type.CLOSING_BRACKET, ")")]
        self.assertEqual(join_tokens(convert_to_rpn(sample)), "2 sin")
        sample = [FunctionToken("pow", pow), Token(Type.OPENING_BRACKET, "("), Token(Type.NUMBER, "2"),
                  Token(Type.FUNC_DIVISOR, ","), Token(Type.NUMBER, "3"), Token(Type.CLOSING_BRACKET, ")")]
        self.assertEqual(join_tokens(convert_to_rpn(sample)), "2 , 3 pow")


class EvaluationTest(unittest.TestCase):

    def test_evaluation(self):
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "+"), Token(Type.NUMBER, "3")]
        self.assertEqual(evaluate_rpn(convert_to_rpn(sample)), 5)
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "+"), Token(Type.NUMBER, "3"),
                  Token(Type.OPERATOR, "-"), Token(Type.NUMBER, "4")]
        self.assertEqual(evaluate_rpn(convert_to_rpn(sample)), 1)
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "+"), Token(Type.NUMBER, "2"),
                  Token(Type.OPERATOR, "*"), Token(Type.NUMBER, "2")]
        self.assertEqual(evaluate_rpn(convert_to_rpn(sample)), 6)
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "^"), Token(Type.NUMBER, "3"),
                  Token(Type.OPERATOR, "^"), Token(Type.NUMBER, "4")]
        self.assertEqual(evaluate_rpn(convert_to_rpn(sample)), 2 ** 3 ** 4)
        sample = [Token(Type.NUMBER, "2"), Token(Type.OPERATOR, "/"), Token(Type.NUMBER, "3"),
                  Token(Type.OPERATOR, "/"), Token(Type.NUMBER, "4")]
        self.assertEqual(evaluate_rpn(convert_to_rpn(sample)), 2 / 3 / 4)
        sample = [FunctionToken("sin", sin), Token(Type.OPENING_BRACKET, "("), Token(Type.NUMBER, "2"),
                  Token(Type.CLOSING_BRACKET, ")")]
        self.assertEqual(evaluate_rpn(convert_to_rpn(sample)), sin(2))
        sample = [FunctionToken("pow", pow), Token(Type.OPENING_BRACKET, "("), Token(Type.NUMBER, "2"),
                  Token(Type.FUNC_DIVISOR, ","), Token(Type.NUMBER, "3"), Token(Type.CLOSING_BRACKET, ")")]
        self.assertEqual(evaluate_rpn(convert_to_rpn(sample)), pow(2, 3))


if __name__ == "__main__":
    unittest.main()
