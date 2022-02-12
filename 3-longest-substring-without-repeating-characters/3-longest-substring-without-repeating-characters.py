class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer_dic = collections.defaultdict(list)
        
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        for i in range(len(s) - 1):
            temp_list = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] in temp_list:
                    break
                temp_list.append(s[j])
            answer_dic[len(temp_list)].append("".join(temp_list))
        
        return max(list(answer_dic.keys()))
        