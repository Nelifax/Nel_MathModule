from NelMath.objects.math_base.Operators.Minus.OperatorMinus import OperatorMinus
from NelMath.objects.math_base.Rational import Rational

class OperatorMinusRR(OperatorMinus):    
    @staticmethod
    def execute(operand_a: Rational, operand_b: Rational):
        numb_a=operand_a.copy()
        numb_b=operand_b.copy()
        if numb_b==numb_a:
            return Rational('0', {'max float part':operand_a._Rational__flags['max float part']})
        match(numb_a.sign, numb_b.sign):
            case ('-', '-'):
                if -numb_a > -numb_b:
                    return -(abs(numb_a)-abs(numb_b))
                elif -numb_a < -numb_b:                    
                    return abs(numb_b)-abs(numb_a)
                else:
                    return Rational('0', {'max float part':operand_a._Rational__flags['max float part']})
            case ('-', '+'):
                return -((-numb_a)+numb_b)
            case ('+', '-'):
                return numb_a+(-numb_b)   
            case _:
                if numb_a<numb_b:
                    return -(numb_b-numb_a)
                if operand_a.references['float part'] != '0' or operand_b.references['float part'] != '0':
                    float_a = operand_a.references['float part']
                    float_b = operand_b.references['float part']
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
                    integer_part = Rational(operand_a.references['integer part'])-Rational(operand_b.references['integer part'])-reminder_last
                    if reminder_last == 1:
                        return Rational(integer_part.value+'.'+calculated_float[:-1][::-1], {'max float part':operand_a._Rational__flags['max float part']})
                    else:
                        return Rational(integer_part.value+'.'+calculated_float[::-1], {'max float part':operand_a._Rational__flags['max float part']})
                if operand_a.references['integer part'] == '0':
                    return -numb_b
                elif operand_b.references['integer part'] == '0':
                    return numb_a
                else:
                    calculated = ''
                    int_a = operand_a.references['integer part'][::-1]
                    int_b = operand_b.references['integer part'][::-1]
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
                    return Rational(calculated[::-1], {'max float part':operand_a._Rational__flags['max float part']})