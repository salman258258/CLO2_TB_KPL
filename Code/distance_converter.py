# Simple code reuse: reuse existing functions (e.g., meter <-> kilometer)

def meters_to_kilometers(m):
    return m / 1000

def kilometers_to_meters(km):
    return km * 1000

def meters_to_centimeters(m):
    return m * 100

def centimeters_to_meters(cm):
    return cm / 100

def convert_distance(value, from_unit, to_unit):
    assert isinstance(value, (int, float)), "Value must be numeric"
    valid_units = ['m', 'km', 'cm']
    assert from_unit in valid_units, "Invalid from_unit"
    assert to_unit in valid_units, "Invalid to_unit"

    if from_unit == to_unit:
        return value

    # Reuse small functions
    if from_unit == 'm' and to_unit == 'km':
        return meters_to_kilometers(value)
    elif from_unit == 'km' and to_unit == 'm':
        return kilometers_to_meters(value)
    elif from_unit == 'm' and to_unit == 'cm':
        return meters_to_centimeters(value)
    elif from_unit == 'cm' and to_unit == 'm':
        return centimeters_to_meters(value)
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")