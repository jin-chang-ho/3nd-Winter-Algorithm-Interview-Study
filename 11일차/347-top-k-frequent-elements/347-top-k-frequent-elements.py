class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        answer = []
    
        for (key, value) in counter.most_common():
            if len(answer) >= k:
                break
            answer.append(key)
        
        return answer