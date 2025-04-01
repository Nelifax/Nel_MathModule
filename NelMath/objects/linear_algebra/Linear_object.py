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
            return Vector(value)
        else:
            from NelMath.objects.linear_algebra.Matrix import Matrix
            return Matrix(value)

    @staticmethod
    def _check_flags(flags, construction)->dict:
        settings=SettingsHandler()
        match(construction):
            case 'Vector':
                std_flags={
                    'all references': False,
                    'max float part': settings.get('mm_max_float_part'),
                    'exponential view': False,
                    'standart view': False,
                    'type changing': settings.get('mm_dynamic_class_changing'),
                    'type': 'integer',
                    }
            case 'Matrix':
                std_flags={
                    'all references': False,
                    'max float part': settings.get('mm_max_float_part'),
                    'exponential view': False,
                    'standart view': False,        
                    'auto-simplify': True,
                    'parts as Rational': True,
                    'float to numerator': True,
                    'type changing': settings.get('mm_dynamic_class_changing'),
                    'type': 'fraction'
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


