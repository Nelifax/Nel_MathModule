from NelMath.objects.math_base.Operators.Mod.OperatorMod import OperatorMod
from NelMath.objects.math_base.Fraction import Fraction

class OperatorModF(OperatorMod):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Fraction):
        operand_a.improper_view()
        operand_b.improper_view()        
        from NelMath.objects.math_base.Operators.Division.OperatorTruedivFF import OperatorTruedivFF
        preFraction=OperatorTruedivFF.execute(operand_a, operand_b)
        return Fraction([preFraction.references['numerator'], preFraction.references['denominator']])