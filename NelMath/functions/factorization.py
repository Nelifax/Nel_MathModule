__all__ = ['factorize' , 'get_primes', 'divisors']

from NelMath.objects.math_base.Rational import Rational
from math import isqrt

def squfof(number:int)->list:
    '''
        returns untrivial divisor for number, else return number if it has no untrivial divisors
        it's squfof implementation of https://homes.cerias.purdue.edu/~ssw/squfof.pdf
    '''
    number=Rational(number)
    if number.sqrt().references['float part'] == '0':
        return number.sqrt()
    if number%4==1:
        D = 2*number
    else:
        D = number
    S = Rational(D.sqrt().references['integer part'])
    Q_d = Rational(1)
    P = S.copy()
    Q = D-(P*P)
    L = Rational((2*((2*D.sqrt()).sqrt())).references['integer part'])
    B = 2*L
    i=0
    queue = []
    is_skipped = True
    while is_skipped:
        if i>B: return 1
        q = Rational(((S+P)/Q).references['integer part'])
        P_s = q*Q-P
        if Q<=L:
            if Q%2 == 0:
                queue.append((Q/2, P%(Q/2)))
            elif Q<=L/2:
                queue.append((Q, P%Q))
        t = Q_d+q*(P-P_s)
        Q_d = Q.copy()
        Q = t.copy()
        P = P_s.copy()
        if i % 2 == 1 or Rational(Q.sqrt().references['integer part'])**2-Q != '0':
            i += 1
            continue
        else:
            r = Rational(Q.sqrt().references['integer part'])
            is_skipped = False
            for pair in queue:
                if pair[0] == 1 and r == 1:
                    return number
                if (P-pair[1])%pair[0] == 0:
                    if r>1:
                        is_skipped = True
                        queue = queue[queue.index(pair)+1:]
                        i += +1
                        continue    
    Q_d = r
    P = P+r*Rational(((S-P)/r).references['integer part'])
    Q = (D-P*P)/Q_d
    iterator_border=i
    i=0
    while True:
        q = Rational(((S+P)/Q).references['integer part'])
        P_s = q*Q-P        
        if P==P_s:
            break
        if i>L:
            return 1
        t = Q_d+q*(P-P_s)
        Q_d = Q.copy()
        Q = t.copy()
        P = P_s.copy()        
        i+=1
    return Q.copy() if Q%2==1 else Q.copy()/2

def factorize(number:Rational|int, mode='std')->list:
    '''
    provides number factorization. returns an array with all factors of number (with duplication). Uses simple primal-division and squfof methods.
    parameters:
        number(int|Rational) - number to factorize
    '''
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if not isinstance(number, Rational):
        number=Rational(number)
    if number<0:
        number = -number
    from .number_functions import is_prime
    if is_prime(number):
        return [int(number)]
    factors = []
    for prime in primes:
        if prime>number:break
        while number%prime==0:
            number = number/prime
            factors.append((prime, True))  
    if number == 1:
        if mode=='degrees':
            factors=[factor[0] for factor in factors]
            unique_factors=set(factors)
            unique_factors=sorted(unique_factors)
            factors_with_degrees = []
            for elem in unique_factors:
                factors_with_degrees.append((elem, factors.count(elem)))
            return factors_with_degrees
        factors = [int(factor[0]) for factor in factors]
        factors.sort()
        return factors
    if is_prime(number):
        factors.append((number, True))
        number=1
    else:
        factors.append((number, False))
    while number != 1:
        for element in range(len(factors)):
            if factors[element][1]==True:
                continue
            factor=squfof(factors[element][0])
            factors.pop(element)
            if is_prime(factor):
                factors.append((factor, True))
            else:
                factors.append((factor, False))
            number=number/factor
            if is_prime(number):
                factors.append((number, True))
                number=1
            else:
                factors.append((number, False))
    if mode=='degrees':
        factors=[int(factor[0]) for factor in factors]
        unique_factors=set(factors)
        unique_factors=sorted(unique_factors)
        factors_with_degrees = []
        for elem in unique_factors:
            factors_with_degrees.append((elem, factors.count(elem)))
        return factors_with_degrees
    factors = [int(factor[0]) for factor in factors]
    factors.sort()
    return factors
        

def divisors(number:int|list)->list:
    '''
        return list of all divisors for current number
    '''

    if type(number)==int or isinstance(number, Rational):
        primes=factorize(number)
    else:
        primes=number
    divisors = {1}
    for factor in primes:
        divisors |= {d * factor for d in divisors}
    result=sorted(list(divisors))
    return result

def get_primes(limit: int) -> list:
    primes = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]