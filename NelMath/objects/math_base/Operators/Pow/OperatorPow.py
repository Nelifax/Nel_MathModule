from NelMath.objects.math_base.Operators.Operator import Operator

class OperatorPow(Operator):    
    @staticmethod
    def execute(operand: any, exponent: any, modulo: any = None):         
        from NelMath.objects import Rational, Fraction
        if type(operand) in {int, float, str}: operand=Rational(operand)
        if type(exponent) in {int, float, str}: exponent=Rational(exponent)
        if type(modulo) in {int, float, str}: modulo=Rational(modulo)
        if isinstance(exponent, Rational) and exponent.references['float part']=='0':
            if isinstance(operand, Rational):            
                if operand.references['float part']=='0':
                    from NelMath.objects.math_base.Operators.Pow.OperatorPowR import OperatorPowR
                    return OperatorPowR.execute(operand, exponent, modulo)
                else:
                    from NelMath.objects.math_base.Operators.Pow.OperatorPowF import OperatorPowF
                    return Rational((OperatorPowF.execute(Fraction(operand), exponent, modulo)).value)
            if isinstance(operand, Fraction):            
                from NelMath.objects.math_base.Operators.Pow.OperatorPowF import OperatorPowF
                return OperatorPowF.execute(operand, exponent, modulo)
        if isinstance(exponent, Rational) and exponent.references['float part']!='0':
            exponent=Fraction(exponent)
        if isinstance(exponent, Fraction):
            pass
        raise NotImplementedError(f'Operation for {type(operand)} not implemented yet')


