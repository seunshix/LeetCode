class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        array = []
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                array.append(nums)
        
        return len(array)
                
        