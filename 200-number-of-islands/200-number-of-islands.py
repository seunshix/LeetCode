class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Note that 1's have to be connected horizontally or vertically
        
        We can easily map out number of islands by looking at the grid array but how do we determine the neighbours and mark them as visited.
        
        So when we see a node, we visit it's adjacent neighbours and mark them as visited and keep doing that for each node. We don't have to
        revisit nodes that have been marked.
        
        This is a graph traversal algorithm starting at the original point and marking each layer of 1's. We can implement using a BFS or DFS 
        algorithm.
        
        Implementation
        First, we do some input validation. So if we have an empty grid, we return 0
        
        '''
        
        if not grid:
            return 0
        
        
        def bfs(r, c):
            '''
            BFS is not a recursive algorithm, it is iterative so we need a data structure for memory. We can use a queue as it is normally used for 
            BFS implementation
            
            So we add the (row, col) to the visited array and add it to the queue
            '''
            
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))
            
            '''
            while our queue is not empty, we will be expanding our island
            
            we will pop the first node from the queue and we will check if the neighbours of the node we just popped. We can do that using a
            directions array of U, D, L, R [0,1],[0,-1],[-1,0],[1,0]
            
            Using a for loop, we ensure the position is in bounds and not beyond the grid
            
            '''
            while queue:
                row, col = queue.popleft()
                directions = [[0,1],[0,-1],[-1,0],[1,0]]
                
                for rowDir, colDir in directions:
                    rowAdj = row + rowDir
                    colAdj = col + colDir
                    
                    if (rowAdj in range(rows) and 
                        colAdj in range(columns) and 
                        grid[rowAdj][colAdj] == '1' and 
                        (rowAdj, colAdj) not in visited):
                        
                        queue.append((rowAdj, colAdj)) # append node to the queue so we can run BFS on the node
                        visited.add((rowAdj, colAdj))  # add the node to visit set so we don't visit it twice

        '''
        Next, we get the dimensions of the grids, and we want to mark nodes visited and we can use a set to do that.
        And we initialize the resulting islands
        
        '''
        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        '''
        Now, we iterate through each row and column, if we visit a 0, we don't have to do anything but if we visit 1, we have to mark it as visited
        
        '''
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == '1' and (row,col) not in visited:
                    '''
                    Now we run a bfs traversal and increment island only when we get to a position we haven't visited
                    '''
                    bfs(row,col)
                    islands+=1                     
            
        return islands
'''
Time complexity : O(M×N) where M is the number of rows and NN is the number of columns.

Space complexity : O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).

'''        

        
'''
To do a DFS solution, we change the queue.popleft() to queue.pop() meaning a popright, it will pop the last node that we added instead of the first, meaning it is now a stack implementation


Time complexity : O(M×N) where M is the number of rows and N is the number of columns.

Space complexity : worst case O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.

'''