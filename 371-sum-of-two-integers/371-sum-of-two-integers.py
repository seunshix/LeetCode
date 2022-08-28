class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
        
        
        '''
      To explain, the hexadecimal number 0xffffffff is the same as the binary number 0b1111111111111111111111111111111, containing 32 1's. (It's just easier to type lol.)

In order to make the code work like Java, we want to treat our numbers like they only have 32 bits. ANDing a number with the mask 0xffffffff, or 32 1's, basically turns all of a number's bits into 0's except for the rightmost 32. As a result, the number can be represented as if it only has 32 bits.

We do what Neetcode describes in his video, using XOR for the sum and AND for the carry. We AND with the mask each time we set a and b in order to keep our numbers within 32 bits.

After we exit the while loop, we have our answer a. If a is positive, then we can return it directly. However, in Python, negative numbers are represented in binary as having an unlimited number of leading 1's. The current answer would only have values in the rightmost 32 bits. Therefore, if the answer is negative, we need to convert it into Python's representation of negative numbers. 

First, we need to check if the answer is negative. We cannot just check to see if the answer is less than zero because our representation of the answer is not the same as Python's (since Python's have unlimited leading 1's). We are still treating our answer as if it only fits into 32 bits. 

A 32-bit signed integer is positive if the 32nd bit is a 0 and is negative if the 32nd bit is a 1. If we divide our mask (0xffffffff) by 2, we will get the binary number 0b0111111111111111111111111111111, which has 31 1's. This number is the greatest value we can have before the 32nd bit becomes a 1. Therefore, if our answer a > mask // 2, it is negative. Otherwise, it is positive and we can just return a itself.

If the number is negative, we then need to convert it into Python's representation of negative numbers. To do so, we can XOR with the mask of 32 1's in order to flip the rightmost 32 bits, since XORing a bit with 1 flips the bit. We can then NOT the number in order to turn all of the leading 0's into 1's. For example, say that the answer is -3, and (....0000000) or (....1111111) denote leading 0's or 1's until the 32nd bit:

Our representation of -3 in 32 bits: (...0000000)11111111111111111111111111111101
XOR with mask, aka flip rightmost 32 bits: (...0000000)00000000000000000000000000000010
NOT, aka flipping all bits: (...1111111)1111111111111111111111111111101
The result is Python's representation of -3, including an unlimited number of leading 1's.

Overall, the code uses the same process as Neetcode's Java code, but with masking to get numbers into 32 bits and some manipulation to get those 32-bit numbers back into Python's representation before returning.
      
      '''  
        
         
        
        '''
        this solution doesn't work in python because in Python, negative numbers are represented in binary as having an unlimited number           of leading 1's.
        
        
        
       
        while b !=0:
            carry = (a & b) << 1
            print(carry)
            a = a ^ b
            print(a)
            b = carry
            print(b)
            print("")
        return a
        
        '''     
        
        
        
        