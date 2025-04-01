import NelMath
from NelMath.objects.math_base.Operators.Operator import Operator

class OperatorMultiply(Operator):
    @staticmethod
    def execute(operand_a: any, operand_b: any):        
        from NelMath.objects import Rational, Fraction
        if type(operand_a) in {int, float, str}: operand_a=Rational(operand_a)
        if type(operand_b) in {int, float, str}: operand_b=Rational(operand_b)
        if isinstance(operand_b, NelMath.objects.math_constructions.Equation):
            from NelMath.objects.math_constructions.Equation import Equation
            return operand_b.__mul__(operand_a)
        if isinstance(operand_a, Rational):
            if isinstance(operand_b, Rational):
                from NelMath.objects.math_base.Operators.Multiply.OperatorMultiplyRR import OperatorMultiplyRR
                return OperatorMultiplyRR.execute(operand_a, operand_b)
            if isinstance(operand_b, Fraction):
                from NelMath.objects.math_base.Operators.Multiply.OperatorMultiplyFR import OperatorMultiplyFR
                return OperatorMultiplyFR.execute(operand_b, operand_a)
        if isinstance(operand_a, Fraction):
            if isinstance(operand_b, Rational):
                from NelMath.objects.math_base.Operators.Multiply.OperatorMultiplyFR import OperatorMultiplyFR
                return OperatorMultiplyFR.execute(operand_a, operand_b)
            if isinstance(operand_b, Fraction):
                from NelMath.objects.math_base.Operators.Multiply.OperatorMultiplyFF import OperatorMultiplyFF
                return OperatorMultiplyFF.execute(operand_a, operand_b)
        raise NotImplementedError(f'Operation between {type(operand_a)} and {type(operand_b)} not implemented yet')


