from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        last_cell = (row - 1, col - 1)
        
        if k >= row + col - 2:
            return row + col - 2
        
        state = (0, 0 , k)
        queue = deque([(0, state)])
        seen = set([state])
        
        while queue:
            steps, (r, c, k) = queue.popleft()
            
            #if we reach the last cell, return steps
            if (r, c) == last_cell:
                return steps
            
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            
            for new_row, new_col in directions:
                if (0 <= new_row < row) and (0 <= new_col < col):
                    new_k = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_k)
                    if new_k >=0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))
        return -1
            