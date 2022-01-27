class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        notZero = True
        for i in range(len(arr)):
            if arr[i] == 0 and notZero:
                arr.pop(-1)
                arr.insert(i + 1, 0)
                notZero = False
            else:
                notZero = True
                