class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(array, left, right):
            x = array[right]
            left_pointer = left
            for right_pointer in range(left, right):
                if array[right_pointer] <= x:
                    array[right_pointer], array[left_pointer] = array[left_pointer], array[right_pointer]
                    left_pointer += 1
            array[left_pointer], array[right] = array[right], array[left_pointer]
            return left_pointer


        def quicksort(arr, left, right):
            if left < right:
                pivot = partition(arr, left, right)
                quicksort(arr, left, pivot - 1)
                quicksort(arr, pivot + 1, right)
            return arr
        
        return quicksort(nums, 0, len(nums) - 1)
        