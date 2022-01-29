import unittest
from fractions import Fraction

from my_sum import sum


class TestSum(unittest.TestCase):
    # def setUp(self):
    #     print("execute before each test method")

    # def tearDown(self):
    #     print("execute after each test method")

    def test_list_int(self):
        """
        Sum list of integers
        """
        
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_float(self):
        """
        Sum list of floats
        """
        
        data = [1.1, 2.4, 3.5]
        result = sum(data)
        self.assertEqual(result, 7)

    def test_a_tuple(self):
        """
        Sum of tupel elements
        """

        data = (1, 2, 3)
        result = sum(data)
        self.assertEqual(result, 6)

    def test_a_set(self):
        """
        Sum of set elements
        """

        data = {1, 2, 3}
        result = sum(data)
        self.assertEqual(result, 6)

    def test_single_value_in_seq(self):
        """
        Sum for single value in sequence
        """

        data = [1]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_list_fraction(self):
        """
        Sum of fractions
        """
        
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


def test_suite_one():
    suite = unittest.TestSuite()
    suite.addTest(TestSum('test_list_int'))
    suite.addTest(TestSum('test_list_float'))
    return suite


def test_suite_two():
    suite = unittest.TestSuite()
    suite.addTest(TestSum('test_a_tuple'))
    suite.addTest(TestSum('test_a_set'))
    return suite

def test_suite_three():
    suite = unittest.TestSuite()
    suite.addTest(TestSum('test_list_fraction'))
    suite.addTest(TestSum('test_single_value_in_seq'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite_three())
