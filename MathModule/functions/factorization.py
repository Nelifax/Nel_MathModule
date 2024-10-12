
__all__ = ['factorize' , 'get_primes']

def trunc_func(number:float)->int:
    return int(str(number).split('.')[0])

def squfof(number:int)->list:
    '''
        returns untrivial divisor for number, else return number if it has no untrivial divisors
        it's squfof implementation
    '''
    from .number_functions import is_full_square, trunc
    if is_full_square(number):
        return trunc(number**0.5)
    if number%4==1:
        D = 2*number
    else:
        D = number
    S = trunc(D**0.5)
    Q_d = 1
    P = S
    Q = D-(P*P)
    L = trunc(2*((2*(D**0.5))**0.5))
    B = 2*L
    i=2
    queue = []
    #2a
    is_skipped = True
    while is_skipped:
        if i>B: return 1
        q = trunc((S+P)/Q)
        P_s = q*Q-P
        #2b
        if Q<=L:
            if Q%2 == 0:
                queue.append((Q/2, P%(Q/2)))
            elif Q<=L/2:
                queue.append((Q, P%Q))
        #2c
        t = Q_d+q*(P-P_s)
        Q_d = Q
        Q = t
        P = P_s
        #2d
        if i % 2 == 1 or not is_full_square(Q):
            i += 1
            #this is 2e part
            continue
        else:
            #is_skipped = False
            r = trunc(Q**0.5)
            for pair in queue:
                if pair[0] == 1 and r == 1:
                    return number
                if (P-pair[1])%pair[0] == 0:
                    if r>1:
                        is_skipped = True
                        queue = queue[queue.index(pair)+1:]
                        i += +1
                        continue
        #print(f'---------------------F_{i}---------------------')
        #print(f'i={i}, Q_i-1={(-1)**(i-1)*Q_d}, 2P_i=2*{P}, Q_i={(-1)**i*Q}')
        if is_full_square(Q): break
    
    Q_d = r
    P = P+r*trunc((S-P)/r)
    Q = (D-P*P)/Q_d
    i=1
    while True:
        q = trunc((S+P)/Q)
        P_s = q*Q-P        
        if P==P_s:
            break
        t = Q_d+q*(P-P_s)
        Q_d = Q
        Q = t
        P = P_s        
        i+=1
        #print(f'---------------------G_{i}---------------------')
        #print(f'i={i}, Q_i-1={(-1)**(i-1)*Q}, 2P_i=2*{P}, Q_i={(-1)**i*Q_d}')
    return int(Q) if Q%2==1 else int(Q/2)

def factorize(number:int)->int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    #print(primes)
    if number<0:
        number = -1*number
    factors = []
    while number != 1:
        factor = squfof(number)
        if factor == 1:
            factors.append(number)
            number = 1
            continue
        number = int(number/factor)
        #print(f'FACTOR:{factor}<--->NUMBER:{number}')
        factors.append(factor)
    is_factors_simple = False
    while not is_factors_simple:
        is_factors_simple = True
        for index in range(0, len(factors)):
            result = squfof(factors[index])
            if result != 1 and result != factors[index]:
                factors.append(result)
                factors[index] = int(factors[index]/result)
                is_factors_simple = False
    for index in range(0, len(factors)):
        for prime in primes:
            if prime>factors[index]:break
            while factors[index] % prime == 0:
                factors.append(prime)
                factors[index] = int(factors[index]/prime)
            
    factors.sort()
    if 1 in factors:
        factors.reverse()
        factors = factors[:factors.index(1)]
        factors.reverse()
    return factors
        


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
    return factors'''

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

def get_primes(limit: int) -> list:
    primes = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]