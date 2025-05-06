import unittest
from weight_converter import WeightConverterAutomata

class TestWeightConverter(unittest.TestCase):
    def setUp(self):
        self.converter = WeightConverterAutomata()

    def test_kg_to_lb(self):
        self.assertAlmostEqual(self.converter.convert(1, 'kg', 'lb'), 2.20462, places=5)
    def test_lb_to_kg(self):
        self.assertAlmostEqual(self.converter.convert(2.20462, 'lb', 'kg'), 1, places=5)