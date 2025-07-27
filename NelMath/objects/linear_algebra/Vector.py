from NelMath.objects.linear_algebra.Linear_object import Linear_object
__all__ = ['Vector']

class Vector(Linear_object):
    def __init__(self, values:list):
        if isinstance(values, Vector):
            self.data = [k for k in values.data]
        else:
            self.data = values
        self.__flags = {
            'Dimension': len(values),
            'Normalized': False,
            #'Unit': Vector.is_vector_unit(self)
            }
        self.__length=None

    def __getitem__(self, index):
        return self.data[index]
    def __len__(self):
        return len(self.data)
        
    @staticmethod
    def find_length(vector:'Vector')->int|float:
        from NelMath import Number
        length = Number(sum(x**2 for x in vector.data))
        return length.sqrt()

    @property
    def length(self):
        if self.__length==None:
            self.__length=Vector.find_length(self)
        return self.__length

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
        from NelMath.objects.math_base.Fraction import Fraction
        for i in range(0, len(self.data)):
            self.data[i] = Fraction([self.data[i],self.length])
        self.__flags['Normalized'] = True
        self.__length = 1
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
            return Vector([x+y for x,y in zip(self.data, addVector.data)])
            
    def __mul__(self, mulVector)->int|float:
        '''
            provides scolar multiply for vectors
        '''
        if type(mulVector) == Vector:
            if len(self.data) != len(mulVector.data):
                raise TimeoutError()
            else:
                return sum(x*y for x,y in zip(self.data, mulVector.data))
        else:
            return Vector([a*mulVector for a in self.data])

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
        return Vector([a*value for a in self.data])
    def vec_add(self,value):
        return Vector([a+value for a in self.data])

    def __sub__(self, subVector):
        '''
            provides sub-operation for vectors
        '''
        if type(subVector) == Vector:
            if len(self.data) != len(subVector.data):
                raise TimeoutError()
            else:
                return Vector([x-y for x,y in zip(self.data, subVector.data)])
        else:
            return Vector([a-subVector for a in self.data])

    def copy(self):
        new_vec_data=[]
        for i in range(len(self.data)):
            new_vec_data.append(self.data[i])
        return Vector(new_vec_data)

    def __repr__(self):
        return '['+', '.join([str(dat) for dat in self.data])+']'

    def zero(n)->'Vector':
        '''
        returns Vector object with n zero elements
        '''        
        from NelMath import Rational
        return Vector([Rational(0) for _ in range(n)])