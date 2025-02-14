from NelMath.objects.math_base.Operators.Plus.OperatorPlus import OperatorPlus
from NelMath.objects import Rational, Fraction

class OperatorPlusFR(OperatorPlus):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Rational):
        operand_a.improper_view()
        match (operand_a.sign, operand_b.sign):
            case ('-', '-'):
                operand_b._Rational__sign_invert()
                numerator=-(operand_a.references['numerator']+operand_b*operand_a.references['denominator'])
            case ('-', '+'):
                numerator=operand_b*operand_a.references['denominator']-operand_a.references['numerator']
            case ('+', '-'):
                operand_b._Rational__sign_invert()
                numerator=operand_a.references['numerator']-operand_b*operand_a.references['denominator']
            case _:
                numerator=operand_a.references['numerator']+operand_b*operand_a.references['denominator']
        return Fraction([numerator, operand_a.references['denominator']], operand_a._Fraction__flags)