__all__ = ['factorize']

def factorize(number:int)->list:
    '''
        returns list of all divisors except 1
        wrong for numbers>2^32
    '''
    factors=[]
    while number%2 == 0:
        number = int(number/2)
        factors.append(2)
    border = int(number**0.5)+1
    for i in range(3,border, 2):
        while number%i == 0:
            number = int(number/i)
            factors.append(i)
    if number != 1:
        factors.append(number)
    return factors

def divisors(number:int)->list:
    '''
        return list of all divisors for current number
    '''
    divisors = []
    factors = factorize(number)
    iterator = 0
    count = 1
    for factor in set(factors):
        divisors.append(factor)
    while count != len(factors):
        divisors.append(factors[iterator]*factors[iterator+1])
        count+=1
    #TODO