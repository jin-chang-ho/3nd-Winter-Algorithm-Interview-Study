from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letter_map = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        com_list = []
        for digit in digits:
            com_list.append(digit)
        
        check_list = []
        for com in com_list:
            check_list.append(letter_map[com])
        
        answer_list = list(product(*check_list))
        
        for i in range(len(answer_list)):
            answer_list[i] = "".join(answer_list[i])
            
        return answer_list
        