from cgitb import handler
from unittest import TestCase

from calculator import Calculator as calc


class MultiplyTestCase(TestCase):
    def test_multiply_two_integer_numbers(self):
        self.assertEqual(calc.mul(2, 3), 6)

    def test_multiply_two_float_numbers(self):
        self.assertEqual(calc.mul(2.2, 1.0), 2.2)

    def test_multiply_a_string_with_a_number(self):
        self.assertEqual(calc.mul(2, 'egg'), 'eggegg')

    def test_multiply_multiple_numbers(self):
        print(calc.mul(2, 3, 4))
        self.assertEqual(calc.mul(2, 3, 4), 24)