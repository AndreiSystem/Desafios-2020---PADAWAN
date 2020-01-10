import unittest

from OrderDesc.app.order_desc import desc_order


class TestDescOrder(unittest.TestCase):


    def test_descending_order(self):
        self.assertEqual(desc_order(21445), 54421)
        self.assertEqual(desc_order(145263), 654321)
        self.assertEqual(desc_order(123456789), 987654321)

