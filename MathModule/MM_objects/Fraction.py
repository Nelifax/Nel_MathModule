from MM_objects.MathNumber import MathNumber


class MM_Fraction(MathNumber):
    def __init__(self, value, flags:dict={}):
        self.value = value