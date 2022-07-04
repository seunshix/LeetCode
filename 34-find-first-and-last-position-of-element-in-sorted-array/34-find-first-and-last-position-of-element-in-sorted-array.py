class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin = 0
        end = len(nums) - 1
        result = [-1, -1]
        
        while begin <= end:
            mid = (begin + end)//2
        
            if nums[mid] == target:
                while mid >= begin and nums[mid] == target:
                    mid = mid - 1
                result[0] = mid + 1
                mid = mid + 1
                while mid <= end and nums[mid] == target:
                    mid = mid + 1
                result[1] = mid -1
                break 
            elif nums[mid] > target:
                end = end - 1
            else:
                begin = begin + 1

        return result