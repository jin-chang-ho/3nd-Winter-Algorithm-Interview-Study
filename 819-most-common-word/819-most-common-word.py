class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', " ")
        par_list = paragraph.split()

        for i in range(len(par_list)):
            if par_list[i].isalpha():
                par_list[i] = par_list[i].lower()
            else:
                par_list[i] = [al for al in par_list[i] if al.isalpha()]  
                par_list[i] = "".join(par_list[i]).lower()
                
        par_list = [par for par in par_list if par not in banned]
        
        count = Counter(par_list)
        
        for key, value in count.items():
            if value == max(count.values()):
                return key
        
        
    