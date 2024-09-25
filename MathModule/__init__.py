#тут импорты
from MM_objects import *
from MM_objects.Matrix import Matrix
from MM_tests.__init__ import *

full_test()
a = Matrix('1,2,3,2,1,3,3,2,1')
(a.invert()*a.invert()).print()
((a**2)**-1).print()

