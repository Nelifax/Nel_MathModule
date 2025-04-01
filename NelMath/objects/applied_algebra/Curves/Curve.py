__all__=['Curve']

from NelMath.properties.settings_handler import SettingsHandler

class Curve():
    __qualname__='Curve'
    __module__='Curve'
    def __new__(cls, params:str|list, modulo=None, flags=None): 
        ccls=cls
        if cls is not Curve:
            return super().__new__(cls) 
        params=Curve.define_curve_params(params)
        settings=SettingsHandler()
        is_elliptic, elliptic_type=Curve.is_elliptic(params)
        if is_elliptic:
            from NelMath.objects.applied_algebra.Curves.EllipticCurve import EllipticCurve
            if flags!=None:
                flags.update({'curve view':'elliptic', 'curve type':elliptic_type})
            else:
                flags={'curve view':'elliptic', 'curve type':elliptic_type}
            return EllipticCurve(params, modulo, flags)

    @staticmethod
    def find_discriminant(a1, a2, a3, a4, a6):
        d2 = a1**2+4*a2
        d4 = 2*a4+a1*a3
        d6 = a3**2+4*a6
        d8 = a1**2*a6+4*a2*a6-a1*a3*a4+a2*a3**2-a4**2
        c4 = d2**2-24*d4    
        det = 9*d2*d4*d6 - d2**2*d8 - 8*d4**3 - 27*d6**2
        return (det, c4)

    @staticmethod
    def is_elliptic(params):
        """
        if a_i define an elliptic curve - returns tuple:(true, eliptic) or typle:(False, singular:{type}), where type can be [node, casp] 
        """
        det, c4 = Curve.find_discriminant(*params)
        if det!=0:
            return (True, 'eliptic')
        else:
            if det==0 and c4!=0:
                return (False, 'singular:node')
            else:
                return (False, 'singular:casp')

    @staticmethod
    def define_curve_params(params):
        if type(params)==list:
            if len(params)!=5:
                raise TimeoutError()
            return params
