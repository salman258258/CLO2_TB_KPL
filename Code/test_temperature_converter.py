import unittest
from temperature_converter import convert_temperature

class TestTemperatureConverter(unittest.TestCase):
    def test_c_to_f(self):
        self.assertAlmostEqual(convert_temperature(0, 'C', 'F'), 32)
    def test_f_to_c(self):
        self.assertAlmostEqual(convert_temperature(32, 'F', 'C'), 0)
    def test_c_to_k(self):
        self.assertAlmostEqual(convert_temperature(100, 'C', 'K'), 373.15)