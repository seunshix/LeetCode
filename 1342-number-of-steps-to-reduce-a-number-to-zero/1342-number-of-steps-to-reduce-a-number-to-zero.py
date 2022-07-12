class Solution:
    def numberOfSteps(self, num: int) -> int:
        '''
        1. we have to keep running count of steps
        2. if the number is divisible by 2, divide it by 2
        3. if number is odd, subract 1
        '''
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num/2
                steps +=1
            if num % 2 == 1:
                num = num - 1
                steps +=1
        return steps
        '''
        Tc: o(logn), at each point, we halve the num
        '''