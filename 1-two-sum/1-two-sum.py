class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        res = []
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hmap:
                return [hmap[complement], i]
                
            hmap[nums[i]] = i
            
        return []
        