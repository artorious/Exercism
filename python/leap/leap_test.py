""" Tests for leap.py """
import unittest

from leap import is_leap_year


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0

class YearTest(unittest.TestCase):
    """ Test Cases for is_leap_year() """
    def test_year_not_divisible_by_4(self):
        """ Test provided year - not divisible by 4 """
        self.assertIs(is_leap_year(2015), False)

    def test_year_divisible_by_4_not_divisible_by_100(self):
        """ Test provided year - divisible by 4 but not by 100 """
        self.assertIs(is_leap_year(1996), True)

    def test_year_divisible_by_100_not_divisible_by_400(self):
        """ Test provided year - divisible by 100 but not by 400 """
        self.assertIs(is_leap_year(2100), False)

    def test_year_divisible_by_400(self):
        """ Test provided year - divisible by 400 """
        self.assertIs(is_leap_year(2000), True)

    def test_function_only_accepts_integers(self):
        """ Test provided year is a valid integer """
        with self.assertRaises(TypeError):
            is_leap_year('Two thousand eighteen')


if __name__ == '__main__':
    unittest.main()
