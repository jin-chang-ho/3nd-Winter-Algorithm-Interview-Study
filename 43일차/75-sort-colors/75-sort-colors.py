class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_list = [0, 0, 0]
        
        for num in nums:
            if num == 0:
                num_list[0] += 1
            elif num == 1:
                num_list[1] += 1
            else:
                num_list[2] += 1
        
        for i in range(len(nums)):
            if num_list[0] != 0:
                nums[i] = 0
                num_list[0] -= 1
            elif num_list[1] != 0:
                nums[i] = 1
                num_list[1] -= 1
            elif num_list[2] != 0:
                nums[i] = 2
                num_list[2] -= 1