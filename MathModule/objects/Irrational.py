from objects.Number import Number

class Irrational(Number):
    def __init__(self, value, flags):
        if isinstance(value, Number):
            super().__init__(value)