__all__ = ['Number']

global MM_number_max_float_part
MM_number_max_float_part = 10

class Number():
    """
    provides str-number class that aimed to long-arythmetics
    warning: due to python ristriction if float used as generator -> be careful if float part is short enough
    """
    def __init__(self, value:str|int|float, flags:dict={}):
        self.__flags = {
        'all_references': False,
        'max_float_part': MM_number_max_float_part,
        'exponential_view': False,
        'standart_view': False,
        'type': 'integer',  
        'sign': '+',
        }
        self.references = {
        'integer part': '0',
        'float part': '0',                
        }
        if flags != {}:
            for key, fvalue in flags.items():
                if key not in self.__flags.keys():
                    raise TimeoutError()
            self.__flags.update(flags)
        value = str(value)
        if value[0] == '+' or value[0]=='-':
            self.__flags['sign'] = value[0]
            value = value[1:]
        if value.replace('.', '', 1).isdigit():            
            if '.' in value:
                value = value.split('.')
                if value[0].lstrip('0')!='':
                    self.references['integer part'] = value[0].lstrip('0')
                if value[1].rstrip('0')!='':
                    self.references['float part'] = value[1].rstrip('0')
                self.value = self.__flags['sign']+self.references['integer part']
                if self.references['float part'] != '0':
                    self.value+='.'+self.references['float part']
                    self.__flags['type'] = 'float'
            elif value!='0':
                value = value.lstrip('0')
                self.references['integer part'] = value
                self.value = self.__flags['sign']+value
            else:
                self.value = '0'
        else:
            raise TimeoutError() 
        if self.value[0]=='+':
            self.value = self.value[1:]

    def get_sign(self):
        return self.__flags['sign']

    def __sign_invert(self):
        if self.__flags['sign'] == '+':
            self.__flags['sign'] = '-'
            self.value = '-'+self.value
        else:
            self.__flags['sign'] = '+'
            self.value = self.value[1:]

    def copy(self)->'Number':
        return Number(self.value,self.__flags)

    def __neg__(self):
        neg = self.copy()
        neg.__sign_invert()
        return neg

    def __lt__(self, other):#< 
        if not isinstance(other, Number):
            other = Number(other)
        match (self.__flags['sign'], other.__flags['sign']):
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
        if not isinstance(other, Number):
            other = Number(other)
        match (self.__flags['sign'], other.__flags['sign']):
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
        if not isinstance(other, Number):
            other = Number(other)
        match (self.__flags['sign'], other.__flags['sign']):
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
            return True

    def __ge__(self, other):#>=
        if not isinstance(other, Number):
            other = Number(other)
        match (self.__flags['sign'], other.__flags['sign']):
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
            return True

    def __eq__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        if self.references == other.references and self.__flags['sign']==other.__flags['sign']:
            return True
        else:
            return False
    
    def __abs__(self):
        if self.__flags['sign'] == '-':
            return -self
        else:
            return self

    def __sub__(self, other)->'Number':
        if not isinstance(other, Number):
            other = Number(other)
        numb_a=self.copy()
        numb_b=other.copy()
        if self.__flags['sign'] == '-' and other.__flags['sign'] == '-':
            if (-numb_a) > (-numb_b):
               return -((-numb_a)-(-numb_b))
            elif (-numb_a) < (-numb_b):
                return (-other)-(-numb_a)
            else:
               return Number('0')
        if self.__flags['sign'] == '-' and other.__flags['sign'] == '+':
           return -((-numb_a)+numb_b)
        if self.__flags['sign'] == '+' and other.__flags['sign'] == '-':
           return numb_a+(-numb_b)          
        if numb_a<numb_b:
            return -(numb_b-numb_a)
        if self.references['float part'] != '0' or other.references['float part'] != '0':
            float_a = self.references['float part']
            float_b = other.references['float part']
            reminder_last = 0
            while len(float_a) < len(float_b):
                float_a = float_a+'0'
            if float_a < float_b:
                float_a = '1'+float_a
                reminder_last = 1
            calculated_float = ''
            float_a = float_a[::-1]
            float_b = float_b[::-1]
            while len(float_b)<len(float_a):
                float_b = float_b+'0'               
            reminder=0
            for i in range(0,len(float_a)):
                if int(float_a[i])<int(float_b[i])+reminder:
                    calculated_float += str((int(float_a[i])-reminder+10) - int(float_b[i]))
                    reminder = 1
                else:
                    calculated_float += str((int(float_a[i])-reminder) - int(float_b[i]))
                    reminder=0
            integer_part = Number(self.references['integer part'])-Number(other.references['integer part'])-reminder_last
            if reminder_last == 1:
                return Number(integer_part.value+'.'+calculated_float[:-1][::-1])
            else:
                return Number(integer_part.value+'.'+calculated_float[::-1])
        if self.references['integer part'] == '0':
            return -numb_b
        elif other.references['integer part'] == '0':
            return numb_a
        else:
            if numb_a<numb_b:
                return -(other-self)
            calculated = ''
            int_a = self.references['integer part'][::-1]
            int_b = other.references['integer part'][::-1]
            while len(int_b)<len(int_a):
                int_b = int_b+'0'                
            reminder=0
            for i in range(0,len(int_a)):
                if int(int_a[i])<int(int_b[i])+reminder:
                    calculated += str((int(int_a[i])-reminder+10) - int(int_b[i]))
                    reminder = 1
                else:
                    calculated += str((int(int_a[i])-reminder) - int(int_b[i]))
                    reminder=0
            return Number(calculated[::-1])
        

    def __add__(self, other)->'Number':
        if not isinstance(other, Number):
            other = Number(other)
        numb_a=self.copy()
        numb_b=other.copy()
        if self.__flags['sign'] == '-' and other.__flags['sign'] == '-':            
            numb_a.__sign_invert()
            numb_b.__sign_invert()
            return -(numb_a+numb_b)
        if self.__flags['sign'] == '-' and other.__flags['sign'] == '+':
           if (-numb_a) > numb_b:
               return -((-numb_a)-numb_b)
           elif (-numb_a) < numb_b:
               return numb_b-(-numb_a)
           else:
               return Number('0')
        if self.__flags['sign'] == '+' and other.__flags['sign'] == '-':
           if numb_a > (-numb_b):
               return numb_a-(-numb_b)
           elif numb_a < (-numb_b):
               return -((-numb_b)-numb_a)
           else:
               return Number('0')
        if self.references['float part'] != '0' or other.references['float part'] != '0':
            float_a = self.references['float part']
            float_b = other.references['float part']            
            float_part = Number(float_a) + Number(float_b)
            calculated_float = ''
            reminder = 0
            float_a = float_a[::-1]
            float_b = float_b[::-1]
            if len(float_a) < len(float_b):
                float_a, float_b = float_b, float_a
            while len(float_b)<len(float_a):
                float_b = '0' + float_b                
            border = len(float_a)
            for i in range(0, len(float_a)):
                numb = int(float_a[i]) + int(float_b[i])+reminder
                reminder = int(numb//10)     
                numb = numb - int(reminder*10)
                calculated_float += str(numb) 
            if reminder != 0:
                calculated_float += str(reminder)
            if len(calculated_float)>border:
                reminder = calculated_float[::-1][0]
                calculated_float = calculated_float[::-1][1:]
            else:
                calculated_float = calculated_float[::-1]
                reminder=0
            integer_part = Number(self.references['integer part'])+Number(other.references['integer part'])+reminder
            return Number(integer_part.value+'.'+calculated_float)
        if self.references['integer part'] == '0':
            return other
        elif other.references['integer part'] == '0':
            return self
        else:
            calculated = ''
            reminder = 0
            int_a = self.references['integer part'][::-1]
            int_b = other.references['integer part'][::-1]
            if len(int_a)<len(int_b):
                int_a, int_b = int_b, int_a
            while len(int_b) < len(int_a):
                int_b=int_b+'0'
            for i in range(0, len(int_a)):
                numb = int(int_a[i]) + int(int_b[i])+reminder
                reminder = int(numb//10)     
                numb= numb - int((numb//10)*10)
                calculated += str(numb) 
            if reminder != 0:
                calculated += str(reminder)
            return Number(calculated[::-1])
        

