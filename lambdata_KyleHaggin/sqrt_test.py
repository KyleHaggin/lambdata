import unittest
from sqrt import newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt


# This is the test file for my square root functions
# run this in terminal with python sqrt_test.py
# optionally you can do verbose mode by adding -v to that command


class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square roots!"""
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt1(2), 1.41421356237)


​class SquaringTests(unittest.TestCase):
    def test_thing(self):
        pass
​
if __name__ == '__main__':
    unittest.main()
