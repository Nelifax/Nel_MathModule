__all__ = ['Fraction']

class Fraction():
    def __init__(self, value, flags:dict={}):
        if type(value)==int:
            self.numerator = value
            self.denominator = 1
        elif type(value) == float:
            denominator = '1'
            value = str(value).rstrip('0').split('.')
            if len(value[1]) == 0:
                self.numerator = int(value[0])
                self.denominator = 1
            else:
                while len(denominator) <= len(value[1]):
                    denominator+='0'
                self.numerator = int(value[0])*int(denominator)+int(value[1])
                self.denominator = int(denominator)
        elif type(value) == str:
            if '/' in value:
                if '/' in value.replace('/','',1):
                    raise TimeoutError()
                value = value.split('/')
                if '.' in value[0] and '.' not in value[1]:
                    preFraction = Fraction(float(value[0]))/int(value[1])
                    self.numerator = preFraction.numerator
                    self.denominator = preFraction.denominator
                elif '.' not in value[0] and '.' in value[1]:
                    preFraction = Fraction(int(value[0]))/Fraction(float(value[1]))
                    self.numerator = preFraction.numerator
                    self.denominator = preFraction.denominator
                elif '.' in value[0] and '.' in value[1]:
                    preFraction = Fraction(float(value[0]))/Fraction(float(value[1]))                    
                    self.numerator = preFraction.numerator
                    self.denominator = preFraction.denominator
                else:
                    self.numerator = int(value[0])
                    self.denominator = int(value[1])
            elif '.' in value:
                if '.' in value.replace('.','',1):
                    raise TimeoutError()
                preFraction = Fraction(float(value))
                self.numerator = preFraction.numerator
                self.denominator = preFraction.denominator
        elif isinstance(value, Fraction):
            self.numerator = value.numerator
            self.denominator = value.denominator
        elif type(value) == list:
            if len(value) > 2 or len(value) == 0:
                raise TimeoutError()
            if len(value) == 1:
                preFraction = Fraction(value[0])
                self.numerator = preFraction.numerator
                self.denominator = preFraction.denominator
            elif type(value[0]) == int and type(value[1]) == int:
                self.numerator = value[0]
                self.denominator = value[1]
            elif isinstance(value[0], Fraction) and isinstance(value[1], Fraction):                
                preFraction = value[0]/value[1]
                self.numerator = preFraction.numerator
                self.denominator = preFraction.denominator

        self.value = self.numerator/self.denominator
        self.integer = self.numerator//self.denominator

            

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