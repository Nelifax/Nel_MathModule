__all__ = ['factorize' , 'get_primes', 'divisors', 'LPS', 'ECM' ,'Ferma_method']

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

def LPS(number:Rational, B=None, trials=None):
    """
    Факторизация числа N с использованием LLL-алгоритма.
    
    Параметры:
    - N: число для факторизации (составное, не простое)
    - B: граница для базы простых чисел (по умолчанию ~exp(0.5 * sqrt(log N log log N)))
    - trials: количество попыток перед отказом
    
    Возвращает: нетривиальный делитель N или None, если не удалось
    """    
    from NelMath.properties.settings_handler import SettingsHandler
    from NelMath.objects.math_additions.Random import Random   
    import random
    import math    
    settings=SettingsHandler()
    scale=Rational('1'+'0'*(settings.get('mm_max_float_part')-1))
    N=int(number)
    rand=Random()
    def primes_list_till_border(border):
        primes_list=[]
        from NelMath.functions.number_functions import next_prime
        a=next_prime(2)
        while border>a:
            primes_list.append(Rational(a))
            a=next_prime(a+1)
        return primes_list
    # Шаг 1: Выбор базы простых чисел
    if B==None:
        B = int(math.exp(0.5 * math.sqrt(math.log(N) * math.log(math.log(N)))))
        #B = int(number.nroot(15))
    
    primes = primes_list_till_border(B)
    if trials==None:
        trials=settings.get('mm_LPS_max_trials')
    
    for _ in range(trials):
        # Шаг 2: Построение векторов решётки
        k = len(primes)
        lattice_vectors = []
        
        # Добавляем векторы вида (log(p_i), 0, ..., 0, log(N) * e_i)
        for i in range(k):
            vec = [Rational(0)] * (k + 1)
            vec[i] = Rational((primes[i].log() * scale).references['integer part'])
            vec[k] = Rational((number.log() * random.randint(0, 1) * scale).references['integer part'])  # случайный коэффициент
            lattice_vectors.append(vec)
        
        # Добавляем вектор (0, ..., 0, C), где C ≈ sqrt(k) * log(N)
        C = Rational((Rational(k).sqrt() * number.log() * scale).references['integer part'])
        last_vec = [Rational(0)] * (k + 1)
        last_vec[k] = C
        lattice_vectors.append(last_vec)
        from NelMath.objects.applied_algebra.Lattice import Lattice
        # Шаг 3: Применение LLL-алгоритма
        from NelMath.objects.linear_algebra.Vector import Vector
        a=[Vector(vec) for vec in lattice_vectors]
        lattice = Lattice([Vector(vec) for vec in lattice_vectors])
        print(len(lattice_vectors))
        reduced_basis = lattice.LLL()
        # Шаг 4: Поиск нетривиального соотношения
        for vec in reduced_basis.vectors:
            print(vec)
            if abs(vec.data[-1]) < scale/10:  # Проверка остатка
                x = 1
                x=[x*pow(primes[i], pow(vec.data[i],1,number), number) for i in range(k)]
                d = math.gcd(pow(x[0],1,N), N)
                if 1 < d < N:
                    return d
    return None

def ECM(number:Rational, B=None, curves=None):
    from NelMath.properties.settings_handler import SettingsHandler
    from NelMath.objects.applied_algebra.Curves.EllipticCurve import EllipticCurve
    from NelMath.functions.number_functions import get_primes_list, gcd, is_prime
    settings=SettingsHandler()
    if B==None:
        B=settings.get('mm_ECM_B_border')
        if B==0:
            #B=10**int(number.log(10))
            B=10**6
    if curves==None:
        curves=settings.get('mm_ECM_curve_trials')    
    '''
    primes=get_primes_list(B)
    for i in range(0,curves):
        E,P=EllipticCurve.get_random_curve(1,number-1, number, True)
        Q = P
        for p in primes:
            power = p
            while power <= B:
                try:
                    Q = Q * int(power)  # Умножаем на p^k
                except TimeoutError as e:
                    ee=int(str(e).split('gcd(')[1].split(',')[0])
                    d = gcd(ee, number)
                    if d > 1 and d < number:
                        return d
                power *= p
    '''
    for i in range(0,curves):
        E,P=EllipticCurve.get_random_curve(1,number-1, number, True)
        Q = P
        p = 2  # Начинаем с первого простого числа
        while p <= B:
            if is_prime(p):  # Проверяем простоту на лету
                power = p
                while power <= B:
                    try:
                        Q = Q * int(power)
                    except TimeoutError as e:
                        ee=int(str(e).split('gcd(')[1].split(',')[0])
                        d = gcd(ee, number)
                        if d > 1 and d < number:
                            return d
                    power *= p  # Следующая степень: p^2, p^3, ...
            p += 1 if p == 2 else 2

def Ferma_method(number:Rational):
    """
    Метод Ферма для факторизации числа N = p * q, где p ≈ q.
    Работает, если p и q близки друг к другу.
    Возвращает: (p, q) или None, если не удалось факторизовать.
    """
    a = Rational(number.sqrt().references['integer part'])
    if a * a < number:
        a += 1

    while True:
        b2 = a * a - number
        b = Rational(b2.sqrt().references['integer part'])
        if b * b == b2:
            p = a - b
            q = a + b
            if p * q == number:
                return (p, q)
            else:
                return None
        a += 1

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