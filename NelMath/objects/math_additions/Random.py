__all__ = ['Random']
class Random:
    #MT19937
    __w, __n, __m, __r = 32, 624, 397, 31
    __a = 0x9908B0DF
    __u, __d = 11, 0xFFFFFFFF
    __s, __b = 7, 0x9D2C5680
    __t, __c = 15, 0xEFC60000
    __l = 18
    __f = 1812433253
    __lower_mask = (1 << __r) - 1
    __upper_mask = (~__lower_mask) & ((1 << __w) - 1)
    
    def __init__(self, seed:int = 2147483549):
        '''
        provides class to work with random numbers
        class based on mersenne twister and realizes MT19937
        standart seed = 2147483549 but it can be changed by Random(seed:int)
        '''
        self.index = self.__n
        self.MT = [0] * self.__n
        self.MT[0] = seed
        for i in range(1, self.__n):
            self.MT[i] = (self.__f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (self.__w - 2))) + i) & 0xFFFFFFFF
    
    def __twist(self):
        for i in range(self.__n):
            x = (self.MT[i] & self.__upper_mask) + (self.MT[(i + 1) % self.__n] & self.__lower_mask)
            xA = x >> 1
            if x % 2 != 0:  # x — нечетное
                xA ^= self.__a
            self.MT[i] = self.MT[(i + self.__m) % self.__n] ^ xA
        self.index = 0
    
    def randint(self):
        if self.index >= self.__n:
            self.__twist()
        
        y = self.MT[self.index]
        self.index += 1
        
        y ^= (y >> self.__u) & self.__d
        y ^= (y << self.__s) & self.__b
        y ^= (y << self.__t) & self.__c
        y ^= y >> self.__l
        
        return y & 0xFFFFFFFF
    
    def rand_range(self, beg:int, end:int):
        '''
        returns randint from [beg:end] interval including both end points
        '''
        if beg>end:
            raise TimeoutError()
        number = self.randint() % end+1
        if number < beg:
            return number+beg
        else:
            return number
    
    def rand_primal(self, end:int = 2147483549):
        from functions.number_functions import is_simple
        a = self.rand_range(2, end)
        while not is_simple(a):
            a = self.rand_range(2, end)
        return a


