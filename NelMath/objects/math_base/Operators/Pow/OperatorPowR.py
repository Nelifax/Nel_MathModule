from NelMath.objects.math_base.Operators.Pow.OperatorPow import OperatorPow
from NelMath.objects.math_base.Rational import Rational

class OperatorPowR(OperatorPow):    
    @staticmethod
    def execute(operand: Rational, exponent: any, modulo: any = None):
        numb = operand.copy()
        exp = exponent.copy()
        if exp.references['float part'] == '0':
            if exp.references['integer part'] == '0':
                return Rational(1, {'max float part':operand._Rational__flags['max float part']})
            if modulo==None:
                if exp.sign == '+':
                    if exp==2:
                        return numb.__mul__(numb)
                    result=Rational(1)
                    while exp > 0:
                        if exp % 2 == 1:
                            result=result.__mul__(numb)
                        numb=numb**2
                        exp //= 2
                    return result
                else:
                    exp._Rational__sign_invert()
                    return 1/(numb.__pow__(exp, None))
            else:
                if exp.sign == '+':
                    if numb>modulo:
                        numb=numb%modulo
                    result=Rational(1)
                    while exp > 0:
                        if exp % 2 == 1:
                            result=result.__mul__(numb)%modulo
                        numb=numb**2
                        exp //= 2
                        if numb>modulo:
                            numb=numb%modulo
                    result=result%modulo
                    return result if result>0 else result+modulo
                else:
                    from NelMath.functions.number_functions import gcd, is_prime
                    if gcd(numb, modulo)!=1:
                        raise TimeoutError('gcd(elem,mod)!=0')
                    if is_prime(modulo):
                        return numb.__pow__(modulo-2, modulo)%modulo
                    else:
                        from NelMath.functions.number_functions import euler_phi
                        return numb.__pow__(euler_phi(modulo)-1, modulo)%modulo
        else:
            raise TimeoutError('NOT IMPLEMENTED YET')  