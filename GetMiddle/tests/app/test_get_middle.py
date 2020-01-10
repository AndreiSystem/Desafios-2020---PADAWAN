import unittest

from GetMiddle.app.get_middle import Kata


class TestKata(unittest.TestCase):
    def test_get_middle(self):
        kata = Kata()

        self.assertEqual('es', kata.get_middle('test'))
        self.assertEqual('t', kata.get_middle('testing'))
        self.assertEqual('A', kata.get_middle('A'))
        self.assertEqual('ol', kata.get_middle('bola'))

