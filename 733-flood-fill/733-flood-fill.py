class Solution:
    
    def neighbours(self, image, sr, sc, start):
        directions = [(sr - 1, sc), (sr + 1, sc), (sr, sc + 1), (sr, sc - 1)]
        return [(sr, sc) for (sr, sc) in directions if self.isValid(image, sr, sc) and image[sr][sc] == start]
    
    def isValid(self, image, sr, sc):
        return sr >= 0 and sc >= 0 and sr < len(image) and sc < len(image[0])
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        queue = [(sr, sc)]
        start = image[sr][sc]
        
        while queue:
            sr, sc = queue.pop(0)
            visited.add((sr, sc))
            image[sr][sc] = color
            for sr, sc in self.neighbours(image, sr, sc, start):
                if (sr, sc) not in visited:
                    queue.append((sr, sc))
        return image
    
    