from NelMath.objects.math_base.Operators.Plus.OperatorPlus import OperatorPlus
from NelMath.objects.math_base.Fraction import Fraction

class OperatorPlusFF(OperatorPlus):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Fraction):      
        operand_a.improper_view()
        operand_b.improper_view()
        match (operand_a.sign, operand_b.sign):
            case ('-', '-'):
                numerator=-(operand_a.references['numerator']*operand_b.references['denominator']+operand_b.references['numerator']*operand_a.references['denominator'])
                denominator=operand_a.references['denominator']*operand_b.references['denominator']
            case ('-', '+'):
                numerator=operand_b.references['numerator']*operand_a.references['denominator']-operand_a.references['numerator']*operand_b.references['denominator']
                denominator=operand_a.references['denominator']*operand_b.references['denominator']
            case ('+', '-'):
                numerator=operand_a.references['numerator']*operand_b.references['denominator']-operand_b.references['numerator']*operand_a.references['denominator']
                denominator=operand_a.references['denominator']*operand_b.references['denominator']
            case _:
                numerator=operand_a.references['numerator']*operand_b.references['denominator']+operand_b.references['numerator']*operand_a.references['denominator']
                denominator=operand_a.references['denominator']*operand_b.references['denominator']
        return Fraction([numerator, denominator], operand_a._Fraction__flags)