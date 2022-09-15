
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n < 2:
            return 0
        lo, hi = 0, n-1
        mid = lo + (hi - lo)//2
        
        left_prices = prices[0:mid+1]
        right_prices = prices[mid+1: ]
        
        left_profit = self.maxProfit(left_prices)
        right_profit = self.maxProfit(right_prices)
        
        left_min = min(left_prices)
        right_max = max(right_prices)
        
        combine_profits = right_max - left_min
        
        return max(left_profit, right_profit, combine_profits)
        
        '''
        
        O(n^2) solution TLE, Brute Force
        def maxProfit(self, prices: List[int]) -> int:
        larger_difference = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] - prices[i] > larger_difference:
                    larger_difference = prices[j] - prices[i]
        return larger_difference
        
        
        '''
        
        
        '''
        Divide and conquer approach
        def maxProfit(self, prices: List[int]) -> int:
       
        n = len(prices)
        if n < 2:
            return 0
        
        mid = n//2
        
        left_prices = prices[: mid+1]
        right_prices = prices[mid-1: ]
        
        left_profit = self.maxProfit(left_prices)
        right_profit = self.maxProfit(right_prices)
        
        left_min = min(left_prices)
        right_max = max(right_prices)
        
        combine_profits = right_max - left_min
        
        return max(left_profit, right_profit, combine_profits)
        
        '''
        