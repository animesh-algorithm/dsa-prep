class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def fun(s, e, ans):
            if s <= e:
                mid = s+(e-s)//2
                if letters[mid] <= target:
                    return fun(mid+1, e, ans)
                else:
                    return fun(s, mid-1, letters[mid])
            return ans
        res = fun(0, len(letters)-1, " ")
        return res if res != " " else letters[0]
