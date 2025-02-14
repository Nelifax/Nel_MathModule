from NelMath.objects.math_base.Operators.Pow.OperatorPow import OperatorPow
from NelMath.objects.math_base.Fraction import Fraction

class OperatorPowF(OperatorPow):    
    @staticmethod
    def execute(operand: Fraction, exponent: any, modulo: any = None):
        from NelMath.objects.math_base.Operators.Pow.OperatorPowR import OperatorPowR
        operand.improper_view()
        numerator=operand.references['numerator'].copy()
        denominator=operand.references['denominator'].copy()
        if exponent<0:
            return Fraction([OperatorPowR.execute(denominator, -exponent, modulo), OperatorPowR.execute(numerator, -exponent, modulo)], operand._Fraction__flags)
        else:
            return Fraction([OperatorPowR.execute(numerator, exponent, modulo), OperatorPowR.execute(denominator, exponent, modulo)], operand._Fraction__flags)