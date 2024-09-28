__all__ = ['Number']

global MM_number_max_float_part
MM_number_max_float_part = 10

class Number():
    def __init__(self, value:str|int|float, flags:dict={}):
        if type(value) == str:
            self.value = value.lstrip('0')
        else:
            self.value = str(value)
        self.__flags = flags

    def __add__(self, other)->'Number':
        if not isinstance(other, Number):
            other = Number(other)
        a = self.value[::-1]
        b = other.value[::-1]
        for i in range(0, min(len(a), len(b))+1):
            pass

