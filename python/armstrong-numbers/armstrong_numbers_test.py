import unittest

from armstrong_numbers import is_armstrong


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class ArmstrongNumbersTest(unittest.TestCase):

    def test_single_digit_numbers_are_armstrong_numbers(self):
        self.assertTrue(is_armstrong(5))

    def test_there_are_no_two_digit_armstrong_numbers(self):
        self.assertFalse(is_armstrong(10))

    def test_three_digit_number_that_is_an_armstrong_number(self):
        self.assertTrue(is_armstrong(153))

    def test_three_digit_number_that_is_not_an_armstrong_number(self):
        self.assertFalse(is_armstrong(100))

    def test_four_digit_number_that_is_an_armstrong_number(self):
        self.assertTrue(is_armstrong(9474))

    def test_four_digit_number_that_is_not_an_armstrong_number(self):
        self.assertFalse(is_armstrong(9475))

    def test_seven_digit_number_that_is_an_armstrong_number(self):
        self.assertTrue(is_armstrong(9926315))

    def test_seven_digit_number_that_is_not_an_armstrong_number(self):
        self.assertFalse(is_armstrong(9926314))


if __name__ == '__main__':
    unittest.main()
