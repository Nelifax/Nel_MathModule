from NelMath.objects.math_base.Operators.Multiply.OperatorMultiply import OperatorMultiply
from NelMath.objects import Rational, Fraction

class OperatorMultiplyFR(OperatorMultiply):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Rational):
        operand_a.improper_view()
        if operand_a.sign==operand_b.sign:
            return Fraction([operand_a.references['numerator']*operand_b, operand_a.references['denominator']])