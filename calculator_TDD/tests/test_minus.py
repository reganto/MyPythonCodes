from typing import Type
from unittest import TestCase

from calculator import Calculator as calc


class MinusTestCase(TestCase):
    def test_minus_two_integer_numbers(self):
        self.assertEqual(calc.minus(4, 2), 2)

    def test_minus_two_float_numbers(self):
        self.assertEqual(calc.minus(6.3, 2.3), 4)

    def test_minus_a_string_value_from_a_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calc.minus('foo', 3), 3)

    def test_minus_multiple_numbers(self):
        self.assertEqual(calc.minus(4, 2, 1), 1)