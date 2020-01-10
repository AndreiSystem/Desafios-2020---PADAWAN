import unittest

from Grumble.app.grumble import accum


class TestGrumble(unittest.TestCase):

    def test_accum(self):
        self.assertEqual(
            accum("ZpglnRxqenU"),
            "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
        )
        self.assertEqual(accum("RqaEzty"), "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")
        self.assertEqual(accum("cwAt"), "C-Ww-Aaa-Tttt")
