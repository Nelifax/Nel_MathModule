__all__ = ['Fraction']

from NelMath.objects.math_base.Rational import Rational, MM_number_max_float_part
from NelMath.functions.number_functions import lcm, gcd
from .Math_object import Math_object

class Fraction(Rational):
    """
    provides class to operate with fractions
    can build fractions from whatever type of data: int|float|list|tuple|str. Best way - list|tuple:[numerator, denominator]
    """
    def __init__(self, value:any, flags:dict={}):
        if isinstance(value, Rational):
            value = value.value
        if type(value) != list and type(value) != tuple and '/' not in str(value) and '.' not in str(value).replace('.', '', 1):
            super().__init__(value)
            self.__flags = self._Rational__flags
            del(self._Rational__flags)
            self.__flags['auto-simplify'] = True
            self.__flags['float to numerator'] = True
            self.__flags['parts as Rational'] = True
            if self.references['float part'] == '0':
                self.references['numerator'] = Rational(self.references['integer part'])
                self.references['denominator'] = Rational('1')
            else:
                denominator = '1'
                while len(self.references['float part']) >= len(denominator):
                    denominator+='0'
                self.references['numerator'] = Rational(self.references['integer part']+self.references['float part'])
                self.references['denominator'] = Rational(denominator)            
            self.references['integer part'] = Rational(0)
            self.references.pop('float part')
            self.references['real value'] = Rational(0)
        else:
            self.__flags={
                'all references': False,
                'max float part': MM_number_max_float_part,
                'exponential view': False,
                'standart view': False,        
                'auto-simplify': True,
                'parts as Rational': True,
                'float to numerator': True,
                'type': 'integer',  
                'sign': '+',
            }
            self.references={
                'integer part': Rational('0'),
                'real value': Rational('0'),
                'numerator': Rational('0'),
                'denominator': Rational('1'),
            }
            if type(value)==str:
                if not value.replace('/','',1).replace('.', '', 2).replace('-', '', 2).isdigit():
                    raise TimeoutError()
                elif '/' in value:
                    value = value.split('/')
                for part in value:
                    if '.' in part.replace('.', '', 1).replace('-', '', 1):
                        raise TimeoutError()            
            if type(value)==list:
                if len(value)==1:
                    self.references['numerator']=Rational(value[0])
                    self.references['denominator']=Rational(1)
                elif len(value)==2:
                    if str(value[0]) == '' or str(value[1]) == '0':
                        raise TimeoutError
                    match(isinstance(value[0], Fraction), isinstance(value[1], Fraction)):
                        case(True, True):
                            value[0].improper_view()
                            value[1].improper_view()
                            self.references['numerator']=value[0].references['numerator']*value[1].references['denominator']
                            self.references['denominator']=value[1].references['numerator']*value[0].references['denominator']
                        case(True, False):                            
                            value[0].improper_view()
                            value=[value[0], Rational(value[1])]
                            self.references['numerator']=value[0].references['numerator']
                            self.references['denominator']=value[0].references['denominator']*value[1]
                        case(False, True):
                            value[1].improper_view()
                            value=[Rational(value[0]), value[1]]
                            self.references['numerator']=value[0]*value[1].references['denominator']
                            self.references['denominator']=value[1].references['numerator']
                        case _:
                            value=[Rational(value[0]), Rational(value[1])]
                            self.references['numerator']=value[0]
                            self.references['denominator']=value[1]   
            else:
                self.references['numerator'] = Rational(value[0])
                self.references['denominator'] = Rational(value[1])
        if flags!={}:
            for flag in flags:
                if flag not in self.__flags.keys():
                    raise TimeoutError()
        self.__flags.update(flags)
        self.standartize()
        self.simplify()        
        self.references['real value']=self.references['integer part'] + self.references['numerator']/self.references['denominator']
        if self.get_sign()=='-':
            self.references['real value']=-self.references['real value']
    
    def standartize(self)->'Fraction':
        while self.references['denominator'].references['float part']!='0' or self.references['numerator'].references['float part']!='0':
            self.references['denominator'] *= 10
            self.references['numerator'] *= 10
        if self.references['numerator']>self.references['denominator']:
            self.references['integer part'] = self.references['numerator']//self.references['denominator']
            self.references['numerator'] = self.references['numerator']-self.references['denominator']*self.references['integer part']
        if self.references['numerator']==self.references['denominator']:
            self.references['integer part']+=1
            self.references['numerator']=0
        if self.references['numerator']==0:
            return Rational(self.references['integer part'])
        if self.references['numerator']==self.references['denominator']:
            return Rational(self.references['integer part'])

    def improper_view(self)->'Fraction':
        if self.references['integer part']!=0:
            self.references['numerator']+=self.references['integer part']*self.references['denominator']
            self.references['integer part'] = 0     

    def __transform_mul(self, value)->'Fraction':
        self.references['numerator']*=value
        self.references['denominator']*=value

    def __transform_div(self, value)->'Fraction':
        self.references['numerator']/=value
        self.references['denominator']/=value

    def simplify(self)->'Fraction':
        fraction_gcd=gcd(self.references['numerator'], self.references['denominator'])
        if fraction_gcd!=1:
            self.references['numerator'] /= fraction_gcd 
            self.references['denominator'] /= fraction_gcd 
        else:
            return

    def __sign_invert(self):
        if self.__flags['sign']=='+':
            self.__flags['sign']='-'
        elif self.flags['sign']=='-':
            self.__flags['sign']='+'

    def __abs__(self):
        if self.__flags['sign'] == '-':
            return -self
        else:
            return self

    def copy(self)->'Fraction':
        self.improper_view()
        return Fraction([self.references['numerator'], self.references['denominator']], self.__flags)

    def get_sign(self):
        return self.__flags['sign']

    def __neg__(self):
        neg=self.copy()
        if neg.references['float part'] == '0' and neg.references['integer part'] == '0':
            if neg.get_sign() == '+':
                return neg          
        neg.__sign_invert()
        return neg
   
    def __mul__(self, other)->'Fraction':
        if isinstance(other, Fraction): 
            self.improper_view()
            other.improper_view()            
            if self.get_sign()==other.get_sign():
                return Fraction([self.references['numerator']*other.references['numerator'], self.references['denominator']*other.references['denominator']])
            else:
                return Fraction([self.references['numerator']*other.references['numerator'], self.references['denominator']*other.references['denominator']],{'sign':'-'})
        else:
            return self*Fraction(other)

    def __rmul__(self, other)->'Fraction':
        return self*other

    def __truediv__(self, other)->'Fraction':
        if isinstance(other, Fraction):            
            self.improper_view()
            other.improper_view()
            if self.get_sign()==other.get_sign():
                return Fraction([self.references['numerator']*other.references['denominator'], self.references['denominator']*other.references['numerator']])
            else:
                return Fraction([self.references['numerator']*other.references['denominator'], self.references['denominator']*other.references['numerator']],{'sign':'-'})
        else:
            return self/Fraction(other)

    def __rtruediv__(self, other) -> 'Rational':
        if isinstance(other, Fraction):            
            self.improper_view()
            other.improper_view()
            if self.get_sign()==other.get_sign():
                return Fraction([other.references['numerator']*self.references['denominator'], other.references['denominator']*self.references['numerator']])
            else:
                return Fraction([other.references['numerator']*self.references['denominator'], other.references['denominator']*self.references['numerator']],{'sign':'-'})
        else:
            return Fraction(other)/self

    def __add__(self, other)-> 'Fraction':
        if isinstance(other, Fraction):
            self.improper_view()
            other.improper_view()
            if self.references['denominator']==other.references['denominator']:
                if self.get_sign()==other.get_sign():
                    return Fraction([self.references['numerator']+other.references['numerator'], self.references['denominator']], {'sign':self.get_sign()})
                else:
                    numerator=Rational(self.references['numerator'],{'sign':self.get_sign()})+Rational(other.references['numerator'],{'sign':other.get_sign()})
                    return Fraction([numerator, self.references['denominator']],{'sign':numerator.get_sign()})
            else:
                fraction_lcm=lcm(self.references['denominator'], other.references['denominator'])
                self.__transform_mul(fraction_lcm/self.references['denominator'])
                other.__transform_mul(fraction_lcm/other.references['denominator'])
                if self.get_sign()==other.get_sign():
                    return Fraction([self.references['numerator']+other.references['numerator'], self.references['denominator']], {'sign':self.get_sign()})
                else:
                    numerator=Rational(self.references['numerator'],{'sign':self.get_sign()})+Rational(other.references['numerator'],{'sign':other.get_sign()})
                    return Fraction([numerator, self.references['denominator']],{'sign':numerator.get_sign()})
        else:
            return self+Fraction(other)

    def __radd__(self, other):
        return self+Fraction(other)

    def __sub__(self, other) -> 'Fraction':
        if isinstance(other, Fraction):
            self.improper_view()
            other.improper_view()
            if self.references['denominator']==other.references['denominator']:
                match(self.get_sign(), other.get_sign()):
                    case('-','-'):
                        if self.references['numerator']>other.references['numerator']:
                            return Fraction([self.references['numerator']-other.references['numerator'],self.references['denominator']],{'sign':'-'})
                        elif self.references['numerator']<other.references['numerator']:
                            return Fraction([other.references['numerator']-self.references['numerator'],self.references['denominator']],{'sign':'+'})
                        else: return Fraction(0)
                    case('+','+'):
                        if self.references['numerator']>other.references['numerator']:
                            return Fraction([self.references['numerator']-other.references['numerator'],self.references['denominator']],{'sign':'+'})
                        elif self.references['numerator']<other.references['numerator']:
                            return Fraction([other.references['numerator']-self.references['numerator'],self.references['denominator']],{'sign':'-'})
                        else: return Fraction(0)
                    case('-','+'):
                        return Fraction([self.references['numerator']+other.references['numerator'],self.references['denominator']],{'sign':'-'})
                    case('+','-'):
                        return Fraction([self.references['numerator']+other.references['numerator'],self.references['denominator']],{'sign':'+'})
            else:
                fraction_lcm=lcm(self.references['denominator'], other.references['denominator'])
                self.__transform_mul(fraction_lcm/self.references['denominator'])
                other.__transform_mul(fraction_lcm/other.references['denominator'])
                return self-other
        else:
            return self-Fraction(other)

    def __rsub__(self, other) -> 'Fraction':
        return Fraction(other)-self

    def __eq__(self, other:'Fraction')->bool:
        if self.numerator == other.numerator and self.denominator == other.denominator and self.integer==other.integer: 
            return True
        return False

    def __str__(self):
        sign=''
        if self.get_sign()=='-':
            sign='-'
        if self.references["numerator"]!=0 and self.references['numerator']!=self.references['denominator']:
            if self.references['integer part']==0:
                return f'{sign}{self.references["numerator"]}/{self.references["denominator"]}'
            else:    
                return f'{sign}({self.references["integer part"]}+{self.references["numerator"]}/{self.references["denominator"]})'
        else:
            return f'{sign}{self.references["integer part"]}'

    def __repr__(self):
        return self.__str__()

    def print(self):
        print(f'Fraction:{self.references["integer part"]}+{self.references["numerator"]}/{self.references["denominator"]}')
        print(f'With:\n Integer part={self.references["integer part"]}\n   And value={self.references["real value"]}')

    @staticmethod
    def build(periodic_float:str)->'Fraction':
        nonperiodic, periodic_part = periodic_float[0:-1].split('(')
        deg=10**len(periodic_part)
        nonperiodic=Rational(nonperiodic+periodic_part)
        periodic=Rational(Rational(nonperiodic).references['integer part'])
        return Fraction([nonperiodic*deg-periodic, deg-1])
