class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def fun(pick, nums, res):
            if nums == []:
                res.append(pick)
                return res
            fun(pick+[nums[0]], nums[1:], res)
            fun(pick, nums[1:], res)
            return res
        return fun([], nums, [])