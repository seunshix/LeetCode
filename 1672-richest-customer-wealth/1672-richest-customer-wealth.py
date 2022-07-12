class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        '''
        1. calculate sum of each row 
        2. find the max sum and return sum
        TC is O(m.n), cos we iterate through rows and columns of the grid
        SC: O(1), no extra space is allocated
        '''
        wealthCalculated = 0
        for account in accounts:
            print(account)
            currentWealth = sum(account)
            wealthCalculated = max(wealthCalculated, currentWealth)
        return wealthCalculated
            
        