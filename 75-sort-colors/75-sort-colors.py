class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(array, left, right):
            if left < right:
                pivot = partition(array, left, right)
                quicksort(array, left, pivot - 1)
                quicksort(array, pivot + 1, right)
            return array
        
        def partition(arr, left, right):
            x = arr[right]
            smaller = left
            for larger in range(left, right):
                if arr[larger] <= x:
                    arr[smaller], arr[larger] = arr[larger], arr[smaller]
                    smaller +=1
            arr[smaller], arr[right] = arr[right], arr[smaller]
            return smaller
        
        return quicksort(nums, 0, len(nums) - 1)
        