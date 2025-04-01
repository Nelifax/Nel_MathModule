__all__ = ['Point']
from NelMath.objects.applied_algebra.Curves.Point import Point
from NelMath.objects.math_base.Rational import Rational

class EllipticCurvePoint(Point):
    def __init__(self, coords:dict, modulo=None):
        for param in coords.keys():
            if type(param)!=str or len(param)>2:
                raise TimeoutError()
        self.params=coords.keys()
        for param, value in coords.items():
            if value=='∞':
                exec(f'self.{param}=value')
            else:
                exec(f'self.{param}=Rational(value)')
        self.modulo=modulo

    def __add__(self, other):
        self.is_points_on_one_curve(other)
        #ситуации с точкой в бесконечности
        if self.modulo!=other.modulo or self.a!=other.a or self.b!=other.b:
            raise TimeoutError()
        if self.y=='∞': 
            return other.copy()
        if other.y=='∞': 
            return self.copy()
        #стандартные ситуации расчётов
        if self.x==other.x and self.y==other.y:#удвоение точки
            if self.y==0:
                return EllipticCurvePoint.infinity(self.a, self.b, self.modulo)
            if self.modulo!=None:
                l=pow((pow(3*self.x**2+self.a,1,self.modulo)*pow(2*self.y,-1,self.modulo)),1,self.modulo) #наклон
                x3=pow(l**2-2*self.x,1,self.modulo)
                y3=pow(l*(self.x-x3)-self.y,1,self.modulo)
            else:
                l=(3*self.x**2+self.a)/(2*self.y) #наклон
                x3=l**2-2*self.x
                y3=l*(self.x-x3)-self.y
            return EllipticCurvePoint({'a':self.a, 'b':self.b, 'x':x3, 'y':y3, 'z':1},self.modulo)
        elif self.x==other.x and pow(self.y + other.y,1,self.modulo) == 0:#противоположные точки
            return EllipticCurvePoint.infinity(self.a, self.b, self.modulo)
        else:#ситуация разных точек
            if self.modulo!=None:
                l=pow(pow(other.y-self.y,1,self.modulo)*pow(other.x-self.x,1,self.modulo),1,self.modulo) #наклон
                x3=pow(l**2-self.x-other.x,1,self.modulo)
                y3=pow(l*(self.x-x3)-self.y,1,self.modulo)
            else:
                l=(other.y-self.y)/(other.x-self.x) #наклон
                x3=l**2-self.x-other.x
                y3=l*(self.x-x3)-self.y
            return EllipticCurvePoint({'a':self.a, 'b':self.b, 'x':x3, 'y':y3, 'z':1}, self.modulo)

    def __radd__(self, other):
        return other+self

    def __eq__(self, other):
        if self.params==other.params and self.modulo==other.modulo:
            for param in self.params:
                try:
                    check=getattr(self, param)==getattr(other, param) 
                    if not check:
                        return False
                except:
                    return False
            return True
        return False

    def __mul__(self, other):
        Q=EllipticCurvePoint.infinity(self.a, self.b, self.modulo)
        P=self.copy()
        if other==2:#удваивание точки
            return P+P
        k=list(str(bin(other))[2:])
        for bit in k:                
            Q=Q*2
            if bit=='1':
                Q=P+Q
        return Q

    def __rmul__(self, other):
        return other*self

    def is_points_on_one_curve(self, other):
        if self.modulo!=other.modulo or self.a!=other.a or self.b!=other.b:
            raise TimeoutError()

    def copy(self):
        result_params={}
        for param in self.params:
            result_params[param]=getattr(self, param)
        return EllipticCurvePoint(result_params, self.modulo)

    @staticmethod
    def infinity(a,b, modulo=None):
        return EllipticCurvePoint({'a':a,'b':b,'x':'∞','y':'∞','z':1}, modulo)

    def __repr__(self):
        r=[]
        for param in self.params:
            if param !='a' and param !='b':
                r.append(str(getattr(self, param)))
        r=':'.join(r)
        return f'[{r}]'

    def SumProj(a, b, q, x1, y1, z1, x2, y2, z2, mode='std', belongs=False):
        #ситуации с точкой в бесконечности
        if z1==0:
            return [x2, y2, z2]
        if z2==0:
            return [x1, y1, z1]
        if mode=='jacoby':#разные точки, проективные координаты якоби
            print('Used Jacoby (x=x/z^2, y=y/z^3) mode')
            #!!!реализация для кривых с проективными координатами в системе координат Якоби
            #то есть для таких, где x=x/z^2 и y=y/z^3
            #аналог для стандартных проективных, где x=x/z и y=y/z будет ниже        
            #вспомогательные переменные
            u1=(x1*z2^2)%q
            u2=(x2*z1^2)%q
            s1=(y1*z2^3)%q
            s2=(y2*z1^3)%q
            if u1==u2 and s1==s2:#ситуация равенства точек
                W=(3*x1^2+a*z1^2)%q
                S=(y1*z1)%q
                B=(x1*y1*S)%q
                H=(W^2-8*B)%q
                x3=(2*H*S)%q
                y3=(W*(4*B-H)-8*y1^2*S^2)%q
                z3=(8*s^3)%q
                return [x3, y3, z3]
            elif x1*pow(z1^2, -1, q)==x2*pow(z2^2, -1, q) and (y1*pow(z1^3, -1, q) + y2*pow(z2^3, -1, q)) % q == 0: #противоположные точки
                return [1, 1, 0] #как я понял, можно также вернуть [0,1,0] - разницы нет, главное, чтобы z=0
            else:#ситуация разных точек      
                H=(u2-u1)%q
                R=(s2-s1)%q
                x3=(R^2-H^3-2*u1*H^2)%q
                y3=(R*(u1*H^2-x3)-s1*H^3)%q
                z3=(H*z1*z2)%q
                return [(x3*pow(z3^2, -1, q))%q, (y3*pow(z3^3, -1, q))%q, z3/z3] #не обязательно делать pow,- так я лишь показываю, что по модулю идёт умножение на обратный а не деление
        else:#разные точки, обычные проективные координаты
            #вспомогательные переменные
            u1=(y1*z2)%q
            u2=(y2*z1)%q
            v1=(x1*z2)%q
            v2=(x2*z1)%q
            if u1==u2 and v1==v2:#ситуация равенства точек
                m=((3*x1^2+a)/(2*y1))%q#наклон
                x3=(m^2-2*x1)%q
                y3=(m*(x1-x3)-y1)%q
                return [x3/z3, y3/z3, z3/z3]
            elif x1*pow(z1, -1, q)==x2*pow(z2, -1, q) and (y1*pow(z1, -1, q) + y2*pow(z2, -1, q)) % q == 0: #противоположные точки
                return [1, 1, 0] #как я понял, можно также вернуть [0,1,0] - разницы нет, главное, чтобы z=0
            else:#ситуация разных точек 
                u=(u2-u1)%q
                v=(v2-v1)%q
                w=(u^2*z1*z2-v^3-2*v^2*x1*z2)%q
                x3=(v*w)%q
                y3=(u*(x1*v^2*z2-w)-v^3*z2*y1)%q
                z3=(v^3*z1*z2)%q
                return [(x3/z3)%q, (y3/z3)%q, z3/z3]
        

