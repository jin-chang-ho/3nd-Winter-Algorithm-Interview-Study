class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_output = []
        p = 1
        
        for i in range(len(nums)):
            left_output.append(p)
            p = p * nums[i]
        
        right_output = []
        p = 1
        
        for i in range(len(nums) - 1, -1, -1):
            right_output.append(p)
            p = p * nums[i]
            
        right_output.reverse()
        
        output = []
        
        for i in range(len(nums)):
            output.append(left_output[i] * right_output[i])
            
        return output
            