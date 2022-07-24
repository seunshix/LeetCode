class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list) # create hashmap, 
                                               #defaultdict is used to catch edge case when string is not present
        for s in strs:
            count = [0] * 26 # create character count array (26 non-negative numbers) a...z
            for c in s:
                count[ord(c) - ord('a')] += 1 # ascii value calc supported by ord in python
            result[tuple(count)].append(s) # tuples are non- mutable
        return result.values() # we need values not the array
    
# O(M.N) 
# M - number of input strings i.e ["eat","tea","tan","ate","nat","bat"] M = 6
# N - average length of a string in input i.e N = 3, all strings are length 3 

# The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified.

# The Python defaultdict type behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key, then defaultdict will automatically create the key and generate a default value for it. This makes defaultdict a valuable option for handling missing keys in dictionaries.