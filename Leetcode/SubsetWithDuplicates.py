class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def fun(pick, nums, res):
            if nums == []:
                if sorted(pick) not in res:
                    res.append(sorted(pick))
                return res
            fun(pick+[nums[0]], nums[1:], res)
            fun(pick, nums[1:], res)
            return res
        return fun([], nums, [])