class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        a_bin = bin(a & MASK)[2:].zfill(32) # 크기가 32가 되도록 앞을 0으로 채워주는 함수
        b_bin = bin(b & MASK)[2:].zfill(32)
        
        result = []
        carry = 0
        sum = 0
        
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])
            
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = Q2 ^ carry
            carry = Q1 | Q3
            
            result.append(str(sum))
        
        if carry == 1:
            result.append('1')
            
        result = int(''.join(result[::-1]), 2) & MASK # 2진수로 해석해 int로 바꾸기
        
        if result > INT_MAX:
            result = ~(result ^ MASK) # ~ : 양수면 2의 보수로 재해석 
            
        return result
            