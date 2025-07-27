from NelMath.objects.math_base.Operators.Logx.OperatorLog import OperatorLog
from NelMath.objects.math_base.Rational import Rational

class OperatorLnX(OperatorLog):    
    @staticmethod
    def execute(operand: Rational, precision=0):
        from NelMath.objects.math_base.Constant import Constant
        if operand <= '0':
            raise TimeoutError()
        e=Constant()
        return operand.log()/e.e().log(2)