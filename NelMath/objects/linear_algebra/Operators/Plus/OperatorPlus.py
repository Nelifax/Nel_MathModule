from NelMath.objects.linear_algebra.Operators.Operator import Operator

class OperatorPlus(Operator):    
    @staticmethod
    def execute(operand_a: any, operand_b: any):        
        from NelMath.objects import Vector, Matrix, Rational
        if type(operand_a) in {int, float, str}: operand_a=Rational(operand_a)
        if type(operand_b) in {int, float, str}: operand_b=Rational(operand_b)
        if isinstance(operand_a, Rational):
            if isinstance(operand_b, Rational):
                from NelMath.objects.math_base.Operators.Plus.OperatorPlusRR import OperatorPlusRR
                return OperatorPlusRR.execute(operand_a, operand_b)
            if isinstance(operand_b, Fraction):
                from NelMath.objects.math_base.Operators.Plus.OperatorPlusFR import OperatorPlusFR
                return OperatorPlusFR.execute(operand_b, operand_a)
        if isinstance(operand_a, Fraction):
            if isinstance(operand_b, Rational):
                from NelMath.objects.math_base.Operators.Plus.OperatorPlusFR import OperatorPlusFR
                return OperatorPlusFR.execute(operand_a, operand_b)
            if isinstance(operand_b, Fraction):
                from NelMath.objects.math_base.Operators.Plus.OperatorPlusFF import OperatorPlusFF
                return OperatorPlusFF.execute(operand_a, operand_b)
        raise NotImplementedError(f'Operation between {type(operand_a)} and {type(operand_b)} not implemented yet')