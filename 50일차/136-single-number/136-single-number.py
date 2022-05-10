class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        for (key, value) in counter.items():
            if value == 1:
                return key
        
        
        