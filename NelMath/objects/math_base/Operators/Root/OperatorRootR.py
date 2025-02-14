from NelMath.objects.math_base.Operators.Root.OperatorRoot import OperatorRoot
from NelMath.objects.math_base.Rational import Rational

class OperatorRootR(OperatorRoot):    
    @staticmethod
    def execute(operand: Rational, exponent: any, precision=0):
        if operand.sign == '-' and exponent%2==0:
            raise TimeoutError('NOT IMPLEMENTED YET')        
        numb = operand.copy()
        result = Rational(1, {'max float part':operand._Rational__flags['max float part']})
        border = Rational('0.'+'0'*(precision+int(operand._Rational__flags['max float part'])-1)+'1', {'max float part':operand._Rational__flags['max float part']})
        while True:
            result_next = ( ( (exponent - 1)*result) + numb/( result**(exponent - 1) ) )/exponent
            if abs(result_next - result) < border:
                break
            result = result_next
        return result._Rational__self_round_float()