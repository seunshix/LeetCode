class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        1. since we need to modify the array in place, we can use the two-pointer approach here
        2. since the array is sorted, we know duplicate elements will definitely be grouped together
        3. main question is how do we know we have a unique value that we haven't encountered yet
        
        Approach
        1. we initialize two pointers starting at the second(1th) index because we don't need to update the first element
        2. then we compare the value at our left pointer with the value at the first index to check duplicate, if its a duplicate we increment the right pointer.
        3. we compare the value at the right pointer with that at the left pointer, if its not a unique value we haven't encountered, we put the value where the left pointer is supposed to be. Then we increment the left and right pointer and repeat above steps accordingly.
        Note: we don't shift the left pointer if the elements at the left and right pointers are duplicates.
        4. Once we go out of bounds, we return the value of the left pointer
        '''
        left = 1 
        right = 1
        
               
        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left +=1
            right += 1
        return left
        
    '''
    TC: O(N)
    SC: O(1)
    '''