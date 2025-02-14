from NelMath.objects.math_base.Number import Number
from NelMath.objects.math_base.Rational import Rational
import re

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
            }
            parts = re.findall(r'\+*\-*\d*\^\d*', value)
            if parts == []:
                raise TimeoutError()
            if len(parts)==1:
                self.references['degree'] = Rational(parts[0].split('^')[1])
                self.references['base'] = Rational(parts[0].split('^')[0])
                if self.__flags['calculate value']:
                    self.value=pow(self.references['base'], self.references['degree'])
                return
  
            else:
                self.references['irrational parts'] = []
            for part in parts:
                value=value.replace(part, '')
                self.references['irrational parts'].append(Irrational(part))
            if value!='':
                raise TimeoutError() 
            
            
