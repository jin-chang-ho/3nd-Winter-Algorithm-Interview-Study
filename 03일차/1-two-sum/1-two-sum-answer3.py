class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map: # 해당 in 연산자는 딕셔너리의 키 값으로 찾음
                return [nums_map[target - num], i]
            nums_map[num] = i