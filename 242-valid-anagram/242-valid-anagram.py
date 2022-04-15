class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        check_dict = collections.defaultdict(int)
        
        for t_value in t:
            if t_value not in check_dict:
                check_dict[t_value] = 0
            check_dict[t_value] += 1
            
        s_c = collections.Counter(s)
        
        for key, value in check_dict.items():
            if key not in s_c or s_c[key] < value:
                return False
            
        return True
             