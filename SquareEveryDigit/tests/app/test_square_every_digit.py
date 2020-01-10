import unittest

from SquareEveryDigit.app.square_every_digit import squared


class TestSquare(unittest.TestCase):

    def test_square_digits(self):
        self.assertEqual(squared(9119), 811181)
        self.assertEqual(squared(9), 81)
        self.assertEqual(squared(0), 0)
