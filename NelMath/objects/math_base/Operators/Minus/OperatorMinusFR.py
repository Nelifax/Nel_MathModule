from NelMath.objects.math_base.Operators.Minus.OperatorMinus import OperatorMinus
from NelMath.objects import Rational, Fraction

class OperatorMinusFR(OperatorMinus):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Rational):
        operand_a.improper_view()
        operand_b=Fraction(operand_b, {'auto-simplify': False, 'max float part': operand_a._Fraction__flags['max float part'], 'type changing':False})
        from NelMath.objects.math_base.Operators.Minus.OperatorMinusFF import OperatorMinusFF
        return OperatorMinusFF.execute(operand_a, operand_b)