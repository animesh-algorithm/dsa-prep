class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = [0]*(len(s)+1)
        low = 0
        high = len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                perm[i]=low
                low+=1
            if s[i] == 'D':
                perm[i]=high
                high-=1
        perm[len(s)] = high
        return perm