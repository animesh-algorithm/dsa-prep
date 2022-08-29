class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma = 1
        mi = 1
        res = max(nums)
        for num in nums:
            if num == 0:
                ma = 1
                mi = 1
            ma, mi = max(num*ma, num*mi, num), min(num*ma, num*mi, num)
            res = max(res, ma)
        return res