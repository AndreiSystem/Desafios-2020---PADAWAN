import unittest

from Plant.app.garden import Garden
from Plant.app.plant import Plant


class TestGarden(unittest.TestCase):

    def test_growing_up_return_10(self):
        p = Plant(100, 10, 910)
        g = Garden(p)

        self.assertEqual(10, g.growing_up())

    def test_growing_up_return_1(self):
        p = Plant(10, 9, 4)
        g = Garden(p)

        self.assertEqual(1, g.growing_up())

    def test_growing_up_return_8(self):
        p = Plant(90, 30, 500)
        g = Garden(p)

        self.assertEqual(8, g.growing_up())

    def test_growing_up_return_26(self):
        p = Plant(50, 15, 900)
        g = Garden(p)

        self.assertEqual(26, g.growing_up())




