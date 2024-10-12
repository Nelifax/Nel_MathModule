#тут импорты
from random import randint
from objects import Matrix, Vector, Fraction, Random, Number
from tests.__init__ import *
from functions import factorize, is_simple, gcd, lcm, get_primes

full_test()
a=Number('114.4001')
b=Number('51.3002')
print((a-b).value)