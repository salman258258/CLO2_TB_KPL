import json
from temperature_converter import convert_temperature
from distance_converter import convert_distance
from weight_converter import WeightConverterAutomata

# Load config
with open('config.json') as f:
    config = json.load(f)

print("=== Temperature Conversion ===")
temp = convert_temperature(100, 'C', 'F')
print(f"100 Celsius to Fahrenheit: {temp}")

print("\n=== Distance Conversion ===")
dist = convert_distance(1, 'km', 'm')
print(f"1 Kilometer to Meter: {dist}")

print("\n=== Weight Conversion ===")
converter = WeightConverterAutomata()
result = converter.convert(70, 'kg', 'lb')
print(f"70 kg to lb: {result}")