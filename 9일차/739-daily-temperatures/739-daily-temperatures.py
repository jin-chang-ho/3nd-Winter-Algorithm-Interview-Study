class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        gap_stack = [0 for _ in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            if temp_stack and temperatures[temp_stack[-1]] < temperatures[i]:
                while temp_stack and temperatures[temp_stack[-1]] < temperatures[i]:
                    gap_stack[temp_stack[-1]] = i - temp_stack[-1]
                    temp_stack.pop()
            
            temp_stack.append(i)
            
        return gap_stack