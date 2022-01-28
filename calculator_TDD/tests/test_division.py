from unittest import TestCase

from calculator import Calculator as calc


class TestDivision(TestCase):
    def test_two_integer_numbers_can_divide(self):
        self.assertEqual(calc.div(4, 2), 2)

    def test_two_float_numbers_can_divide_each_other(self):
        self.assertEqual(calc.div(14.5, 2), 7.25)

    def test_divison_by_zero_is_forbiden(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(calc.div(10, 0), 5)

    def test_division_multiple_value(self):
        self.assertEqual(calc.div(6, 2, .5), 6)