class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        count each character occurence in ransomNote and check if it is <= the character occurence in magazine. return true else return false
        
        '''
        ransomNotedict = Counter(ransomNote)
        print(ransomNotedict)
        magazinedict = Counter(magazine)
        print(magazinedict)
        
        # dictionary = {}
        # # for letter in ransomeNote:
        # #     if letter not in dictionary:
        # #         dictionary[letter] = 0
        # #     dictionary[letter] += 1
        
       # letters = "abcdefghijk..."
       # letters = ascii_lowercase
        included_letters = ransomNotedict.keys()
        
        for ch in included_letters:
            print(ch)
            # if ransomNotedict[ch] <= magazinedict[ch]:
            #     print(ch)
            #     return True
            if ransomNotedict[ch] > magazinedict[ch]:
                return False
        return True
            
            # print(ransomNotedict.get(ch))
            # print(ransomNotedict.keys())
            # print(ransomNotedict.values())
            # print(ransomNotedict.items())
            
        