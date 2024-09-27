from objects.MathNumber import MathNumber


class Fraction(MathNumber):
    def __init__(self, value, flags:dict={}):
        self.value = value