class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2]) # 리스트 요소들의 합을 구해주는 sum 함수