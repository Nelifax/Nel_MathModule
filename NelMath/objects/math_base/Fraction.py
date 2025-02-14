__all__ = ['Fraction']

from NelMath.objects.math_base.Rational import Rational
from NelMath.objects.math_base.Number import Number
from NelMath.functions.number_functions import lcm, gcd
from NelMath.properties.settings_handler import SettingsHandler

class Fraction(Number):
    """
    provides class to operate with fractions
    can build fractions from whatever type of data: int|float|list|tuple|str. Best way - list|tuple:[numerator, denominator]
    """    
    def __new__(cls, value, flags={}):
        settings=SettingsHandler()
        if ('type changing' in flags and flags['type changing']) or ('type changing' not in flags and settings.get('mm_dynamic_class_changing')):            
            instance = ''
            if type(value)==tuple or type(value)==list:
                value=list(value)
            else:
                value=[value]
            if len(value)==1:
                if type(value[0])==str and Number.is_rational(value):
                    instance = super().__new__(Number, value[0], flags)
                else:                    
                    instance = super().__new__(cls, value, flags)
            else:
                if value[1]=='1' or value[1]==1 or value[1]==1.0:                
                    instance = super().__new__(Number, value[0], flags)
                div=Rational(value[0], {'type changing':False})/Rational(value[1])
                if div.references['float part']=='0':
                    instance = super().__new__(Number, div, flags)
            if instance == '':
                instance = super().__new__(cls, value, flags)
        else:
            instance = super().__new__(cls, value, flags)
        return instance
    
    def __init__(self, value:any, flags:dict={}):
        self.sign='+'
        if type(value)==list and len(value)==1:
            value=value[0]
        self.__flags=Number._check_flags(flags, 'Fraction')   
        self.references={
                'integer part': Rational('0'),
                'numerator': Rational('0'),
                'denominator': Rational('1'),
            }
        if Number.is_rational(value): 
            value=Rational(value)
            if value.references['float part'] == '0':
                self.references['numerator'] = Rational(value.references['integer part'])
                self.references['denominator'] = Rational('1')
            else:
                denominator = '1'
                while len(value.references['float part']) >= len(denominator):
                    denominator+='0'
                self.references['numerator'] = Rational(value.references['integer part']+value.references['float part'])
                self.references['denominator'] = Rational(denominator)            
            self.references['integer part'] = Rational(0)
            self.sign=value.sign
            self.value = Rational(0)
        elif Number.is_fraction(value):                        
            self.value = Rational(0)
            if type(value)==str:
                if value[0]=='-':
                    self.__sign_invert()
                    value=value[1:]
                if '(' in value and ')' in value:                    
                    value=value[1:-1]
                    value=value.split('+')
                    self.references['integer part']=value[0]
                    value=value[1]
                if '/' in value:
                    value = value.split('/')     
            if type(value)==tuple:
                value=list(value)
            if type(value)==list:
                if len(value)==1:
                    if '/'in str(value[0]):
                        self.references['numerator'], self.references['denominator'] = map(Rational, value[0].split('/'))
                    else:
                        self.references['numerator']=Rational(value[0])
                        self.references['denominator']=Rational(1)
                elif len(value)==2:
                    for i in range(len(value)):
                        if '(' in value and ')' in value:
                            value[i]=Fraction(value[i])
                    if str(value[1]) == '0':
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
            raise TimeoutError()
        if self.references['numerator'].sign=='-':
            self.__sign_invert()
            self.references['numerator']._Rational__sign_invert()
        if self.references['denominator'].sign=='-':
            self.__sign_invert()
            self.references['denominator']._Rational__sign_invert()
        self.standartize()
        self.simplify()   
        from NelMath.objects.math_base.Operators.Division.OperatorTruedivRR import OperatorTruedivRR
        self.value=self.references['integer part'] + OperatorTruedivRR().execute(self.references['numerator'], self.references['denominator'])
        if self.sign=='-':
            self.value=-self.value
    
    def standartize(self)->'Fraction':
        while self.references['denominator'].references['float part']!='0' or self.references['numerator'].references['float part']!='0':
            self.references['denominator'] *= 10
            self.references['numerator'] *= 10
        if self.references['numerator']>self.references['denominator']:
            self.references['integer part'] = self.references['numerator']//self.references['denominator']
            self.references['numerator'] = self.references['numerator']-self.references['denominator']*self.references['integer part']
        if self.references['numerator']==self.references['denominator']:
            self.references['integer part']+=1
            self.references['numerator']=Rational(0)
        if self.references['numerator']==0:
            return Rational(self.references['integer part'])
        if self.references['numerator']==self.references['denominator']:
            return Rational(self.references['integer part'])

    def improper_view(self)->None:
        if self.references['integer part']!=0:
            self.references['numerator']+=self.references['integer part']*self.references['denominator']
            self.references['integer part'] = Rational(0)     

    def __transform_mul(self, value)->'Fraction':
        self.references['numerator']*=value
        self.references['denominator']*=value

    def __transform_div(self, value)->'Fraction':
        self.references['numerator']/=value
        self.references['denominator']/=value

    def simplify(self)->'Fraction':
        if self.references['numerator']=='0':
            return
        fraction_gcd=gcd(self.references['numerator'], self.references['denominator'])
        if fraction_gcd!=1:
            self.references['numerator'] /= fraction_gcd 
            self.references['denominator'] /= fraction_gcd 
        else:
            return

    def __sign_invert(self):
        if self.sign=='+':
            self.sign='-'
        elif self.sign=='-':
            self.sign='+'

    def __abs__(self):
        if self.sign == '-':
            return -self
        else:
            return self

    def copy(self)->'Fraction':
        if self.references['integer part']!='0':
            numerator=self.references['numerator']+self.references['denominator']*self.references['integer part']
            denominator=self.references['denominator']
        else:
            numerator=self.references['numerator']
            denominator=self.references['denominator']
        if self.sign=='-':
            return -Fraction([numerator, denominator], self.__flags)
        else:
            return Fraction([numerator, denominator], self.__flags)

    def get_sign(self):
        return self.sign

    def __neg__(self):
        neg=self.copy()
        if neg.references['numerator'] == '0' and neg.references['integer part'] == '0':
            if neg.sign == '+':
                return neg          
        neg.__sign_invert()
        return neg

    def __eq__(self, other)->bool:
        if other=='':
            return False
        if not isinstance(other, Fraction):
            other=Fraction(other, {'type changing':False})
        if self.sign!=other.sign:
            return False
        fraction=self.copy()
        fraction.improper_view()
        other.improper_view()
        fraction_lcm=lcm(fraction.references['denominator'], other.references['denominator'])
        fraction.__transform_mul(fraction_lcm/fraction.references['denominator'])
        other.__transform_mul(fraction_lcm/other.references['denominator'])
        for key in self.references.keys():
            if fraction.references[key]!=other.references[key]:
                return False
        return True

    def __str__(self):
        sign=''
        if self.sign=='-':
            sign='-'
        if self.references["numerator"]!=0 and self.references['numerator']!=self.references['denominator']:
            if self.references['integer part'] == 0:
                return f'{sign}{self.references["numerator"]}/{self.references["denominator"]}'
            elif self.references['denominator'] == 1:    
                return f'{sign}{self.references["numerator"]}'
            else:
                return f'{sign}({self.references["integer part"]}+{self.references["numerator"]}/{self.references["denominator"]})'
        else:
            return f'{sign}{self.references["integer part"]}'
    
    def __repr__(self, mode='std'):
        fraction=self.copy()
        fraction.improper_view()
        if mode=='debug':
            if self.sign=='-':
                return [f'Fraction object', f'Fraction(-{str(fraction.references["numerator"])}/{str(fraction.references["denominator"])})']
            return [f'Fraction object', f'Fraction({str(fraction.references["numerator"])}/{str(fraction.references["denominator"])})']
        else:
            return self.__str__()

    def print(self):
        print(f'Fraction:{self.references["integer part"]}+{self.references["numerator"]}/{self.references["denominator"]}')
        print(f'With:\n Integer part={self.references["integer part"]}\n   And value={self.value}')

    def __format__(self, format_spec): 
        if format_spec:
            return format(self.__str__(), format_spec)
        else:
            return self.__str__()

    @staticmethod
    def build(periodic_float:str)->'Fraction':
        '''
        builds a fraction from periodic view such as 2.13(12) that means 2.1312121212...
        parameters:
            periodic_float(str) - string via float format such as n.kl...(abc...)
        returns
            @Fraction class based on periodic view
        ex:
            Fraction.build('2.13(37)') [that means 2.133737...] returns Fraction(5281/2475)==2.13373737...
            Fraction.build('1.(3)') [that means 1.333333...] returns Fraction(4/3)==1.333333333...
            Fraction.build('3.11(213)') [that means 1.333333...] returns Fraction(51817/16650)==3.11213213...
        '''
        nonperiodic_part, periodic_part = periodic_float[0:-1].split('(')
        deg=0
        k=0
        if nonperiodic_part[-1]=='.':
            nonperiodic=Rational(nonperiodic_part+periodic_part)
            periodic=nonperiodic.copy()
            while nonperiodic.references['float part']!='0':
                nonperiodic*=10
                deg+=1
            nonperiodic=Rational(nonperiodic.references['integer part']+'.'+periodic_part)
            while len(nonperiodic.references['float part'])<len(periodic.references['float part']):
                nonperiodic=Rational(nonperiodic.value+nonperiodic_part)
        else:
            nonperiodic=Rational(nonperiodic_part)
            periodic=nonperiodic.copy()
            while nonperiodic.references['float part']!='0':
                nonperiodic*=10
                deg+=1
            nonperiodic=Rational(nonperiodic.references['integer part']+'.'+periodic_part)
            periodic=Rational(periodic.value+periodic_part)
            if (len(nonperiodic.references['float part'])-len(periodic.references['float part']))%len(nonperiodic_part)==0:                
                while len(nonperiodic.references['float part'])!=len(periodic.references['float part']):
                    nonperiodic=Rational(nonperiodic.value+periodic_part)
            else:
                k=deg
                periodic=nonperiodic.copy()
                while nonperiodic.references['float part']!='0': 
                    nonperiodic*=10
                    deg+=1
                nonperiodic=Rational(nonperiodic.references['integer part']+'.'+periodic_part)
        return Fraction([nonperiodic-periodic, (10**deg)-(10**k)])
    
    @staticmethod
    def __fractionize_value(obj:any)->list:
        if isinstance(obj, Rational):
            return [obj, Rational('1')]
        if type(obj)==str:
            if Number.is_rational(obj):
                return [Rational(obj), Rational(1)]
            if Number.is_fraction(obj):
                if type(obj)==str:
                    sign=''
                    integer=1
                    if obj[0]=='-':
                        obj=obj[1:]
                        sign='-'
                    if '(' in obj and ')' in obj:                    
                        obj=obj[1:-1]
                        obj=obj.split('+')
                        integer=Rational(obj[0])
                        obj=obj[1]
                    if '/' in obj:
                        obj = obj.split('/')
                    return [Rational(sign+obj[0])*integer, Rational(obj[1])]
                if type(obj)==tuple:
                    obj=list(obj)
                if len(obj)==1:
                    return Fraction.__fractionize_value(obj[0])
        
