from NelMath.objects.math_base.Operators.Operator import Operator

class OperatorPow(Operator):    
    @staticmethod
    def execute(operand: any, exponent: any, modulo: any = None):         
        from NelMath.objects import Rational, Fraction
        if type(operand) in {int, float, str}: operand=Rational(operand)
        if type(exponent) in {int, float, str}: exponent=Rational(exponent)
        if type(modulo) in {int, float, str}: modulo=Rational(modulo)
        if isinstance(exponent, Rational):
            if isinstance(operand, Rational):
                from NelMath.objects.math_base.Operators.Pow.OperatorPowR import OperatorPowR
                return OperatorPowR.execute(operand, exponent, modulo)
            if isinstance(operand, Fraction):            
                from NelMath.objects.math_base.Operators.Pow.OperatorPowF import OperatorPowF
                return OperatorPowF.execute(operand, exponent, modulo)
        if isinstance(exponent, Rational) and exponent.references['float part']!='0':
            exponent=Fraction(exponent)
        if isinstance(exponent, Fraction):
            from NelMath.objects.math_base.Operators.Pow.OperatorPowR import OperatorPowR
            preresult=OperatorPowR.execute(operand, exponent.references['integer part'], modulo)
            exponent=exponent-exponent.references['integer part']            
            exponent.improper_view()
            return preresult*OperatorPowR.execute(operand, exponent.references['numerator'], modulo).nroot(exponent.references['denominator'])
        raise NotImplementedError(f'Operation for {type(operand)} not implemented yet')


