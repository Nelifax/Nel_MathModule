from NelMath.objects.math_base.Operators.Operator import Operator

class OperatorLog(Operator):    
    @staticmethod
    def execute(operand: any, base:any):         
        from NelMath.objects import Rational, Fraction
        if type(operand) in {int, float, str}: operand=Rational(operand)
        if type(base) in {int, float, str}: exponent=Rational(base)
        if isinstance(operand, Rational):
            from NelMath.objects.math_base.Operators.Logx.OperatorLogR import OperatorLogR
            return OperatorLogR.execute(operand, base)


