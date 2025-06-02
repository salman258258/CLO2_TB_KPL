import unittest
import json
from service import BengkelAntrian

with open("config.json") as f:
    CONFIG = json.load(f)

class TestBengkelAntrian(unittest.TestCase):

    def setUp(self):
        self.antrian = BengkelAntrian(CONFIG)

    def test_tambah_antrian(self):
        result = self.antrian.tambah_antrian("Andi", "ringan")
        self.assertEqual(result, "Andi ditambahkan ke antrian ringan.")
    
    def test_kerusakan_tidak_valid(self):
        result = self.antrian.tambah_antrian("Budi", "parah")
        self.assertEqual(result, "Jenis kerusakan tidak dikenal.")

    def test_proses_antrian(self):
        self.antrian.tambah_antrian("Citra", "berat")
        result = self.antrian.proses_antrian()
        self.assertIn("Citra", result)

if __name__ == "__main__":
    unittest.main()