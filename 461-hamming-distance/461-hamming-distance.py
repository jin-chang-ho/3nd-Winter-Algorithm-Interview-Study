class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        
        for n in bin(x ^ y):
            if n == '1':
                result = result + 1
                
        return result