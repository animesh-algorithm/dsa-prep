class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        ans = 1
        for i in range(len(nums)):
            ans *= nums[i]
            res[i] = ans
        res[-1] = res[-2]
        ans = 1
        for i in range(len(nums)-2, 0, -1):
            ans *= nums[i+1]
            res[i] = res[i-1]*ans
        res[0] = ans*nums[1]
        return res