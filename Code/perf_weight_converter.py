import time
from weight_converter import WeightConverterAutomata

def performance_test():
    converter = WeightConverterAutomata()
    start = time.time()
    for _ in range(100000):
        converter.convert(70, 'kg', 'lb')
    end = time.time()
    print(f"Weight conversion 100,000x took {end - start:.4f} seconds")

if __name__ == "__main__":
    performance_test()