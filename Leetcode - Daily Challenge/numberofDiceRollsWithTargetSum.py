class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n==1:
            if target <= k:
                return 1
            return 0
        res = 0
        for i in range(1, k+1):
            res += self.numRollsToTarget(n-1, k, target-i)
        return res