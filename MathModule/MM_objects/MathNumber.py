from MM_objects.Matrix import Matrix
from MM_objects.Fraction import MM_Fraction


class MathNumber():
    def __init__(self, value, flags:dict={}):
        self.value = value
        self.__flags = flags
        self.__matrix_view = Matrix(value)
        self.__fraction_view = Frac