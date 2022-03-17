class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        stack = []
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    stack.append((i, j))
                    grid[i][j] = "0"
                    count = count + 1
                    temp_i = i
                    temp_j = j
                    
                    while True:
                        if (temp_j + 1 < len(grid[0]) and grid[temp_i][temp_j + 1] == "1"):
                            if (temp_j - 1 >= 0 and grid[temp_i][temp_j - 1] == "1"):
                                stack.append((temp_i, temp_j))
                            temp_j = temp_j + 1
                            grid[temp_i][temp_j] = "0"
                            stack.append((temp_i, temp_j))
                            continue
                        
                        
                        if (temp_i + 1 < len(grid) and grid[temp_i + 1][temp_j] == "1"):
                            if (temp_i - 1 >= 0 and grid[temp_i - 1][temp_j] == "1"):
                                stack.append((temp_i, temp_j))
                            temp_i = temp_i + 1
                            grid[temp_i][temp_j] = "0"
                            stack.append((temp_i, temp_j))
                            continue
                            
                        if (temp_j - 1 >= 0 and grid[temp_i][temp_j - 1] == "1"):
                            if (temp_j - 1 >= 0 and grid[temp_i][temp_j - 1] == "1"):
                                stack.append((temp_i, temp_j))
                            temp_j = temp_j - 1
                            grid[temp_i][temp_j] = "0"
                            stack.append((temp_i, temp_j))
                            continue
                        
                        if (temp_i - 1 >= 0 and grid[temp_i - 1][temp_j] == "1"):
                            if (temp_j + 1 < len(grid[0]) and grid[temp_i][temp_j + 1] == "1"):
                                stack.append((temp_i, temp_j))
                            temp_i = temp_i - 1
                            grid[temp_i][temp_j] = "0"
                            stack.append((temp_i, temp_j))
                            continue
                                                
                        if stack:
                            temp_i, temp_j = stack.pop()
                        else:
                            break       
                    
                        
        return count
                        