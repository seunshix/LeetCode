class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        n = len(nums)
        print(n)
        answer = [1] * n
        
        '''
        # O(n) time complexity and space complexity
        n = len(nums) 
        print(n)
        prefix = [1] * n
        postfix = [1] * n
        answer = [1] * n
        

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
        