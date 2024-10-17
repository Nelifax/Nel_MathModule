__all__ = ['Fraction']

from objects.Number import Number, MM_number_max_float_part

class Fraction(Number):
    """
    provides class to operate with fractions
    can build fractions from whatever type of data: int|float|list|tuple|str. Best way - list|tuple:[numerator, denominator]
    """
    def __init__(self, value:any, flags:dict={}):
        if isinstance(value, Number):
            value = value.value
        if type(value) != list and type(value) != tuple and '/' not in str(value) and '.' not in str(value).replace('.', '', 1):
            super().__init__(value)
            self.__flags = self._Number__flags
            del(self._Number__flags)
            self.__flags['auto-simplify'] = True
            self.__flags['float to numerator'] = True
            self.__flags['parts as Number'] = True
            if self.references['float part'] == '0':
                self.references['numerator'] = Number(self.references['integer part'])
                self.references['denominator'] = Number('1')
            else:
                denominator = '1'
                while len(self.references['float part']) >= len(denominator):
                    denominator+='0'
                self.references['numerator'] = Number(self.references['integer part']+self.references['float part'])
                self.references['denominator'] = Number(denominator)
            #self.simplify()
        else:
            self.__flags={
                'all references': False,
                'max float part': MM_number_max_float_part,
                'exponential view': False,
                'standart view': False,        
                'auto-simplify': True,
                'parts as Number': True,
                'float to numerator': True,
                'type': 'integer',  
                'sign': '+',
            }
            self.references={
                'integer part': '0',
                'float part': '0',
                'numerator': '0',
                'denominator': '1',
            }
            if type(value)==str:
                if not value.replace('/','',1).replace('.', '', 2).replace('-', '', 2).isdigit():
                    raise TimeoutError()
                elif '/' in value:
                    value = value.split('/')
                for part in value:
                    if '.' in part.replace('.', '', 1).replace('-', '', 1):
                        raise TimeoutError()
            if value[1] == '' or value[1] == '0':
                raise TimeoutError
            self.references['numerator'] = Number(value[0])
            self.references['denominator'] = Number(value[1])
            '''
            self.simplify()
            value = self.references['numerator']/self.references['denominator']
            self.value = value.value
            self.references['integer part'] = value.references['integer part']
            self.references['float part'] = value.references['float part']
            '''


        

            

    def transform_mul(fraction:'Fraction', value)->'Fraction':
        return Fraction([fraction.numerator*value, fraction.denominator*value])

    def transform_div(fraction:'Fraction', value)->'Fraction':
        return Fraction([fraction.numerator/value, fraction.denominator/value])

    def simplify(fraction)->'Fraction':
        return Fraction(str(fraction.numerator)+'/'+str(fraction.denominator))

    def __mul__(self, other)->'Fraction':
        if isinstance(other, Fraction):
            print(self.numerator)
            print(self.denominator)
            print(other.numerator)
            print(other.denominator)
            return Fraction([self.numerator*other.numerator, self.denominator*other.denominator])
        else:
            return self*Fraction(other)

    def __truediv__(self, other)->'Fraction':
        if isinstance(other, Fraction):
            return Fraction([self.numerator*other.denominator, self.denominator*other.numerator])
        else:
            return self/Fraction(other)

    def __add__(self, other)->'Fraction':
        if isinstance(other, Fraction):
            return Fraction([self.numerator*other.denominator+other.numerator*self.denominator, self.denominator*other.denominator])
        else:
            return self+Fraction(other)

    def __eq__(self, other:'Fraction')->bool:
        if self.numerator == other.numerator and self.denominator == other.denominator and self.integer==other.integer: 
            return True
        return False

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def print(self):
        print(f'Fraction:{self.numerator}/{self.denominator}')
        print(f'With:\n Integer part={self.integer}\n   And value={self.value}')