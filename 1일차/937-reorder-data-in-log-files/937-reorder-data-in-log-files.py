class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_logs_list = []
        num_logs_list = []
        
        for log in logs:
            if log.split()[1].isdigit(): # 문자열이 숫자인지 확인하는 str.isdigit() 함수
                num_logs_list.append(log)
            else:
                alpha_logs_list.append(log)

        # 리스트를 정렬하는 list.sort() 함수 -> key 값은 lambda 함수로 지정가능
        alpha_logs_list.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return alpha_logs_list + num_logs_list # 리스트끼리 합치면 확장
