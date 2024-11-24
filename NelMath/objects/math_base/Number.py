__all__=['Number']

from NelMath.properties.settings_handler import SettingsHandler
settings=SettingsHandler()

class Number():
    def __new__(cls, value, flags={}):        
        if cls is not Number:
            return super().__new__(cls)
        if ('type changing' in flags and flags['type changing']) or ('type changing' not in flags and settings.get('mm_dynamic_class_changing')):
            if Number.is_fraction(value):
                from NelMath.objects.math_constructions import Fraction
                return Fraction(value, cls._check_flags(flags, 'Fraction'))
            elif Number.is_rational(value):
                from NelMath.objects.math_base.Rational import Rational
                return Rational(value)
        else:
            if Number.is_rational(value):
                from NelMath.objects.math_base.Rational import Rational
                return Rational(value)
            elif Number.is_fraction(value):
                from NelMath.objects.math_constructions import Fraction
                return Fraction(value, cls._check_flags(flags, 'Fraction'))
            

    @staticmethod
    def _check_flags(flags, construction)->dict:
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
        from NelMath.objects.math_constructions import Fraction
        if isinstance(value, Fraction):
            return True
        if type(value)==str:             
            if value=='':
                return False
            if '/' not in value:
                if value[0]=='-' or value[0]=='+':
                    value=value[1:]
                if value.replace('.', '', 1).isdigit():
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
        from NelMath.objects.math_constructions import Fraction
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
