#тут импорты
from random import randint
from objects import Matrix, Vector, Fraction, Random, Number
from tests.__init__ import *
from functions import factorize, is_simple, gcd, lcm, get_primes

#full_test()
k=37023229.32617
l=-27838260.66104 
print(k)
print(l)
a=Number(str(k))
b=Number(str(l))
print((a-b).value)
e=k-l
form = "{:.8f}".format(e)
print(form)