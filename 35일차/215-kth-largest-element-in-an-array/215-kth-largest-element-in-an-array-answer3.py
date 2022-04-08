class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heap.nlargest(k, nums)[-1]
