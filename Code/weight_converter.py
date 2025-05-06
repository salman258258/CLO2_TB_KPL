class WeightConverterAutomata:
    def __init__(self):
        # Automata-like state mapping
        self.states = {
            ('kg', 'lb'): self.kg_to_lb,
            ('lb', 'kg'): self.lb_to_kg,
            ('kg', 'g'): self.kg_to_g,
            ('g', 'kg'): self.g_to_kg
        }

    def convert(self, value, from_unit, to_unit):
        assert isinstance(value, (int, float)), "Value must be numeric"
        assert from_unit in ['kg', 'lb', 'g'], "Invalid from_unit"
        assert to_unit in ['kg', 'lb', 'g'], "Invalid to_unit"

        if from_unit == to_unit:
            return value

        transition = (from_unit, to_unit)
        if transition not in self.states:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

        return self.states[transition](value)

    def kg_to_lb(self, kg):
        return kg * 2.20462

    def lb_to_kg(self, lb):
        return lb / 2.20462

    def kg_to_g(self, kg):
        return kg * 1000

    def g_to_kg(self, g):
        return g / 1000