# Import unittest and pytest as these are the dependencies to create our tests and run
import unittest
import pytest

from simple_calc import SimpleCalc


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    # Assertions to write our test cases
    # We will use our basic calculator example to write the tests first then the code

    # Naming convention is essential to have the test in the name of our method
    def test_add(self):
        # Checking if there is an add method, try to pass two ints, and does the outcome equals another int
        self.assertEqual(self.calc.add(3, 2), 5) # if True test would pass
        # return num1 + num2

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_multi(self):
        self.assertEqual(self.calc.multi(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
