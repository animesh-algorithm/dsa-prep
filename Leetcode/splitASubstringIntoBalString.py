class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        bal = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l += 1
            elif s[i] == 'R':
                r += 1
            if r == l:
                bal += 1
        return bal
