class Solution:
    def numTrees(self, n: int) -> int:
        if n<=1:
            return 1
        res = 0
        for i in range(1, n+1):
            res += self.numTrees(i-1)*self.numTrees(n-i)
        return res

class Solution1:
    def numTrees(self, n: int) -> int:
        def solve(n, dp):       
            if n<=1:
                return 1
            if dp[n] != 0:
                return dp[n]
            res = 0
            for i in range(1, n+1):
                res += solve(i-1, dp)*solve(n-i, dp)
            dp[n] = res
            return dp[n]
        dp = [0]*(n+1)
        return solve(n, dp)

class Solution2:
    def numTrees(self, n: int):
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            res = 0
            for j in range(1, i+1):
                res += dp[j-1]*dp[i-j]
            dp[i] = res
        return dp[n]