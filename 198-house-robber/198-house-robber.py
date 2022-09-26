class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        print(N)
        if N == 0:
            return 0
        
        maxAmount = [None for i in range(N + 1)]
        
        maxAmount[N], maxAmount[N-1] = 0, nums[N- 1]
        print(maxAmount[N], maxAmount[N-1])
        
        for i in range(N - 2, -1, -1):
            maxAmount[i] = max(maxAmount[i+1], maxAmount[i + 2] + nums[i])
            print(maxAmount[i])
        return maxAmount[0]
        