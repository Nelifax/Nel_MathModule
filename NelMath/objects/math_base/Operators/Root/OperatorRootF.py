from NelMath.objects.math_base.Operators.Root.OperatorRoot import OperatorRoot
from NelMath.objects.math_base.Fraction import Fraction

class OperatorRootF(OperatorRoot):    
    @staticmethod
    def execute(operand: Fraction, exponent: any, precision=0):
        if operand.sign == '-' and exponent%2==0:
            raise TimeoutError('NOT IMPLEMENTED YET')        
        fraction = operand.copy()  
        fraction.improper_view()
        from NelMath.objects.math_base.Operators.Root.OperatorRootR import OperatorRootR
        numerator = OperatorRootR.execute(fraction.references['numerator'], exponent, precision)
        denominator = OperatorRootR.execute(fraction.references['denominator'], exponent, precision)         
        return Fraction([numerator, denominator], fraction._Fraction__flags)