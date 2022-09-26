class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0 
            
        for char in moves:
            if char == "U":
                x += 1
            if char == "D":
                x -= 1 
            if char == "L":
                y -= 1
            if char == "R":
                y +=1
        if x == 0 and y == 0:
            return True
        return False
        
                    
                    
        