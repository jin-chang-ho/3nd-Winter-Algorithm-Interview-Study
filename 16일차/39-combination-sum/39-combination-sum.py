class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def check(path):
            for i in range(len(candidates)):
                path.append(candidates[i]) 
                if sum(path) >= target:
                    if sum(path) == target:
                        check_answer.append(path[:])
                    path.pop()
                    break   
                check(path)
                path.pop()
            return
            
        check_answer = []
        candidates.sort()
        check([])
        
        for li in check_answer:
            li.sort()
            
        answer = []
        for li in check_answer:
            if li in answer:
                continue
            answer.append(li)
        
        return answer
        