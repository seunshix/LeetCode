class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        we can modify the quicksort algorithm for this problem by swapping the element only if the mod2 of the element is less than the other
        1. initialize two pointers, left, right. left takes the first element while right takes the last element
        2. while left pointer is less than right pointer, compare the elements at left and right. if the mod2 of left element is less than mod2 of element at the right, swap them else incrementif the mod2 of left elementy is 0 and mod2 of right element is 1
        3. return the array
        '''
        left, right = 0 , len (nums) -1
        
        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
                
            
            if nums[left] % 2 == 0:
                left +=1
            if nums[right] % 2 == 1:
                right -=1
        return nums