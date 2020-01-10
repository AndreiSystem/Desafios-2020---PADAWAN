import unittest

from CountSmile.app.count_smile import SmileFace


class TestSmileyFace(unittest.TestCase):
    def setUp(self):
        self.smile_face_class = SmileFace()


    def test_smile_face(self):

        self.assertEqual(self.smile_face_class.smile_face_check([' :) ', ';(', ';}', ':-D']), 2)
        self.assertEqual(self.smile_face_class.smile_face_check([';D', ':-(', ':-)', ';~)']), 3)
        self.assertEqual(self.smile_face_class.smile_face_check([';]', ':[', ';*', ':$', ';-D']), 1)
        self.assertEqual(self.smile_face_class.smile_face_check([':^)', ':-(', ':-)', ';~)']), 2)
        self.assertEqual(self.smile_face_class.smile_face_check([';|', ':{', ';*', ':#', ';+D']), 0)
        self.assertEqual(self.smile_face_class.smile_face_check([]), 0)

