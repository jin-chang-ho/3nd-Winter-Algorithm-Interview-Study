class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minv = sys.maxsize
        
        for price in prices:
            minv = min(minv, price)
            maxp = max(maxp, price - minv)
            
        return maxp