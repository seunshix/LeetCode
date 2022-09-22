class Solution:
    def minSteps(self, s: str, t: str) -> int:
            
        leftCount = Counter(s)
        rightCount = Counter(t)
        
        print(leftCount)
        print(rightCount)
        
        
        difference = dict(leftCount - rightCount)
        print(difference)
        
        return sum(difference.values())