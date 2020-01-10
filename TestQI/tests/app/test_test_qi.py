import unittest

from TestQI.app.test_qi import iq_test


class TestTestQi(unittest.TestCase):

    def test_iq_test(self):
        self.assertEqual(iq_test("2 4 7 8 10"), 3)
        self.assertEqual(iq_test("1 1 1 2 3"), 4)
        self.assertEqual(iq_test("2 3 8 8 6"), 2)
        self.assertEqual(iq_test("1 4 7 8 10"), 1)
