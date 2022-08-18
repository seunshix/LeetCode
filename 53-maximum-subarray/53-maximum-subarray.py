class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArr = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxArr = max(maxArr, curSum)
        return maxArr
        