import unittest

import pytest

from Plant.app.plant import Plant


class TestPlant(unittest.TestCase):
    def setUp(self):
        self.plant = Plant(100, 10, 910)

    def test_plant_atributes(self):

        self.assertEqual(100, self.plant.up_speed)
        self.assertEqual(10, self.plant.down_speed)
        self.assertEqual(910, self.plant.desired_height)

    def test_check_is_true(self):
        self.assertTrue(self.plant.up_speed)
        self.assertTrue(self.plant.down_speed)
        self.assertTrue(self.plant.desired_height)

    def test_speed_must_be_greater_than_5_or_less_than_1(self):

        with pytest.raises(ValueError) as ex:
            self.plant_exception = Plant(101, 10, 910)

        self.assertEqual(str(ex.value), 'Up Speed Invalid! Acima de 5 ou abaixo de 100')

    def test_speed_must_be_less_than_2_or_greater_than_speed_up(self):

        with pytest.raises(ValueError) as ex:
            self.plant_exception = Plant(100, 102, 910)

        self.assertEqual(str(ex.value), 'Down Speed Invalid! Acima de 2 ou abaixo do Up Speed!')

    def test_desired_height_must_be_greater_than_4_or_less_than_1000(self):

        with pytest.raises(ValueError) as ex:
            self.plant_exception = Plant(100, 10, 3)

        self.assertEqual(str(ex.value), 'Desired Height Invalid! Acima de 4 ou abaixo de 1000 apenas!')

    def test_is_arraived_in_desired_height_is_false(self):

        self.assertFalse(self.plant.is_arraived_in_desired_height())


