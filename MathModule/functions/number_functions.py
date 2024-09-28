from .factorization import factorize
__all__ = ['is_simple', 'gcd', 'lcm']

def is_simple(number)->bool:
    '''
        function based on factorization so useless for numbers>2^32
    '''
    factors = factorize(number)
    if len(factors) == 1:
        return True
    else:
        return False

def gcd(numbers:list[int])->int:
    pass

def lcm(numbers:list[int])->int:
    factors = set([1])
    for number in numbers:
        factors.add(set(factorize(number)))
    result = 1
    for number in factors:
        result = result*number
    return result