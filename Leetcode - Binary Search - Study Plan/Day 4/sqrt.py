class Solution:
    def mySqrt(self, x: int) -> int:
        def fun(s, e):
            if s <= e:
                mid = s+(e-s)//2
                if mid*mid==x:
                    return mid
                if mid*mid>x:
                    return fun(s, mid-1)
                else:
                    return fun(mid+1, e)
            return e
        return fun(0, x)