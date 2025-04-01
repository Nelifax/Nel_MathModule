from NelMath.objects.linear_algebra.Linear_object import Linear_object
__all__ = ['Vector']

class Vector(Linear_object):
    def __init__(self, values:list):
        self.data = values
        self.__flags = {
            'Length': 0,
            'Dimension': len(values),
            'Normalized': False,
            'Unit': Vector.is_vector_unit(self)
            }
        
    @staticmethod
    def find_length(vector:'Vector')->int|float:
        from NelMath import Rational
        length = Rational(0)
        for i in range(0, len(vector.data)):
            length+=vector.data[i]**2
        return length.sqrt()

    @staticmethod
    def find_sinus(vector_A:'Vector', vector_B:'Vector')->float:
        return (vector_A*vector_B)/(vector_A.__flags['Length']*vector_B.__flags['Length'])

    @staticmethod
    def is_vectors_collinear(vector_A:'Vector', vector_B:'Vector')->bool:        
        if len(vector_A.data) != len(vector_B.data):
            raise TimeoutError()
        if vector_A.__flags['Length'] == 0 or vector_B.__flags['Length'] == 0:
            return True
        result = []
        for i in range(0, len(vector_A.data)):
            if vector_B[i] == 0 and vector_A[i] != 0:
                return False
            elif vector_B[i] == 0 and vector_A[i] == 0:
                continue
            result.append(vector_A.data[i]/vector_B.data[i])
        if len(set(result)) == 1:
            return True
        else: return False

    @staticmethod
    def is_vectors_complanar(vectorList:list['Vector'])->bool:
        non_collinear_max = 0
        if len(vectorList) < 3:
            raise TimeoutError()
        for i in range(0, len(vectorList)):
            non_collinear = 0
            for j in range(0, len(vectorList)):
                if i == j: continue
                if not Vector.is_vectors_collinear(vectorList[i], vectorList[b]):
                    non_collinear += 1
            if non_collinear > non_collinear_max:
                non_collinear_max = non_collinear
        if non_collinear_max <=2:
            return True
        else:
            return False

    def normalize(self):
        for i in range(0, len(self.data)):
            self.data[i] = self.data[i]/self.__flags['Length']
        self.__flags['Normalized'] = True
        self.__flags['Unit'] = Vector.is_vector_unit(self)
        self.__flags['Length'] = 1
        return self

    @staticmethod
    def is_vector_unit(vector:'Vector')->bool:
        has_unit = False
        for i in range (0, len(vector.data)):
            if vector.data[i] == 0:
                continue
            elif vector.data[i] == 1:
                if has_unit:
                    return False
                else:
                    has_unit = True
                    continue
            else:
                return False
        return has_unit
    
    @staticmethod
    def is_vectors_perpendicular(vector_A:'Vector', vector_B:'Vector')->bool:
        if vector_A*vector_B == 0:
            return True
        else: return False
    
    def __add__(self, addVector:'Vector')->'Vector':
        if len(self.data) != len(addVector.data):
            raise TimeoutError()
        else:
            result = []
            for i in range(0, len(self.data)):
                result.append(self.data[i]+addVector.data[i])
            return Vector(result)
    def __mul__(self, mulVector)->int|float:
        '''
            provides scolar multiply for vectors
        '''
        if type(mulVector) == Vector:
            if len(self.data) != len(mulVector.data):
                raise TimeoutError()
            else:
                result = 0
                for i in range(0, len(self.data)):
                    result += self.data[i]*mulVector.data[i]
            return result
        else:
            result = []
            for i in range(0, len(self.data)):
                result.append(self.data[i]*mulVector)
            return Vector(result)

    def __pow__(self, powVector:'Vector')->'Vector':
        '''
            provides vector multiply for vectors
                resultVector.len is calculated automaticly with sin between vectors
        '''
        if len(self.data) != len(powVector.data):
            raise TimeoutError()
        if len(self.data) != 3:
            raise TimeoutError()
        result = Vector([self.data[1]*powVector.data[2]-self.data[2]*powVector.data[1], -1*(self.data[0]*powVector.data[2]-self.data[2]*powVector.data[0]), self.data[0]*powVector.data[1]-self.data[1]*powVector.data[0]])
        result.__flags['Length']=self.__flags['Length']*powVector.__flags['Length']*Vector.find_sinus(self, powVector)
        return result
    def __str__(self):
        return str(self.data)

    def print(self):
        print(f'This a vector:')
        print(self.data)
        print(f'With flags:')
        for key, value in self.__flags.items():
            print(f'{key}: {value}')

    def vec_mul(self,value):
        a=[]
        for i in range (len(self.data)):
            a.append(self.data[i]*value)
        return Vector(a)

    def __sub__(self, subVector):
        '''
            provides sub-operation for vectors
        '''
        if type(subVector) == Vector:
            if len(self.data) != len(subVector.data):
                raise TimeoutError()
            else:
                result = []
                for i in range(0, len(self.data)):
                    result.append(self.data[i]-subVector.data[i])
            return Vector(result)
        else:
            result = []
            for i in range(0, len(self.data)):
                result.append(self.data[i]*subVector)
            return Vector(result)

    def copy(self):
        new_vec_data=[]
        for i in range(len(self.data)):
            new_vec_data.append(self.data[i])
        return Vector(new_vec_data)