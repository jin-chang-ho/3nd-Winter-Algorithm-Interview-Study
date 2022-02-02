class Solution:
    def isValid(self, s: str) -> bool:
        check_list = []
        
        for check in s:
            if check == '(' or check == '{' or check == '[':
                check_list.append(check)
            if check == ')' or check == '}' or check == ']':
                if len(check_list) == 0:
                    return False
                if check == ')':
                    if check_list.pop() != '(':
                        return False
                if check == '}':
                    if check_list.pop() != '{':
                        return False
                if check == ']':
                    if check_list.pop() != '[':
                        return False
        
        if check_list:
            return False
        
        return True