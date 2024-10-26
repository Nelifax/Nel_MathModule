from .Number import Number

class Irrational(Number):
    def __init__(self, value, flags):
        '''
        provides string-based class for irrational numbers. it will not calculate the references but will aply math functions to irrationals
        '''
        if isinstance(value, Number):
            super().__init__(value)
            self.__flags = self._Number__flags
            del(self._Number__flags)
            self.__flags['root() view'] = True
            self.__flags['parts as Number'] = True
