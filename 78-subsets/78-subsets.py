class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def check(index, path):
            for i in range(index, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                check(i + 1, path)
                answer.append(path[:])
                path.pop()
            return
        
        answer = [[]]
        check(0, [])
        return answer