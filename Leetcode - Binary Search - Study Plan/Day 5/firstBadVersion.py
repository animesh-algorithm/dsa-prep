# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def solve(s, e):
            if s <= e:
                mid = e+(s-e)//2
                if isBadVersion(mid):
                    return solve(s, mid-1)
                else:
                    return solve(mid+1, e)
            return s

        return solve(0, n)
