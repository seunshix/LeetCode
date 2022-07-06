class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        take input list and sort by first value of each interval
        
        '''
        intervals.sort(key = lambda x:x[0])
        
        '''
        create a resulting array with the first interval stored in it
        '''
        result = [intervals[0]]
        
        '''
        iterate through every interval excluding the first interval
        '''
        for start, end in intervals[1:]:
            
            '''
            from the result array, we get the end value of the most recent intervl in output array, call it prevEnd
            '''
            prevEnd = result[-1][1]
            
            '''
            now we compare the start value with prevEnd and check if there is overlap...
            
            if there is overlap, we merge the intervals by taking the end value of the previously added interval and set it to the max value of 
            either it's own end value or the current interval's end value.
            
            if non-overlapping, we add the current interval to the result array
            '''
            if start <= prevEnd:
                result[-1][1] = max(prevEnd, end)
                
            else:
                result.append([start,end])
            
        return result

'''

Time complexity : O(nlogn)

Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(nlogn) complexity of sorting.

Space complexity : O(logN) (or O(n))

If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.


'''
                
            