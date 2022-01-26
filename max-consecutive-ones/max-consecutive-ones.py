class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        prevCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                prevCount = max(prevCount, count)
                
                count = 0
        
        return max(prevCount, count)
           
        