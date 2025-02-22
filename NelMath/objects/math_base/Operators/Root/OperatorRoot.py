from NelMath.objects.math_base.Operators.Operator import Operator

class OperatorRoot(Operator):    
    @staticmethod
    def execute(operand: any, exponent: any, precision: int = 0):         
        from NelMath.objects import Rational, Fraction
        if type(operand) in {int, float, str}: operand=Rational(operand)
        if type(exponent) in {int, float, str}: exponent=Rational(exponent)
        if exponent==1:
            return operand
        if isinstance(exponent, Rational) and exponent.references['float part']=='0' and exponent>1:
            if isinstance(operand, Rational):   
                exponent._Rational__flags['max float part']=operand._Rational__flags['max float part']*2
                from NelMath.objects.math_base.Operators.Root.OperatorRootR import OperatorRootR
                return OperatorRootR.execute(operand, exponent)
            if isinstance(operand, Fraction):            
                from NelMath.objects.math_base.Operators.Root.OperatorRootF import OperatorRootF
                return OperatorRootF.execute(operand, exponent)
        raise NotImplementedError(f'Operation for {type(operand)} not implemented yet')


