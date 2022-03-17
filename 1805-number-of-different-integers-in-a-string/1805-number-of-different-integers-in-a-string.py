class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numSet = set()
        i = 0
        while i < len(word):
            digit = ''
            while i < len(word) and word[i].isdigit():
                digit += word[i]
                i+=1
            if digit != '':
                if digit.startswith('0'):
                    digit = digit.lstrip('0')
                numSet.add(digit)
            i+=1
        return len(numSet)