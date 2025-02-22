from NelMath.objects.math_base.Operators.Root.OperatorRoot import OperatorRoot
from NelMath.objects.math_base.Rational import Rational

class OperatorRootR(OperatorRoot):    
    @staticmethod
    def execute(operand: Rational, exponent: any, precision=0):
        if operand.sign == '-' and exponent%2==0:
            raise TimeoutError('NOT IMPLEMENTED YET')        
        numb = operand.copy()
        startpoint_int_bin=bin(int(operand.references['integer part']))[2:]
        if len(startpoint_int_bin)>int(exponent):
            startpoint_int=str(int(startpoint_int_bin[:len(startpoint_int_bin)//int(exponent)+1],2))
        else:
            startpoint_int='1'
        if operand.references['float part']!='0':
            startpoint=startpoint_int+operand.references['float part']
        else:
            startpoint=startpoint_int
        result = Rational(startpoint, {'max float part':operand._Rational__flags['max float part']*2})
        border = Rational('0.'+'0'*(precision+int(operand._Rational__flags['max float part'])-1)+'1', {'max float part':operand._Rational__flags['max float part']})
        from NelMath.objects.math_base.Operators.Division.OperatorTruedivRR import OperatorTruediv
        while True:
            result_next = ( ( (exponent - 1)*result) + numb/( result**(exponent - 1) ) ) / exponent
            if abs(result_next - result) < border:
                break
            result = result_next
        result = Rational(result.references['integer part']+'.'+result.references['float part'][0:operand._Rational__flags['max float part']+1], {'max float part':operand._Rational__flags['max float part']})
        return result._Rational__self_round_float()