class Solution:
    def rob(self, nums: List[int]) -> int:
        def fun(i):
            if i == 0:
                return nums[i]
            if i < 1:
                return 0
            return max(nums[i]+fun(i-2), 0+fun(i-1))
        return fun(len(nums)-1)


class Solution:


def rob(self, nums: List[int]) -> int:
    def fun(i, dp):
        if i == 0:
            dp[i] = nums[i]
            return dp[i]
        if dp[i] != -1:
            return dp[i]
        if i < 1:
            dp[i] = 0
            return dp[i]
        dp[i] = max(nums[i]+fun(i-2, dp), 0+fun(i-1, dp))
        return dp[i]
    dp = [-1]*(len(nums))
    return fun(len(nums)-1, dp)
