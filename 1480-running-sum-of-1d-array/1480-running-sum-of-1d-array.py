class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        '''
        1. iterate through the array
        2. at each index, calculate the sums of index i to index n-1
        3. return answer in result
        4. this solution can be done in-place
        
        '''
        n = len(nums) 
        for i in range(1, n):
            
            nums[i] = nums[i] + nums[i-1]
            
        return nums