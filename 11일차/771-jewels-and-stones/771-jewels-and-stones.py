class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter([s for s in stones])
        answer = 0
        
        for jewel in [s for s in jewels]:
            if contains(counter, jewel): # counter의 키에 jewel이 있는지 확인하는 contains 함수
                answer = answer + counter[jewel]
        
        return answer
        
        