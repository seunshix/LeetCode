class Solution(object):
    def minTotalDistance(self, grid):
        rows = []
        cols = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)
                    
        cols.sort()
        
        def findMin(v):
            t = 0
            for i in range(len(v)):
                t += v[i] - v[i >> 1]
            return t
        return findMin(rows) + findMin(cols)
        