from NelMath.objects.math_base.Operators.Division.OperatorFloordiv import OperatorFloordiv
from NelMath.objects import Rational, Fraction

class OperatorFloordivFR(OperatorFloordiv):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Rational):
        operand_a.improper_view()
        from NelMath.objects.math_base.Operators.Division.OperatorTruedivFR import OperatorTruedivFR
        if operand_a.sign==operand_b.sign:
            return OperatorTruedivFR.execute(operand_a, operand_b).references['integer part']
        else:
            return -OperatorTruedivFR.execute(operand_a, operand_b).references['integer part']