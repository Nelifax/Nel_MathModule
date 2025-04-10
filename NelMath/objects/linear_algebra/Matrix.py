from math import e
from NelMath.objects.errors.Error import MatrixError
from NelMath.objects.math_base.Rational import Rational, Number
from NelMath.objects.linear_algebra.Linear_object import Linear_object

__all__=['MM_matrix_manual', 'Matrix']

global MM_matrix_manual
MM_matrix_manual = True;

class Matrix(Linear_object):
    __module__="LinearAlgebra"
    MM_matrix_factor_standart = 0
    MM_matrix_factor_diagonal = 1
    MM_matrix_form_square = 0
    MM_matrix_form_rectangle = 1
    def __init__(self, generator_attribute:str|list[list], flags:dict={})->'Matrix':
        """
        Предоставляет класс Matrix для работы и вычислений с матрицами
        Параметры:
            generator_attribute (str|list[list]): Определяет, из чего создать матрицу. Может быть как числом, так и строковым представлением числа или вложенным массивом подобных элементов
            [str pattern]: '_attributes:123,1231,123,1233' для матрицы 2х2 и произвольных аттрибутов ([rec]/[sq]/T/I)
            flags (dict): словарь настроек генератора матрицы
                flags: transposed, inverted, form, factor, invertible, columns, rows, calculated
            Если установлены и флаги и строковые атрибуты, - аттрибуты игнорируются
        """
        self.__generator_attribute = generator_attribute
        self.generator_stroke = generator_attribute

        self.values = []
        self.determinant = 'undefined'

        self.__flags = {
                'transposed': False, 
                'inverted': False, 
                'form': Matrix.MM_matrix_form_square, 
                'factor': Matrix.MM_matrix_factor_standart,
                'invertible': False,
                'dimension': (0,0),
                'columns': 0,
                'rows': 0,
                'rang': 'undefined',
                'calculated': False
                }
        if flags == {'factor':Matrix.MM_matrix_factor_diagonal}:
            self.__flags['factor'] = Matrix.MM_matrix_factor_diagonal
            if generator_attribute.replace(',','').replace(' ','').replace('-','').isdigit():
                values = generator_attribute.split(',')
                diagonalValues = []
                iterator=0
                self.__generator_attribute = ''
                for i in range(0, len(values)):
                    diagonalValues.append([])
                    for j in range(0, len(values)):
                        if i==j:
                            diagonalValues[i].append(Rational(values[iterator]))
                            self.__generator_attribute+= str(values[iterator]) + ','
                            iterator+=1
                        else:
                            diagonalValues[i].append(Rational(0))
                            self.__generator_attribute+= '0,'
                self.__generator_attribute = self.__generator_attribute[0:-1]
                self.values = diagonalValues
                self.__flags['rows'] = len(values)
                self.__flags['columns'] = len(values)
                self.__flags['invertible'] = True
                self.__flags['dimension'] = (len(values), len(values))
                self.determinant = 0
                self.find_determinant()
                return
        if flags != {}:
            for key, value in flags.items():
                if key not in self.__flags.keys():
                    raise MatrixError(MatrixError.MM_error_wrong_flags, [key])
            self.__flags.update(flags)

        #block of manual matrix-generation----------------------------------------------------
        if MM_matrix_manual:
            if type(generator_attribute) == str and flags=={}:
                if 'I' in generator_attribute and '[rec]' in generator_attribute:
                    raise MatrixError(MatrixError.MM_error_inverted_rectangle)
                if 'T' in generator_attribute:
                    self.__flags['transposed'] = 'in_process'
                    self.__generator_attribute = self.__generator_attribute.replace('T', '', 1)
                if 'I' in generator_attribute:
                    self.__flags['inverted'] = 'in_process'
                    self.__generator_attribute = self.__generator_attribute.replace('I', '', 1)
                if '[sq]' in generator_attribute:
                    self.__flags['form'] = Matrix.MM_matrix_form_square
                    self.__generator_attribute = self.__generator_attribute.replace('[sq]', '', 1)
                if '[rec]' in generator_attribute:
                    raise MatrixError(MatrixError.MM_error_wrong_flags)
            elif type(generator_attribute) == str and flags!={}:
                if '[sq]' in generator_attribute:
                    if self.__flags['rows'] != self.__flags['columns']:
                        raise MatrixError(MatrixError.MM_error_wrong_flags)
                    self.__flags['form'] = Matrix.MM_matrix_form_square
                    self.__generator_attribute = self.__generator_attribute.replace('[sq]', '', 1)
                if '[rec]' in generator_attribute:
                    self.__flags['form'] = Matrix.MM_matrix_form_rectangle
                    self.determinant = 'undefined'
                    self.__generator_attribute = self.__generator_attribute.replace('[rec]', '', 1)
                if 'T' in generator_attribute:
                    self.__flags['transposed'] = 'in_process'
                    self.__generator_attribute = self.__generator_attribute.replace('T', '', 1)
                if 'I' in generator_attribute:
                    self.__flags['inverted'] = 'in_process'
                    self.__generator_attribute = self.__generator_attribute.replace('I', '', 1)
                self.__generator_attribute = self.__generator_attribute.replace('T', '', 1).replace('I', '', 1).replace('[sq]', '', 1).replace('[rec]', '', 1).replace(' ', '')
                       
            if self.__flags['form'] == Matrix.MM_matrix_form_rectangle and (self.__flags['columns'] == 0 or self.__flags['rows'] == 0):
                raise MatrixError(MatrixError.MM_error_wrong_flags, ['need \'columns\' and \'rows\' flags'])
        #end of manual matrix-generation-------------------------------------------------------------------------

            generator_attribute = self.__generator_attribute
            
            if type(generator_attribute) == str:
                if not generator_attribute.replace(',','').replace(' ','').replace('-','').replace('.','').isdigit():
                    raise MatrixError(MatrixError.MM_error_wrong_generator_keys)
                values = generator_attribute.split(',')
                if self.__flags['form'] == Matrix.MM_matrix_form_square:
                    dim = int(str(len(values)**0.5).split('.')[0])
                    if dim**2 != len(values):
                        raise MatrixError(MatrixError.MM_error_not_enough_numbers)
                    else:
                        self.__flags['dimension'] = (dim,dim)
                        self.__flags['rows'] = dim
                        self.__flags['columns'] = dim
                else:
                    if len(values)/self.__flags['rows'] == self.__flags['columns']:
                        self.__flags['dimension'] = (self.__flags['rows'], self.__flags['columns'])
                    else:
                        raise MatrixError(MatrixError.MM_error_not_enough_numbers)
            elif type(generator_attribute) == list:
                self.values = generator_attribute
                row_len = len(generator_attribute[0])
                for row in generator_attribute:
                    if len(row) !=row_len:
                        raise MatrixError(MatrixError.MM_error_not_enough_numbers)                
                for i in range(len(generator_attribute)):
                    for j in range(len(generator_attribute[0])):
                        generator_attribute[i][j]=Rational(generator_attribute[i][j])
                self.__flags['rows'] = len(generator_attribute)
                self.__flags['columns'] = len(generator_attribute[0])
                self.__flags['dimension'] = (self.__flags['rows'], self.__flags['columns'])
                if self.__flags['rows'] == self.__flags['columns']:
                    self.__flags['form'] = Matrix.MM_matrix_form_square
                else:
                    self.__flags['form'] = Matrix.MM_matrix_form_rectangle
                if self.__flags['rows'] != self.__flags['columns']: 
                    self.determinant = 'undefined'
                    self.__flags['calculated'] = True
                if not self.__flags['calculated']:self.find_determinant()
            else: raise TimeoutError

        if not MM_matrix_manual and type(generator_attribute) == str and ('T' in generator_attribute or 'I' in generator_attribute or '[rec]' in generator_attribute or '[sq]' in generator_attribute):
            raise MatrixError(MatrixError.MM_error_manual_disabled)
                
        if type(generator_attribute) == str:
            counter = 0
            for i in range(0, self.__flags['rows']):
                self.values.append([])
                for j in range(0, self.__flags['columns']):
                    self.values[i].append(Number(values[counter]))
                    counter+=1
            if not self.__flags['calculated']:self.find_determinant()
        elif type(generator_attribute) == list:            
            self.values = generator_attribute
            for i in range(0, len(self.values)):
                for j in range(0, len(self.values[0])):
                    self.values[i][j]=Number(self.values[i][j])
            if not self.__flags['calculated']:self.find_determinant()
        else: raise TimeoutError

        
        self.check_factor()
        self.columns = []
        self.rows = []
        for i in range(0, len(self.values)):
            self.rows.append(self.values[i])
        for i in range(0, len(self.values[0])):            
            column = []
            for j in range(0, len(self.values)):
                column.append(self.values[j][i])
            self.columns.append(column)

        if self.determinant != 'undefined' and self.determinant !=0: self.__flags['invertible'] = True
        if self.__flags['inverted'] == 'in_process': self.invert()
        if self.__flags['transposed'] == 'in_process': self.transpose()
        if self.__flags['rang']=='undefined':
            self.find_rang()
            self.__flags['rang'] = self.rang
        

    def find_determinant(self):
        self.__flags['calculated'] = True
        if self.__flags['form'] != Matrix.MM_matrix_form_square:
            self.determinant = 'undefined'
        else:
            self.determinant=0
            sign = 0
            if self.__flags['columns'] == 1 and self.__flags['rows'] == 1:
                self.determinant = self.values[0][0]
                return
            if self.__flags['rows']==self.__flags['columns'] and self.__flags['rows'] == 2:
                self.determinant = self.values[0][0]*self.values[1][1]-self.values[1][0]*self.values[0][1]
                return
            if self.__flags['rows']==self.__flags['columns'] and self.__flags['rows'] == 3:
                self.determinant = self.values[0][0]*self.values[1][1]*self.values[2][2]+self.values[0][1]*self.values[1][2]*self.values[2][0]+self.values[0][2]*self.values[1][0]*self.values[2][1]-self.values[0][2]*self.values[1][1]*self.values[2][0]-self.values[0][0]*self.values[1][2]*self.values[2][1]-self.values[0][1]*self.values[1][0]*self.values[2][2]
                return
            if self.__flags['rows']==self.__flags['columns'] and self.__flags['rows'] > 3:
                for i in range(0, self.__flags['columns']):
                    self.determinant = self.determinant+self.find_addition(0,i)*self.values[0][i]
    
    def find_minor(self, row:int|list, column:int|list)->'Matrix':
        newMatrixRational = ''
        newMatrixValues = []
        if type(row)==list and type(column)==list:
            for i in range(0, len(row)):
                newMatrixValues.append([])
                for j in range(0, len(column)):
                    newMatrixValues[i].append([])
            countI = 0
            countJ = 0
            for i in row:
                countJ=0
                for j in column:
                    newMatrixValues[countI][countJ]=self.values[i][j]
                    countJ+=1
                countI+=1
            return Matrix(newMatrixValues)
        is_parsing_int = True
        addI = 0
        addJ = 0
        if self.__flags['columns'] == self.__flags['rows'] and self.__flags['columns'] == 1:
            return self.values[row][column];
        for i in range(0,self.__flags['rows'] - 1):
            newMatrixValues.append([])
            for j in range(0,self.__flags['columns'] - 1):
                newMatrixValues[i].append([])
        for i in range(0, self.__flags['rows']):
            addJ = 0
            if i == row:
                addI = 1
                continue
            else:
                for j in range(0, self.__flags['columns']):
                    if j == column:
                        addJ = 1
                        continue
                    else:
                        newMatrixRational+=str(self.values[i][j])+','
                        newMatrixValues[i-addI][j-addJ] = self.values[i][j]
                        if '.' in str(self.values[i][j]):
                            is_parsing_int = False
        newMatrixRules = self.__flags.copy()
        newMatrixRules['rows'] -= 1
        newMatrixRules['columns'] -= 1
        newMatrixRules['rang'] = 'undefined'
        newMatrixRules.update({'calculated':False})
        newMatrixRules.update({'inverted':False})
        if is_parsing_int:
            newMatrix = Matrix(newMatrixRational[:-1], newMatrixRules)
        else:
            newMatrix = Matrix(newMatrixValues, newMatrixRules)
        return newMatrix

    def find_addition(self, row:int, column:int):
        if (row+column)%2==0:
            sign = 1;
        else: 
            sign = -1;
        return self.find_minor(row, column).determinant*sign

    def transpose(self)->'Matrix':
        newValues = []
        for i in range(0,self.__flags['columns']):
            newValues.append([])
            for j in range(0, self.__flags['rows']):
                newValues[i].append(self.values[j][i])
        self.__flags['columns'] = self.__flags['rows']
        self.__flags['rows'] = self.__flags['dimension'][1]
        self.__flags['transposed'] = True
        self.__flags['dimension'] = (self.__flags['rows'], self.__flags['columns'])
        self.values = newValues
        #self.find_determinant()
        saveattr = self.rows
        self.rows = self.columns
        self.columns = saveattr
        return self
    
    def get_generator_attribute(self)->str:
        return self.__generator_attribute

    def invert(self)->'Matrix':
        if self.determinant == 0 or self.determinant == 'undefined':
            raise MatrixError(MatrixError.MM_error_zero_determinant)
        if self.__flags['inverted'] == 'in_process':
            self.__flags['inverted'] = True
            self.transpose()
            newValues = []
            for i in range(0, self.__flags['rows']):
                newValues.append([])
                for j in range(0, self.__flags['columns']):
                    newValues[i].append(self.find_addition(i, j)/self.determinant)
            self.values = newValues
            self.__flags.update({'transposed': False})
            self.check_factor()
            return self
        self.__flags['inverted'] = True
        newMatrix = self.copy()
        self.transpose()
        for i in range(0, self.__flags['rows']):
            for j in range(0, self.__flags['columns']):
                newMatrix.values[i][j] = self.find_addition(i, j)/self.determinant
        self.transpose()
        newMatrix.find_determinant()
        newMatrix.check_factor()
        return newMatrix

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

    def find_rang(self):
        if len(self.rows)<=len(self.columns):
            rows = self.rows.copy()
            for i in range(0, len(self.rows)-1):
                for j in range(i+1, len(self.rows)):
                    if rows[i][i] == 0:
                        continue
                    if rows[i][i]>0 and rows[j][i]>=0:
                        rows[j] = Matrix.addVector(Matrix.mulVector(rows[i].copy(), -1*rows[j][i]/rows[i][i]),rows[j].copy())
                    elif rows[i][i]<0 and rows[j][i]<0:
                        rows[j] = Matrix.addVector(Matrix.mulVector(rows[i].copy(), rows[j][i]/rows[i][i]),rows[j].copy())
                    else:
                        rows[j] = Matrix.addVector(Matrix.mulVector(rows[i].copy(), -1*rows[j][i]/rows[i][i]),rows[j].copy())
            independent = 0
            for i in range(0, len(rows)):
                if len(set(rows[i])) != 1 and set(rows[i]) !={0}:
                    independent+=1                   
            self.rang = independent
            self.ranged = Matrix(rows, {'rang':self.rang})
        else:
            columns = self.columns.copy()
            for i in range(0, len(self.columns)-1):
                for j in range(i+1, len(self.columns)):
                    if columns[i][i] == 0:
                        continue
                    if columns[i][i]>=0 and columns[j][i]>=0:
                        columns[j] = Matrix.addVector(Matrix.mulVector(columns[i].copy(), -1*columns[j][i]/columns[i][i]),columns[j].copy())
                    elif columns[i][i]<0 and columns[j][i]<0:
                        columns[j] = Matrix.addVector(Matrix.mulVector(columns[i].copy(), -1*columns[j][i]/columns[i][i]),columns[j].copy())
                    else:
                        columns[j] = Matrix.addVector(Matrix.mulVector(columns[i].copy(), columns[j][i]/columns[i][i]),columns[j].copy())
            independent = 0
            for i in range(0, len(columns)):
                if len(set(columns[i])) != 1 and set(columns[i]) !={0}:
                    independent+=1   
            self.rang = independent
            self.ranged = Matrix(columns, {'rang':self.rang, 'transposed':'in_process'})


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
        print(f'Current matrix: \ngenerator:"{self.generator_stroke}"')
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
        flags.update({'calculated':True})
        copied_matrix = Matrix(self.values, flags)
        copied_matrix.determinant = self.determinant
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
            resultMatrix.find_determinant()
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
            result.find_determinant()
            return result
        if value > 1:
            result = result*(pow(result, value-1, modulo))            
            if modulo != None:
                for i in range(0, self.__flags['rows']):
                    for j in range(0, self.__flags['columns']):
                        result.values[i][j] = result.values[i][j] % modulo
            result.find_determinant()
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
        result.find_determinant()
        return result
    
    def __sub__(self, other:'Matrix')->'Matrix':
        if self.__flags['columns'] != other.__flags['columns'] or self.__flags['rows'] != other.__flags['rows']:
                raise MatrixError(MatrixError.MM_error_wrong_line_count)
        result = self.copy()
        for i in range(0, self.__flags['rows']):
            for j in range(0, self.__flags['columns']):
                result.values[i][j] = self.values[i][j]-other.values[i][j]
        result.find_determinant()
        return result

    def __eq__(self, other:'Matrix')->bool:
        if isinstance(other, Matrix):
            if self.get_flags() == other.get_flags() and self.values == other.values:
                return True
        return False