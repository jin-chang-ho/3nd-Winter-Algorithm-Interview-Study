class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split() if word not in banned] # 해당 정규식은 단어 문자를 제외한 값은 ' '로 치환한다는 뜻

        counts = collections.Counter(words)

        # 흔하게 등장하는 단어와 그 갯수를 출력하는 dictionary.most_common() 함수 -> 출력 형태는 [()]
        return counts.most_common(1)[0][0]
        
        
    