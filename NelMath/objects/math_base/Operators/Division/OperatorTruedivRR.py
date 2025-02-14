from NelMath.objects.math_base.Operators.Division.OperatorTruediv import OperatorTruediv
from NelMath.objects.math_base.Rational import Rational

class OperatorTruedivRR(OperatorTruediv):    
    @staticmethod
    def execute(operand_a: Rational, operand_b: Rational):
        numb_a = operand_a.copy()
        numb_b = operand_b.copy()
        if operand_b.value == '0':
            raise ZeroDivisionError()
        if operand_a.value == '0':
            return Rational(0, {'max float part':operand_a._Rational__flags['max float part']})
        match (numb_a.sign, numb_b.sign):
            case ('+', '+'):
                invert = False
            case ('-', '-'):
                invert = False
            case _:
                invert = True
        if numb_a.sign == '-':
            numb_a._Rational__sign_invert()
        if numb_b.sign == '-':
            numb_b._Rational__sign_invert()
        if operand_b.value == '10':
            float_part = numb_a.references['float part']
            integer_part = numb_a.references['integer part']
            if integer_part != '0':
                float_part=integer_part[-1]+float_part
                integer_part = integer_part[0:-1]
                return -Rational(integer_part+'.'+float_part, {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(integer_part+'.'+float_part, {'max float part':operand_a._Rational__flags['max float part']})
            else:
                return -Rational('0.0'+float_part, {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational('0.0'+float_part, {'max float part':operand_a._Rational__flags['max float part']})
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
            return -Rational(numb, {'max float part':operand_a._Rational__flags['max float part']}) if invert else Rational(numb, {'max float part':operand_a._Rational__flags['max float part']})
        if '.' not in numb:
            numb = numb+'.0'
        while len(result_float)<operand_a._Rational__flags['max float part']+1:            
            deg = 0
            while numerator<denominator:
                if len(numb)!=0 and numb[0]!='.':
                    if result=='':
                        numerator = Rational(numerator.references['integer part']+numb[0], {'max float part':operand_a._Rational__flags['max float part']})
                        numb = numb[1:]
                    else:
                        numerator = Rational(numerator.references['integer part']+numb[0], {'max float part':operand_a._Rational__flags['max float part']})
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
                        numerator = Rational(numerator.references['integer part']+'0', {'max float part':operand_a._Rational__flags['max float part']})
                        numb = numb[1:]
                    else:
                        numerator = Rational(numerator.references['integer part']+'0', {'max float part':operand_a._Rational__flags['max float part']})
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
        result = Rational(result, {'max float part':operand_a._Rational__flags['max float part']})._Rational__self_round_float()
        return -result if invert else result