__all__ = ['Rational', 'MM_number_max_float_part', 'MM_number_timeout_cap']

global MM_number_max_float_part, MM_number_timeout_cap
MM_number_max_float_part = 4
MM_number_timeout_cap = 3

class Rational():
    """
    provides str-number class that aimed to long-arythmetics
    warning: due to python ristriction if float used as generator -> be careful if float part is short enough or use str-format instead
    """
    def __init__(self, value:str|int|float, flags:dict={}):
        if isinstance(value, Rational):
            value = value.value
        self.__flags = {
        'all references': False,
        'max float part': MM_number_max_float_part,
        'exponential view': False,
        'standart view': False,
        'type changing': True,
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
        if '/' in value:
            return
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
            elif value.lstrip('0')=='':
                self.value = self.__flags['sign']+'0'
            elif value!='0':
                value = value.lstrip('0')
                self.references['integer part'] = value
                self.value = self.__flags['sign']+value
            else:
                self.value = '0'
        else:
            raise TimeoutError() 
        if self.value[0] == '+':
            self.value = self.value[1:]
        if self.value[0] == '-' and self.references['integer part'] == '0' and self.references['float part'] == '0':
            self.value = '0'
            self.__sign_invert()


    def get_sign(self):
        return self.__flags['sign']

    def __sign_invert(self):
        if self.__flags['sign'] == '+':
            self.__flags['sign'] = '-'
            self.value = '-'+self.value
        else:
            self.__flags['sign'] = '+'
            self.value = self.value[1:]

    def copy(self)->'Rational':
        return Rational(self.value, self.__flags)

    def __neg__(self):
        neg = self.copy()
        if neg.references['float part'] == '0' and neg.references['integer part'] == '0':
            if neg.get_sign() == '+':
                return neg          
        neg.__sign_invert()
        return neg

    def __lt__(self, other):#< 
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
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
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
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
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
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
        if self.references['float part'] == other.references['float part']:
            return True
        else:
            return False

    def __ge__(self, other):#>=
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
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
        elif self.references['float part'] == other.references['float part']:
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        if self.references == other.references and self.__flags['sign']==other.__flags['sign']:
            return True
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __abs__(self):
        if self.__flags['sign'] == '-':
            return -self
        else:
            return self

    def __sub__(self, other)->'Rational':
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        numb_a=self.copy()
        numb_b=other.copy()
        if self.__flags['sign'] == '-' and other.__flags['sign'] == '-':
            if (-numb_a) > (-numb_b):
               return -((-numb_a)-(-numb_b))
            elif (-numb_a) < (-numb_b):
                return (-other)-(-numb_a)
            else:
               return Rational('0', {'max float part':self.__flags['max float part']})
        if numb_b==numb_a:
            return Rational('0', {'max float part':self.__flags['max float part']})
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
            while len(float_b) < len(float_a):
                float_b = float_b+'0'
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
            integer_part = Rational(self.references['integer part'])-Rational(other.references['integer part'])-reminder_last
            if reminder_last == 1:
                return Rational(integer_part.value+'.'+calculated_float[:-1][::-1], {'max float part':self.__flags['max float part']})
            else:
                return Rational(integer_part.value+'.'+calculated_float[::-1], {'max float part':self.__flags['max float part']})
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
            return Rational(calculated[::-1], {'max float part':self.__flags['max float part']})  
    
    def __rsub__(self, other)->'Rational':
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        return other - self

    def __add__(self, other)->'Rational':
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
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
                return Rational('0', {'max float part':self.__flags['max float part']})
        if self.__flags['sign'] == '+' and other.__flags['sign'] == '-':
            if numb_a > (-numb_b):
                return numb_a-(-numb_b)
            elif numb_a < (-numb_b):
                return -((-numb_b)-numb_a)
            else:
                return Rational('0', {'max float part':self.__flags['max float part']})
        if self.references['float part'] != '0' or other.references['float part'] != '0':
            float_a = self.references['float part']
            float_b = other.references['float part']            
            float_part = Rational(float_a, {'max float part':self.__flags['max float part']}) + Rational(float_b, {'max float part':self.__flags['max float part']})
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
            integer_part = Rational(self.references['integer part'])+Rational(other.references['integer part'], {'max float part':self.__flags['max float part']})+reminder
            return Rational(integer_part.value+'.'+calculated_float, {'max float part':self.__flags['max float part']})
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
            return Rational(calculated[::-1], {'max float part':self.__flags['max float part']})

    def __radd__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        return other+self

    def __mul__(self, other, mode='std')->'Rational':      
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        numb_a = self.copy()
        numb_b = other.copy()        
        match (numb_a.__flags['sign'], numb_b.__flags['sign']):
            case ('+', '+'):
                invert = False
            case ('-', '-'):
                invert = False
            case _:
                invert = True
        if abs(numb_b)==10:
            if numb_a.references['float part'] != '0':
                return -Rational(numb_a.references['integer part']+numb_a.references['float part'][0]+'.'+numb_a.references['float part'][1:], {'max float part':self.__flags['max float part']}) if invert else Rational(numb_a.references['integer part']+numb_a.references['float part'][0]+'.'+numb_a.references['float part'][1:], {'max float part':self.__flags['max float part']})
            else:
                return -Rational(numb_a.references['integer part']+'0', {'max float part':self.__flags['max float part']}) if invert else Rational(numb_a.references['integer part']+'0', {'max float part':self.__flags['max float part']})
        int_a = int(numb_a.references['integer part'])
        int_b = int(numb_b.references['integer part'])
        float_a = int(numb_a.references['float part'])
        float_b = int(numb_b.references['float part']) 
        int_part = int_a * int_b
        if float_a == 0 and float_b == 0:
            return -Rational(str(int_part), {'max float part':self.__flags['max float part']}) if invert else Rational(str(int_part), {'max float part':self.__flags['max float part']})    
        float_part = 0
        if float_a != 0 and float_b == 0:#(a+0.b)*(c+0)=ac+0.b*c
            additional_deg=len(numb_a.references['float part']) - len(numb_a.references['float part'].lstrip('0'))
            deg_a = len(numb_a.references['float part'])
            float_part = str(float_a*int_b)
            while len(float_part)<=deg_a+additional_deg:
               float_part = '0' + float_part
            to_int = int(float_part[0:-deg_a])
            float_part = float_part[-deg_a:]
            if mode != 'std':
                return -Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']}).__self_round_float(mode) if invert else Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']}).__self_round_float(mode)
            else:
                return -Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']}) if invert else Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']}) 
        if float_a == 0 and float_b != 0:#(a+0)*(c+0.d)=ac+a*0.d
            additional_deg=len(numb_b.references['float part']) - len(numb_b.references['float part'].lstrip('0'))
            deg_b = len(numb_b.references['float part'])
            float_part = str(float_b*int_a)
            while len(float_part)<=deg_b+additional_deg:
               float_part = '0' + float_part
            to_int = int(float_part[0:-deg_b])
            float_part = float_part[-deg_b:]
            if mode != 'std':
                return -Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']}).__self_round_float(mode) if invert else Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']}).__self_round_float(mode)
            else:
                return -Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']}) if invert else Rational(str(int_part+to_int)+'.'+float_part, {'max float part':self.__flags['max float part']})
        if float_a != 0 and float_b != 0:#(a+0.b)*(c+0.d)=ac+a*0.d+0.b*c+0.d*0.b
            #additional_deg=(len(numb_a.references['float part']) - len(numb_a.references['float part'].lstrip('0'))) + (len(numb_b.references['float part']) - len(numb_b.references['float part'].lstrip('0')))
            deg_a = len(numb_a.references['float part'])
            deg_b = len(numb_b.references['float part'])
            float_part = str(float_a * float_b)
            int_part = Rational(str(int_part), {'max float part':self.__flags['max float part']})
            while len(float_part) < deg_a+deg_b:
                float_part = '0'+float_part            
            float_part = Rational('0.'+float_part, {'max float part':self.__flags['max float part']})
            float_part_one = str(float_a*int_b)
            float_part_two = str(float_b*int_a)
            while len(float_part_one) < deg_a:
                float_part_one = '0'+float_part_one  
            while len(float_part_two) < deg_b:
                float_part_two = '0'+float_part_two  
            float_part_one = Rational(float_part_one[0:-deg_a]+'.'+float_part_one[-deg_a:], {'max float part':self.__flags['max float part']})
            float_part_two = Rational(float_part_two[0:-deg_b]+'.'+float_part_two[-deg_b:], {'max float part':self.__flags['max float part']})
            float_part = float_part + float_part_one + float_part_two
            int_part = int_part+Rational(float_part.references['integer part'], {'max float part':self.__flags['max float part']})
            if mode != 'std':
                return -Rational(int_part.references['integer part'] + '.' + float_part.references['float part'], {'max float part':self.__flags['max float part']}).__self_round_float(mode) if invert else Rational(int_part.references['integer part'] + '.' + float_part.references['float part'], {'max float part':self.__flags['max float part']}).__self_round_float(mode)
            else:
                return -Rational(int_part.references['integer part'] + '.' + float_part.references['float part'], {'max float part':self.__flags['max float part']}) if invert else Rational(int_part.references['integer part'] + '.' + float_part.references['float part'], {'max float part':self.__flags['max float part']}) 

    def __rmul__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        return other*self

    def __truediv__(self, other, mode='std')->'Rational':#/
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']}) 
        numb_a = self.copy()
        numb_b = other.copy()
        if other.value == '0':
            raise ZeroDivisionError()
        if self == 0:
            return Rational(0, {'max float part':self.__flags['max float part']})
        match (numb_a.__flags['sign'], numb_b.__flags['sign']):
            case ('+', '+'):
                invert = False
            case ('-', '-'):
                invert = False
            case _:
                invert = True
        if numb_a.__flags['sign'] == '-':
            numb_a.__sign_invert()
        if numb_b.__flags['sign'] == '-':
            numb_b.__sign_invert()
        if other.value == '10':
            float_part = numb_a.references['float part']
            integer_part = numb_a.references['integer part']
            if integer_part != '0':
                float_part=integer_part[-1]+float_part
                integer_part = integer_part[0:-1]
                return -Rational(integer_part+'.'+float_part, {'max float part':self.__flags['max float part']}) if invert else Rational(integer_part+'.'+float_part, {'max float part':self.__flags['max float part']})
            else:
                return -Rational('0.0'+float_part, {'max float part':self.__flags['max float part']}) if invert else Rational('0.0'+float_part, {'max float part':self.__flags['max float part']})
        while numb_b.references['float part'] != '0':
            numb_b = numb_b*10
            numb_a = numb_a*10
        result=''
        result_float='0'
        floated=False
        numerator = Rational(0)
        denominator = numb_b.copy()
        iterator=0
        numb = numb_a.value
        if denominator == 1:
            return -Rational(numb, {'max float part':self.__flags['max float part']}) if invert else Rational(numb, {'max float part':self.__flags['max float part']})
        if '.' not in numb:
            numb = numb+'.0'
        while len(result_float)<self.__flags['max float part']+1:            
            deg = 0
            while numerator<denominator:
                if len(numb)!=0 and numb[0]!='.':
                    if result=='':
                        numerator = Rational(numerator.references['integer part']+numb[0], {'max float part':self.__flags['max float part']})
                        numb = numb[1:]
                    else:
                        numerator = Rational(numerator.references['integer part']+numb[0], {'max float part':self.__flags['max float part']})
                        numb = numb[1:]
                        deg+=1
                elif len(numb)!=0 and numb[0]=='.':
                    numb=numb[1:]    
                    if deg!=0:
                        result+='0'*deg
                        deg=0
                    floated = True
                    if result=='':
                        result='0.'
                    else:
                        result+='.'
                elif len(numb)==0:
                    if result=='':
                        numerator = Rational(numerator.references['integer part']+'0', {'max float part':self.__flags['max float part']})
                        numb = numb[1:]
                    else:
                        numerator = Rational(numerator.references['integer part']+'0', {'max float part':self.__flags['max float part']})
                        numb = numb[1:]
                        deg+=1
                if len(numb)==0 and numerator==0:
                    break
            if deg>1:
                result = result+'0'*(deg-1)
            count=0
            while numerator >= denominator:
                numerator=numerator-denominator
                count+=1
            result+=str(count)
            if numerator==0 and numb!='':
                while len(numb)>0 and numb[0]=='0':
                    result+='0'
                    numb=numb[1:]
            if numb=='' and numerator ==0:
                break   
            if '.' in result:
                result_float = result.split('.')[1]
            else:
                result_float = '0'
        result = Rational(result, {'max float part':self.__flags['max float part']})
        if mode != 'std':
            return -result if invert else result
        else:
            return -result.__self_round_float() if invert else result.__self_round_float()

    def __rtruediv__(self, other)->'Rational':
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']}) 
        return other/self

    def sqrt(self)->'Rational':
        numb = self.copy()
        result = numb/2
        if self.get_sign() == '-':
            raise TimeoutError('NOT IMPLEMENTED YET')
        border = Rational('0.'+'0'*(int(self.__flags['max float part'])-1)+'1', {'max float part':self.__flags['max float part']})
        while True:
            result_next = (result + numb.__truediv__(result, 'root')).__mul__(0.5, 'root')
            if abs(result_next - result) < border:
                break
            result = result_next        
        return result.__self_round_float()

    def __self_round_float(self, mode = 'std')->'Rational':
        if mode != 'std':
            if len(self.references['float part'])>self.__flags['max float part']*2:
                bord_float = self.references['float part'][self.__flags['max float part']*2]
                if bord_float>'4':
                    values = self.value.split('.')
                    self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']*2], {'max float part':self.__flags['max float part']})
                    if self.references['float part'] == '0':
                        return self
                    self=self+Rational('0.'+'0'*(self.__flags['max float part']*2-1)+'1', {'max float part':self.__flags['max float part']})
                    return self
                else:
                    values = self.value.split('.')
                    self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']*2], {'max float part':self.__flags['max float part']})
                    return self
            else:
                return self
        if len(self.references['float part'])>self.__flags['max float part']:
            bord_float = self.references['float part'][self.__flags['max float part']]
            if bord_float>'4':
                values = self.value.split('.')
                self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']], {'max float part':self.__flags['max float part']})
                if self.references['float part'] == '0':
                    return self
                self=self+Rational('0.'+'0'*(self.__flags['max float part']-1)+'1', {'max float part':self.__flags['max float part']})
                return self
            else:
                values = self.value.split('.')
                self=Rational(values[0]+'.'+values[1][0:self.__flags['max float part']], {'max float part':self.__flags['max float part']})
                return self
        else:
            return self

    def nroot(self, exp)->'Rational':
        if type(exp) != int and not isinstance(exp, Rational):
            from NelMath.objects.math_constructions.Fraction import Fraction
            exp = Fraction(str(exp))
            return self.nroot(exp.references['denominator'])
        if not isinstance(exp, Rational):
            exp = Rational(exp, {'max float part':self.__flags['max float part']})
        if self.get_sign() == '-' and exp%2==0:
            raise TimeoutError('NOT IMPLEMENTED YET')        
        numb = self.copy()
        result = Rational(1, {'max float part':self.__flags['max float part']})
        border = Rational('0.'+'0'*(int(self.__flags['max float part'])-1)+'1', {'max float part':self.__flags['max float part']})
        while True:
            result_next = ((exp - 1).__mul__(result, 'nroot') + numb.__truediv__(result.__pow__(exp - 1, mode='nroot'), 'nroot')).__truediv__(exp, 'nroot')
            if abs(result_next - result) < border:
                break
            result = result_next
        return result.__self_round_float()

    def __floordiv__(self, other)->'Rational':#//
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})            
        numb_a = self.copy()
        numb_b = other.copy() 
        match (numb_a.__flags['sign'], numb_b.__flags['sign']):
            case ('+', '+'):
                invert = False
            case ('-', '-'):
                invert = False
            case _:
                invert = True 
        preresult=numb_a/numb_b
        result = Rational(preresult.references['integer part'], {'max float part':self.__flags['max float part']})
        result = result+1 if Rational(preresult.references['float part'])>0 and invert else result
        return -result if invert else result

    def __rfloordiv__(self, other)->'Rational':
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']}) 
        return other//self

    def __mod__(self, other)->'Rational':#%
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        numb_a = self.copy()
        if numb_a == 0:
            return Rational(0, {'max float part':self.__flags['max float part']})
        numb_b = other.copy()        
        if numb_b == 0:
            raise TimeoutError()
        if other==2 and self.references['float part']=='0':
            if self.references['integer part'][-1] in ['0','2','4','6','8']:
                return Rational(0, {'max float part':self.__flags['max float part']})
            else:                
                return Rational(1, {'max float part':self.__flags['max float part']})
        inverted = False
        if numb_b.get_sign() == '-':
            inverted = True
        deg=0
        while numb_b.references['float part'] != '0':
            numb_b*=10
            numb_a*=10
            deg+=1 
        if numb_b == 1:
            return Rational(0, {'max float part':self.__flags['max float part']})
        #if numb_b.references['integer part'].rstrip('0')=='1' and other<self:
            #return Rational(self.references['integer part'][-(len(other.references['integer part'])-1):]+'.'+self.references['float part'], {'max float part':self.__flags['max float part']})+numb_b if inverted else Rational(self.references['integer part'][-(len(other.references['integer part'])-1):]+'.'+self.references['float part'], {'max float part':self.__flags['max float part']})
        numb_a = numb_a-numb_b*(numb_a//numb_b)
        return numb_a/10**deg       

    def __rmod__(self, other)->'Rational':
        if not isinstance(other, Rational):
            other = Rational(other, {'max float part':self.__flags['max float part']})
        numb_a = self.copy()
        numb_b = other.copy()
        return other%self

    def __pow__(self, value, modulo = None, mode = 'std'):
        if not isinstance(value, Rational):
            value = Rational(value, {'max float part':self.__flags['max float part']})
        numb = self.copy()
        exp = value.copy()
        exp_sign = exp.get_sign()
        if exp.references['float part'] == '0':
            if exp.references['integer part'] == '0':
                return Rational(1, {'max float part':self.__flags['max float part']})
            elif exp_sign == '+':
                return numb.__mul__(numb.__pow__(value-1, mode), mode)
            elif exp_sign == '-':
                exp.__sign_invert()
                return 1/(numb.__pow__(exp, mode))
        else:
            raise TimeoutError('NOT IMPLEMENTED YET')  

    def __str__(self)->str:
        return self.value

    def __repr__(self)->str:
        return self.value

    def __int__(self)->int:
        if self.__flags['sign'] == '-':
            return -int(self.references['integer part'])
        else:
            return int(self.references['integer part'])

    def __float__(self)->float:       
        if self.__flags['sign'] == '-':
            return -float(self.references['integer part']+'.'+self.references['float part'][0:self.__flags['max float part']])
        else:
            return float(self.references['integer part']+'.'+self.references['float part'][0:self.__flags['max float part']])
