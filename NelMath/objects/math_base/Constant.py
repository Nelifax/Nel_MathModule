from .Rational import Rational, MM_number_max_float_part

__all__ = ['Constant']
 
global MM_use_constant_file
MM_use_constant_file = False

class Constant():
    '''
    determines singleton-constant class allow to set custom constants and get them whenever them needed
    constants are not changeble untill .update method
    there are builded constants such as pi or exponent
    parameter:
        float_part(int): determines length of float part for calculated constants
    '''
    __instance = None
    __initialized = False

    def __new__(cls, float_part:int=MM_number_max_float_part):
        if cls.__instance is None:
            cls.__instance = super(Constant, cls).__new__(cls)
        return cls.__instance

    def __init__(self, float_part:int=MM_number_max_float_part):
        if not self.__initialized:
            self.__max_float_part = float_part
            self.__initialized = True
    
    def e(self)->'Rational':
        '''
        returns an exponent with custom length of float part determined in Constant class
        exponent() returns a Rational class, to release a value use .e().value
        when .e() is calculated it's similar to use .exponent instead .e()
        '''
        if hasattr(self, 'exponent'):
            return self.exponent
        else:
            self.__get_exponent()
            return self.exponent

    def register(self, constants:dict={}):
        '''
        register new constant to release it later
        if constant already presents in constant-list it won't be rewrited. Use .update() instead
        parameter:
            constants(dict): {'constant_name':constant_value, ...}
        '''
        if not hasattr(self, 'constants'):
            self.constants = {}
        for constant, value in constants.items():
            if constant in self.constants:
                pass
            else:
                self.constants[constant]=value

    def release(self, constant:str)->any:
        '''
        returns a constant's value
        if there are no constant with current name: returns None. also returns None if no constants are registered
        parameter:
            constant(str): the name of constant you want to release
        '''
        if not hasattr(self, 'constants'):
            return None
        if constant in self.constants.keys():
            return self.constant[constant]
        else:
            return None

    def update(self, constants:dict={}):
        '''
        updates all matched constants which present in constants dict and class dict
        if updated constant not present in class constants - do nothing. To add a constant use .register instead
        parameter:
            constants(dict): {constant_name: new_constant_value, ...} 
        '''
        if not hasattr(self, 'constants'):
            return
        for constant, value in constants.items():
            if constant in self.constants:
                self.constants[constant] = value

    def forget(self, constant):
        '''
        delete a constant with it value from dictionary
        parameter:
            constant(str): a constant to delete
        do nothing if constant isn't present in constant dict
        '''
        if not hasattr(self, 'constants'):
            return
        if constant in self.constants.items():
            self.constants.pop(constant)

    def __get_exponent(self):        
        result = Rational(1, {'max float part': self.__max_float_part}) 
        result_next = result.copy()   
        iterator = Rational(1, {'max float part': self.__max_float_part})
        border = Rational('0.'+'0'*(self.__max_float_part-1)+'1', {'max float part': self.__max_float_part})
        while True:
            result_next = result_next.__mul__(1/iterator, 'exp')
            result += result_next
            if abs(result_next) < border:
                break
            iterator += 1
        self.exponent=result._Rational__self_round_float()

    def __get_pi(self):
        pass