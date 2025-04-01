from NelMath.objects.math_base.Number import Number
__all__ = ['Rational', 'MM_number_max_float_part', 'MM_number_timeout_cap']

global MM_number_max_float_part, MM_number_timeout_cap
MM_number_max_float_part = 4
MM_number_timeout_cap = 3

class Rational(Number):
    """
    provides str-number class that aimed to long-arythmetics
    warning: due to python ristriction if float used as generator -> be careful if float part is short enough or use str-format instead
    """
    __module__="Number"
    #def __new__(cls, value, flags={}):
        #instance = super().__new__(cls, value, flags)
        #return instance

    def __init__(self, value:str|int|float, flags:dict={}):
        if isinstance(value, Number):
            value = value.value

        self.references = {
        'integer part': '0',
        'float part': '0',                
        }

        self.sign='+'
        
        self.__flags = super()._check_flags(flags, 'Rational')
        if type(value) == list or type(value)==tuple and len(type)==1:
            value=value[0]
        value = str(value)
        
        if value[0] == '+' or value[0]=='-':
            self.sign = value[0]
            value = value[1:]
        if value.replace('.', '', 1).isdigit():            
            if '.' in value:
                value = value.split('.')
                if value[0].lstrip('0')!='':
                    self.references['integer part'] = value[0].lstrip('0')
                if value[1].rstrip('0')!='':
                    self.references['float part'] = value[1].rstrip('0')
                self.value = self.sign+self.references['integer part']
                if self.references['float part'] != '0':
                    self.value+='.'+self.references['float part']
                    self.__flags['type'] = 'float'
            elif value.lstrip('0')=='':
                self.value = '0'
            elif value!='0':
                value = value.lstrip('0')
                self.references['integer part'] = value
                self.value = self.sign+value
            else:
                self.value = '0'
        else:
            raise TimeoutError() 
        if self.value[0] == '+':
            self.value = self.value[1:]
        if self.value[0] == '-' and self.references['integer part'] == '0' and self.references['float part'] == '0':
            self.value = '0'
            self.__sign_invert()

    def copy(self)->'Rational':
        return Rational(self.value, self.__flags)

    def __lt__(self, other):#< 
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        match (self.sign, other.sign):
            case ('-', '+'):
                return True
            case ('+', '-'):
                return False
            case ('-', '-'):
                invert=True
            case ('+', '+'):
                invert=False
        if len(self.references['integer part']) < len(other.references['integer part']):
            return False if invert else True
        elif len(self.references['integer part']) > len(other.references['integer part']):
            return True if invert else False
        else:
            if self.references['integer part'] < other.references['integer part']:
                return False if invert else True
            elif self.references['integer part'] > other.references['integer part']:
                return True if invert else False
        if self.references['float part'] < other.references['float part']:
            return False if invert else True
        else:
            return False        

    def __gt__(self, other):#>
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        match (self.sign, other.sign):
            case ('-', '+'):
                return False
            case ('+', '-'):
                return True
            case ('-', '-'):
                invert=True
            case ('+', '+'):
                invert=False
        if len(self.references['integer part']) > len(other.references['integer part']):
            return False if invert else True
        elif len(self.references['integer part']) < len(other.references['integer part']):
            return True if invert else False
        else:
            if self.references['integer part'] > other.references['integer part']:
                return False if invert else True
            elif self.references['integer part'] < other.references['integer part']:
                return True if invert else False
        if self.references['float part'] > other.references['float part']:
            return False if invert else True
        else:
            return False

    def __le__(self, other):#<=
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        match (self.sign, other.sign):
            case ('-', '+'):
                return True
            case ('+', '-'):
                return False
            case ('-', '-'):
                invert=True
            case ('+', '+'):
                invert=False
        if len(self.references['integer part']) < len(other.references['integer part']):
            return False if invert else True
        elif len(self.references['integer part']) > len(other.references['integer part']):
            return True if invert else False
        else:
            if self.references['integer part'] < other.references['integer part']:
                return False if invert else True
            elif self.references['integer part'] > other.references['integer part']:
                return True if invert else False
        if self.references['float part'] < other.references['float part']:
            return False if invert else True
        if self.references['float part'] == other.references['float part']:
            return True
        else:
            return False

    def __ge__(self, other):#>=
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        match (self.sign, other.sign):
            case ('-', '+'):
                return False
            case ('+', '-'):
                return True
            case ('-', '-'):
                invert=True
            case ('+', '+'):
                invert=False
        if len(self.references['integer part']) > len(other.references['integer part']):
            return False if invert else True
        elif len(self.references['integer part']) < len(other.references['integer part']):
            return True if invert else False
        else:
            if self.references['integer part'] > other.references['integer part']:
                return False if invert else True
            elif self.references['integer part'] < other.references['integer part']:
                return True if invert else False
        if self.references['float part'] > other.references['float part']:
            return False if invert else True
        elif self.references['float part'] == other.references['float part']:
            return True
        else:
            return False
    
    

    def __eq__(self, other):
        if other=='' or other == None:
            return False
        if type(other)==list and len(other)>1:
            return False
        if type(other)==tuple and len(other)>1:
            return False
        if not isinstance(other, Rational):
            if type(other)==str:
                if not other.replace('.','',1).isdigit():
                    return False
        other = Rational(other, {'max float part':self.__flags['max float part']})
        if self.references == other.references and self.sign==other.sign:
            return True
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    
    

    def __self_round_float(self, mode = 'std')->'Rational':
        if self.sign=='-': 
            inverse=True
            self=-self
        else: inverse=False
        if mode != 'std':
            if len(self.references['float part'])>self.__flags['max float part']*2:
                bord_float = self.references['float part'][self.__flags['max float part']*2]
                if bord_float>'4':
                    values = self.value.split('.')
                    self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']*2], {'max float part':self.__flags['max float part']})
                    if self.references['float part'] == '0':
                        return self
                    self=self+Rational('0.'+'0'*(self.__flags['max float part']*2-1)+'1', {'max float part':self.__flags['max float part']})
                    return -self if inverse else self
                else:
                    values = self.value.split('.')
                    self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']*2], {'max float part':self.__flags['max float part']})
                    return -self if inverse else self
            else:
                return -self if inverse else self
        if len(self.references['float part'])>self.__flags['max float part']:
            bord_float = self.references['float part'][self.__flags['max float part']]
            if bord_float>'4':
                values = self.value.split('.')
                self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']], {'max float part':self.__flags['max float part']})
                if self.references['float part'] == '0':
                    return -self if inverse else self
                self=self+Rational('0.'+'0'*(self.__flags['max float part']-1)+'1', {'max float part':self.__flags['max float part']})
                return -self if inverse else self
            else:
                values = self.value.split('.')
                self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']], {'max float part':self.__flags['max float part']})
                return -self if inverse else self
        else:
            return -self if inverse else self

    

    #def __repr__(self)->str:
        #return f'Number.Rational'

    def __hash__(self):
        return hash(self.value)


