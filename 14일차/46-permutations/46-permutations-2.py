class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def check(path, nums):
            prev_nums = nums[:]
            
            if len(path) == nums_len:
                answer.append(path[:])
                return
            
            for i in range(len(nums)):
                path.append(nums.pop(i))
                check(path, nums)
                nums = prev_nums[:]
                path.pop(-1)
        
        if not nums:
            return [[]]
        
        answer = []
        
        nums_len = len(nums)
        
        check([], nums)
        
        return answer
