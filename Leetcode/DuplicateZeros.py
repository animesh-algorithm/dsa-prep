class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i   = 0
        n   = len(arr)
        while i < len(arr):
            if arr[i]  = = 0:
                arr.insert(i+1, 0)
                i   = i+2
                continue
            i  + = 1
        n1 = len(arr)
        for i in range(n1-n):
            arr.pop()

