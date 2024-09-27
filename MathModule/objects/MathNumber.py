from objects.Matrix import Matrix
from objects.Fraction import Fraction


class MathNumber():
    def __init__(self, value, flags:dict={}):
        self.value = value
        self.__flags = flags
        self.__matrix_view = Matrix(value)
        self.__fraction_view = Frac