class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = n * curMax
            curMax = max(n * curMax, n* curMin, n)
            curMin = min(temp, n * curMin, n)
            
            answer = max(answer, curMax)
        return answer
            
        
        