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
    
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def helper(n, k, target, dp):
            if n==1:
                if target <= k:
                    return 1
                return 0
            if dp[n][target]:
                return dp[n][target]
            res = 0
            for i in range(1, k+1):
                res += self.numRollsToTarget(n-1, k, target-i)
            dp[n][target]=res
            return dp[n][target]
        dp = [[None for _ in range(target+1)] for _ in range(n+1)]
        return helper(n, k, target, dp)