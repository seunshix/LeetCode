class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        #@functools.lru_cache(None)
        def foo(i, j):
            if i==j==-1:
                return True

            if j<0:
                return False
            
            if i<0:
                return p[j]=="*" and foo(i, j-2)
                
            if p[j]=="*":
                if foo(i, j-2): 
                    return True
                
                if (p[j-1]=="." or s[i]==p[j-1]) and foo(i-1, j):   
                    return True
                        
            elif (p[j]=="." or p[j]==s[i]) and foo(i-1, j-1):
                return True

            return False
                
        return foo(len(s)-1, len(p)-1)