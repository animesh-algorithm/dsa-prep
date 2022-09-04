class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for a in arr1:
            index = bisect.bisect_left(arr2, a)
            if index == 0:
                if abs(a - arr2[index]) > d:
                    count += 1
            elif index < len(arr2):
                if abs(a - arr2[index]) > d and abs(a - arr2[index - 1]) > d:
                    count += 1
            elif index == len(arr2):
                if abs(a - arr2[index - 1]) > d:
                    count += 1
        return count

