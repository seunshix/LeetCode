class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        climb = 0
        n = len(arr)
        
        while (climb < n - 1 and arr[climb] < arr[climb + 1]):
            climb +=1
            
        if (climb == 0 or climb == n - 1):
            return False
        
        while (climb < n - 1 and arr[climb] > arr[climb + 1]):
            climb += 1
            
        if climb == n -1:
            return True
        else:
            return False
            