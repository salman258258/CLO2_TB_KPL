import unittest
from distance_converter import convert_distance

class TestDistanceConverter(unittest.TestCase):
    def test_km_to_m(self):
        self.assertEqual(convert_distance(1, 'km', 'm'), 1000)
    def test_m_to_km(self):
        self.assertEqual(convert_distance(500, 'm', 'km'), 0.5)