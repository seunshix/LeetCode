class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        table = {}
        for i in arr:
            if i in table:
                return True
            table[i / 2] = True
            table[i * 2] = False
        return False
        