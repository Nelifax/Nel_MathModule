from NelMath.objects.math_base.Operators.Division.OperatorFloordiv import OperatorFloordiv
from NelMath.objects.math_base.Rational import Rational

class OperatorFloordivRR(OperatorFloordiv):    
    @staticmethod
    def execute(operand_a: Rational, operand_b: Rational):
        if not isinstance(operand_b, Rational):
            operand_b = Rational(operand_b, {'max float part':operand_a._Rational__flags['max float part']})            
        numb_a = operand_a.copy()
        numb_b = operand_b.copy() 
        match (numb_a.sign, numb_b.sign):
            case ('+', '+'):
                invert = False
            case ('-', '-'):
                invert = False
            case _:
                invert = True 
        from NelMath.objects.math_base.Operators.Division.OperatorTruedivRR import OperatorTruedivRR
        preresult=OperatorTruedivRR().execute(numb_a, numb_b)
        result = Rational(preresult.references['integer part'], {'max float part':operand_a._Rational__flags['max float part']})
        from NelMath.properties.settings_handler import SettingsHandler
        settings=SettingsHandler()
        result = result+1 if settings.get('mm_number_floordiv_ceiling_up') and Rational(preresult.references['float part'])>0 and invert else result
        return -result if invert else result