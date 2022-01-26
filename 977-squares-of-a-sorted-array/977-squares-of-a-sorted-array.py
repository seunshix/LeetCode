class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        array = [0] * len(nums)
        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])
            
            if left > right:
                array[r - l] = left * left
                l+=1
            else:
                array[r - l] = right* right
                r-=1
            
        return array
            
        