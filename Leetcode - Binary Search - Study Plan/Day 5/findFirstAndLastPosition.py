class Solution:
    def searchRange(self, a: List[int], target: int) -> List[int]:
        i = 0
        j = len(a)-1
        while i <= len(a)-1:
            if a[i] == target:
                break
            i += 1
        while j >= 0:
            if a[j] == target:
                break
            j -= 1
        if i >= len(a):
            i = -1
        return [i, j]
