from NelMath.objects.math_base.Operators.Multiply.OperatorMultiply import OperatorMultiply
from NelMath.objects.math_base.Rational import Rational

class OperatorMultiplyRR(OperatorMultiply):    
    @staticmethod
    def execute(operand_a: Rational, operand_b: Rational):
        numb_a = operand_a.copy()
        numb_b = operand_b.copy()        
        match (numb_a.sign, numb_b.sign):
            case ('+', '+'):
                invert = False
            case ('-', '-'):
                invert = False
            case _:
                invert = True
        if abs(numb_b)==10:
            if numb_a.references['float part'] != '0':
                return -Rational(numb_a.references['integer part']+numb_a.references['float part'][0]+'.'+numb_a.references['float part'][1:], {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(numb_a.references['integer part']+numb_a.references['float part'][0]+'.'+numb_a.references['float part'][1:], {'max float part':operand_a._Rational__flags['max float part']})
            else:
                return -Rational(numb_a.references['integer part']+'0', {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(numb_a.references['integer part']+'0', {'max float part':operand_a._Rational__flags['max float part']})
        int_a = int(numb_a.references['integer part'])
        int_b = int(numb_b.references['integer part'])
        float_a = int(numb_a.references['float part'])
        float_b = int(numb_b.references['float part']) 
        int_part = int_a * int_b
        if float_a == 0 and float_b == 0:
            return -Rational(str(int_part), {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(str(int_part), {'max float part':operand_a._Rational__flags['max float part']})    
        float_part = 0
        if float_a != 0 and float_b == 0:#(a+0.b)*(c+0)=ac+0.b*c
            additional_deg=len(numb_a.references['float part']) - len(numb_a.references['float part'].lstrip('0'))
            deg_a = len(numb_a.references['float part'])
            float_part = str(float_a*int_b)
            while len(float_part)<=deg_a+additional_deg:
               float_part = '0' + float_part
            to_int = int(float_part[0:-deg_a])
            float_part = float_part[-deg_a:]
            return -Rational(str(int_part+to_int)+'.'+float_part, {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(str(int_part+to_int)+'.'+float_part, {'max float part':operand_a._Rational__flags['max float part']}) 
        if float_a == 0 and float_b != 0:#(a+0)*(c+0.d)=ac+a*0.d
            additional_deg=len(numb_b.references['float part']) - len(numb_b.references['float part'].lstrip('0'))
            deg_b = len(numb_b.references['float part'])
            float_part = str(float_b*int_a)
            while len(float_part)<=deg_b+additional_deg:
               float_part = '0' + float_part
            to_int = int(float_part[0:-deg_b])
            float_part = float_part[-deg_b:]
            return -Rational(str(int_part+to_int)+'.'+float_part, {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(str(int_part+to_int)+'.'+float_part, {'max float part':operand_a._Rational__flags['max float part']})
        if float_a != 0 and float_b != 0:#(a+0.b)*(c+0.d)=ac+a*0.d+0.b*c+0.d*0.b
            #additional_deg=(len(numb_a.references['float part']) - len(numb_a.references['float part'].lstrip('0'))) + (len(numb_b.references['float part']) - len(numb_b.references['float part'].lstrip('0')))
            deg_a = len(numb_a.references['float part'])
            deg_b = len(numb_b.references['float part'])
            float_part = str(float_a * float_b)
            int_part = Rational(str(int_part), {'max float part':operand_a._Rational__flags['max float part']})
            while len(float_part) < deg_a+deg_b:
                float_part = '0'+float_part            
            float_part = Rational('0.'+float_part, {'max float part':operand_a._Rational__flags['max float part']})
            float_part_one = str(float_a*int_b)
            float_part_two = str(float_b*int_a)
            while len(float_part_one) < deg_a:
                float_part_one = '0'+float_part_one  
            while len(float_part_two) < deg_b:
                float_part_two = '0'+float_part_two  
            float_part_one = Rational(float_part_one[0:-deg_a]+'.'+float_part_one[-deg_a:], {'max float part':operand_a._Rational__flags['max float part']})
            float_part_two = Rational(float_part_two[0:-deg_b]+'.'+float_part_two[-deg_b:], {'max float part':operand_a._Rational__flags['max float part']})
            float_part = float_part + float_part_one + float_part_two
            int_part = int_part+Rational(float_part.references['integer part'], {'max float part':operand_a._Rational__flags['max float part']})
            return -Rational(int_part.references['integer part'] + '.' + float_part.references['float part'], {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(int_part.references['integer part'] + '.' + float_part.references['float part'], {'max float part':operand_a._Rational__flags['max float part']}) 