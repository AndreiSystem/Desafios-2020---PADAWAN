import unittest

from VowelCount.app.vowel_count import VowelCount


class TestVowel(unittest.TestCase):
    def setUp(self):
        self.vowel_count = VowelCount()

    def test_vowel_count(self):
        self.assertEqual(5, self.vowel_count.check_word("abracadabra"))
        self.assertEqual(3, self.vowel_count.check_word("modulo"))
        self.assertEqual(2, self.vowel_count.check_word("bola"))

