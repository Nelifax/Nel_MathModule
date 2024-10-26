from objects import Matrix, Random
from functions import is_simple

__all__ = ['Key', 'mm_minimum_key_value', 'mm_maximum_key_value', 'mm_key_only_primals', 'mm_key_enable_number_repeating', 'mm_key_maximum_repeat_count', 'mm_key_pattern']

global mm_minimum_key_value, mm_maximum_key_value, mm_key_only_primals, mm_key_enable_number_repeating, mm_key_maximum_repeat_count, mm_key_pattern
mm_minimum_key_value = 2
mm_maximum_key_value = 2147483648
mm_key_only_primals = True
mm_key_enable_number_repeating = True
mm_key_maximum_repeat_count = -1
mm_key_pattern = [[0,1,0],[1,0,1],[0,1,0]]

class Key():
    MM_key_symmetrical = 0
    MM_key_asymmetrical = 1
    def __init__(self, keySequence = '', dim:int=3, keyPath:str='', keyType:int=MM_key_asymmetrical):
        try:
            with open(keyPath, 'r', encoding='UTF-8') as keyFile:
                keyFileType = keyFile.readline()
                if keyFileType != keyType:
                    raise TimeoutError()
                self.key = Matrix(keyFile.readline())
        except:
            with open(keyPath, 'w', encoding='UTF-8') as keyFile:
                if keySequence == '':
                    self.key = Key.generate(keyType, dim)
                    keyFile.writelines([keyType,self.key])
                else:
                    self.key = Matrix(keySequence)
                    keyFile.writelines([keyType,self.key])

    def generate(keyType:int, dim:int = 3):
        generator = Random()
        keyGenerator = ''
        used_generator_patterns = []
        for i in range(0, dim**2):
            if mm_key_only_primals:
                generator+= str(Random)+','
            else:
                pass
