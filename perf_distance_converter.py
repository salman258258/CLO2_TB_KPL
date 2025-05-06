import time
from distance_converter import convert_distance

def performance_test():
    start = time.time()
    for _ in range(100000):
        convert_distance(1000, 'm', 'km')
    end = time.time()
    print(f"Distance conversion 100,000x took {end - start:.4f} seconds")

if __name__ == "__main__":
    performance_test()