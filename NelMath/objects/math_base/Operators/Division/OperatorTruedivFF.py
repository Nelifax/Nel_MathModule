from NelMath.objects.math_base.Operators.Division.OperatorTruediv import OperatorTruediv
from NelMath.objects.math_base.Fraction import Fraction

class OperatorTruedivFF(OperatorTruediv):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Fraction):      
        operand_a.improper_view()
        operand_b.improper_view()    
        if operand_a.sign==operand_b.sign:
            return Fraction([operand_a.references['numerator']*operand_b.references['denominator'], operand_a.references['denominator']*operand_b.references['numerator']])
        else:
            return -Fraction([operand_a.references['numerator']*operand_b.references['denominator'], operand_a.references['denominator']*operand_b.references['numerator']])