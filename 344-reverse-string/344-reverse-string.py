class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        
        for i in range(length // 2):
            temp = s[i]
            s[i] = s[length- 1 - i]
            s[length- 1 - i] = temp
        