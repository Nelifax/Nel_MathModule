from NelMath.objects.math_base.Operators.Division.OperatorFloordiv import OperatorFloordiv
from NelMath.objects.math_base.Fraction import Fraction

class OperatorFloordivFF(OperatorFloordiv):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Fraction):      
        operand_a.improper_view()
        operand_b.improper_view()    
        from NelMath.objects.math_base.Operators.Division.OperatorTruedivFF import OperatorTruedivFF
        if operand_a.sign==operand_b.sign:
            return OperatorTruedivFF.execute(operand_a, operand_b).references['integer part']
        else:
            return -OperatorTruedivFF.execute(operand_a, operand_b).references['integer part']