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

    class Solution:


def searchRange(self, a: List[int], target: int) -> List[int]:
    def solve(s, e, first=False, ans=-1):
        if s <= e:
            mid = s+(e-s)//2
            if a[mid] > target:
                return solve(s, mid-1, first, ans)
            elif a[mid] < target:
                return solve(mid+1, e, first, ans)
            else:
                ans = mid
                if first:
                    return solve(s, mid-1, first, ans)
                else:
                    return solve(mid+1, e, first, ans)
        return ans
    res = [-1, -1]
    res[0] = solve(0, len(a)-1, True, -1)
    res[1] = solve(0, len(a)-1, False, -1)
    return res
