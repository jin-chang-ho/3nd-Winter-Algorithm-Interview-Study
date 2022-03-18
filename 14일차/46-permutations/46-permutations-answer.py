from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def check(index, path, nums):
            prev_nums = nums[:]
            
            if len(path) == nums_len:
                answer.append(path[:])
                return
            
            for i in range(len(nums)):
                path.append(nums.pop(i))
                check(i + 1, path, nums)
                nums = prev_nums[:]
                path.pop(-1)
        
        if not nums:
            return [[]]
        
        answer = []
        
        nums_len = len(nums)
        
        check(0, [], nums)
        
        return answer
