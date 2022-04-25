class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        score = []
        
        for i, point in enumerate(points):
            score.append([sqrt(point[0] * point[0] + point[1] * point[1]), i])
        
        score.sort()
        
        answer = []
        count = 0
        for _, index in score:
            if count == k:
                break
            answer.append(points[index])
            count = count + 1
            
        return answer