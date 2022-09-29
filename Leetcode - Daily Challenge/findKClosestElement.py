class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []
        for num in arr:
            temp.append([abs(num-x), num])
        temp.sort()
        res = []
        for i in range(k):
            res.append(temp[i][1])
        return sorted(res)