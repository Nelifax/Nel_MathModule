__all__=['EllipticCurve']
from math import sqrt
from NelMath.objects.applied_algebra.Curves.EllipticCurvePoint import EllipticCurvePoint
from NelMath.objects.applied_algebra.Curves.Curve import Curve
from scipy.spatial import ConvexHull

class EllipticCurve(Curve):  
    #y^2+a1xy+a3y=x^3+a2x^2+a4x+a6
    def __new__(cls, params, modulo=None, flags=None):
        if cls is not EllipticCurve:
            return super().__new__(cls, params, modulo, flags)
        else:
            if flags!=None:
                instance=super().__new__(EllipticCurve,params, modulo, flags)
            else:                
                instance=super().__new__(EllipticCurve,params, modulo)
        return instance

    def __init__(self,params:str|list, modulo=None, flags=None):
        if flags!=None:
            self.flags=flags
        if modulo!=None:
            params = [pow(x,1,modulo) for x in params]
        self.params=params
        self.modulo=modulo
        self._determinant=None
        self._jInvariant=None
        self._points=None
        self._params_short=None
        equation=f''
        if len(self.params)==5:
            self.references={
                'curve equation': f'y^2+{params[0]}xy+{params[2]}y=x^3+{params[1]}x^2+{params[3]}x+{params[4]}' if self.modulo==None else f'y^2+{params[0]}xy+{params[2]}y=x^3+{params[1]}x^2+{params[3]}x+{params[4]} (mod {self.modulo})'
                }
        else:
            self.references={
                'short form': f'y^2=x^3+{params[0]}x+{params[1]}' if self.modulo==None else f'y^2=x^3+{params[0]}x+{params[1]} (mod {self.modulo})'
                }
            self._params_short=params

    @property
    def points(self):
        if self._points is None:
            if self.point_border()[0]>100:
                self._points='too many points to unpack'
            else:
                A, B = self.params_short
                from NelMath.objects.applied_algebra.Curves.EllipticCurvePoint import EllipticCurvePoint
                self._points=[]
                for i in range(self.modulo):
                    for j in range(self.modulo):
                        if pow(i,2,self.modulo)==pow(pow(j,3,self.modulo)+pow(A*j,1,self.modulo)+B,1,self.modulo):
                            self._points.append(EllipticCurvePoint({'a':self._params_short[0],'b':self._params_short[1],'x':j,'y':i,'z':1}, self.modulo))
                self._points=[EllipticCurvePoint.infinity(*self._params_short,self.modulo)]+(sorted(self._points, key=lambda x: x.x))
        return self._points



    def point_border(self):
        if self.modulo!=None:
            return (self.modulo+1-2*sqrt(self.modulo),self.modulo+1+2*sqrt(self.modulo))
        else:
            return '∞'
    
    @property
    def params_short(self):
        if self._params_short==None:
            if len(self.params)==2:
                self._params_short=self.params
                return self._params_short
            a1,a2,a3,a4,a6=self.params
            if self.modulo==None:
                d2 = (a1**2) + 4*a2
                d4 = 2*a4 + a1*a3
                d6 = (a3**2) + 4*a6
                d8 = (a1**2)*a6 + 4*a2*a6 - a1*a3*a4 + a2*(a3**2) - (a4**2)
                c4 = (d2**2) - 24*d4
                c6 = -(d2**3) + 36*d2*d4 - 216*d6
                A = -27*c4
                B = -54*c6
            else:
                d2 = pow(pow(a1,2,self.modulo)+4*a2,1,self.modulo)
                d4 = pow(2*a4 + a1*a3,1,self.modulo)
                d6 = pow(pow(a3,2,self.modulo) + 4*a6,1,self.modulo)
                d8 = pow(pow(a1,2,self.modulo)*a6 + pow(4*a2*a6,1,self.modulo) - pow(a1*a3*a4,1,self.modulo) + a2*pow(a3,2,self.modulo) - pow(a4,2,self.modulo),1,self.modulo)
                c4 = pow(pow(d2,2,self.modulo) - pow(24*d4,1,self.modulo),1,self.modulo)
                c6 = pow(-pow(d2,3,self.modulo) + pow(36*d2*d4,1,self.modulo) - pow(216*d6,1,self.modulo),1,self.modulo)
                A = pow(-27*c4,1,self.modulo)
                B = pow(-54*c6,1,self.modulo)
            self._params_short=[A,B]
            self.references['short form']=f'y^2=x^3+{A}x+{B}' if self.modulo==None else f'y^2=x^3+{A}x+{B} (mod {self.modulo})'
        return self._params_short

    @property
    def determinant(self):
        if self._determinant is None:
            if len(self.params)==5:
                self._determinant = self.__find_discriminant(*self.params)
            else:
                self._determinant=[-16*(4*(self.params[0]**3) + 27*(self.params[1]**2))]
        return self._determinant[0]

    def point(self, pos=0, params={}):
        from NelMath.objects.applied_algebra.Curves.EllipticCurvePoint import EllipticCurvePoint
        if pos==0 and params=={}:
            return EllipticCurvePoint.infinity(*self._params_short,self.modulo)
        elif pos==0 and params!={}:
            return EllipticCurvePoint({'a':self.params_short[0], 'b':self.params_short[1], 'x':params['x'], 'y':params['y'], 'z':1},self.modulo)
        else:
            if pos<len(self.points):
                return self.points[pos]
            else:
                a,b=self.params_short[0],self.params_short[1]
                return EllipticCurvePoint.infinity(*self._params_short, self.modulo)

    def __find_discriminant(self,a1,a2,a3,a4,a6):
        d2 = a1**2+4*a2
        d4 = 2*a4+a1*a3
        d6 = a3**2+4*a6
        d8 = a1**2*a6+4*a2*a6-a1*a3*a4+a2*a3**2-a4**2
        c4 = d2**2-24*d4    
        det = 9*d2*d4*d6 - d2**2*d8 - 8*d4**3 - 27*d6**2
        return (det, c4 , d2, d4, d6, d8)

    @property
    def jInvariant(self):
        if self._jInvariant is None:
            if self._determinant is None:
                self.determinant
            if len(self.params)==5:
                det, c4 , d2, d4, d6 , d8 = self._determinant
                if self.determinant != 0:
                    a = -27*c4
                    b = -56*(d2^3+36*d2*d4-216*d6)
                    detS = -16*(4*a^3+27*b^2)
                    if self.modulo!=None and self.modulo>3:
                        self._jInvariant = pow((c4**3)*pow(det,-1,self.modulo), 1, self.modulo)
                    elif self.modulo!=None and self.modulo>1 and self.modulo<4:                
                        self._jInvariant-1728*(4*a**3)/detS
                    else:
                        self._jInvariant = c4**3/det
                else:
                    raise Exception('the curve has a node')
            else:
                self._jInvariant = -1728*((4*self.params[0])**3)/self.determinant
        return self._jInvariant

    def print(self):
        #print(self.flags)
        print(self.params)
        for key, value in self.references.items():
            print(f'{key}: {value}')

    def __repr__(self):
        repr_str='Elliptic Curve defined by '
        if self.references['short form']:
            repr_str+=self.references['short form']
        else:
            repr_str+=self.references['curve equation']
        return repr_str

    def torsion_points(self, border=100):
        '''
        В основе теорема Нагеля—Лутца
        '''
        from NelMath.objects.math_base.Rational import Rational
        from NelMath.functions.factorization import divisors
        divs=divisors(self.determinant)
        #y^2=x^3+ax+b -> если y^2=c -> x^3+ax+b-c=0 - кубическое уравнение
        results=[]
        if 'curve equation' not in self.references.keys(): 
            if self.params_short[1]==0: #y^2=x^3+ax -> y^2=x(x^2+a)
                results.append(EllipticCurvePoint.infinity(self._params_short[0], self._params_short[1], self.modulo))
                results.append(EllipticCurvePoint({'a':self._params_short[0],'b':self._params_short[1],'x':Rational(abs(self._params_short[0])).sqrt(),'y':0,'z':1}, self.modulo))
                results.append(EllipticCurvePoint({'a':self._params_short[0],'b':self._params_short[1],'x':-Rational(abs(self._params_short[0])).sqrt(),'y':0,'z':1}, self.modulo))
            else:
                for div in divs:
                    if Rational(div).sqrt().references['float part']=='0': #y^2|det -> y-корень
                        potential_roots=divisors(self.params_short[1]-div) #делители свободного члена
                        for pr in potential_roots:
                            #print(self.params_short[0], self.params_short[1])
                            if pow(pr,3)+self.params_short[0]*pr==div-self.params_short[1]:
                                results.append(EllipticCurvePoint({'a':self._params_short[0],'b':self._params_short[1],'x':pr,'y':int(Rational(div).sqrt()),'z':1}, self.modulo))
                                results.append(EllipticCurvePoint({'a':self._params_short[0],'b':self._params_short[1],'x':pr,'y':-int(Rational(div).sqrt()),'z':1}, self.modulo))
                            if pow(-pr,3)+self.params_short[0]*(-pr)==div-self.params_short[1]:
                                results.append(EllipticCurvePoint({'a':self._params_short[0],'b':self._params_short[1],'x':-pr,'y':int(Rational(div).sqrt()),'z':1}, self.modulo))
                                results.append(EllipticCurvePoint({'a':self._params_short[0],'b':self._params_short[1],'x':-pr,'y':-int(Rational(div).sqrt()),'z':1}, self.modulo))
        else:
            divs.append(0)
            for div in divs:
                y=Rational(div).sqrt()
                if y.references['float part']=='0': #y^2|det -> y-корень
                    for i in range(-border, border):
                        if pow(y,2) + self.params[0]*i*y + self.params[2]*y == pow(i,3) + self.params[1]*pow(i,2) + self.params[3]*i + self.params[4]:
                            results.append(EllipticCurvePoint({'a':self.params_short[0],'b':self.params_short[1],'x':i,'y':int(y),'z':1}, self.modulo))
                        if pow(-y,2) + self.params[0]*i*(-y) + self.params[2]*(-y) == pow(i,3) + self.params[1]*pow(i,2) + self.params[3]*i + self.params[4]:
                            results.append(EllipticCurvePoint({'a':self.params_short[0],'b':self.params_short[1],'x':i,'y':-int(y),'z':1}, self.modulo))
            end_results=[]
            for i in results:
                if i not in end_results:
                    end_results.append(i)
            return {},end_results
        torsion_results={}
        all_torsion_points=[EllipticCurvePoint.infinity(self.params_short[0], self.params_short[1], self.modulo)]
        for res in results:  
            if res not in all_torsion_points:
                all_torsion_points.append(res)
            points=[]
            for i in range(2,14):
                point=res*i
                points.append(point)
                if point not in all_torsion_points:
                    all_torsion_points.append(point)
                if point==EllipticCurvePoint.infinity(self.params_short[0], self.params_short[1], self.modulo):
                    torsion_results[(str(res),i)]=points
                    break
        return torsion_results, sorted(all_torsion_points[1:], key=lambda x: x.x)


    def plot(self, points, x_range=(-100, 100), step=0.01):
        import numpy as np
        import matplotlib.pyplot as plt        
        x = np.arange(x_range[0], x_range[1] + step, step)
        if 'curve equation' in self.references.keys():
            #y^2 +a1xy + a3y = x^3 + a2x^2+a4x+a6
            x = np.linspace(-5, 5, 400)
            a1,a2,a3,a4,a6 = self.params
            # Вычисляем дискриминант ∆
            delta = (a1 * x + a3) ** 2 + 4 * (x ** 3 + a2 * x ** 2 + a4 * x + a6)

            # Фильтруем только те x, где дискриминант неотрицательный
            valid = delta >= 0
            x_valid = x[valid]
            delta_valid = delta[valid]

            # Вычисляем два значения y
            y1 = (-(a1 * x_valid + a3) + np.sqrt(delta_valid)) / 2
            y2 = (-(a1 * x_valid + a3) - np.sqrt(delta_valid)) / 2
            title=f'Эллиптическая кривая: $y^2 + {a1}xy + {a3}y = x^3 + {a2}x^2 + {a4}x + {a6}$'
        else:
            a,b=self.params_short
            y_squared = x**3 + a * x + b
            title=f'Эллиптическая кривая: $y^2 = x^3 + {a}x + {b}$'
        
            # Фильтрация точек с вещественными y
            valid_indices = y_squared >= 0
            x_valid = x[valid_indices]
            y_squared_valid = y_squared[valid_indices]
    
            y_positive = np.sqrt(y_squared_valid)
            y_negative = -y_positive
    
            # Создание графика
            plt.figure(figsize=(10, 8))
    
            # Рисование эллиптической кривой
            plt.plot(x_valid, y_positive, 'b', label=f'$y^2 = x^3 + {a}x + {b}$')
            plt.plot(x_valid, y_negative, 'b')                
        
        if len(points) >= 3:  # Для построения оболочки нужно минимум 3 точки
            # Отображение заданных точек и выпуклой оболочки
            points=np.array([[int(p.x), int(p.y)] for p in points])
            center = np.mean(points, axis=0)
            # Сортируем точки по углу относительно центра
            angles = np.arctan2(points[:, 1] - center[1], points[:, 0] - center[0])
            sorted_points = points[np.argsort(angles)]
            x_points = sorted_points[:, 0]
            y_points = sorted_points[:, 1]


            # Многоугольник (соединяем точки линиями)
            x_poly = np.append(x_points, x_points[0])
            y_poly = np.append(y_points, y_points[0])

            plt.plot(x_poly, y_poly, 'r--', linewidth=2, label='Многоугольник')
            plt.scatter(x_points, y_points, color='red', s=100, label='Точки', zorder=5)
    
        elif len(points)<3:
            # Если точек меньше 3, просто отображаем их
            x_points = [p[0] for p in points]
            y_points = [p[1] for p in points]
            plt.scatter(x_points, y_points, color='red', s=100, label='Заданные точки')
    
        # Настройка графика
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')
        if 'curve equation' in self.references.keys():
            plt.plot(x_valid, y1, 'b', label="Верхняя ветвь")
            plt.plot(x_valid, y2, 'r', label="Нижняя ветвь")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        #plt.axis('equal')
        plt.show()

    @staticmethod
    def get_random_curve(beg_border, end_border, modulo=None, return_random_point=False)->'EllipticCurve':
        '''
        returns EllipticCurve class as y^2=x^3+Ax+B curve that non-singular with randomized A and B with modulo if needed
        '''
        from NelMath.objects.math_additions.Random import Random
        rand=Random()
        while True:
            A=rand.rand_range(beg_border,end_border)
            x0=rand.rand_range(beg_border,end_border)
            y0=rand.rand_range(beg_border,end_border)
            if modulo!=None:
                B = pow(y0**2 - x0**3 - A*x0, 1, modulo)
            else:
                B = y0**2 - x0**3 - A*x0
            try:
                E=EllipticCurve([A,B],modulo)
                if return_random_point:
                    P=EllipticCurvePoint({'a':A, 'b':B, 'x':x0, 'y':y0, 'z':1}, E.modulo)
                break
            except:
                pass
        if return_random_point:
            return E,P
        else:
            return E