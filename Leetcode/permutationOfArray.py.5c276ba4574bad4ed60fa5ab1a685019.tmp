class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def fun(up, p, res):
            if up==[]:
                res.append(p)
                return res
            ch = [up[0]]
            for i in range(len(p)+1):
                f = p[:i]
                l = p[i:]
                fun(up[1:], f+ch+l, res)
            return res
        return fun(nums, [], [])