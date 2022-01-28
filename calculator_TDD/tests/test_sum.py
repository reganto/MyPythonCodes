from unittest import TestCase

from calculator import Calculator as calc


class TestSum(TestCase):
    def test_we_can_sum_two_integer_number(self):
        self.assertEqual(calc.sum(2, 3), 5)

    def test_we_can_sum_two_float_number(self):
        self.assertEqual(calc.sum(1.5, .5), 2)

    def test_sum_operation_of_a_number_and_a_not_number_should_throw_and_exception(self):
        with self.assertRaises(TypeError):
            self.assertEqual(calc.sum(2, 'a'), '2a')

    def test_sum_multiple_values(self):
        self.assertEqual(calc.sum(1, 3.5, 6), 10.5)