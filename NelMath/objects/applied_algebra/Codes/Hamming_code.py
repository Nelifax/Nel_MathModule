__all__ = ["Hamming_code"]

class Hamming_code():
    def __init__(self, data):   
        from NelMath import convert  
        self.data = convert(data, bin, list())
        self.n = len(self.data)
        self.m = self.n
        self.r = self.m - self.n
        while 2**self.r<self.m+1:
            self.m+=1
            self.r=self.m-self.n

    def encode(self):
        codeword = [0] * self.m
        data_pos = 0
        for i in range(1, self.m + 1):
            if not (i & (i - 1)) == 0:
                codeword[i - 1] = self.data[data_pos]
                data_pos += 1
        for p in [2**i for i in range(self.r)]:
            if p > self.m:
                continue
            xor_sum = 0
            for i in range(1,self.m+1):
                if i & p:
                    xor_sum ^= codeword[i - 1]
            codeword[p - 1] = xor_sum
        return codeword

    def decode(self, codeword):
        """Декодирование с исправлением 1 ошибки: codeword (m бит) -> исправленные данные (n бит)"""
        if len(codeword) != self.m:
            raise ValueError(f"Ожидается {self.m} бит в кодовом слове.")

        # Вычисляем синдром
        syndrome = 0
        for p in [2**i for i in range(self.r)]:
            if p > self.m:
                continue
            xor_sum = 0
            for i in range(1, self.m + 1):
                if i & p:
                    xor_sum ^= codeword[i - 1]
            if xor_sum:
                syndrome += p
        error_pos = None
        if 1 <= syndrome <= self.m:
            codeword[syndrome - 1] ^= 1
            error_pos = syndrome
        decoded_data = []
        for i in range(1,self.m+1):
            if not (i & (i - 1)) == 0:
                decoded_data.append(codeword[i - 1])

        return (decoded_data,error_pos-1) if error_pos!=None else (decoded_data, None)
