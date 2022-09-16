class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
            
        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            top +=1
                
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
                
            if not (left < right and top < bottom):
                 break
                    
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -=1
                
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left +=1
        return result
            
            
            
            
            
            
#             if offset == len(matrix) - offset - 1:
#                 spiral.append(matrix[offset][offset])
#             return
#             spiral.extend(matrix[offset][offset:-1 - offset])
#             spiral.extend(list(zip(matrix))[-1 - offset][offset:-1-offset])
#             spiral.extend(matrix[-1 - offset][-1 - offset:offset:-1])
#             spiral.extend(list(zip(matrix))[offset][-1 - offset:offset:-1])
              
        
#         spiral = []
#         for offset in range((len(matrix) + 1)//2):
#             matrix_clockwise(offset)
#         return spiral
        