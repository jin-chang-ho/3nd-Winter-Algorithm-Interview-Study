class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # 아래 정규식의 기능은 문자열에서 알파벳 소문자 혹은 숫자가 아닌 문자를 모두 없애버리는 것이다.
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


