class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        '''
        DFS approach recursively
        
        similar to No. of Islands
        
        1. initialize a set
        2. using the dfs algorithm, when we see an element that is 1, we run dfs on every direction of the element 4D and mark it as visited
        '''
        visited = set()
        rows , cols = len(grid), len(grid[0])
        
        
        def dfs(row, col):
            
            if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row, col))
        
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col  - 1))
                    
                    
        area = 0
        for row in range(rows):
            for col in range(cols):
                area = max(area, dfs(row, col))
        return area
            
        
        
        
        
        