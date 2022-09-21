class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisMap = {'[' : ']', '{' : '}', '(' : ')'}
        lookup = []
        
        for c in s:
            if c in parenthesisMap:
                lookup.append(c)
            elif not lookup or parenthesisMap[lookup.pop()] != c:
                return False
        return not lookup
            
        