class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        print(n)
        prefix = [0] * n
        postfix = [0] * n
        answer = [0] * n
        
        prefix[0] = 1
        postfix[n - 1] = 1
        print(prefix)
        print(postfix)
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            postfix[j] = postfix[j + 1] * nums[j + 1]
            
        for i in range(n):
            answer[i] = prefix[i] * postfix[i]
            
        return answer
        
        print(prefix)
        print(postfix)