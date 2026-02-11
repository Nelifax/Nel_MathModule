from math import e
from NelMath.objects.errors.Error import MatrixError
from NelMath.objects.math_base import Rational, Number, Fraction
from NelMath.objects.linear_algebra.Linear_object import Linear_object
from NelMath.objects.linear_algebra.Vector import Vector

__all__=['Matrix']


class Matrix(Linear_object):
    __module__="LinearAlgebra"
    def __init__(self, values:list[list], flags:dict={})->'Matrix':
        """
        Предоставляет класс Matrix для работы и вычислений с матрицами
        Параметры:
            flags (dict): словарь настроек генератора матрицы
                flags: transposed, inverted, form, factor, invertible, columns, rows, calculated
        """
        if flags=={}:
            self.__flags=Linear_object._check_flags({}, 'Matrix')
        else: 
            self.__flags=flags
        self.__generator_stroke = values.__repr__()
        self.rows=[Vector(stroke) for stroke in values]
        self.values=self.rows.copy()
        self.columns=[Vector([row[i] for row in values]) for i in range(len(values[0]))]
        self.__flags.update({'dimension':Linear_object.get_dimensions(values),
                             'columns': len(self.columns),
                             'rows': len(self.columns), 
                             'is_square': False if len(self.columns)!=len(self.columns) else True})
        
        self.__determinant=None

        if self.__flags['auto_calculations']:
            from NelMath.properties.settings_handler import SettingsHandler
            settings=SettingsHandler()
            calculated_properties=settings.get('mm_matrix_auto_calculated_values')
            if calculated_properties!=[]:
                for prop in calculated_properties:
                    if hasattr(Matrix, f'find_{prop}'):
                        self.__flags.update({prop:exec(f'self.{prop}')})

    @property
    def determinant(self)->int|str:
        if self.__determinant!=None:
            return self.__determinant
        if not self.__flags['is_square']: 
            self.__determinant = 'undefined'
            self._Matrix__flags['invertible']==False
        else:
            self.__determinant=0
            if self.__flags['columns'] == 1:
                self.__determinant = self.columns[0][0]
            elif self.__flags['columns'] == 2:
                self.__determinant = self.columns[0][0]*self.columns[1][1]-self.columns[1][0]*self.columns[0][1]
            elif self.__flags['columns'] == 3:
                self.__determinant = self.columns[0][0]*self.columns[1][1]*self.columns[2][2]+self.columns[0][1]*self.columns[1][2]*self.columns[2][0]+self.columns[0][2]*self.columns[1][0]*self.columns[2][1]-self.columns[0][2]*self.columns[1][1]*self.columns[2][0]-self.columns[0][0]*self.columns[1][2]*self.columns[2][1]-self.columns[0][1]*self.columns[1][0]*self.columns[2][2]
            else:
                for i in range(0, self.__flags['columns']):
                    self.__determinant = self.__determinant+self.find_addition(0,i)*self.values[0][i]
            self._Matrix__flags['invertible'] = False if self.__determinant==0 else True
        return self.__determinant
    
    def lu_decomposition(A):
        n = len(A)
        L = np.eye(n)  # Единичная матрица для L
        U = np.copy(A)  # Копия A для U
    
        for k in range(n - 1):
            # Частичный выбор ведущего элемента
            pivot_row = np.argmax(np.abs(U[k:, k])) + k
            if pivot_row != k:
                U[[k, pivot_row]] = U[[pivot_row, k]]
                L[[k, pivot_row], :k] = L[[pivot_row, k], :k]
        
            # Исключение Гаусса
            for i in range(k + 1, n):
                L[i, k] = U[i, k] / U[k, k]
                U[i, k:] -= L[i, k] * U[k, k:]
    
        return L, U

    def find_minor(self, row:int, column:int)->'Matrix':
        new_matrix_values=[]
        for i in range(len(self.values)):
            if i==row:
                continue
            k=[]
            for j in range(len(self.values[i])):
                if j==column:
                    continue
                k.append(self.values[i][j])
            new_matrix_values.append(Vector(k))
        nm=Matrix(new_matrix_values)
        return nm

    def find_addition(self, row:int, column:int)->int:
        if (row+column)%2==0:            
            return self.find_minor(row, column).determinant
        else: 
            return -self.find_minor(row, column).determinant

    def transpose(self)->'Matrix':        
        self.values=self.columns.copy()
        self.columns, self.rows = self.rows.copy(), self.columns.copy()
        self.__generator_stroke=self.values.__repr__()
        return self
    
    def get_generator_attribute(self)->str:
        return self.__generator_attribute

    def additions_matrix(self)->'Matrix':
        if self.determinant == 0 or self.determinant == 'undefined':
            raise MatrixError(MatrixError.MM_error_zero_determinant)
        additions_matrix=[]
        for i in range(0, self.__flags['rows']):
            additions_matrix.append([])
            for j in range(0, self.__flags['columns']):
                frac=Fraction([self.find_addition(i, j),self.determinant])
                #frac.improper_view()
                additions_matrix[i].append(frac)
        additions_matrix=Matrix([Vector(additions_matrix[i]) for i in range(len(additions_matrix))])
        additions_matrix._Matrix__determinant=Fraction([1,self.determinant])

        return additions_matrix

    def invert(self)->'Matrix':
        if self.determinant == 0 or self.determinant == 'undefined':
            raise MatrixError(MatrixError.MM_error_zero_determinant)
        additions_matrix=[]
        for i in range(0, self.__flags['rows']):
            additions_matrix.append([])
            for j in range(0, self.__flags['columns']):
                frac=Fraction([self.find_addition(i, j),self.determinant])
                #frac.improper_view()
                additions_matrix[i].append(frac)
        additions_matrix=Matrix([Vector(additions_matrix[i]) for i in range(len(additions_matrix))])
        additions_matrix._Matrix__determinant=Fraction([1,self.determinant])

        return additions_matrix.transpose()

    def get_flags(self):
        return self.__flags

    def update_flags(self, flagsToUpdate:dict):
        self.__flags.update(flagsToUpdate)

    def get_generator(self):
        generator_stroke = ''
        for i in range(0,self.__flags['rows']):
            for j in range(0, self.__flags['columns']):
                generator_stroke+=str(self.values[i][j])+','
        return generator_stroke[0:-1]

    def find_rank(self):
        copied=self.copy()
        if len(self.columns)<len(self.rows):
            copied.transpose()


    def addVector(v1:list, v2:list)->list:
        result = []
        for i in range(0, len(v1)):
            result.append(v1[i]+v2[i])
        return result

    def mulVector(v1:list, value:int|float)->list:
        for i in range(0, len(v1)):
            v1[i]=v1[i]*value
        return v1


    def print(self):
        print(f'Current matrix: \ngenerator:"{self.__generator_stroke}"')
        maxSymbols = 1
        for i in range(0,self.__flags['rows']):
            for j in range(0,self.__flags['columns']):
                symlen = len(str(self.values[i][j]))
                if symlen>maxSymbols:
                    maxSymbols = symlen
        for i in range(0,self.__flags['rows']):
            for j in range(0,self.__flags['columns']):
                print(f"{self.values[i][j]:^{maxSymbols+2}}", end='|')
            print('\n'+'-'*(self.__flags['columns'])*(maxSymbols+3))
        print(f'determinant = {self.determinant}')
        for key, value in self.__flags.items():
            print(f'{key}: {value}')
    
    def check_factor(self):
        for i in range(0,self.__flags['rows']):
            for j in range(0, self.__flags['columns']):
                if i==j:
                    continue
                if self.values[i][j] != 0 or self.values[i][j] != 0.0:
                    self.update_flags({'factor':Matrix.MM_matrix_factor_standart})
                    return
        self.update_flags({'factor':Matrix.MM_matrix_factor_diagonal})

    def copy(self)->'Matrix':
        flags = self.__flags.copy()
        copied_matrix = Matrix(self.values, flags)
        copied_matrix._Matrix__determinant = self.__determinant
        return copied_matrix

    def SVD(self)->tuple['Matrix']:
        '''
            returns matrix SVD
        '''
        U = self.copy()*self.copy().transpose()
        V = self.copy().transpose()*self.copy()

    def lyambda_notation(matrix:'Matrix'):
        pass

        
    def __mul__(self, other)->'Matrix':
        resultMatrix = self.copy()
        newMatrixValues = []
        if isinstance(other, int):
            for i in range(0, self.__flags['rows']):
                for j in range(0,self.__flags['columns']):
                    resultMatrix.values[i][j] = resultMatrix.values[i][j]*other
            resultMatrix.determinant()
            resultMatrix.check_factor()
            return resultMatrix
        elif isinstance(other, Matrix):
            if self.__flags['columns'] != other.__flags['rows'] or self.__flags['rows'] != other.__flags['columns']:
                raise MatrixError(MatrixError.MM_error_wrong_line_count)
            else:
                for i in range(0, self.__flags['rows']):
                    newMatrixValues.append([])
                    for j in range(0,other.__flags['columns']):
                        value = Rational(0)
                        for k in range(0, other.__flags['rows']):
                            value += self.values[i][k]*other.values[k][j]
                        newMatrixValues[i].append(value)       
            resultMatrix = Matrix(newMatrixValues)
            resultMatrix.check_factor()
            return resultMatrix
        else: raise TimeoutError

    def __pow__(self, value:int, modulo:int = None)->'Matrix':
        result = self.copy()
        if self.__flags['rows'] != self.__flags['columns']:
            raise MatrixError(MatrixError.MM_error_wrong_line_count)
        if value <0:
            return (result**abs(value)).invert()
        if value == 0:
            for i in range(0, self.__flags['rows']):
                for j in range(0, self.__flags['columns']):
                    if i == j:
                        result.values[i][j] = 1
                    else: 
                        result.values[i][j] = 0
            result.__flags.update({'factor':Matrix.MM_matrix_factor_diagonal})
            result.determinant = 1
            return result
        if value == 1:
            if modulo != None:
                for i in range(0, self.__flags['rows']):
                    for j in range(0, self.__flags['columns']):
                        result.values[i][j] = result.values[i][j] % modulo                        
            result.determinant()
            return result
        if value > 1:
            result = result*(pow(result, value-1, modulo))            
            if modulo != None:
                for i in range(0, self.__flags['rows']):
                    for j in range(0, self.__flags['columns']):
                        result.values[i][j] = result.values[i][j] % modulo
            result.determinant()
            return result

    
    def __truediv__(self, other)->'Matrix':
        if self.__flags['rows'] != self.__flags['columns']:
            raise MatrixError(MatrixError.MM_error_wrong_line_count)
        if self.__flags['rows'] != other.__flags['rows'] or self.__flags['rows'] != other.__flags['columns']:
            raise MatrixError(MatrixError.MM_error_wrong_line_count)
        if isinstance(other, Matrix):
            return self*other.invert()
        else: raise MatrixError(MatrixError.MM_error_div_not_allowed)
    
    def __add__(self, other:'Matrix')->'Matrix':
        if self.__flags['columns'] != other.__flags['columns'] or self.__flags['rows'] != other.__flags['rows']:
                raise MatrixError(MatrixError.MM_error_wrong_line_count)
        result = self.copy()
        for i in range(0, self.__flags['rows']):
            for j in range(0, self.__flags['columns']):
                result.values[i][j] = self.values[i][j]+other.values[i][j]
        result.determinant()
        return result
    
    def __sub__(self, other:'Matrix')->'Matrix':
        if self.__flags['columns'] != other.__flags['columns'] or self.__flags['rows'] != other.__flags['rows']:
                raise MatrixError(MatrixError.MM_error_wrong_line_count)
        result = self.copy()
        for i in range(0, self.__flags['rows']):
            for j in range(0, self.__flags['columns']):
                result.values[i][j] = self.values[i][j]-other.values[i][j]
        result.determinant()
        return result

    def __eq__(self, other:'Matrix')->bool:
        if isinstance(other, Matrix):
            if self.get_flags() == other.get_flags() and self.values == other.values:
                return True
        return False

    @staticmethod
    def unit(n,m=0)->'Matrix':
        '''
            returns a unit matrix with NxM dims.
            if M=0, returns NxN unit matrix
        '''
        return Matrix([Vector.zero(m).vec_add(1) for _ in range(n)] if m!=0 else [Vector.zero(n).vec_add(1) for _ in range(n)])
    
    @staticmethod
    def zeros(n,m=0)->'Matrix':
        '''
            returns a zeros matrix with NxM dims.
            if M=0, returns NxN zero matrix
        '''
        return Matrix([Vector.zero(m) for _ in range(n)] if m!=0 else [Vector.zero(n) for _ in range(n)])

    @staticmethod
    def random(lbound, rbound, n, m=0):
        '''
        return matrix with NxM dims filled by random elements from [lbound, rbound] both endpoints
        if m=0 matrix will have NxN dims
        '''
        from NelMath.objects.math_additions.Random import Random
        rand=Random()
        new_matrix=[Vector([Rational(rand.rand_range(lbound,rbound)) for x in range(m)]) for y in range(n)] if m!=0 else [Vector([Rational(rand.rand_range(lbound,rbound)) for x in range(n)]) for y in range(n)]
        return Matrix(new_matrix)