def convert_temperature(value, from_unit, to_unit):
    assert isinstance(value, (int, float)), "Value must be numeric"
    assert from_unit in ['C', 'F', 'K'], "Invalid from_unit"
    assert to_unit in ['C', 'F', 'K'], "Invalid to_unit"

    if from_unit == to_unit:
        return value

    # Table-driven approach
    table = {
        ('C', 'F'): lambda c: c * 9/5 + 32,
        ('C', 'K'): lambda c: c + 273.15,
        ('F', 'C'): lambda f: (f - 32) * 5/9,
        ('F', 'K'): lambda f: (f - 32) * 5/9 + 273.15,
        ('K', 'C'): lambda k: k - 273.15,
        ('K', 'F'): lambda k: (k - 273.15) * 9/5 + 32,
    }

    func = table.get((from_unit, to_unit))
    if not func:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")
    return func(value)