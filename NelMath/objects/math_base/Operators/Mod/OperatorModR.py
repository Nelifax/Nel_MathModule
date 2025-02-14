from NelMath.objects.math_base.Operators.Mod.OperatorMod import OperatorMod
from NelMath.objects.math_base.Rational import Rational

class OperatorModR(OperatorMod):    
    @staticmethod
    def execute(operand_a: Rational, operand_b: any):
        numb_a = operand_a.copy()
        if numb_a == 0:
            return Rational(0, {'max float part':operand_a._Rational__flags['max float part']})
        numb_b = operand_b.copy()        
        if numb_b == 0:
            raise TimeoutError()
        if operand_b==2 and operand_a.references['float part']=='0':
            if operand_a.references['integer part'][-1] in ['0','2','4','6','8']:
                return Rational(0, {'max float part':operand_a._Rational__flags['max float part']})
            else:                
                return Rational(1, {'max float part':operand_a._Rational__flags['max float part']})
        inverted = False
        if numb_b.sign == '-':
            inverted = True
        deg=0
        while numb_b.references['float part'] != '0':
            numb_b*=10
            numb_a*=10
            deg+=1 
        if numb_b == 1:
            return Rational(0, {'max float part':operand_a._Rational__flags['max float part']})
        numb_a = numb_a-numb_b*(numb_a//numb_b)
        return numb_a/10**deg    