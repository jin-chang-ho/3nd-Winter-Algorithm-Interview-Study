class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[len(row) - 1]:
                index = bisect.bisect_left(row, target)
                if index < len(row) and row[index] == target:
                    return True
        
        return False