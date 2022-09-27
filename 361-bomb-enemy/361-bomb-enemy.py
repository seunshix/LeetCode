class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        '''
    for each empty square in the grid, i want to count how many points i can get by placing a bomb in that square. So, I just need to count how many people are  to the left, right, up, and down from each cell
    
    
So I can write a function that creates a scoreboard for each direction
        
        '''
        row_length, col_length = len(grid), len(grid[0])
        scoreboardUp = [[0] * col_length for _ in range(row_length)]
        scoreboardLeft = [[0] * col_length for _ in range(row_length)]
        scoreboardDown = [[0] * col_length for _ in range(row_length)]
        scoreboardRight = [[0] * col_length for _ in range(row_length)]
                     
                
        def scoreFunction(boardEntry, numOfPeople):
            if boardEntry == "E":
                return numOfPeople + 1, 0
            elif boardEntry == "W":
                return 0, 0
            else:
                return numOfPeople, numOfPeople
         
        #left
        for i in range(row_length):
            number_of_people = 0
            for j in range(col_length - 1, -1, -1):
                number_of_people, scoreboardLeft[i][j] = scoreFunction(grid[i][j], number_of_people)
                
        # right
        for i in range(row_length):
            number_of_people = 0
            for j in range(col_length):
                number_of_people, scoreboardRight[i][j] = scoreFunction(grid[i][j], number_of_people)
                
        #up
        for j in range(col_length):
            number_of_people = 0
            for i in range(row_length - 1, -1, -1):
                number_of_people, scoreboardUp[i][j] = scoreFunction(grid[i][j], number_of_people)
                
        #down
        for j in range(col_length):
            number_of_people = 0
            for i in range(row_length):
                number_of_people, scoreboardDown[i][j] = scoreFunction(grid[i][j], number_of_people)
            
        result= 0
        for i in range(row_length):
            for j in range(col_length):
                result = max(result, scoreboardLeft[i][j] + scoreboardRight[i][j] + scoreboardUp[i][j]+ scoreboardDown[i][j])
                
        
        for row in scoreboardDown:
            print(row)
        for row in scoreboardUp:
            print(row)
            
        return result
        