__all__=['Number']

from NelMath.properties.settings_handler import SettingsHandler

class Number():
    __qualname__='Number'
    __module__='Number'
    def __new__(cls, value, flags={}):        
        if cls is not Number:
            return super().__new__(cls)        
        settings=SettingsHandler()
        if ('type changing' in flags and flags['type changing']) or ('type changing' not in flags and settings.get('mm_dynamic_class_changing')):
            if Number.is_fraction(value):
                from NelMath.objects.math_base import Fraction
                return Fraction(value, cls._check_flags(flags, 'Fraction'))
            elif Number.is_rational(value):
                from NelMath.objects.math_base.Rational import Rational
                return Rational(value)
        else:
            if Number.is_rational(value):
                from NelMath.objects.math_base.Rational import Rational
                return Rational(value)
            elif Number.is_fraction(value):
                from NelMath.objects.math_base import Fraction
                return Fraction(value, cls._check_flags(flags, 'Fraction'))
            

    @staticmethod
    def _check_flags(flags, construction)->dict:
        settings=SettingsHandler()
        match(construction):
            case 'Rational':
                std_flags={
                    'all references': False,
                    'max float part': settings.get('mm_max_float_part'),
                    'exponential view': False,
                    'standart view': False,
                    'type changing': settings.get('mm_dynamic_class_changing'),
                    'type': 'integer',
                    }
            case 'Fraction':
                std_flags={
                    'all references': False,
                    'max float part': settings.get('mm_max_float_part'),
                    'exponential view': False,
                    'standart view': False,        
                    'auto-simplify': True,
                    'parts as Rational': True,
                    'float to numerator': True,
                    'type changing': settings.get('mm_dynamic_class_changing'),
                    'type': 'fraction'
                }
        if flags!={}:
            for flag in flags:
                if flag not in std_flags.keys():
                    raise TimeoutError()
            std_flags.update(flags)
        return std_flags

    @staticmethod
    def is_fraction(value:int|float|list|tuple|str)->bool:
        '''
        returns is number or string(list/tuple/etc) is fraction-typed
        '''
        if type(value)==int:
            return False
        if type(value)==float:
            return True
        from NelMath.objects.math_base.Rational import Rational
        if isinstance(value, Rational):
            return False
        from NelMath.objects.math_base import Fraction
        if isinstance(value, Fraction):
            return True
        if type(value)==str:
            if value=='':
                return False
            if '/' not in value:
                if value[0]=='-' or value[0]=='+':
                    value=value[1:]
                if value.isdigit():
                    return False
                if '.' in value and value.replace('.', '', 1).isdigit():
                    return True
            import re
            sample = re.match(r'([\+\-]*\d+(\.\d+)?\/[\+\-]*\d+(\.\d+)?)', value)            
            if sample!=None:
                value=value.replace(sample.group(), '').replace('(','',1).replace(')','',1)
                if value!='':
                    return False
            return True
        if type(value)==tuple:
            value=list(value)
        if len(value)>2:
            return False
        if len(value)==1:
            return Number.is_fraction(value[0])
        for elem in value:
            if not Number.is_fraction(elem) and not Number.is_rational(elem):
                return False
        return True

    @staticmethod
    def is_rational(value:int|float|list|tuple|str)->bool:
        '''
        returns is number or string(list/tuple/etc) is rational-typed
        '''
        if type(value)==int:
            return True
        if type(value)==float:
            return True
        from NelMath.objects.math_base.Rational import Rational
        if isinstance(value, Rational):
            return True
        from NelMath.objects.math_base import Fraction
        if isinstance(value, Fraction):
            return False
        if type(value)==str:              
            if value=='':
                return False 
            if '/' in value:
                return False           
            if value[0]=='-' or value[0]=='+':
                value=value[1:]
            if not value.replace('.', '', 1).isdigit():
                return False
            import re
            sample = re.match(r'([\+\-]*\d+(\.\d+)?)', value)
            if sample!=[]:
                value=value.replace(sample.group(), '')
                if value!='':
                    return False
            return True
        if type(value)==tuple:
            value=list(value)
        if len(value)==1:
            return Number.is_rational(value[0])
        return False

    def __add__(self, other):
        from NelMath.objects.math_base.Operators.Plus.OperatorPlus import OperatorPlus
        return OperatorPlus().execute(self, other)

    def __radd__(self, other):
        from NelMath.objects.math_base.Operators.Plus.OperatorPlus import OperatorPlus
        return OperatorPlus().execute(other, self)

    def __sub__(self, other):        
        from NelMath.objects.math_base.Operators.Minus.OperatorMinus import OperatorMinus
        return OperatorMinus().execute(self, other)

    def __rsub__(self, other):        
        from NelMath.objects.math_base.Operators.Minus.OperatorMinus import OperatorMinus
        return OperatorMinus().execute(other, self)
    
    def __sign_invert(self):
        if self.sign == '+':
            self.sign = '-'
            self.value = '-'+self.value
        else:
            self.sign = '+'
            self.value = self.value[1:]

    def __neg__(self):
        neg = self.copy()
        if neg.references['float part'] == '0' and neg.references['integer part'] == '0':
            if neg.sign == '+':
                return neg          
        neg.__sign_invert()
        return neg

    def __mul__(self, other):        
        from NelMath.objects.math_base.Operators.Multiply.OperatorMultiply import OperatorMultiply
        return OperatorMultiply().execute(self, other)

    def __rmul__(self, other):        
        from NelMath.objects.math_base.Operators.Multiply.OperatorMultiply import OperatorMultiply
        return OperatorMultiply().execute(other, self)

    def __truediv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorTruediv import OperatorTruediv
        return OperatorTruediv().execute(self, other)

    def __rtruediv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorTruediv import OperatorTruediv
        return OperatorTruediv().execute(other, self)

    def __floordiv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorFloordiv import OperatorFloordiv
        return OperatorFloordiv().execute(self, other)

    def __rfloordiv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorFloordiv import OperatorFloordiv
        return OperatorFloordiv().execute(other, self)

    def __pow__(self, exponent, modulo = None):
        from NelMath.objects.math_base.Operators.Pow.OperatorPow import OperatorPow
        return OperatorPow().execute(self, exponent, modulo)

    def __mod__(self, other):
        from NelMath.objects.math_base.Operators.Mod.OperatorMod import OperatorMod
        return OperatorMod().execute(self, other)
    
    def __rmod__(self, other):
        from NelMath.objects.math_base.Operators.Mod.OperatorMod import OperatorMod
        return OperatorMod().execute(other, self)

    def sqrt(self, precision:int=0):
        from NelMath.objects.math_base.Operators.Root.OperatorRoot import OperatorRoot
        return OperatorRoot().execute(self, 2, precision)

    def nroot(self, exponent, precision:int=0):
        from NelMath.objects.math_base.Operators.Root.OperatorRoot import OperatorRoot
        return OperatorRoot().execute(self, exponent, precision)

    def ln(self):
        from NelMath.objects.math_base.Operators.Logx.OperatorLnX import OperatorLnX
        return OperatorLnX().execute(self)

    def log(self, base=2):
        from NelMath.objects.math_base.Operators.Logx.OperatorLog import OperatorLog
        return OperatorLog().execute(self, base)

    def bit_length(self):
        return int(self.references['integer part']).bit_length()


    def __abs__(self):
        if self.sign == '-':
            return -self
        else:
            return self

    def __int__(self)->int:
        if self.sign == '-':
            return -int(self.references['integer part'])
        else:
            return int(self.references['integer part'])

    def __index__(self):
        if self.references['float part']=='0':
            return int(self.value)
        raise TimeoutError('Number has an float part')

    def __float__(self)->float:       
        return float(self.value)

    def __str__(self)->str:
        return str(self.value)

    def __hash__(self):
        return hash(self.value)    

    def __format__(self, format_spec):        
        if format_spec == "hex":
            return hex(self.value)
        elif format_spec == "bin":
            return bin(self.value)
        elif format_spec:
            return format(str(self.value), format_spec)
        else:
            return self.__str__()

    def __repr__(self):
        return str(self.value)

    def __round__(self):
        if '.' in self.value:
            if self.value.split('.')[1][0]>='5':
                return self+1
        else: return self