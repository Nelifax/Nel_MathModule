from NelMath.objects.math_base.Operators.Plus.OperatorPlus import OperatorPlus
from NelMath.objects.math_base.Rational import Rational

class OperatorPlusRR(OperatorPlus):    
    @staticmethod
    def execute(operand_a: Rational, operand_b: Rational):
        numb_a=operand_a.copy()
        numb_b=operand_b.copy()
        if numb_b==-numb_a:
            return Rational('0', {'max float part':operand_a._Rational__flags['max float part']})
        match(numb_a.sign, numb_b.sign):
            case ('-', '-'):            
                numb_a._Number__sign_invert()
                numb_b._Number__sign_invert()
                return -(numb_a+numb_b)
            case ('-', '+'):
                if -numb_a > numb_b:
                    return -((-numb_a)-numb_b)
                elif -numb_a < numb_b:
                    return numb_b-(-numb_a)
                else:
                    return Rational('0', {'max float part':operand_a._Rational__flags['max float part']})
            case ('+', '-'):
                if numb_a > -numb_b:
                    return numb_a-(-numb_b)
                elif numb_a < (-numb_b):
                    return -((-numb_b)-numb_a)
                else:
                    return Rational('0', {'max float part':operand_a._Rational__flags['max float part']})
            case _:
                if operand_a.references['float part'] != '0' or operand_b.references['float part'] != '0':
                    float_a = operand_a.references['float part']
                    float_b = operand_b.references['float part']            
                    float_part = Rational(float_a, {'max float part':operand_a._Rational__flags['max float part']}) + Rational(float_b, {'max float part':operand_a._Rational__flags['max float part']})
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
                    integer_part = Rational(operand_a.references['integer part'])+Rational(operand_b.references['integer part'], {'max float part':operand_a._Rational__flags['max float part']})+reminder
                    return Rational(integer_part.value+'.'+calculated_float, {'max float part':operand_a._Rational__flags['max float part']})
                if operand_a.references['integer part'] == '0':
                    return operand_b
                elif operand_b.references['integer part'] == '0':
                    return operand_a
                else:
                    calculated = ''
                    reminder = 0
                    int_a = operand_a.references['integer part'][::-1]
                    int_b = operand_b.references['integer part'][::-1]
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
                    return Rational(calculated[::-1], {'max float part':operand_a._Rational__flags['max float part']})