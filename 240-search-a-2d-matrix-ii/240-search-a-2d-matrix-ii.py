class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # iterate through each row and column, if value at grid[row][column] = target, return true. This is not an efficient solution and the fact the matrix is sorted ascending should be used for an efficient solution
        # first brute force solution
        
        for i in matrix:
            if target in i:
                return True
        return False