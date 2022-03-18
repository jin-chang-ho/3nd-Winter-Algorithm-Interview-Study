class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
                
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                
        results = []
        prev_elements = []
        
        dfs(nums)
        
        return results
                
