class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        
        check = 0
        
        while check + 1 < len(intervals):
            if intervals[check + 1][0] >= intervals[check][0] and intervals[check + 1][0] <= intervals[check][1]:
                start = intervals[check][0]
                
                if intervals[check][1] > intervals[check + 1][1]:
                    end = intervals[check][1]
                else:
                    end = intervals[check + 1][1]
            
                intervals.pop(check)
                intervals.pop(check)
                intervals.insert(check, [start, end])
                continue
            
            check = check + 1
            
        return intervals