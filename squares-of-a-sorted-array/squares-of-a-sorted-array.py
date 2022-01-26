class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(len(nums)):
            array.append(pow(nums[i], 2))
            array.sort()
            
            
        return array
            
        