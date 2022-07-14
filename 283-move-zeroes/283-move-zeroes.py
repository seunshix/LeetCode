class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        1. it is a two pointer problem
        2. the left pointer and right pointer should start from the beginning
        3. we then iterate through the array using the right pointer. if the element at right pointer is non-zero, we swap elements at the left and right pointer
        4. return the array
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right+=1
        return nums
        
        