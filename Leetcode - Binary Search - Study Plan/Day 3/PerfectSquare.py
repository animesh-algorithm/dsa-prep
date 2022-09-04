class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def fun(s, e):
            if s <= e:
                mid = s+(e-s)//2
                if mid*mid  = = num:
                    return True
                if mid*mid   > num:
                    return fun(s, mid-1)
                else:
                    return fun(mid+1, e)
            return False
        return fun(0, num)

