from NelMath.objects.math_base.Operators.Logx.OperatorLog import OperatorLog
from NelMath.objects.math_base.Rational import Rational

class OperatorLogR(OperatorLog):    
    @staticmethod
    def execute(operand: Rational, base: any):          
        if operand==base: return Rational(1)
        if operand==1: return Rational(0)
        from NelMath.properties.settings_handler import SettingsHandler
        settings=SettingsHandler()
        max_float_part=settings.get('mm_max_float_part')
        if base==2:
            k = Rational(operand.bit_length() - 1,{'max float part':max_float_part+3})
            frac = Rational(operand/Rational(2)**k,{'max float part':max_float_part+3})
            result = k
            f = frac
            x = Rational(0,{'max float part':max_float_part+3})
            p = Rational(0.5,{'max float part':max_float_part+3})
            for _ in range(4*max_float_part):
                f = Rational(f * f,{'max float part':max_float_part*2})
                f=f._Rational__self_round_float()
                if f >= 2:
                    f /= 2
                    x += p
                p /= 2
            result=Rational(result + x,{'max float part':max_float_part})
            return result._Rational__self_round_float()
        else:
            return operand.log(2)/Rational(base).log(2)
