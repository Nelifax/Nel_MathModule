from NelMath.objects.math_base.Operators.Division.OperatorTruediv import OperatorTruediv
from NelMath.objects import Rational, Fraction

class OperatorTruedivFR(OperatorTruediv):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Rational):
        operand_a.improper_view()   
        if operand_a.sign==operand_b.sign:
            return Fraction([operand_a.references['numerator'], operand_a.references['denominator']*operand_b])
        else:
            return -Fraction([operand_a.references['numerator'], operand_a.references['denominator']*operand_b])