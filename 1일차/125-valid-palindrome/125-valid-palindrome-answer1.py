class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars: Deque = collections.deque() # 양방향 큐인 deque 선언
        
        for char in s:
            if char.isalnum(): # 해당 문자가 영문자와 숫자인지 판별하는 string.isalnum() 함수
                chars.append(char.lower())

        while len(chars) > 1:
            if chars.popleft() != chars.pop():
                return False

        return True