class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_logs_list = []
        num_logs_list = []
        
        for log in logs:
            if log.split()[1].isdigit():
                num_logs_list.append(log)
            else:
                alpha_logs_list.append(log)
                
        alpha_logs_list.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return alpha_logs_list + num_logs_list