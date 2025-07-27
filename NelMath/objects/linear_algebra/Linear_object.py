from NelMath.properties.settings_handler import SettingsHandler
__all__=['Linear_object']

class Linear_object(list):
    __qualname__='LinearAlgebra'
    __module__='LinearAlgebra'
    def __new__(cls, value, flags={}):
        from NelMath.objects.linear_algebra.Vector import Vector
        if cls is not Linear_object:
            return super().__new__(cls)        
        settings=SettingsHandler()
        #todo:use settings params
        if type(Linear_object.check_list_dim_structure(value)[0])!=list:
            from NelMath.objects.linear_algebra.Vector import Vector
            return Vector(value,cls._check_flags(flags, 'Vector'))
        else:
            from NelMath.objects.linear_algebra.Matrix import Matrix
            flags=cls._check_flags(flags, 'Matrix')
            return Matrix(value,flags)

    @staticmethod
    def _check_flags(flags, construction)->dict:
        settings=SettingsHandler()
        match(construction):
            case 'Vector':
                std_flags={
                    'Length': 0,
                    'Dimension': 0,
                    'Normalized': False,
                    #'Unit': Vector.is_vector_unit(self)
                    'auto_calculations': settings.get('mm_vector_auto_calculations'),
                    'type': 'Vector',
                    }
            case 'Matrix':
                std_flags={
                    'is_square': False, 
                    'factor': 0,
                    'invertible': False,
                    'dimension': (0,0),
                    'columns': 0,
                    'rows': 0,
                    'rank': 'undefined',
                    'auto_calculations': settings.get('mm_matrix_auto_calculations'),
                    'type': 'Matrix'
                    }
        if flags!={}:
            for flag in flags:
                if flag not in std_flags.keys():
                    raise TimeoutError()
            std_flags.update(flags)
        return std_flags

    @staticmethod
    def get_dimensions(element_list:list)->list|int:
        '''
        returns tuple of list dimensions [x,y,...]
           ex:get_dimensions([[2,3],[2,3]]) returns [2,2]
           ex:get_dimensions([[2,3,1],[2,3,2]]) returns [2,3]
           ex:get_dimensions([2,3,1,2,3,2]) returns 6
            Note!: if list has incorrect structure this method returns (0)
            ex:get_dimensions([1,3],[2]) returns (0)
        '''
        structure=Linear_object.check_list_dim_structure(element_list)
        if not Linear_object.is_structure_correct(element_list, structure):
            return 0
        dims=[]
        if type(structure[0])!=list:
            return structure[0]
        while type(structure)==list and len(structure)!=1:  
            dims.append(len(structure))          
            structure=structure[0]
        dims.append(structure[0])
        return dims


    @staticmethod
    def is_structure_correct(element_list=None, structure=None)->bool:
        '''
        checks if list structure is correct: is list has equal element count in suited lists
        '''
        if structure==None:
            if element_list==None:
                return False
            structure=Linear_object.check_list_dim_structure(element_list)
        if type(structure[0])==list and type(structure[-1])==list:
            base_structure=structure[0]
            for struct in structure:
                if base_structure!=struct:
                    return False
        return True

    @staticmethod
    def check_list_dim_structure(elem_list:list)->list:
        '''
        returns True if all elements in list have equal structure
        else returns False
        '''
        structure=[]
        elems=0
        if elem_list==[]:           
            structure.append(0)
        for element in elem_list:
            if type(element)==list:
                structure.append(Linear_object.check_list_dim_structure(element))
            else:
                elems+=1
        if elems>0:
            structure.append(elems)
        return structure

    @staticmethod
    def check_list_element_types(elem_list:list, el_type=None)->list:
        '''
        returns True if all elements in list have equal types
        else returns False
        '''
        if el_type==None:
            elem=elem_list[0]
            while type(elem)==list:
                elem=elem[0]
            el_type=type(elem)
        for element in elem_list:
            inner_result=True
            if type(element)==list:
                inner_result=Linear_object.check_list_element_types(element, el_type)
            elif type(element)!=el_type:
                return False
            if not inner_result:
                return False
        return True
    '''

    def __add__(self, other):
        from NelMath.objects.math_base.Operators.Plus.OperatorPlus import OperatorPlus
        return OperatorPlus().execute(self, other)

    def __radd__(self, other):
        from NelMath.objects.math_base.Operators.Plus.OperatorPlus import OperatorPlus
        return OperatorPlus().execute(other, self)

    def __sub__(self, other):        
        from NelMath.objects.math_base.Operators.Minus.OperatorMinus import OperatorMinus
        return OperatorMinus().execute(self, other)

    def __rsub__(self, other):        
        from NelMath.objects.math_base.Operators.Minus.OperatorMinus import OperatorMinus
        return OperatorMinus().execute(other, self)
    
    def __sign_invert(self):
        if self.sign == '+':
            self.sign = '-'
            self.value = '-'+self.value
        else:
            self.sign = '+'
            self.value = self.value[1:]

    def __neg__(self):
        neg = self.copy()
        if neg.references['float part'] == '0' and neg.references['integer part'] == '0':
            if neg.sign == '+':
                return neg          
        neg.__sign_invert()
        return neg

    def __mul__(self, other):        
        from NelMath.objects.math_base.Operators.Multiply.OperatorMultiply import OperatorMultiply
        return OperatorMultiply().execute(self, other)

    def __rmul__(self, other):        
        from NelMath.objects.math_base.Operators.Multiply.OperatorMultiply import OperatorMultiply
        return OperatorMultiply().execute(other, self)

    def __truediv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorTruediv import OperatorTruediv
        return OperatorTruediv().execute(self, other)

    def __rtruediv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorTruediv import OperatorTruediv
        return OperatorTruediv().execute(other, self)

    def __floordiv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorFloordiv import OperatorFloordiv
        return OperatorFloordiv().execute(self, other)

    def __rfloordiv__(self, other):
        from NelMath.objects.math_base.Operators.Division.OperatorFloordiv import OperatorFloordiv
        return OperatorFloordiv().execute(other, self)

    def __pow__(self, exponent, modulo = None):
        from NelMath.objects.math_base.Operators.Pow.OperatorPow import OperatorPow
        return OperatorPow().execute(self, exponent, modulo)

    def __mod__(self, other):
        from NelMath.objects.math_base.Operators.Mod.OperatorMod import OperatorMod
        return OperatorMod().execute(self, other)
    
    def __rmod__(self, other):
        from NelMath.objects.math_base.Operators.Mod.OperatorMod import OperatorMod
        return OperatorMod().execute(other, self)

    def sqrt(self, precision:int=0):
        from NelMath.objects.math_base.Operators.Root.OperatorRoot import OperatorRoot
        return OperatorRoot().execute(self, 2, precision)

    def nroot(self, exponent, precision:int=0):
        from NelMath.objects.math_base.Operators.Root.OperatorRoot import OperatorRoot
        return OperatorRoot().execute(self, exponent, precision)

    def ln(self):
        from NelMath.objects.math_base.Operators.Logx.OperatorLnX import OperatorLnX
        return OperatorLnX().execute(self)

    def log(self, base=2):
        from NelMath.objects.math_base.Operators.Logx.OperatorLog import OperatorLog
        return OperatorLog().execute(self, base)

    def __abs__(self):
        if self.sign == '-':
            return -self
        else:
            return self

    def __int__(self)->int:
        if self.sign == '-':
            return -int(self.references['integer part'])
        else:
            return int(self.references['integer part'])

    def __index__(self):
        if self.references['float part']=='0':
            return int(self.value)
        raise TimeoutError('Number has an float part')

    def __float__(self)->float:       
        return float(self.value)

    def __str__(self)->str:
        return str(self.value)

    def __hash__(self):
        return hash(self.value)    

    def __format__(self, format_spec):        
        if format_spec == "hex":
            return hex(self.value)
        elif format_spec == "bin":
            return bin(self.value)
        elif format_spec:
            return format(str(self.value), format_spec)
        else:
            return self.__str__()
        '''