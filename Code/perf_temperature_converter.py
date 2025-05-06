import time
from temperature_converter import convert_temperature

def performance_test():
    start = time.time()
    for _ in range(100000):
        convert_temperature(100, 'C', 'F')
    end = time.time()
    print(f"Temperature conversion 100,000x took {end - start:.4f} seconds")

if __name__ == "__main__":
    performance_test()