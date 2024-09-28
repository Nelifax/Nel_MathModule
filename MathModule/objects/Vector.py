__all__ = ['Vector']

class Vector():
    def __init__(self, values:list):
        self.values = values
        self.__flags = {
            'Length': Vector.find_length(self),
            'Dimension': len(values),
            'Normalized': False,
            'Unit': Vector.is_vector_unit(self)
            }
        
    @staticmethod
    def find_length(vector:'Vector')->int|float:
        length = 0
        for i in range(0, len(vector.values)):
            length+=vector.values[i]**2
        return length**0.5

    @staticmethod
    def find_sinus(vector_A:'Vector', vector_B:'Vector')->float:
        return (vector_A*vector_B)/(vector_A.__flags['Length']*vector_B.__flags['Length'])

    @staticmethod
    def is_vectors_collinear(vector_A:'Vector', vector_B:'Vector')->bool:        
        if len(vector_A.values) != len(vector_B.values):
            raise TimeoutError()
        if vector_A.len == 0 or vector_B.len == 0:
            return True
        result = []
        for i in range(0, len(vector_A.values)):
            if vector_B[i] == 0 and vector_A[i] != 0:
                return False
            elif vector_B[i] == 0 and vector_A[i] == 0:
                continue
            result.append(vector_A.values[i]/vector_B.values[i])
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
        for i in range(0, len(self.values)):
            self.values[i] = self.values[i]/self.__flags['Length']
        self.__flags['Normalized'] = True
        self.__flags['Unit'] = Vector.is_vector_unit(self)
        return self

    @staticmethod
    def is_vector_unit(vector:'Vector')->bool:
        has_unit = False
        for i in range (0, len(vector.values)):
            if vector.values[i] == 0:
                continue
            elif vector.values[i] == 1:
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
        if len(self.values) != len(addVector):
            raise TimeoutError()
        else:
            result = []
            for i in range(0, len(self.values)):
                result.append(self.values[i]+addVector.values[i])
            return Vector(result)
    def __mul__(self, mulVector)->int|float:
        '''
            provides scolar multiply for vectors
        '''
        if type(mulVector) == Vector:
            if len(self.values) != len(mulVector.values):
                raise TimeoutError()
            else:
                result = 0
                for i in range(0, len(self.values)):
                    result += self.values[i]*mulVector.values[i]
            return result
        else:
            result = []
            for i in range(0, self.values):
                result.append(self.values[i]*mulVector)
            return Vector(result)

    def __pow__(self, powVector:'Vector')->'Vector':
        '''
            provides vector multiply for vectors
                resultVector.len is calculated automaticly with sin between vectors
        '''
        if len(self.values) != len(powVector.values):
            raise TimeoutError()
        if len(self.values) != 3:
            raise TimeoutError()
        result = Vector([self.values[1]*powVector.values[2]-self.values[2]*powVector.values[1], -1*(self.values[0]*powVector.values[2]-self.values[2]*powVector.values[0]), self.values[0]*powVector.values[1]-self.values[1]*powVector.values[0]])
        result.__flags['Length']=self.__flags['Length']*powVector.__flags['Length']*Vector.find_sinus(self, powVector)
        return result
    def __str__(self):
        return str(self.values)

    def print(self):
        print(f'This a vector:')
        print(self)
        print(f'With flags:')
        for key, value in self.__flags.items():
            print(f'{key}: {value}')