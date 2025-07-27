__all__ = ['is_prime', 'gcd', 'lcm', 'euler_phi', 'carmichael', 'next_prime', 'find_primitive_root', 'legendre_symbol']

from NelMath.objects.math_base.Rational import Rational

def is_prime(number:int|Rational, tries:int=0)->bool:
    '''
        function based on Miller-Rabin
    '''
    if tries==0 or tries<0:        
        from NelMath.properties.settings_handler import SettingsHandler
        settings=SettingsHandler()
        tries=settings.get('mm_MR_prime_max_tries')
    if number<1: return False
    if number<=3: return True
    if number%2==0: return False
    if isinstance(number, Rational):
        number = int(number)
    r, d = 0, number - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    from random import randint
    import time
    for _ in range(tries):
        results=0
        a=randint(2, number-2)
        x = pow(a,d,number)
        if x == 1 or x == number - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True

def next_prime(low_border:int)->int:
    '''
    provides next prime number based on miller-rabin prime test
    '''
    primes=[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime = low_border
    if prime==2 or prime in primes:
        return prime
    if prime<98:
        while prime not in primes:
            prime+=1
        return prime
    if prime%2==0:
        prime+=1
    candidates=[]
    from NelMath.properties.settings_handler import SettingsHandler
    settings=SettingsHandler()
    high_border=settings.get('mm_MR_prime_high_candidate_border')
    while True:        
        for i in range(prime, prime+high_border, 2):
            candidates.append(i)
        for prime_ in primes:
            start = candidates[0] + (prime_ - candidates[0] % prime_) % prime_
            multiples = range(start, candidates[-1] + 1, prime_)
            candidates = [x for x in candidates if x not in multiples] 
        for candidate in candidates:
            if is_prime(candidate):
                return candidate
        prime=candidates[-1]

def get_primes_list(border:int):
    primes=[]
    a=2
    while a<border:
        primes.append(a)        
        a=next_prime(a+1)
    return primes
          


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
    if is_prime(a) and is_prime(b):return 1
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
    from NelMath.objects.math_base.Fraction import Fraction
    if not isinstance(number, Rational):
        number = Rational(number)
    if is_prime(number):
        return number-1
    else:
        res=number
        a=2
        while a<number:
            if res%a=='0':
                res*=Fraction([a-1,a])
            a=next_prime(a+1)
        res.simplify()
        return int(str(res).split('/')[0])

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

def find_primitive_root(modulo:int, divisor_list:list=[], mode='asc'):
    if not is_prime(modulo):
        return None
    if divisor_list==[]:
        from .factorization import divisors
        divisor_list=divisors(euler_phi(modulo))
    is_root_found=False
    match(mode):
        case 'des':
            i=modulo-1
            while not is_root_found:
                check=True
                for degree in divisor_list[1:-1]:
                    if pow(i, degree, modulo)==1:
                        check=False
                        i-=1
                        break
                if check:
                    return i
        case 'random':
            from ..objects.math_additions.Random import Random
            gen=Random()
            while not is_root_found:
                check=True
                root=gen.rand_range(2,modulo-1)                    
                for degree in divisor_list[1:-1]:
                    if pow(root, degree, modulo)==1:
                        check=False
                        break
                if check:
                    return root
        case _:
            i=2
            while not is_root_found:
                check=True
                for degree in divisor_list[1:-1]:
                    if pow(i, degree, modulo)==1:
                        check=False
                        i+=1
                        break
                if check:
                    return i

def legendre_symbol(a,n):
    if a==-1:
        return pow(a,int((n-1)/2))