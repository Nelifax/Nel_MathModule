__all__ = ['is_prime', 'gcd', 'lcm', 'euler_phi', 'carmichael']

from NelMath.objects.math_base.Rational import Rational

def is_prime(number:int|Rational)->bool:
    '''
        function based on factorization and list of primes effective up to 10^9 and still effective but more slowly for n>10^9
    '''
    from .factorization import factorize, squfof
    if number <4:
        return True
    number = Rational(number)
    factor = squfof(number)
    if factor != 1 and factor != number:
        return False
    else:
        factors = factorize(number)
        if len(factors)==1:
            return True
        else: 
            return False

def gcd(*numbers:int|Rational)->int:
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

def euler_phi(number:int|Rational)->Rational:
    '''
    returns euler phi result for number
    '''
    if not isinstance(number, Rational):
        number = Rational(number)
    if is_prime(number):
        return Rational-1
    else:
        from .factorization import factorize
        factors = factorize(number)
        result = 1
        if len(set(factors)) == len (factors):
            for factor in factors:
                result *= factor-1
            return result
        else:
            remembered_factor = factors[0]
            count=0
            for factor in factors:
                if remembered_factor != factor:
                    result*=remembered_factor**count-remembered_factor**(count-1)
                    count=1                    
                    remembered_factor = factor
                else:
                    count+=1
            if count!=1:
                result*=remembered_factor**count-remembered_factor**(count-1)
            else:
                result*=remembered_factor-1
            return result
def carmichael(number:int|Rational):
    '''
    returns carmichael function result for number
    '''
    if not isinstance(number, Rational):
        number = Rational(number)
    if is_prime(number):
        return Rational-1
    else:
        from .factorization import factorize
        factors = factorize(number)
        results = []
        remembered_factor = factors[0]
        count=0
        for factor in factors:
            if remembered_factor != factor:
                if factor == 2 and count > 2:
                    results.append(int((remembered_factor**count-remembered_factor**(count-1))*0.5))
                    count=1                    
                    remembered_factor = factor
                else:
                    results.append(remembered_factor**count-remembered_factor**(count-1))
                    count=1                    
                    remembered_factor = factor
            else:
                count+=1
        if count!=1:
            if factor == 2 and count > 2:
                results.append(int((remembered_factor**count-remembered_factor**(count-1))*0.5))
            else:
                results.append(remembered_factor**count-remembered_factor**(count-1))
        else:
            results.append(remembered_factor-1)
        return lcm(results)
