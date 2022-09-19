class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 0xFFFFFFFF
        count = 0
        
        for c in bin(n & mask):
            if c == '1':
                count = count + 1
                
        return count