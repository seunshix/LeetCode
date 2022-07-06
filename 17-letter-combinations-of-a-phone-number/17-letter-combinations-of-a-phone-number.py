class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for c in letters[digits[index]]:
                backtrack(index + 1, path + c)
            
        if digits:
            backtrack(0, "")
            
        return result
            
        