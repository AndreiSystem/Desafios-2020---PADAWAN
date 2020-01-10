import unittest

from FindShort.app.find_short import ShorterWord


class TestShorterWord(unittest.TestCase):

    def setUp(self):
        self.shorter_word_1 = ShorterWord('bitcoin take over the world maybe who knows perhaps')
        self.shorter_word_2 = ShorterWord('fui comprar pão e comprei café')
        self.shorter_word_3 = ShorterWord('Teste de palavra mais curta')

    def test_find_short(self):

        self.assertEqual(3, self.shorter_word_1.find_short())
        self.assertEqual(1, self.shorter_word_2.find_short())
        self.assertEqual(2, self.shorter_word_3.find_short())

