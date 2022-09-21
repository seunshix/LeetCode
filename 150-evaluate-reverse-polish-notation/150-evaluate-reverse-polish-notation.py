import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        operation = {'+': lambda y, x: x + y,
                    '-': lambda y, x: x - y,
                    '*': lambda y, x: x * y,
                    '/': lambda y, x: int(x / y)}
        for i in tokens:
            if i in operation:
                result.append(operation[i](result.pop(), result.pop()))   
            else:
                result.append(int(i))      
        return result.pop()
    
