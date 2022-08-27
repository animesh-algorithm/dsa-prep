class Solution:
    def getRow(self, n: int) -> List[int]:
        def C(n, r):
            if r == 0 or r == n:
                return 1
            if r > n//2:
                r = n-r
            if r==1:
                return n
            res = 1
            for i in range(r):
                res*=(n-i)
                res//=(i+1)
            return res
        return [C(n, r) for r in range(n+1)]