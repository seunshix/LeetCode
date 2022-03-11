class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 0, x/2
        
        while right >= left:
            pivot = left + (right - left)//2
            a = pivot * pivot
            if a > x:
                right = pivot - 1
            elif a < x:
                left = pivot + 1
            else:
                return int(pivot)
        return int(right)
                