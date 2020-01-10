import unittest

from DoubleSort.app.double_sort import DoubleSort


class TestDoubleSort(unittest.TestCase):

    def setUp(self):
        self.db_sort_1 = DoubleSort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2])
        self.db_sort_2 = DoubleSort(["Morango", "Kiwi", "Pessego", "7", 8, "3"])
        self.db_sort_3 = DoubleSort(["Fiat", "Gol", "7", "Yuri", "18", 3, "3"])

    def test_db_sort(self):

        self.assertEqual([0, 2, 2, "Apple", "Banana", "Mango", "Orange"],
                         self.db_sort_1.return_list_sort()
                         )

        self.assertEqual([8, "3", "7", "Kiwi", "Morango", "Pessego"],
                         self.db_sort_2.return_list_sort()
                         )

        self.assertEqual([3, "18", "3", "7", "Fiat", "Gol", "Yuri"],
                         self.db_sort_3.return_list_sort()
                         )
