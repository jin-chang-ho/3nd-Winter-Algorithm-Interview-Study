class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        inter = []

        if len(nums1) >= len(nums2):
            for n in nums2:
                if n in nums1:
                    if n not in inter:
                        inter.append(n)
        else:
            for n in nums1:
                if n in nums2:
                    if n not in inter:
                        inter.append(n)

        return inter
        