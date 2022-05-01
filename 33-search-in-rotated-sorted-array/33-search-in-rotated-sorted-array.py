# Formula: If a sorted array is shifted, if you take the middle, always one side will be sorted. Take the recursion according to that rule.

# 1- take the middle and compare with target, if matches return.
# 2- if middle is bigger than left side, it means left is sorted & Binary search can be applied on left side.
# 2a- if [left] < target < [middle] then do recursion with left, middle - 1 (right)
# 2b- left side is sorted, but target not in here, search on right side {middle + 1 (left), right} => Here one is NOT claiming that right side is sorted. 
# We are NOT applying binary search here per-se. We are just reducing our search space since we are sure that element is NOT in the part 2a. 
# The next iteration in this method would try to figure out which part of the subarray needs to be looked into.
# 3- if middle is less than right side, it means right is sorted
# 3a- if [middle] < target < [right] then do recursion with middle + 1 (left), right
# 3b- right side is sorted, but target not in here, search on left side i.e. {left, middle -1 (right)} => Here one is NOT claiming that left side is sorted. 
# We are NOT applying binary search here per-se. We are just reducing our search space since we are sure that element is NOT in the part 3a. 
# The next iteration in this method would try to figure out which part of the subarray needs to be looked into.

class Solution:
    def search(self, nums: List[int], target: int, start = None, end = None) -> int:
        if len(nums) == 1 and nums[0] != target: return -1
        
        if start is None:
            start = 0
            end = len(nums) - 1
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[start]  <= target <= nums[mid]:
            return self.search(nums, target, start, mid)
        
        if nums[mid + 1] <= target <= nums[end]:
            return self.search(nums, target, mid + 1, end)
        
        if nums[start] > nums[mid]:
            return self.search(nums, target, start, mid)
        
        if nums[mid + 1] > nums[end]:
            return self.search(nums, target, mid + 1, end)
        
        return -1