from .matrix_tests import *
from .fraction_tests import *
from .number_tests import *

__all__=['full_test']

def full_test()->None:
    matrices_base_test()
    fractions_base_test()
    number_base_test()