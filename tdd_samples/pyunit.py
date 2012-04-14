"""
Sample pyunit tests
"""

import unittest

# Here's our "unit".
def is_odd(number):
    """
    Returns true or false basing on parameter is odd or even
    """
    return number % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):
    """
    Unit tests for IsOdd class
    """

    def test_one(self):
        """
        One shoud be odd
        """
        self.failUnless(is_odd(1))

    def test_two(self):
        """
        Two should be tested as even
        """
        self.failIf(is_odd(2))

def main():
    """
    Test-running procedure
    """
    unittest.main()

if __name__ == '__main__':
    main()
