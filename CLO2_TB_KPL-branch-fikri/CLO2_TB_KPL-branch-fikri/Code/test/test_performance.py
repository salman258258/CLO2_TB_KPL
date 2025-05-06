import time
import json
from service import BengkelAntrian

with open("config.json") as f:
    CONFIG = json.load(f)

def performance_test():
    antrian = BengkelAntrian(CONFIG)
    jumlah = 1000

    start = time.time()
    for i in range(jumlah):
        antrian.tambah_antrian(f"User{i}", "ringan")
    for _ in range(jumlah):
        antrian.proses_antrian()
    end = time.time()

    print(f"Performance Test untuk {jumlah} data selesai dalam {end - start:.4f} detik.")

if __name__ == "__main__":
    performance_test()