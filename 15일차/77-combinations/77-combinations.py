class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def check(index, path, al):
            if len(path) == k:
                result.append(path[:])
                return
            
            prev_al = al[:]
            for i in range(len(al)):
                if path and path[-1] > al[i]:
                    continue
                
                path.append(al[i])
                al.remove(al[i])
                index = index + 1
                check(index, path, al)
                al = prev_al[:]
                path.pop()
            
        result = []
        check(0, [], [c for c in range(1, n + 1)])
        return result
            
        