class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Using the AND operator and right-shift the bits
        
        '''
        num_bits = 0
        while n:
            print(n)
            print(n & 1)
            num_bits += n & 1
            print(n >> 1)
            n >>= 1
            print("")
        return num_bits
            