__all__ = ['is_simple', 'gcd', 'lcm']


def is_simple(number:int)->bool:
    '''
        function based on factorization and list of primes effective up to 10^9 and still effective untill n<10^34
    '''
    from .factorization import get_primes, factorize
    if number <4:
        return True
    if number<=2147483648:
        primes = get_primes(trunc(number**0.5)+1)
        if number in primes:
            return True
        else:
            return False
    else:
        factors = factorize(number)
        #print(factors)
        if len(factors)==1:
            return True
        else: return False

def gcd(*numbers:int)->int:
    '''
    provides greatest common divisor for numbers by \'Euclidean algorithm\'
    parameters:
        *numbers(tuple|int|list): numbers for gcd calculation
            you can use function by list|tuple int numbers
            ex: gcd(33) or gcd([33,44,55]) or gcd(12,15,18,20)    
    '''
    if type(numbers[0]) == list:
        numbers = (*numbers[0],)
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers)>2:
        number_a = numbers[0]
        numbers = numbers[1:]
        while len(numbers) > 1:
            number_b = numbers[0]
            numbers = numbers[1:]
            number_a = gcd(number_a, number_b)
        return gcd(number_a, numbers[0])
    if numbers[0] == numbers[1]: 
        return numbers[0]
    if numbers[0] < numbers[1]:
        b, a = numbers[1], numbers[0]
    else:
        a = numbers[0]
        b = numbers[1]
    reminder = a-b*(a//b)
    while reminder != 0:
        reminder = a-b*(a//b)
        if reminder == 0: break
        a = b
        b = reminder
    return b
          
def lcm(*numbers:int)->int:
    '''
    provides least common multiple function for numbers based on gcd and multiplies
    '''
    if type(numbers[0]) == list:
        numbers = (*numbers[0],)
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers)>2:
        number_a = numbers[0]
        numbers = numbers[1:]
        while len(numbers) > 1:
            number_b = numbers[0]
            numbers = numbers[1:]
            number_a = lcm(number_a, number_b)
        return lcm(number_a, numbers[0])
    return int((numbers[0]*numbers[1])/gcd(numbers[0],numbers[1]))

def trunc(number:float)->int:
    '''
    provides integer part of float (no any round)
    ex: float(2,327...)->int(2); float(3,993)...->int(3)
    '''
    return int(str(number).split('.')[0])

def is_full_square(number:int)->bool:
    if  number != 1 and trunc(number**0.5)**2 == number:
        return True
    else:
        return False