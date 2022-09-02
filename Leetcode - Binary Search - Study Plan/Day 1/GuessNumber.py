# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def fun(s, n):
            if s<=n:
                g = s+(n-s)//2
                if guess(g)==0:
                    return g
                if guess(g)==-1:
                    return fun(s, g-1)
                if guess(g)==1:
                    return fun(g+1, n)
            return -1
        return fun(0, n)