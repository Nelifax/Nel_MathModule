from NelMath.objects.math_base.Number import Number
from NelMath.objects.math_base.Rational import Rational

__all__ = ['Irrational']

class Irrational(Number):
    def __init__(self, value, degree=Rational(1), flags={}):
        '''
        provides string-based class for irrational numbers.
        '''
        if isinstance(value, Rational):
            super().__init__(value)
            self.__flags = self._Rational__flags
            del(self._Rational__flags)
            self.__flags['parts as Rational'] = True
            self.__flags['calculate value'] = True
            self.references['degree'] = degree
            self.__flags.update({'type': 'irrational'})
        else:
            self.__flags = {
            'all references': False,
            'max float part': 2,
            'parts as Rational': True,
            'calculate value': True,
            'type changing': True,
            'type': 'irrational',  
            'sign': '+',
            }

            self.references = {
            'integer part': '0',
            'float part': '0', 
            'degree':'1',
            }
            self.value=self.__flags['sign']+self.references['integer part']+'.'+self.references['float part']

    def print(self):
        deg=self.references['degree']
        print(f'Irrational with base {self.value}^{deg}')
            
            
            
