class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binSearch(nums, target, True)
        last = self.binSearch(nums, target, False)
        
        return [first, last]
    
    def binSearch(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        i = -1
        while left <= right: 
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                i = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i