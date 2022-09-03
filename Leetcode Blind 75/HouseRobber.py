class Solution:
    def rob(self, nums: List[int]) -> int:
        def fun(i):
            if i == 0:
                return nums[i]
            if i < 1:
                return 0
            return max(nums[i]+fun(i-2), 0+fun(i-1))
        return fun(len(nums)-1)
