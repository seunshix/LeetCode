class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hset = set()
        for i in nums:
            if i in hset:
                return True
            hset.add(i)
        return False
                
        
        '''
        
        O(nlogn) solution
        n = len(nums)
        nums.sort()
        if n < 2:
            return False
        for i in range (1, n):
            if nums[i-1] == nums[i]:
                return True
        return False
        
        
        '''

                
        