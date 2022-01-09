class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', " ")
        par_list = paragraph.split()

        for i in range(len(par_list)):
            if par_list[i].isalpha(): # 문자열이 알파벳인지 확인하는 str.isalpha() 함수
                par_list[i] = par_list[i].lower()
            else:
                par_list[i] = [al for al in par_list[i] if al.isalpha()]  
                par_list[i] = "".join(par_list[i]).lower()
                
        par_list = [par for par in par_list if par not in banned] # 특정 문자열이 리스트에 있는지 확인하는 in
        
        count = Counter(par_list) # 각 리스트 요소를 키로, 해당 요소의 갯수를 값으로 저장하는 Counter dictionary
        
        for key, value in count.items(): # 딕셔너리의 키, 값을 반환하는 dictionary.items() 함수
            if value == max(count.values()):
                return key
        
        
    