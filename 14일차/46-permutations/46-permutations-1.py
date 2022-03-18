from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = list(permutations(nums))
        
        for i in range(len(answers)):
            answers[i] = list(answers[i])
        
        return answers
