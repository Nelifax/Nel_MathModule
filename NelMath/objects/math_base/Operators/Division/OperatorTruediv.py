from NelMath.objects.math_base.Operators.Operator import Operator

class OperatorTruediv(Operator):
    @staticmethod
    def execute(operand_a: any, operand_b: any):        
        from NelMath.objects import Rational, Fraction
        if type(operand_a) in {int, float, str}: operand_a=Rational(operand_a)
        if type(operand_b) in {int, float, str}: operand_b=Rational(operand_b)
        if isinstance(operand_a, Rational):
            if isinstance(operand_b, Rational):
                from NelMath.objects.math_base.Operators.Division.OperatorTruedivRR import OperatorTruedivRR
                return OperatorTruedivRR.execute(operand_a, operand_b)
            if isinstance(operand_b, Fraction):
                from NelMath.objects.math_base.Operators.Division.OperatorTruedivFR import OperatorTruedivFR
                return (OperatorTruedivFR.execute(operand_b, operand_a))**(-1)
        if isinstance(operand_a, Fraction):
            if isinstance(operand_b, Rational):
                from NelMath.objects.math_base.Operators.Division.OperatorTruedivFR import OperatorTruedivFR
                return OperatorTruedivFR.execute(operand_a, operand_b)
            if isinstance(operand_b, Fraction):
                from NelMath.objects.math_base.Operators.Division.OperatorTruedivFF import OperatorTruedivFF
                return OperatorTruedivFF.execute(operand_a, operand_b)
        raise NotImplementedError(f'Operation between {type(operand_a)} and {type(operand_b)} not implemented yet')


