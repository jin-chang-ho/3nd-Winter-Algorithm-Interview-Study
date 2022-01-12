class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        sum = 0
        while len(nums) >= 2:       
            sum += min(nums.pop(0), nums.pop(0))
        
        return sum