from NelMath.objects.math_base.Operators.Minus.OperatorMinus import OperatorMinus
from NelMath.objects.math_base.Fraction import Fraction

class OperatorMinusFF(OperatorMinus):    
    @staticmethod
    def execute(operand_a: Fraction, operand_b: Fraction):
        operand_a.improper_view()
        operand_b.improper_view()
        if operand_a.references['denominator']==operand_b.references['denominator']:
            match(operand_a.sign, operand_b.sign):
                case ('-','-'):
                    if operand_a.references['numerator'] > operand_b.references['numerator']:
                        return -Fraction([operand_a.references['numerator']-operand_b.references['numerator'],operand_a.references['denominator']])
                    elif operand_a.references['numerator'] < operand_b.references['numerator']:
                        return Fraction([operand_b.references['numerator']-operand_a.references['numerator'],operand_a.references['denominator']])
                    else: return Fraction(0)
                case ('-','+'):
                    return -Fraction([operand_a.references['numerator']+operand_b.references['numerator'],operand_a.references['denominator']])
                case ('+','-'):
                    return Fraction([operand_a.references['numerator']+operand_b.references['numerator'],operand_a.references['denominator']])
                case _:
                    if operand_a.references['numerator'] > operand_b.references['numerator']:
                        return Fraction([operand_a.references['numerator']-operand_b.references['numerator'],operand_a.references['denominator']])
                    elif operand_a.references['numerator'] < operand_b.references['numerator']:
                        return -Fraction([operand_b.references['numerator']-operand_a.references['numerator'],operand_a.references['denominator']])
                    else: return Fraction(0)
        else:
            operator_a_denominator=operand_a.references['denominator']
            operand_a._Fraction__transform_mul(operand_b.references['denominator'])
            operand_b._Fraction__transform_mul(operator_a_denominator)
            return OperatorMinusFF.execute(operand_a, operand_b)