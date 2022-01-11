class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                # 특정 리스트에서 해당 값의 인덱스를 찾아주는 list.index 함수
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)