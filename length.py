class Length:
    __metric = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344}

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def convert_to_meters(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            result = self.convert_to_meters() + other
        else:
            result = self.convert_to_meters() + other.convert_to_meters()
        return Length(result / Length.__metric[self.unit], self.unit)

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            result = self.convert_to_meters() + other
        else:
            result = self.convert_to_meters() + other.convert_to_meters()
        self.value = result / Length.__metric[self.unit]
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return str(self.convert_to_meters())

    def __repr__(self):
        return str((self.value, self.unit))


# Testing the class
if __name__ == "__main__":
    x = Length(1)
    x += Length(1)
    print("x in meters:", x)
    y = Length(1, "yd") + x
    print("y in meters:", y)
    print("Internal representation of y:", repr(y))
    x = x + 2
    print("x in meters:", x)
    x += 3.5
    print("x in meters:", x)
    z = 2 + x
    print("z in meters:", z)
